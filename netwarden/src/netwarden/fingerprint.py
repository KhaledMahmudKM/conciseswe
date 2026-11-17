"""Identify the product and version behind a banner."""
from __future__ import annotations

import re
from dataclasses import dataclass

from .models import Service

WELL_KNOWN = {21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns", 80: "http", 110: "pop3", 143: "imap",
              443: "https", 445: "smb", 3306: "mysql", 3389: "rdp", 5432: "postgresql", 6379: "redis",
              8080: "http", 8443: "https", 27017: "mongodb"}


@dataclass(frozen=True)
class Rule:
    name: str          # service name, such as "ssh"
    product: str       # product name used by the knowledge base
    pattern: re.Pattern[str]


RULES = [
    Rule("ssh", "OpenSSH", re.compile(r"^SSH-[\d.]+-OpenSSH_([\w.]+)")),
    Rule("ftp", "vsftpd", re.compile(r"^220.*\(vsFTPd ([\d.]+)\)")),
    Rule("ftp", "ProFTPD", re.compile(r"^220 ProFTPD ([\w.]+)")),
    Rule("http", "Apache httpd", re.compile(r"^Server: Apache/([\d.]+)", re.M)),
    Rule("http", "nginx", re.compile(r"^Server: nginx/([\d.]+)", re.M)),
    Rule("mysql", "MySQL", re.compile(r"^.{4}\n([\d.]+)[^\x00]*\x00", re.S)),   # MySQL handshake packet
]


class Fingerprinter:
    """Fill in name, product and version on a Service from its banner."""

    def __init__(self, rules: list[Rule] | None = None):
        self.rules = rules if rules is not None else RULES

    def identify(self, service: Service) -> Service:
        for rule in self.rules:
            match = rule.pattern.search(service.banner)
            if match:
                service.name, service.product, service.version = rule.name, rule.product, match.group(1)
                return service
        if service.banner.startswith("SSH-"):
            service.name = "ssh"
        elif service.banner.startswith("\xff"):           # Telnet option negotiation (IAC)
            service.name = "telnet"
        elif service.banner.startswith("HTTP/"):
            service.name = "http"
        else:
            service.name = WELL_KNOWN.get(service.port, "unknown")
        return service
