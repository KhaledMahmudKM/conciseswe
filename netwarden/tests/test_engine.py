"""Engine tests with test doubles: no sockets are opened here."""
from __future__ import annotations

from unittest.mock import Mock

import pytest

from netwarden.checks import CleartextProtocolCheck, KnownVulnerabilityCheck
from netwarden.engine import Assessment
from netwarden.events import EventBus, FindingRaised, ScanFinished
from netwarden.fingerprint import Fingerprinter
from netwarden.knowledge import KnowledgeBase
from netwarden.models import Host, Service, Severity
from netwarden.scope import Scope, ScopeError


class FakeScanner:
    """A stub: returns canned hosts instead of touching the network."""

    def __init__(self, hosts):
        self.hosts = hosts
        self.calls = []

    async def scan(self, addresses, ports):
        self.calls.append((list(addresses), list(ports)))
        return self.hosts


def make_assessment(hosts, bus=None):
    kb = KnowledgeBase.load()
    scanner = FakeScanner(hosts)
    checks = [KnownVulnerabilityCheck(kb), CleartextProtocolCheck()]
    return Assessment(Scope(["10.0.0.0/24"]), scanner, Fingerprinter(), checks, bus), scanner


def test_pipeline_fingerprints_checks_and_sorts():
    hosts = [Host("10.0.0.5", [Service(23, "\xff\xfd\x18"), Service(21, "220 (vsFTPd 2.3.4)")])]
    assessment, scanner = make_assessment(hosts)
    result = assessment.run(["10.0.0.5"], [21, 23])
    assert scanner.calls == [(["10.0.0.5"], [21, 23])]
    assert [f.severity for f in result.findings] == [Severity.CRITICAL, Severity.MEDIUM, Severity.MEDIUM]
    assert result.findings[0].cve == "CVE-2011-2523"
    assert result.finished is not None


def test_events_are_published_to_observers():
    bus = EventBus()
    spy = Mock()
    bus.subscribe(FindingRaised, spy)
    bus.subscribe(ScanFinished, spy)
    assessment, _ = make_assessment([Host("10.0.0.5", [Service(23, "\xff\xfd")])], bus)
    assessment.run(["10.0.0.5"], [23])
    kinds = [type(c.args[0]).__name__ for c in spy.call_args_list]
    assert kinds == ["FindingRaised", "ScanFinished"]


def test_out_of_scope_target_never_reaches_the_scanner():
    assessment, scanner = make_assessment([])
    with pytest.raises(ScopeError):
        assessment.run(["192.168.1.1"], [22])
    assert scanner.calls == []
