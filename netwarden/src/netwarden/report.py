"""Reports in several formats, chosen by name (strategy + simple factory)."""
from __future__ import annotations

import html
import json
from typing import Protocol

from .models import ScanResult, Severity


class Reporter(Protocol):
    extension: str

    def render(self, result: ScanResult) -> str: ...


def _when(result: ScanResult) -> str:
    return result.started.strftime("%Y-%m-%d %H:%M UTC")


class MarkdownReporter:
    extension = "md"

    def render(self, result: ScanResult) -> str:
        out = ["# NetWarden assessment report", "",
               f"Targets: {', '.join(result.targets)}  ", f"Started: {_when(result)}  ",
               f"Hosts with open ports: {len(result.hosts)}", "", "## Summary", "",
               "| Severity | Findings |", "|---|---|"]
        out += [f"| {name} | {n} |" for name, n in result.counts().items()]
        out += ["", "## Hosts", ""]
        for h in result.hosts:
            svcs = ", ".join(f"{s.port}/{s.name}" + (f" ({s.product} {s.version})" if s.product else "")
                             for s in h.services)
            out.append(f"* **{h.address}**: {svcs}")
        out += ["", "## Findings and remediation", ""]
        for i, f in enumerate(result.findings, 1):
            ref = f" ({f.cve}, CVSS {f.cvss})" if f.cve else ""
            out += [f"### {i}. [{f.severity.name}] {f.title}{ref}", "",
                    f"* Where: {f.host}:{f.port}", f"* Evidence: {f.evidence}", f"* Fix: {f.remediation}", ""]
        if not result.findings:
            out.append("No findings.")
        return "\n".join(out) + "\n"


class JsonReporter:
    extension = "json"

    def render(self, result: ScanResult) -> str:
        return json.dumps({
            "targets": result.targets,
            "started": result.started.isoformat(),
            "finished": result.finished.isoformat() if result.finished else None,
            "summary": result.counts(),
            "hosts": [{"address": h.address, "services": [vars(s) for s in h.services]} for h in result.hosts],
            "findings": [{**vars(f), "severity": f.severity.name} for f in result.findings],
        }, indent=2)


class HtmlReporter:
    extension = "html"
    COLOURS = {Severity.CRITICAL: "#7a1f1f", Severity.HIGH: "#c0392b", Severity.MEDIUM: "#d68910",
               Severity.LOW: "#2e86c1", Severity.INFO: "#7f8c8d"}

    def render(self, result: ScanResult) -> str:
        e = html.escape
        rows = "".join(
            f'<tr><td style="color:#fff;background:{self.COLOURS[f.severity]}">{f.severity.name}</td>'
            f"<td>{e(f.host)}:{f.port}</td><td>{e(f.title)}<br><small>{e(f.cve or '')}</small></td>"
            f"<td>{e(f.evidence)}</td><td>{e(f.remediation)}</td></tr>"
            for f in result.findings)
        summary = " ".join(f"<b>{n}</b> {k.lower()}" for k, n in result.counts().items() if n)
        return (f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>NetWarden report</title>"
                f"<style>body{{font-family:sans-serif;margin:2em}}table{{border-collapse:collapse}}"
                f"td,th{{border:1px solid #ccc;padding:6px;vertical-align:top}}</style></head><body>"
                f"<h1>NetWarden assessment report</h1><p>Targets: {e(', '.join(result.targets))}<br>"
                f"Started: {_when(result)}<br>{summary or 'No findings.'}</p>"
                f"<table><tr><th>Severity</th><th>Where</th><th>Finding</th><th>Evidence</th><th>Fix</th></tr>"
                f"{rows}</table></body></html>\n")


REPORTERS: dict[str, type[Reporter]] = {"md": MarkdownReporter, "json": JsonReporter, "html": HtmlReporter}


def get_reporter(fmt: str) -> Reporter:
    try:
        return REPORTERS[fmt]()
    except KeyError:
        raise ValueError(f"Unknown report format {fmt!r}; choose from {', '.join(REPORTERS)}") from None
