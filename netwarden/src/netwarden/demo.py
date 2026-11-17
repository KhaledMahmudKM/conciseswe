"""Safe practice targets: fake services on 127.0.0.1 that only send banners.

Nothing here is vulnerable; the banners merely claim old versions, so NetWarden has something to find.
"""
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

HTTP_RESPONSE = (b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.49 (Unix)\r\nContent-Type: text/html\r\n"
                 b"Content-Length: 0\r\nConnection: close\r\n\r\n")


@dataclass(frozen=True)
class DemoService:
    name: str
    port: int
    greeting: bytes          # sent as soon as a client connects
    reply: bytes = b""       # sent after the client sends something (HTTP)


DEMO_SERVICES = [
    DemoService("ftp (vsftpd 2.3.4)", 2121, b"220 (vsFTPd 2.3.4)\r\n"),
    DemoService("ssh (OpenSSH 8.9p1)", 2222, b"SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6\r\n"),
    DemoService("telnet", 2323, b"\xff\xfd\x18\xff\xfd\x20login: "),
    DemoService("http (Apache 2.4.49)", 8080, b"", HTTP_RESPONSE),
    DemoService("mysql (8.0.28)", 13306, b"J\x00\x00\x00\n8.0.28\x00" + b"\x00" * 20),
]


def _handler(svc: DemoService) -> Callable[[asyncio.StreamReader, asyncio.StreamWriter], Awaitable[None]]:
    async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            if svc.greeting:
                writer.write(svc.greeting)
                await writer.drain()
            if svc.reply:
                await asyncio.wait_for(reader.read(1024), 2)
                writer.write(svc.reply)
                await writer.drain()
            else:
                await asyncio.sleep(0.2)
        except (TimeoutError, OSError):
            pass
        finally:
            writer.close()
    return handle


async def start_demo(host: str = "127.0.0.1", port_offset: int = 0,
                     services: list[DemoService] | None = None) -> list[tuple[DemoService, asyncio.Server]]:
    """Start the demo services. With port_offset=-1 the OS picks free ports (used by the tests)."""
    started = []
    for svc in services or DEMO_SERVICES:
        port = 0 if port_offset < 0 else svc.port + port_offset
        server = await asyncio.start_server(_handler(svc), host, port)
        started.append((svc, server))
    return started


def bound_port(server: asyncio.Server) -> int:
    port: int = server.sockets[0].getsockname()[1]
    return port


async def serve_forever(host: str = "127.0.0.1", port_offset: int = 0) -> None:
    servers = await start_demo(host, port_offset)
    print("NetWarden demo targets (fake banners, nothing is really vulnerable):")
    for svc, server in servers:
        print(f"  {host}:{bound_port(server):<6} {svc.name}")
    ports = ",".join(str(bound_port(s)) for _, s in servers)
    print(f"\nIn another terminal:\n  netwarden scan {host} --scope examples/lab-scope.txt --ports {ports}")
    print("Press Ctrl+C to stop.")
    await asyncio.gather(*(s.serve_forever() for _, s in servers))
