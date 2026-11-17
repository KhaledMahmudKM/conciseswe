# ADR-0002: A bundled, offline vulnerability knowledge base behind an interface

* Status: Accepted
* Date: 2026-09-21

## Context

Matching versions to vulnerabilities needs data. Online sources (NVD API, OSV) are complete but need
network access, have rate limits, and make tests non-deterministic.

## Decision

Ship a small JSON knowledge base inside the package and access it only through `KnowledgeBase.lookup()`.
A future adapter can load a full feed through the same interface (US-10).

## Consequences

* Positive: works offline and in air-gapped labs; tests are repeatable.
* Negative: the sample is incomplete and goes out of date; the README and reports must say so.
