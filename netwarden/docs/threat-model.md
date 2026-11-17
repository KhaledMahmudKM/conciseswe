# NetWarden: threat model (STRIDE)

Assets: the scope file, scan results (a map of weaknesses, sensitive), the history database, and the
networks being scanned. Trust boundary: everything received from the network is untrusted.

| STRIDE | Threat | Mitigation |
|---|---|---|
| Spoofing | A target sends a fake banner to cause false findings or hide real ones | Treat findings as indicators; report evidence; document limitation |
| Tampering | Someone edits the scope file to include unauthorised networks | Keep scope files under version control and review; record targets in history |
| Repudiation | An operator denies having run a scan | Scan history records time and targets |
| Information disclosure | Reports and the history database reveal vulnerabilities | Store reports with restricted permissions; do not commit them; the container runs as a non-root user |
| Denial of service | A large or aggressive scan disrupts a network | Concurrency limit, timeouts, 1024-host limit (NW-NFR-3, NW-SR-2) |
| Elevation of privilege | Malicious banner content injects HTML or script into the report | All network data is escaped in HTML reports (NW-SR-4) |
