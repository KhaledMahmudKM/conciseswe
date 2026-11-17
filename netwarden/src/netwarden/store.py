"""Scan history in SQLite (repository pattern), and comparison of two scans."""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .models import Finding, ScanResult, Severity

SCHEMA = """
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started TEXT NOT NULL,
    targets TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS findings (
    scan_id INTEGER NOT NULL REFERENCES scans(id),
    host TEXT, port INTEGER, check_id TEXT, title TEXT, severity INTEGER,
    evidence TEXT, remediation TEXT, cvss REAL, cve TEXT
);
"""


@dataclass
class ScanDiff:
    new: list[Finding]
    resolved: list[Finding]
    unchanged: list[Finding]


class ScanRepository:
    """Hides SQL from the rest of the program; swap it for another store without touching callers."""

    def __init__(self, path: str | Path = "netwarden.db"):
        self.db = sqlite3.connect(path)
        self.db.executescript(SCHEMA)

    def save(self, result: ScanResult) -> int:
        with self.db:
            cur = self.db.execute("INSERT INTO scans (started, targets) VALUES (?, ?)",
                                  (result.started.isoformat(), " ".join(result.targets)))
            scan_id = int(cur.lastrowid or 0)
            self.db.executemany(
                "INSERT INTO findings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [(scan_id, f.host, f.port, f.check_id, f.title, int(f.severity), f.evidence, f.remediation,
                  f.cvss, f.cve) for f in result.findings])
        result.scan_id = scan_id
        return scan_id

    def get(self, scan_id: int) -> ScanResult:
        row = self.db.execute("SELECT started, targets FROM scans WHERE id = ?", (scan_id,)).fetchone()
        if row is None:
            raise KeyError(f"No scan with id {scan_id}")
        result = ScanResult(targets=row[1].split(), started=datetime.fromisoformat(row[0]), scan_id=scan_id)
        for r in self.db.execute("SELECT host, port, check_id, title, severity, evidence, remediation, cvss, cve "
                                 "FROM findings WHERE scan_id = ?", (scan_id,)):
            result.findings.append(Finding(r[0], r[1], r[2], r[3], Severity(r[4]), r[5], r[6], r[7], r[8]))
        return result

    def history(self) -> list[tuple[int, str, str, int]]:
        """(id, started, targets, number of findings), newest first."""
        return self.db.execute(
            "SELECT s.id, s.started, s.targets, COUNT(f.scan_id) FROM scans s "
            "LEFT JOIN findings f ON f.scan_id = s.id GROUP BY s.id ORDER BY s.id DESC").fetchall()

    def close(self) -> None:
        self.db.close()

    def __enter__(self) -> ScanRepository:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def diff(old: ScanResult, new: ScanResult) -> ScanDiff:
    before = {f.key: f for f in old.findings}
    after = {f.key: f for f in new.findings}
    return ScanDiff(new=[f for k, f in after.items() if k not in before],
                    resolved=[f for k, f in before.items() if k not in after],
                    unchanged=[f for k, f in after.items() if k in before])
