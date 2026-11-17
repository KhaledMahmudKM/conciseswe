"""Authorised scope: NetWarden refuses to touch any address outside it.

Requirement NW-SR-1: the tool must only scan networks the operator is authorised to test.
"""
from __future__ import annotations

import ipaddress
from collections.abc import Iterable, Iterator
from pathlib import Path

MAX_HOSTS = 1024  # NW-SR-2: guard against accidentally scanning huge ranges


class ScopeError(Exception):
    """A target is outside the authorised scope, or the request is too large."""


Network = ipaddress.IPv4Network | ipaddress.IPv6Network


class Scope:
    """A set of networks the operator is allowed to assess."""

    def __init__(self, networks: Iterable[str]):
        self.networks: list[Network] = [ipaddress.ip_network(n.strip(), strict=False) for n in networks if n.strip()]
        if not self.networks:
            raise ScopeError("The scope is empty: list at least one authorised network")

    @classmethod
    def from_file(cls, path: str | Path) -> Scope:
        """Read one network per line; '#' starts a comment."""
        lines = Path(path).read_text(encoding="utf-8").splitlines()
        return cls(line.split("#", 1)[0] for line in lines)

    def allows(self, address: str) -> bool:
        ip = ipaddress.ip_address(address)
        return any(ip in net for net in self.networks)

    def expand(self, targets: Iterable[str]) -> list[str]:
        """Turn targets (addresses or CIDR blocks) into addresses, all inside the scope."""
        addresses: list[str] = []
        for target in targets:
            for ip in _hosts(target):
                if not self.allows(ip):
                    raise ScopeError(f"{ip} is outside the authorised scope")
                addresses.append(ip)
                if len(addresses) > MAX_HOSTS:
                    raise ScopeError(f"More than {MAX_HOSTS} hosts requested; split the assessment")
        return list(dict.fromkeys(addresses))  # remove duplicates, keep order


def _hosts(target: str) -> Iterator[str]:
    try:
        net = ipaddress.ip_network(target, strict=False)
    except ValueError as exc:
        raise ScopeError(f"Not an IP address or network: {target!r}") from exc
    if net.num_addresses == 1:
        yield str(net.network_address)
    else:
        yield from (str(ip) for ip in net.hosts())
