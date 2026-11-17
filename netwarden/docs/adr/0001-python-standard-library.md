# ADR-0001: Python with the standard library only, asyncio for scanning

* Status: Accepted
* Date: 2026-09-14

## Context

NetWarden must run on lab machines and servers we do not control (NW-NFR-2), be easy for students to
read, and scan hundreds of ports quickly without flooding networks (NW-NFR-1, NW-NFR-3).

## Options

1. Python with third-party libraries (for example scapy, rich, SQLAlchemy).
2. Python with the standard library only, using asyncio for concurrent connections.
3. Go, compiled to a single binary.

## Decision

Option 2. asyncio gives hundreds of concurrent connections in one thread; `ipaddress`, `sqlite3`,
`json` and `argparse` cover the rest.

## Consequences

* Positive: no dependency installation or supply-chain risk at run time; readable code.
* Negative: no raw-packet (SYN) scanning, so scans are TCP connect scans and are logged by targets.
  Development tools (pytest, ruff, mypy) are still dependencies, but only for developers.
