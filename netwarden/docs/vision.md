# NetWarden: product vision

**For** small IT teams, lab administrators and students
**who** need to know which services on their networks are exposed and vulnerable,
**NetWarden** is a command-line assessment tool
**that** discovers services, matches them against known vulnerabilities, and explains how to fix each problem.
**Unlike** full commercial scanners, it is small, free, auditable, and safe by default:
it refuses to scan anything outside an explicit, authorised scope.

## Goals

1. Find exposed services and known-vulnerable versions on an authorised network in minutes.
2. Explain every finding in plain language with a concrete remediation step.
3. Show progress over time: what was fixed and what is new since the last scan.
4. Be easy to run in automation (exit codes, JSON output, a container image).

## Non-goals

* Exploiting vulnerabilities or proving that they are exploitable.
* Scanning networks without authorisation, stealth scanning, or evading detection.
* Replacing a full vulnerability management platform.

## Stakeholders

| Stakeholder | Interest |
|---|---|
| Network administrator (primary user) | Fast, accurate findings and clear fixes |
| Security manager | Trends, severity summary, evidence for audits |
| Asset owner | Assurance that scans will not disrupt services |
| Instructor and students | A realistic, safe project to learn from |
| Network operations | No floods of traffic, predictable scan windows |
