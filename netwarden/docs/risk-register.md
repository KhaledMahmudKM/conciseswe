# NetWarden: project risk register

Probability and impact on a 1 to 5 scale; exposure = probability x impact.

| ID | Risk | P | I | Exposure | Response | Owner |
|---|---|---|---|---|---|---|
| R1 | The tool is used against networks without authorisation | 2 | 5 | 10 | Avoid: scope enforcement, warnings in docs and CLI | Product owner |
| R2 | Banner-based detection gives false positives (backports) | 4 | 3 | 12 | Mitigate: show evidence; backlog item US-11 | Tech lead |
| R3 | Knowledge base becomes outdated | 5 | 3 | 15 | Mitigate: adapter for live feeds (US-10); dated releases | Tech lead |
| R4 | Scans disrupt fragile devices (printers, PLCs) | 2 | 4 | 8 | Mitigate: low concurrency, timeouts, scheduled windows | Operations |
| R5 | Key developer leaves mid-project | 2 | 3 | 6 | Mitigate: pair programming, code review, documentation | Team lead |
| R6 | Scope creep (exploitation, GUI) delays release 1.0 | 3 | 3 | 9 | Avoid: non-goals in vision; backlog prioritisation | Product owner |
