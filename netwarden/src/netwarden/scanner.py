"""Discovery: find open TCP ports and grab service banners, concurrently and politely."""
from __future__ import annotations

import asyncio
from collections.abc import Iterable

from .models import Host, Service

TOP_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 6379, 8080, 8443, 27017]
HTTP_PROBE = b"HEAD / HTTP/1.0\r\n\r\n"


class TcpScanner:
    """Connect scan with a concurrency limit and timeouts (NW-NFR-3: be gentle with networks)."""

    def __init__(self, timeout: float = 1.0, concurrency: int = 100):
        self.timeout = timeout
        self.concurrency = concurrency

    async def scan(self, addresses: Iterable[str], ports: Iterable[int]) -> list[Host]:
        """Scan every port on every address; return only hosts with at least one open port."""
        sem = asyncio.Semaphore(self.concurrency)
        ports = list(ports)
        addresses = list(addresses)
        jobs = [self._probe(sem, a, p) for a in addresses for p in ports]
        results = await asyncio.gather(*jobs)
        hosts: dict[str, Host] = {}
        for address, service in results:
            if service is not None:
                hosts.setdefault(address, Host(address)).services.append(service)
        for host in hosts.values():
            host.services.sort(key=lambda s: s.port)
        return [hosts[a] for a in addresses if a in hosts]

    async def _probe(self, sem: asyncio.Semaphore, address: str, port: int) -> tuple[str, Service | None]:
        async with sem:
            try:
                reader, writer = await asyncio.wait_for(asyncio.open_connection(address, port), self.timeout)
            except (TimeoutError, OSError):
                return address, None
            try:
                banner = await self._banner(reader, writer, port)
            finally:
                writer.close()
                try:
                    await writer.wait_closed()
                except OSError:
                    pass
            return address, Service(port=port, banner=banner)

    async def _banner(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, port: int) -> str:
        """Many services greet first (SSH, FTP, SMTP). If a service stays silent, try an HTTP request."""
        data = b""
        try:
            data = await asyncio.wait_for(reader.read(1024), self.timeout / 2)
        except TimeoutError:
            pass
        if not data:
            writer.write(HTTP_PROBE)
            await writer.drain()
            try:
                data = await asyncio.wait_for(reader.read(2048), self.timeout)
            except TimeoutError:
                pass
        return data.decode("latin-1", errors="replace").strip()


def parse_ports(spec: str) -> list[int]:
    """'top', '22,80', or '20-25,8080' to a sorted list of ports."""
    if spec == "top":
        return list(TOP_PORTS)
    ports: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = (int(x) for x in part.split("-", 1))
            ports.update(range(lo, hi + 1))
        elif part:
            ports.add(int(part))
    if not ports or min(ports) < 1 or max(ports) > 65535:
        raise ValueError(f"Invalid port specification: {spec!r}")
    return sorted(ports)
