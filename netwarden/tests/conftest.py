"""Shared fixtures. The demo targets run in a background thread with their own event loop."""
from __future__ import annotations

import asyncio
import threading
from collections.abc import Iterator

import pytest

from netwarden.demo import bound_port, start_demo
from netwarden.models import Finding, Host, Service, Severity


@pytest.fixture(scope="session")
def demo_ports() -> Iterator[dict[str, int]]:
    """Start the fake services on free ports; yield {service name: port}."""
    loop = asyncio.new_event_loop()
    ready = threading.Event()
    ports: dict[str, int] = {}

    def run() -> None:
        asyncio.set_event_loop(loop)
        servers = loop.run_until_complete(start_demo(port_offset=-1))
        ports.update({svc.name.split()[0]: bound_port(server) for svc, server in servers})
        ready.set()
        loop.run_forever()
        for _, server in servers:
            server.close()
            loop.run_until_complete(server.wait_closed())
        loop.close()

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    assert ready.wait(5), "demo services did not start"
    yield ports
    loop.call_soon_threadsafe(loop.stop)
    thread.join(5)


@pytest.fixture
def scope_file(tmp_path):
    path = tmp_path / "scope.txt"
    path.write_text("# lab only\n127.0.0.1/32\n", encoding="utf-8")
    return path


def make_finding(port: int = 22, severity: Severity = Severity.HIGH, cve: str | None = "CVE-2024-6387") -> Finding:
    return Finding("10.0.0.5", port, "NW-TEST", "test finding", severity, "evidence", "fix it", 8.1, cve)


@pytest.fixture
def host() -> Host:
    return Host("10.0.0.5", [Service(22, "SSH-2.0-OpenSSH_9.6p1", "ssh", "OpenSSH", "9.6p1")])
