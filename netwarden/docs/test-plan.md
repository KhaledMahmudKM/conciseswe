# NetWarden: test plan (summary)

| Level | What | Where | Runs |
|---|---|---|---|
| Unit | Models, scope, port parsing, fingerprints, version comparison, each check | `tests/test_units.py` | Every commit |
| Component | Engine pipeline with a fake scanner (stub) and spy observers (mock) | `tests/test_engine.py` | Every commit |
| Integration | Real sockets against demo targets; reports; SQLite history; CLI exit codes | `tests/test_integration.py` | Every commit |
| Static | Lint (ruff, including security rules), strict typing (mypy) | CI `lint` job | Every commit |
| System | Scan of a lab VLAN with known hosts; compare with expected inventory | Manual checklist | Each release |
| Acceptance | Gherkin scenarios for user stories (see `user-stories.md`) | Manual, then automated | Each sprint review |

Entry criteria: code compiles, lint passes. Exit criteria for a release: all automated tests pass on
Python 3.11 to 3.13, coverage at least 90%, no open defects of severity High or Critical.

Test design techniques used: equivalence partitioning and boundary values (CVSS to severity,
version ranges, port numbers), decision tables (exit codes), and error guessing (empty scope,
bad targets).
