# NetWarden: architecture overview

NetWarden is a layered pipeline. The command-line interface (presentation) calls the
`Assessment` engine (application), which coordinates domain components (scope, scanner,
fingerprinter, checks, knowledge base) and infrastructure (reporters, SQLite repository).

```text
cli.py ──> engine.Assessment ──> scope.Scope           (authorisation)
                              ──> scanner.TcpScanner    (asyncio TCP connect + banners)
                              ──> fingerprint.Fingerprinter
                              ──> checks.Check (strategy)  ──> knowledge.KnowledgeBase
                              ──> events.EventBus (observer) ──> progress printers
cli.py ──> report.get_reporter (factory) ──> Markdown | JSON | HTML
cli.py ──> store.ScanRepository (repository, SQLite) ──> diff()
```

Design patterns: strategy (checks, reporters), observer (event bus), factory (reporters),
repository (scan history), facade (Assessment), dependency injection (Assessment's constructor).

Decisions are recorded in `adr/`. Diagrams are in the book, Chapters 4 and 7.
