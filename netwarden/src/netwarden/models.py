"""Domain model: the things NetWarden knows about. Plain data, no I/O."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import IntEnum


class Severity(IntEnum):
    """Finding severity, ordered so that comparisons work (HIGH > LOW)."""

    INFO = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

    @classmethod
    def from_cvss(cls, score: float) -> Severity:
        """Map a CVSS v3 base score to its qualitative rating."""
        if score >= 9.0:
            return cls.CRITICAL
        if score >= 7.0:
            return cls.HIGH
        if score >= 4.0:
            return cls.MEDIUM
        if score > 0.0:
            return cls.LOW
        return cls.INFO


@dataclass
class Service:
    """An open TCP port and what we learned about the software behind it."""

    port: int
    banner: str = ""
    name: str = "unknown"
    product: str | None = None
    version: str | None = None


@dataclass
class Host:
    """A reachable address and its open services."""

    address: str
    services: list[Service] = field(default_factory=list)


@dataclass(frozen=True)
class Finding:
    """One problem on one service, with the evidence and how to fix it."""

    host: str
    port: int
    check_id: str
    title: str
    severity: Severity
    evidence: str
    remediation: str
    cvss: float | None = None
    cve: str | None = None

    @property
    def key(self) -> tuple[str, int, str]:
        """Identity used to compare findings between scans."""
        return (self.host, self.port, self.cve or self.check_id)


@dataclass
class ScanResult:
    """Everything one assessment produced."""

    targets: list[str]
    started: datetime = field(default_factory=lambda: datetime.now(UTC))
    finished: datetime | None = None
    hosts: list[Host] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    scan_id: int | None = None

    def counts(self) -> dict[str, int]:
        """Number of findings per severity, highest first."""
        return {s.name: sum(1 for f in self.findings if f.severity == s) for s in sorted(Severity, reverse=True)}

    def worst(self) -> Severity | None:
        return max((f.severity for f in self.findings), default=None)
