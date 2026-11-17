"""Unit tests: small, fast, no network."""
from __future__ import annotations

import pytest

from netwarden.checks import (
    CleartextProtocolCheck,
    ExposedDatabaseCheck,
    HttpHeadersCheck,
    KnownVulnerabilityCheck,
    VersionDisclosureCheck,
)
from netwarden.fingerprint import Fingerprinter
from netwarden.knowledge import KnowledgeBase, version_key
from netwarden.models import Host, ScanResult, Service, Severity
from netwarden.scanner import parse_ports
from netwarden.scope import MAX_HOSTS, Scope, ScopeError

from .conftest import make_finding


# --- models ---------------------------------------------------------------
@pytest.mark.parametrize("score, expected", [
    (0.0, Severity.INFO), (0.1, Severity.LOW), (3.9, Severity.LOW), (4.0, Severity.MEDIUM),
    (6.9, Severity.MEDIUM), (7.0, Severity.HIGH), (8.9, Severity.HIGH),
    (9.0, Severity.CRITICAL), (10.0, Severity.CRITICAL),
])
def test_severity_from_cvss_boundaries(score, expected):
    assert Severity.from_cvss(score) == expected


def test_result_counts_and_worst():
    r = ScanResult(["10.0.0.5"], findings=[make_finding(severity=Severity.LOW), make_finding(23, Severity.HIGH)])
    assert r.counts()["HIGH"] == 1 and r.counts()["LOW"] == 1 and r.counts()["CRITICAL"] == 0
    assert r.worst() == Severity.HIGH
    assert ScanResult(["x"]).worst() is None


# --- scope ----------------------------------------------------------------
def test_scope_expands_networks_to_hosts():
    scope = Scope(["192.168.56.0/24"])
    assert scope.expand(["192.168.56.8/30"]) == ["192.168.56.9", "192.168.56.10"]
    assert scope.expand(["192.168.56.5", "192.168.56.5"]) == ["192.168.56.5"]


def test_scope_refuses_targets_outside_it():
    with pytest.raises(ScopeError, match="outside the authorised scope"):
        Scope(["192.168.56.0/24"]).expand(["8.8.8.8"])


def test_scope_refuses_huge_requests():
    with pytest.raises(ScopeError, match=str(MAX_HOSTS)):
        Scope(["10.0.0.0/8"]).expand(["10.0.0.0/16"])


@pytest.mark.parametrize("bad", ["not-an-ip", "300.1.1.1", ""])
def test_scope_rejects_bad_targets(bad):
    with pytest.raises(ScopeError):
        Scope(["10.0.0.0/8"]).expand([bad])


def test_scope_file_ignores_comments(tmp_path):
    f = tmp_path / "scope.txt"
    f.write_text("# lab\n10.1.0.0/16  # servers\n\n", encoding="utf-8")
    assert Scope.from_file(f).allows("10.1.2.3")
    f.write_text("# nothing\n", encoding="utf-8")
    with pytest.raises(ScopeError, match="empty"):
        Scope.from_file(f)


# --- ports ----------------------------------------------------------------
def test_parse_ports():
    assert parse_ports("22, 80,20-21") == [20, 21, 22, 80]
    assert 443 in parse_ports("top")
    for bad in ("0", "70000", ","):
        with pytest.raises(ValueError):
            parse_ports(bad)


# --- fingerprinting -------------------------------------------------------
@pytest.mark.parametrize("port, banner, name, product, version", [
    (22, "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6", "ssh", "OpenSSH", "8.9p1"),
    (21, "220 (vsFTPd 2.3.4)", "ftp", "vsftpd", "2.3.4"),
    (21, "220 ProFTPD 1.3.5a Server (Debian)", "ftp", "ProFTPD", "1.3.5a"),
    (80, "HTTP/1.1 200 OK\r\nServer: Apache/2.4.49 (Unix)", "http", "Apache httpd", "2.4.49"),
    (80, "HTTP/1.1 200 OK\r\nServer: nginx/1.18.0", "http", "nginx", "1.18.0"),
    (3306, "J\x00\x00\x00\n8.0.28\x00\x00\x00", "mysql", "MySQL", "8.0.28"),
    (2323, "\xff\xfd\x18login: ", "telnet", None, None),
    (6379, "", "redis", None, None),
    (40000, "", "unknown", None, None),
])
def test_fingerprint(port, banner, name, product, version):
    s = Fingerprinter().identify(Service(port, banner))
    assert (s.name, s.product, s.version) == (name, product, version)


# --- knowledge base -------------------------------------------------------
def test_version_key_orders_real_versions():
    assert version_key("8.5p1") < version_key("8.9p1") < version_key("9.8p1")
    assert version_key("1.3.5") < version_key("1.3.5a") < version_key("1.3.6")
    assert version_key("2.4.9") < version_key("2.4.49")      # not string comparison


@pytest.mark.parametrize("version, affected", [("8.4p1", False), ("8.5p1", True), ("9.7p1", True), ("9.8p1", False)])
def test_regresshion_range(version, affected):
    ids = [v.id for v in KnowledgeBase.load().lookup("OpenSSH", version)]
    assert ("CVE-2024-6387" in ids) is affected


def test_apache_2_4_50_has_only_the_second_cve():
    assert [v.id for v in KnowledgeBase.load().lookup("Apache httpd", "2.4.50")] == ["CVE-2021-42013"]


# --- checks ---------------------------------------------------------------
def test_known_vulnerability_check(host):
    findings = KnownVulnerabilityCheck(KnowledgeBase.load()).run(host, host.services[0])
    assert [(f.cve, f.severity) for f in findings] == [("CVE-2024-6387", Severity.HIGH)]


def test_known_vulnerability_check_ignores_unknown_versions():
    h = Host("10.0.0.6", [Service(22, "SSH-2.0-Foo", "ssh")])
    assert KnownVulnerabilityCheck(KnowledgeBase.load()).run(h, h.services[0]) == []


def test_cleartext_and_database_checks():
    h = Host("10.0.0.7", [Service(23, name="telnet"), Service(3306, name="mysql"), Service(22, name="ssh")])
    assert [f.title for s in h.services for f in CleartextProtocolCheck().run(h, s)] == ["Cleartext protocol: telnet"]
    assert [f.severity for s in h.services for f in ExposedDatabaseCheck().run(h, s)] == [Severity.HIGH]


def test_http_headers_check():
    h = Host("10.0.0.8")
    weak = Service(80, "HTTP/1.1 200 OK\r\nServer: x")
    good = Service(80, "HTTP/1.1 200 OK\r\nX-Content-Type-Options: nosniff\r\n"
                       "Content-Security-Policy: default-src 'self'")
    assert "Content-Security-Policy" in HttpHeadersCheck().run(h, weak)[0].evidence
    assert HttpHeadersCheck().run(h, good) == []


def test_version_disclosure_is_informational(host):
    assert VersionDisclosureCheck().run(host, host.services[0])[0].severity == Severity.INFO
