"""Security checks. Each check is a strategy: it looks at one service and returns findings.

Adding a check means writing one class and registering it; nothing else changes (open/closed principle).
"""
from __future__ import annotations

from typing import Protocol

from .knowledge import KnowledgeBase
from .models import Finding, Host, Service, Severity


class Check(Protocol):
    """The interface every check implements."""

    id: str

    def run(self, host: Host, service: Service) -> list[Finding]: ...


class KnownVulnerabilityCheck:
    """Match the fingerprinted product and version against the knowledge base."""

    id = "NW-KNOWN-VULN"

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def run(self, host: Host, service: Service) -> list[Finding]:
        return [
            Finding(host.address, service.port, self.id, v.title, Severity.from_cvss(v.cvss),
                    evidence=f"{service.product} {service.version} reported in banner",
                    remediation=v.remediation, cvss=v.cvss, cve=v.id)
            for v in self.kb.lookup(service.product, service.version)
        ]


class CleartextProtocolCheck:
    """Telnet and FTP send passwords unencrypted."""

    id = "NW-CLEARTEXT"
    ADVICE = {"telnet": "Disable Telnet and use SSH instead.",
              "ftp": "Replace FTP with SFTP or FTPS, or restrict it to a trusted network."}

    def run(self, host: Host, service: Service) -> list[Finding]:
        if service.name not in self.ADVICE:
            return []
        return [Finding(host.address, service.port, self.id, f"Cleartext protocol: {service.name}",
                        Severity.MEDIUM, evidence=f"{service.name} is listening on port {service.port}",
                        remediation=self.ADVICE[service.name])]


class ExposedDatabaseCheck:
    """Databases should not be reachable from the network being scanned."""

    id = "NW-EXPOSED-DB"
    NAMES = {"mysql": "MySQL", "postgresql": "PostgreSQL", "redis": "Redis", "mongodb": "MongoDB"}

    def run(self, host: Host, service: Service) -> list[Finding]:
        if service.name not in self.NAMES:
            return []
        db = self.NAMES[service.name]
        return [Finding(host.address, service.port, self.id, f"{db} reachable over the network", Severity.HIGH,
                        evidence=f"TCP port {service.port} accepted a connection",
                        remediation=f"Bind {db} to localhost or a private interface, require authentication, "
                                    f"and allow only application servers through the firewall.")]


class HttpHeadersCheck:
    """Look for missing security headers in an HTTP response banner."""

    id = "NW-HTTP-HEADERS"
    WANTED = ("X-Content-Type-Options", "Content-Security-Policy")

    def run(self, host: Host, service: Service) -> list[Finding]:
        if not service.banner.startswith("HTTP/"):
            return []
        present = {line.split(":", 1)[0].strip().lower() for line in service.banner.splitlines()[1:] if ":" in line}
        missing = [h for h in self.WANTED if h.lower() not in present]
        if not missing:
            return []
        return [Finding(host.address, service.port, self.id, "Missing HTTP security headers", Severity.LOW,
                        evidence="Missing: " + ", ".join(missing),
                        remediation="Add the missing headers in the web server or application configuration.")]


class VersionDisclosureCheck:
    """Banners that reveal exact versions help attackers choose exploits."""

    id = "NW-VERSION-DISCLOSURE"

    def run(self, host: Host, service: Service) -> list[Finding]:
        if not service.version:
            return []
        return [Finding(host.address, service.port, self.id, "Service discloses its version", Severity.INFO,
                        evidence=f"{service.product} {service.version}",
                        remediation="Reduce banner detail where the software allows it (for example ServerTokens Prod "
                                    "in Apache, server_tokens off in nginx).")]


def default_checks(kb: KnowledgeBase) -> list[Check]:
    return [KnownVulnerabilityCheck(kb), CleartextProtocolCheck(), ExposedDatabaseCheck(),
            HttpHeadersCheck(), VersionDisclosureCheck()]
