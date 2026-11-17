"""Command-line interface: netwarden scan | history | diff | demo."""
from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from . import __version__
from .checks import default_checks
from .engine import Assessment
from .events import EventBus, FindingRaised, HostFound, ScanStarted
from .fingerprint import Fingerprinter
from .knowledge import KnowledgeBase
from .models import Severity
from .report import REPORTERS, get_reporter
from .scanner import TcpScanner, parse_ports
from .scope import Scope, ScopeError
from .store import ScanRepository, diff

EXIT_OK, EXIT_FINDINGS, EXIT_ERROR = 0, 1, 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="netwarden", description="Assess hosts you are authorised to test.")
    p.add_argument("--version", action="version", version=f"netwarden {__version__}")
    p.add_argument("--db", default="netwarden.db", help="scan history database (default: %(default)s)")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("scan", help="scan targets and report findings")
    s.add_argument("targets", nargs="+", help="IP addresses or CIDR blocks, such as 192.168.56.0/24")
    s.add_argument("--scope", required=True, help="file listing the networks you are authorised to scan")
    s.add_argument("--ports", default="top", help="'top', or a list such as 22,80,8000-8100")
    s.add_argument("--timeout", type=float, default=1.0, help="seconds per connection (default: %(default)s)")
    s.add_argument("--format", choices=sorted(REPORTERS), default="md")
    s.add_argument("--output", help="write the report to this file instead of the screen")
    s.add_argument("--fail-on", choices=[x.name.lower() for x in Severity], default="high",
                   help="exit with status 1 if any finding is at least this severe (default: %(default)s)")
    s.add_argument("--no-save", action="store_true", help="do not record the scan in the history database")

    sub.add_parser("history", help="list previous scans")
    d = sub.add_parser("diff", help="compare two saved scans")
    d.add_argument("old", type=int)
    d.add_argument("new", type=int)
    m = sub.add_parser("demo", help="start safe practice targets on 127.0.0.1")
    m.add_argument("--port-offset", type=int, default=0)
    return p


def progress(bus: EventBus) -> None:
    """Observers that print progress to stderr, keeping stdout clean for the report."""
    def started(e: ScanStarted) -> None:
        print(f"scanning {e.hosts} host(s), {e.ports} port(s) each", file=sys.stderr)

    def host_found(e: HostFound) -> None:
        print(f"  {e.host.address}: {len(e.host.services)} open port(s)", file=sys.stderr)

    def finding(e: FindingRaised) -> None:
        print(f"    [{e.finding.severity.name}] {e.finding.title}", file=sys.stderr)

    bus.subscribe(ScanStarted, started)
    bus.subscribe(HostFound, host_found)
    bus.subscribe(FindingRaised, finding)


def cmd_scan(args: argparse.Namespace) -> int:
    scope = Scope.from_file(args.scope)
    bus = EventBus()
    progress(bus)
    kb = KnowledgeBase.load()
    assessment = Assessment(scope, TcpScanner(timeout=args.timeout), Fingerprinter(), default_checks(kb), bus)
    result = assessment.run(args.targets, parse_ports(args.ports))
    if not args.no_save:
        with ScanRepository(args.db) as repo:
            print(f"saved as scan {repo.save(result)} in {args.db}", file=sys.stderr)
    report = get_reporter(args.format).render(result)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"report written to {args.output}", file=sys.stderr)
    else:
        print(report, end="")
    worst = result.worst()
    return EXIT_FINDINGS if worst is not None and worst >= Severity[args.fail_on.upper()] else EXIT_OK


def cmd_history(args: argparse.Namespace) -> int:
    with ScanRepository(args.db) as repo:
        rows = repo.history()
    for scan_id, started, targets, n in rows:
        print(f"{scan_id:>4}  {started[:19]}  {n:>3} findings  {targets}")
    return EXIT_OK


def cmd_diff(args: argparse.Namespace) -> int:
    with ScanRepository(args.db) as repo:
        d = diff(repo.get(args.old), repo.get(args.new))
    for label, items in (("new", d.new), ("resolved", d.resolved)):
        print(f"{label}: {len(items)}")
        for f in items:
            print(f"  [{f.severity.name}] {f.host}:{f.port} {f.title}")
    print(f"unchanged: {len(d.unchanged)}")
    return EXIT_FINDINGS if d.new else EXIT_OK


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "scan":
            return cmd_scan(args)
        if args.command == "history":
            return cmd_history(args)
        if args.command == "diff":
            return cmd_diff(args)
        from .demo import serve_forever
        asyncio.run(serve_forever(port_offset=args.port_offset))
        return EXIT_OK
    except (ScopeError, ValueError, KeyError, OSError) as exc:
        print(f"netwarden: error: {exc}", file=sys.stderr)
        return EXIT_ERROR
    except KeyboardInterrupt:
        return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
