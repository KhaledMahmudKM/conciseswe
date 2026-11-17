"""The assessment pipeline: scope -> discover -> fingerprint -> check -> result (a facade)."""
from __future__ import annotations

import asyncio
from collections.abc import Iterable
from datetime import UTC, datetime

from .checks import Check
from .events import EventBus, FindingRaised, HostFound, ScanFinished, ScanStarted
from .fingerprint import Fingerprinter
from .models import ScanResult
from .scanner import TcpScanner
from .scope import Scope


class Assessment:
    """Coordinates one assessment. Collaborators are injected, so tests can replace any of them."""

    def __init__(self, scope: Scope, scanner: TcpScanner, fingerprinter: Fingerprinter,
                 checks: list[Check], bus: EventBus | None = None):
        self.scope = scope
        self.scanner = scanner
        self.fingerprinter = fingerprinter
        self.checks = checks
        self.bus = bus or EventBus()

    def run(self, targets: Iterable[str], ports: Iterable[int]) -> ScanResult:
        return asyncio.run(self.run_async(targets, ports))

    async def run_async(self, targets: Iterable[str], ports: Iterable[int]) -> ScanResult:
        targets, ports = list(targets), list(ports)
        addresses = self.scope.expand(targets)          # raises ScopeError before any packet is sent
        result = ScanResult(targets=targets)
        self.bus.publish(ScanStarted(hosts=len(addresses), ports=len(ports)))
        result.hosts = await self.scanner.scan(addresses, ports)
        for host in result.hosts:
            for service in host.services:
                self.fingerprinter.identify(service)
            self.bus.publish(HostFound(host))
            for service in host.services:
                for check in self.checks:
                    for finding in check.run(host, service):
                        result.findings.append(finding)
                        self.bus.publish(FindingRaised(finding))
        result.findings.sort(key=lambda f: (-f.severity, -(f.cvss or 0), f.host, f.port))
        result.finished = datetime.now(UTC)
        self.bus.publish(ScanFinished(result))
        return result
