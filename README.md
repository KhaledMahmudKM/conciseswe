# Concise Book on Software Engineering

A concise, diagram-rich guide to software engineering for third-year undergraduates: process models and agile methods, requirements, UML and C4 modelling, design principles and patterns, architecture, version control, clean code, refactoring, testing, quality and secure development, CI/CD, DevOps, maintenance, project management, and professional ethics.

**Read it online:** https://khaledmahmudkm.github.io/conciseswe/

## The running example: NetWarden

The [`netwarden/`](netwarden/) folder holds the book's running project, a small, defensive network assessment tool written in Python with only the standard library. It discovers services on hosts you are **authorised** to assess, identifies product versions, matches them against known vulnerabilities, reports remediation advice, and compares scans over time.

It comes with everything the book discusses: vision, requirements, user stories, architecture notes, ADRs, a test plan, a threat model, a risk register, 46 automated tests, a CI workflow ([`.github/workflows/netwarden.yml`](.github/workflows/netwarden.yml)), Dependabot configuration, and a Dockerfile. See [`netwarden/README.md`](netwarden/README.md) to install and run it, including harmless practice targets on your own machine.

> Scan only networks you own or have written permission to test.

## How this repository works

* `chapters/` holds one Markdown file per chapter, with diagrams embedded as SVG, and `chapters.json` for the table of contents.
* `book.json` holds the title, author and palette (`clay`).
* `index.html` loads the shared reader, [bookengine](https://github.com/khaledmahmudkm/bookengine) 1.0.6, from jsDelivr. When opened from a local web server, it uses `../bookengine-git/` instead if that folder exists.

To preview locally, serve the parent folder (the one containing both `conciseswe-git` and `bookengine-git`):

```bash
python3 -m http.server 8000
# then open http://localhost:8000/conciseswe-git/
```

© 2026 Khaled Mahmud. NetWarden is released under the MIT licence.
