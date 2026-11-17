# NetWarden

A small, defensive network assessment tool, and the running example of the
[Concise Book on Software Engineering](https://khaledmahmudkm.github.io/conciseswe/).

NetWarden discovers open TCP services on hosts **you are authorised to assess**, identifies the
software behind them from their banners, matches versions against a knowledge base of known
vulnerabilities, and writes a report with remediation advice. It keeps a history of scans so you
can see what was fixed and what is new.

> **Use it only on networks you own or have written permission to test.** NetWarden enforces this
> with a scope file: it refuses any target outside it.

## Install

```bash
cd netwarden
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

NetWarden itself uses only the Python standard library (3.11 or later).

## Try it safely

`netwarden demo` starts fake services on 127.0.0.1 that only send old-looking banners:

```bash
netwarden demo                       # terminal 1
netwarden scan 127.0.0.1 --scope examples/lab-scope.txt \
    --ports 2121,2222,2323,8080,13306 --format html --output report.html     # terminal 2
netwarden history
netwarden diff 1 2
```

Exit status: `0` no findings at or above `--fail-on` (default `high`), `1` such findings exist,
`2` error (for example a target outside the scope). This makes NetWarden usable in scripts and CI.

## Develop

```bash
pytest --cov          # 46 tests, about 95% coverage
ruff check src tests  # lint
mypy                  # type check (strict)
docker build -t netwarden .
```

## Project documents

| Document | Book chapter |
|---|---|
| [docs/vision.md](docs/vision.md) | 1 |
| [docs/requirements.md](docs/requirements.md) | 3 |
| [docs/user-stories.md](docs/user-stories.md) | 3, 16 |
| [docs/architecture.md](docs/architecture.md) | 4, 7 |
| [docs/adr/](docs/adr/) | 7 |
| [docs/test-plan.md](docs/test-plan.md) | 11 |
| [docs/threat-model.md](docs/threat-model.md) | 12 |
| [docs/risk-register.md](docs/risk-register.md) | 16 |
| [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md) | 8, 13 |
| [SECURITY.md](SECURITY.md) | 12 |

## Limitations

Version matching uses banners, so it can report false positives when a Linux distribution
backports a security fix without changing the version string, and false negatives when a banner is
hidden. The bundled knowledge base is a small teaching sample. See the book, Chapter 15.

MIT licence. © 2026 Khaled Mahmud.
