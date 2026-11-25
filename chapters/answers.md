# Answers to Chapter Questions

Answers and short explanations for the **Check your understanding** questions at the end of each chapter. Try the questions first; each section links back to them.

## Chapter 1: What Is Software Engineering?

**1. A. Systematic, disciplined and quantifiable**

A method, followed even under deadline pressure, with progress and quality measured.

**2. C. Software engineering's practices exist to cope with many authors, users, changes and long lifetimes**

An assignment script has one author and a short life; a product has many authors and a long life.

**3. B. Conformity**

NetWarden must parse banners from dozens of products, each in its own format.

**4. D. Adding people to a late software project makes it later**

New people need training, and each one adds communication paths.

**5. B. A mistake costs more to fix the later in the lifecycle it is found**

A requirements error found in operation can cost many times more than one found in review.

**6. D. Software product quality, split into characteristics such as security and performance efficiency**

The 2023 edition has nine product quality characteristics.

**7. A. They compete: more security checks can slow a scan, and engineering trades them off**

Quality is multi-dimensional and the dimensions pull against each other.

**8. C. It is a requirement: assessing networks you are not authorised to assess is harmful and often illegal**

Software engineers' decisions affect people who never see the code, such as the owners of scanned networks.

[Back to the questions](01-what-is-se.md#check-your-understanding)

## Chapter 2: Software Process Models

**1. D. When requirements are well understood and stable, and the cost of failure is high**

Its weakness is that working software, and early errors, appear very late.

**2. B. It pairs each specification with the test level that will verify it**

Acceptance tests from requirements, system tests from the system specification, and so on.

**3. D. The biggest remaining risks, often resolved by building a prototype**

Risk decides what each iteration tackles.

**4. A. Responding to change over following a plan**

The others are individuals and interactions, working software, and customer collaboration, each valued over its counterpart.

**5. C. The product owner**

The product owner is accountable for maximising value.

**6. D. A shared checklist every increment must satisfy, such as tests passing and code reviewed**

NetWarden's is in its CONTRIBUTING.md; without one, done means something different to everyone.

**7. B. Work in progress**

There are no sprints or prescribed roles; items are pulled when there is capacity.

**8. C. Requirements were expected to change, but safety rules were too important to leave to change: a hybrid**

Choose by the project's risks; most organisations use hybrids.

[Back to the questions](02-process.md#check-your-understanding)

## Chapter 3: Requirements Engineering

**1. A. Validation**

Validation asks 'building the right product?'; verification asks 'building the product right?'.

**2. C. The owners of the machines being scanned**

A stakeholder is anyone who affects or is affected by the system.

**3. D. A /24 network on the 17 default ports shall complete in under 60 s on a LAN**

Non-functional requirements must be measurable to be verifiable.

**4. B. Appropriate: it says how, not what**

Better: 'store scan results between runs'.

**5. C. They record what the conversation decided, and become tests**

Given, When, Then makes them readable and testable.

**6. A. Independent, Negotiable, Valuable, Estimable, Small, Testable**

Bill Wake's criteria for a good user story; a story too big for a sprint is an epic.

**7. A. Capturing alternative flows, such as what happens when a target is out of scope**

Many teams use stories for planning and use cases for complex behaviour.

**8. C. Links showing exactly which design, code and tests realise that requirement**

Traceability links each requirement back to its source and forward to its realisation.

[Back to the questions](03-requirements.md#check-your-understanding)

## Chapter 4: Modelling with UML and C4

**1. B. A simplified representation built to answer particular questions**

Like a subway map: it leaves out what its users don't need.

**2. C. Composition**

In aggregation the part can exist independently.

**3. A. Realization**

In NetWarden, each check realises the Check Protocol.

**4. A. One or more**

* is the same as 0..*.

**5. C. Alternative paths, chosen by guards**

opt is an optional step, loop repeats.

**6. B. When its response to an event depends on its history**

Transitions are labelled event [guard] / action.

**7. D. Anything that runs or stores data separately: an application, a database, a file store**

The C4 levels are context, containers, components and code.

**8. B. They are reviewed and versioned with the code, so they drift out of date less**

PlantUML, Mermaid and Structurizr generate diagrams from text.

[Back to the questions](04-modelling.md#check-your-understanding)

## Chapter 5: Design Principles

**1. A. Low coupling, high cohesion**

Each module has one theme, and a change in one rarely forces changes elsewhere.

**2. C. To hide design decisions likely to change**

Information hiding: each module keeps a likely-to-change decision behind its interface.

**3. B. Open/closed**

NetWarden adds a check with one new class and no engine changes.

**4. D. Liskov substitution**

Substitutability is about behaviour, not just method names.

**5. B. High-level modules depend on abstractions, not on concrete low-level details**

Passing collaborators in, rather than creating them inside, is dependency injection.

**6. D. DRY**

Every piece of knowledge has one authoritative place.

**7. A. YAGNI**

You Aren't Gonna Need It: no features for imagined future needs.

**8. C. One whose callers must know about the details it was meant to hide**

Spolsky observed that all non-trivial abstractions leak to some degree.

[Back to the questions](05-design-principles.md#check-your-understanding)

## Chapter 6: Design Patterns

**1. D. A named solution to a recurring problem in a context, with known consequences**

Patterns are solutions plus the forces and trade-offs around them.

**2. B. Creational, structural, behavioural**

Factory is creational, adapter and facade structural, strategy and observer behavioural.

**3. D. Strategy**

The reporters follow the same pattern.

**4. A. Observer**

Subscribers register for events; the publisher does not depend on them.

**5. C. Facade**

The CLI talks to Assessment, not to the scanner, checks and store separately.

**6. D. Repository**

The rest of the code does not know about SQL.

**7. B. In one composition root, cli.py**

Collaborators are created in one place and passed in.

**8. C. An anti-pattern: one class that knows and does too much**

Use patterns to resolve real forces; recognise anti-patterns too.

[Back to the questions](06-patterns.md#check-your-understanding)

## Chapter 7: Software Architecture

**1. A. The set of structures and decisions that are expensive to change**

Architecture is what is hard to change later.

**2. C. Quality attributes, such as performance, security and modifiability**

Many architectures can deliver the same functions; qualities decide between them.

**3. D. As a scenario with a source, stimulus, environment and a measurable response**

A measurable response makes it testable.

**4. B. A core independent of technology, which makes it testable and adaptable**

Adapters connect the core to databases, networks and user interfaces through ports.

**5. C. A modular monolith, splitting into services only for a real need**

Microservices add operational cost that must be earned.

**6. A. A scenario-based method for evaluating architectures, with a utility tree**

The Architecture Tradeoff Analysis Method.

**7. A. An architecture decision record: a short document of a decision, its context and consequences**

ADRs keep the why of decisions with the code.

**8. C. An automated check that enforces an architectural rule, such as 'the core never imports the network library'**

It keeps key rules true as the code changes.

[Back to the questions](07-architecture.md#check-your-understanding)

## Chapter 8: Version Control and Collaboration

**1. B. Every clone holds the full history and can commit without a server**

A remote is just another repository you share with.

**2. C. Working tree, staging area, commit, then remote**

git add stages; git commit records; git push shares.

**3. A. A cheap, movable pointer to a commit**

History is a graph of commits; branches just point into it.

**4. A. On commits that others already have, because it rewrites history**

Only rebase commits you have not shared.

**5. C. Short-lived branches and frequent integration**

Gitflow, with its release branches, suits scheduled releases.

**6. B. Why the change was made**

Git already records what changed and who; the message carries the reason.

**7. D. Spreading knowledge of the code across the team**

Keep pull requests small and automate style checks so reviewers focus on substance.

**8. B. Revoke and replace the secret, since it remains in history**

Removing it from the latest commit does not remove it from the history or from clones.

[Back to the questions](08-version-control.md#check-your-understanding)

## Chapter 9: Clean Code

**1. A. Code is read far more often than it is written**

Most of a program's cost is in understanding and changing it.

**2. C. open_services**

Intention-revealing names from the domain.

**3. B. Why the code is the way it is**

Let the code show what; docstrings document contracts.

**4. D. Small, doing one thing at one level of abstraction, with few parameters and no hidden side effects**

Small functions are easy to name, test and change.

**5. B. It silently swallows every error, hiding failures**

Raise specific exceptions and report failures at a boundary.

**6. D. Errors caught before running, and documentation that cannot go stale**

Prefer enums, frozen dataclasses and protocols.

**7. A. A formatter and linter, automatically, locally and in CI**

Style debates disappear when a tool decides.

**8. C. A normal outcome to handle locally**

Handle expected conditions locally; reserve exceptions for the unexpected.

[Back to the questions](09-clean-code.md#check-your-understanding)

## Chapter 10: Refactoring and Technical Debt

**1. D. Improving the structure of code without changing its behaviour**

Done in tiny steps protected by tests.

**2. B. A good automated test suite run after each small step**

Without tests, refactoring is just editing.

**3. D. A surface sign that hints at a deeper design problem**

Long functions, duplicated code and long parameter lists are classic smells.

**4. A. Replace conditional with polymorphism**

Each branch becomes a class with the same method.

**5. C. The extra effort every future change costs because of the shortcut**

Debt is not always bad, but the interest must be paid.

**6. D. Prudent and deliberate**

Fowler's debt quadrant: shipping now and planning to repay is prudent and deliberate.

**7. B. Leave the code a little cleaner than you found it**

Continuous small repayments of debt.

**8. C. Hotspots: complex code that changes often**

Debt in code that rarely changes charges little interest.

[Back to the questions](10-refactoring.md#check-your-understanding)

## Chapter 11: Software Testing

**1. A. A person's error causes a fault in the code, which may cause a visible failure**

Testing finds failures; it cannot prove that faults are absent.

**2. C. A pyramid: many fast unit tests, fewer integration tests, few slow end-to-end tests**

Fast tests at the bottom give quick, precise feedback.

**3. D. Arrange, act, assert**

Good tests are also FIRST: fast, independent, repeatable, self-validating, timely.

**4. B. 6.9, 7.0, 8.9 and 9.0**

Defects cluster at the edges of equivalence partitions.

**5. C. Spy**

A stub returns canned answers; a fake is a working lightweight implementation; a mock checks expectations.

**6. A. Injected dependencies: the engine receives its scanner and store**

Dependency injection lets tests pass in a fake scanner.

**7. A. Red, green, refactor**

Write a failing test, make it pass simply, then clean up.

**8. C. Which code was executed by tests, so the other 5% is untested; not how well it is tested**

Coverage shows what is untested, not what is well tested.

[Back to the questions](11-testing.md#check-your-understanding)

## Chapter 12: Quality Assurance and Secure Development

**1. B. QA prevents defects through process; QC detects them in products, and testing is one QC activity**

Reviews, static analysis and testing are QC; standards and process improvement are QA.

**2. C. They examine documents and code directly, so they catch issues such as unclear requirements and missing error handling**

Checklists make them systematic.

**3. A. When a measure becomes a target, it stops being a good measure**

Choose metrics with goal, question, metric, and watch for gaming.

**4. A. A regression test that would have caught it**

Significant defects also get root cause analysis.

**5. C. A use case written from an attacker's point of view, describing misuse the system must resist**

Abuse cases turn into security requirements.

**6. B. Spoofing**

Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.

**7. D. As untrusted input, validated or encoded before use**

Everything from the network, or from any user, is untrusted until validated or encoded.

**8. B. A software bill of materials: an inventory of the components and dependencies in a release**

It supports dependency scanning and supply chain security.

[Back to the questions](12-quality-security.md#check-your-understanding)

## Chapter 13: Build Automation and CI/CD

**1. A. Merging to main frequently, each change verified by a fast, self-testing automated build**

A broken build is fixed first, before new work.

**2. C. pyproject.toml**

Build automation turns source into tested, packaged artifacts with one command.

**3. B. Declare, pin, update deliberately, and audit them**

Pinning gives reproducible builds; audits catch known vulnerabilities.

**4. D. To catch incompatibilities across the versions users run**

A test matrix runs the same jobs in several environments.

**5. B. Delivery keeps every change releasable; deployment releases every passing change automatically**

Both depend on a reliable pipeline.

**6. D. Differences between what was tested and what is released**

Rebuilding for each environment can change what you ship.

**7. A. Major**

MAJOR.MINOR.PATCH: minor for compatible features, patch for compatible fixes.

**8. C. Least privilege, managed secrets, and care with untrusted pull requests**

The pipeline is a target: it holds credentials and produces releases.

[Back to the questions](13-cicd.md#check-your-understanding)

## Chapter 14: Deployment and DevOps

**1. D. Culture, Automation, Lean, Measurement, Sharing**

DevOps is as much about culture and flow as about tools.

**2. B. A small final image without build tools**

Build in one stage, copy only what runs into the final stage, and run as a non-root user.

**3. D. Outside the code, in the environment or configuration files per deployment**

The same artifact runs in every environment with different configuration.

**4. A. Canary**

Blue-green switches all traffic between two identical environments; rolling replaces instances gradually.

**5. C. Deploy code with a feature turned off, and turn it on separately from the deployment**

They separate deployment from release.

**6. D. Logs, metrics and traces**

SLOs define the reliability targets these signals are measured against.

**7. B. They improve together in high-performing teams**

Deployment frequency, lead time, change failure rate and recovery time move together.

**8. C. Mitigating the impact, then learning through a blameless postmortem**

Blameless postmortems focus on systems, not people.

[Back to the questions](14-devops.md#check-your-understanding)

## Chapter 15: Maintenance and Evolution

**1. A. More**

Most of the cost of successful software comes after its first release.

**2. C. It must keep changing, and its complexity grows unless actively reduced**

Software that stops changing becomes less useful.

**3. D. Adaptive**

Adaptive maintenance keeps software working in a changed environment.

**4. B. Code without tests**

Without tests, every change is risky.

**5. C. Characterisation tests at seams, recording what the code does today**

They protect current behaviour while you change the structure.

**6. A. Replacing a system incrementally, routing more and more to the new parts until the old one can go**

Big-bang rewrites are risky; incremental replacement keeps the system working.

**7. A. Deprecate it first, with a warning and a timeline, then remove it**

Users need time to move.

**8. C. A requirements gap revealed in operation, handled through the normal process**

Backported security fixes keep the old version number, so version matching alone is wrong.

[Back to the questions](15-maintenance.md#check-your-understanding)

## Chapter 16: Project Management

**1. B. Scope, time, cost and quality**

Agile fixes time and cost and lets scope vary.

**2. C. A hierarchy of the work, split into deliverable pieces small enough to estimate**

In agile projects, the backlog plays this role.

**3. A. Early estimates are uncertain and narrow as the project learns more**

Estimate in ranges, especially early.

**4. A. Quick team estimation that surfaces different assumptions**

Big disagreements reveal misunderstandings worth discussing.

**5. C. The longest chain of dependent tasks**

Any delay on the critical path delays the project.

**6. B. Story points are relative to each team, so the numbers are not comparable**

Comparing invites inflated estimates.

**7. D. Transfer**

The four responses are avoid, transfer, mitigate and accept.

**8. B. Probability times impact**

It ranks which risks deserve attention first.

[Back to the questions](16-project-management.md#check-your-understanding)

## Chapter 17: Teams, Ethics and AI-Assisted Development

**1. A. Forming, storming, norming, performing**

Storming is normal; good teams work through it.

**2. C. Psychological safety**

People must feel safe to admit mistakes and ask questions.

**3. C. 15**

n(n - 1) / 2 = 6 x 5 / 2 = 15.

**4. D. A system's structure tends to mirror the communication structure of the organisation that builds it**

Team structure and architecture shape each other.

**5. B. The public interest**

Engineers act consistently with the public interest.

**6. D. The same capability can defend or attack, so it builds in limits and requires authorisation**

Assess systems only with written authorisation and agreed rules of engagement.

**7. A. They set what you may do with the code, such as distribution and attribution conditions**

Copyleft licences, for example, attach conditions to distribution.

**8. C. The engineer who accepts it, who must verify it with tests, analysis and review**

AI assistants make confident mistakes; the engineer remains accountable.

[Back to the questions](17-teams-ethics-ai.md#check-your-understanding)
