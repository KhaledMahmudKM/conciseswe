# NetWarden: software requirements specification (excerpt)

Version 1.0. Requirement identifiers are referenced from code comments, tests and commits.

## 1. Purpose and scope

NetWarden assesses hosts on networks the operator is authorised to test. See `vision.md`.

## 2. Functional requirements

| ID | Requirement | Priority | Verified by |
|---|---|---|---|
| NW-FR-1 | The system shall accept targets as IPv4/IPv6 addresses or CIDR blocks. | Must | test_scope_* |
| NW-FR-2 | The system shall detect open TCP ports from a configurable list (default: common ports). | Must | test_end_to_end_findings |
| NW-FR-3 | The system shall record each open service's banner and identify product and version where possible. | Must | test_fingerprint |
| NW-FR-4 | The system shall report known vulnerabilities for identified versions, with CVE ID, CVSS score and severity. | Must | test_known_vulnerability_check |
| NW-FR-5 | The system shall flag cleartext protocols, exposed databases and missing HTTP security headers. | Should | test_cleartext_and_database_checks |
| NW-FR-6 | Every finding shall include evidence and a remediation step. | Must | test_reports_render |
| NW-FR-7 | The system shall produce reports in Markdown, JSON and HTML. | Must | test_reports_render |
| NW-FR-8 | The system shall store scan results and list previous scans. | Should | test_history_and_diff |
| NW-FR-9 | The system shall compare two scans and list new, resolved and unchanged findings. | Should | test_history_and_diff |
| NW-FR-10 | The system shall exit with status 1 when findings meet a chosen severity threshold. | Should | test_cli_scan_exit_codes |

## 3. Security and safety requirements

| ID | Requirement | Priority |
|---|---|---|
| NW-SR-1 | The system shall refuse any target outside the authorised scope file, before sending any packet. | Must |
| NW-SR-2 | The system shall refuse requests of more than 1024 hosts. | Must |
| NW-SR-3 | The system shall not attempt to exploit, log in to, or change any target. | Must |
| NW-SR-4 | Reports shall escape all data taken from the network (HTML injection). | Must |

## 4. Non-functional requirements

| ID | Quality | Requirement |
|---|---|---|
| NW-NFR-1 | Performance | A /24 network on the 17 default ports shall complete in under 60 s on a LAN. |
| NW-NFR-2 | Portability | Runs on Linux, macOS and Windows with Python 3.11 or later and no third-party packages. |
| NW-NFR-3 | Politeness | At most 100 concurrent connections; each connection times out after 1 s by default. |
| NW-NFR-4 | Maintainability | Adding a check requires one new class and no changes to the engine. Test coverage of at least 90%. |
| NW-NFR-5 | Usability | A first-time user can run the demo scan by following the README in under 5 minutes. |

## 5. Constraints and assumptions

* Version detection relies on banners; distributions that backport fixes may cause false positives.
* The bundled knowledge base is a sample; production use needs a maintained feed (ADR-0002).
