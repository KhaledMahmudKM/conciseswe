# NetWarden: product backlog (user stories)

Estimates are story points (Fibonacci). Sprint numbers refer to the plan in the book, Chapter 16.

| ID | Story | Points | Sprint |
|---|---|---|---|
| US-1 | As an administrator, I want to define the networks I am allowed to scan, so that I never scan someone else's systems by mistake. | 3 | 1 |
| US-2 | As an administrator, I want to scan a network for open ports, so that I know what is exposed. | 5 | 1 |
| US-3 | As an administrator, I want to see which software and version runs on each port, so that I can judge its risk. | 5 | 1 |
| US-4 | As an administrator, I want known vulnerabilities flagged with severity, so that I fix the worst first. | 8 | 2 |
| US-5 | As an administrator, I want each finding to say how to fix it, so that I do not need to research every CVE. | 3 | 2 |
| US-6 | As a security manager, I want an HTML report, so that I can share results with asset owners. | 3 | 2 |
| US-7 | As a security manager, I want to compare this month's scan with last month's, so that I can see progress. | 5 | 3 |
| US-8 | As a DevOps engineer, I want a non-zero exit code on serious findings, so that a pipeline can fail. | 2 | 3 |
| US-9 | As a student, I want safe practice targets, so that I can learn without a lab network. | 3 | 3 |
| US-10 | As an administrator, I want to load an up-to-date vulnerability feed, so that new CVEs are detected. | 13 | Backlog |
| US-11 | As an administrator, I want backported distribution fixes recognised, so that I get fewer false positives. | 8 | Backlog |

## Example acceptance criteria (US-1)

```gherkin
Feature: Authorised scope
  Scenario: Target outside the scope is refused
    Given a scope file containing "192.168.56.0/24"
    When I run "netwarden scan 10.0.0.5 --scope scope.txt"
    Then no connection is attempted
    And the error says "10.0.0.5 is outside the authorised scope"
    And the exit status is 2
```
