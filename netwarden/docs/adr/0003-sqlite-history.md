# ADR-0003: SQLite for scan history, behind a repository

* Status: Accepted
* Date: 2026-10-05

## Context

US-7 needs scan results kept between runs and compared. Options: JSON files per scan, SQLite, or a
database server such as PostgreSQL.

## Decision

SQLite through `ScanRepository`. One file, no server, transactions included, and queries for history.

## Consequences

* Positive: zero administration; easy to back up; the rest of the code never sees SQL.
* Negative: not suited to many concurrent writers. If NetWarden becomes a shared service, replace the
  repository with a PostgreSQL implementation; callers do not change.
