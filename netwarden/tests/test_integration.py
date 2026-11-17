"""Integration tests: real sockets against the demo targets on 127.0.0.1."""
from __future__ import annotations

import json

from netwarden.checks import default_checks
from netwarden.cli import main
from netwarden.engine import Assessment
from netwarden.fingerprint import Fingerprinter
from netwarden.knowledge import KnowledgeBase
from netwarden.report import get_reporter
from netwarden.scanner import TcpScanner
from netwarden.scope import Scope
from netwarden.store import ScanRepository, diff


def scan_demo(ports):
    a = Assessment(Scope(["127.0.0.1/32"]), TcpScanner(timeout=1.0), Fingerprinter(),
                   default_checks(KnowledgeBase.load()))
    return a.run(["127.0.0.1"], sorted(ports.values()))


def test_end_to_end_findings(demo_ports):
    result = scan_demo(demo_ports)
    assert len(result.hosts) == 1 and len(result.hosts[0].services) == 5
    cves = {f.cve for f in result.findings if f.cve}
    assert cves == {"CVE-2011-2523", "CVE-2024-6387", "CVE-2021-41773", "CVE-2021-42013"}
    titles = {f.title for f in result.findings}
    assert {"Cleartext protocol: telnet", "Cleartext protocol: ftp", "MySQL reachable over the network"} <= titles


def test_reports_render(demo_ports):
    result = scan_demo(demo_ports)
    assert "## Findings and remediation" in get_reporter("md").render(result)
    data = json.loads(get_reporter("json").render(result))
    assert data["summary"]["CRITICAL"] == 2
    assert "<table>" in get_reporter("html").render(result)


def test_history_and_diff(demo_ports, tmp_path):
    with ScanRepository(tmp_path / "h.db") as repo:
        first_id = repo.save(scan_demo(demo_ports))
        second = scan_demo(demo_ports)
        second.findings = [f for f in second.findings if f.cve != "CVE-2011-2523"]   # pretend vsftpd was fixed
        second_id = repo.save(second)
        d = diff(repo.get(first_id), repo.get(second_id))
        assert [f.cve for f in d.resolved] == ["CVE-2011-2523"] and d.new == []
        assert [row[0] for row in repo.history()] == [second_id, first_id]


def test_cli_scan_exit_codes(demo_ports, scope_file, tmp_path, capsys):
    ports = ",".join(str(p) for p in demo_ports.values())
    db = str(tmp_path / "cli.db")
    code = main(["--db", db, "scan", "127.0.0.1", "--scope", str(scope_file), "--ports", ports, "--format", "json"])
    out = capsys.readouterr().out
    assert code == 1 and json.loads(out)["summary"]["HIGH"] >= 1
    assert main(["--db", db, "scan", "10.9.9.9", "--scope", str(scope_file)]) == 2
    assert "outside the authorised scope" in capsys.readouterr().err
    assert main(["--db", db, "history"]) == 0
    assert "findings" in capsys.readouterr().out


def test_cli_report_file_and_diff(demo_ports, scope_file, tmp_path, capsys):
    ports = ",".join(str(p) for p in demo_ports.values())
    db, out = str(tmp_path / "d.db"), tmp_path / "report.html"
    args = ["--db", db, "scan", "127.0.0.1", "--scope", str(scope_file), "--ports", ports, "--fail-on", "critical"]
    assert main(args + ["--format", "html", "--output", str(out)]) == 1
    assert out.read_text(encoding="utf-8").startswith("<!DOCTYPE html>")
    assert main(args + ["--no-save"]) == 1
    assert main(["--db", db, "diff", "1", "1"]) == 0
    assert "unchanged: " in capsys.readouterr().out
    assert main(["--db", db, "diff", "1", "99"]) == 2
