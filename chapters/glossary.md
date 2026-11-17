# Glossary

**Abstraction.** Working with the essential properties of something while hiding the details.

**Abuse case.** A description of how a system could be misused, used to derive security requirements.

**Acceptance criteria.** Conditions a user story must meet to be accepted, often written as Given, When, Then.

**Activity diagram.** A UML behaviour diagram showing a workflow with actions, decisions, forks and joins.

**Adapter.** A design pattern that converts one interface into another that a client expects.

**ADR (architecture decision record).** A short document recording one architectural decision, its context and consequences.

**Agile.** A family of iterative, incremental methods based on the values of the 2001 Agile Manifesto.

**Architecture.** The set of structures and significant decisions of a system that are expensive to change.

**Artifact.** Any product of the development process: a document, model, test, binary package or container image.

**Backlog.** An ordered list of work items, usually user stories, for a product or a sprint.

**Baseline.** An agreed, controlled version of a set of artifacts, changed only through change control.

**Black-box testing.** Designing tests from the specification without looking at the code.

**Blue-green deployment.** Running old and new versions side by side and switching traffic between them at once.

**Boundary value analysis.** Testing at and next to the edges of input partitions.

**Branch.** In Git, a movable pointer to a commit, used to develop work in isolation.

**Burn-down, burn-up chart.** Charts of remaining work, or completed work against scope, over time.

**C4 model.** A way of describing architecture at four levels: context, containers, components and code.

**Canary release.** Exposing a new version to a small share of users before rolling it out fully.

**Characterisation test.** A test that records what existing code currently does, to make changing it safe.

**CI/CD.** Continuous integration and continuous delivery or deployment.

**Class diagram.** A UML structure diagram of classes, their attributes, operations and relationships.

**Code review.** Examination of code changes by people other than the author, usually through pull requests.

**Code smell.** A surface symptom in code that suggests a deeper design problem.

**Cohesion.** How strongly the parts of a module belong together.

**Composition.** A whole-part relationship in which the parts are created and destroyed with the whole.

**Configuration management.** Identifying, controlling and tracking versions of all project artifacts.

**Container.** A packaged application with its dependencies that runs isolated on a shared operating system kernel.

**Continuous delivery.** Keeping every change releasable through an automated pipeline; release is a manual decision.

**Continuous deployment.** Automatically releasing every change that passes the pipeline.

**Continuous integration.** Merging small changes into a shared mainline frequently, each verified by an automated build.

**Conway's law.** Systems tend to mirror the communication structure of the organisations that build them.

**Coupling.** The degree to which modules depend on one another.

**Coverage.** The proportion of code (statements, branches) executed by tests.

**Critical path.** The longest chain of dependent tasks in a project schedule; tasks on it have no slack.

**CVE.** Common Vulnerabilities and Exposures: a public identifier for a known vulnerability.

**CVSS.** Common Vulnerability Scoring System: a 0 to 10 score of a vulnerability's severity.

**Cyclomatic complexity.** The number of independent paths through a piece of code.

**Definition of done.** A shared checklist every increment must satisfy before it counts as done.

**Dependency injection.** Supplying an object's collaborators from outside rather than creating them inside.

**Deployment diagram.** A UML diagram of nodes, execution environments and the artifacts deployed on them.

**DevOps.** A culture and set of practices uniting development and operations through automation and shared ownership.

**DORA metrics.** Measures of software delivery performance: deployment frequency, lead time, change failure rate, recovery time, and rework rate.

**Elicitation.** Discovering requirements from stakeholders and other sources.

**Epic.** A large user story that must be split before it fits in a sprint.

**Equivalence partitioning.** Dividing inputs into classes that should be treated alike, and testing one from each.

**Facade.** A design pattern providing one simple interface to a complex subsystem.

**Factory.** A pattern or function that creates objects without callers naming the concrete class.

**Failure.** Observable behaviour that deviates from what is required.

**Fault (defect, bug).** An imperfection in code or documents that may cause a failure.

**Feature flag.** A configuration switch that turns functionality on or off without deploying new code.

**Fingerprinting.** Identifying the product and version behind a network service, for example from its banner.

**Fitness function.** An automated check that an architectural characteristic is preserved.

**Functional requirement.** A statement of what the system shall do.

**Gantt chart.** A bar chart of tasks against time.

**GQM (goal, question, metric).** A method for choosing metrics that answer questions about defined goals.

**Hexagonal architecture.** Ports and adapters: a domain core with interfaces (ports) implemented by replaceable adapters.

**Incident.** An unplanned interruption or reduction in the quality of a service.

**Increment.** A usable, done piece of the product produced in a sprint.

**Infrastructure as code.** Defining infrastructure in version-controlled files applied by tools.

**Information hiding.** Concealing design decisions likely to change behind a stable interface.

**Inspection.** A formal review process with defined roles, preparation, checklists and follow-up.

**Integration testing.** Testing the interactions between components or with external systems.

**Kanban.** A method that visualises work on a board and limits work in progress.

**Legacy code.** Code without tests, which is therefore risky to change.

**Lehman's laws.** Observations on how real-world software evolves: continuing change, increasing complexity and others.

**Liskov substitution principle.** Subtypes must be usable wherever their base type is expected.

**Maintenance.** All modification of software after delivery: corrective, adaptive, perfective and preventive.

**Merge.** Combining two lines of development, in Git creating a commit with two parents.

**Microservices.** An architectural style of small, independently deployable services.

**Mock.** A test double that is programmed with expectations and verifies how it was called.

**MoSCoW.** Prioritisation into Must, Should, Could and Won't have this time.

**Multiplicity.** In UML, how many objects take part in a relationship.

**Non-functional requirement.** A required quality or constraint, such as performance, security or portability.

**Observer.** A design pattern in which subscribers are notified of events published by a subject.

**Open/closed principle.** Software should be open for extension but closed for modification.

**Pipeline.** An automated sequence of build, test and deployment stages.

**Planning poker.** A consensus estimation technique using cards with relative sizes.

**Postmortem.** A blameless review of an incident to learn and prevent recurrence.

**Process model.** A description of the activities, order and roles of software development.

**Product owner.** The Scrum accountability for maximising product value and ordering the backlog.

**Psychological safety.** A shared belief that a team is safe for interpersonal risk-taking.

**Pull request.** A request to merge a branch, used for review and automated checks.

**Quality assurance.** Process-oriented activities that prevent defects.

**Quality attribute.** A measurable property of a system, such as performance, security or maintainability.

**Rebase.** Re-applying commits on top of another base, rewriting them.

**Refactoring.** Improving internal structure without changing observable behaviour.

**Regression.** Behaviour that worked before and no longer does.

**Repository (pattern).** An object that makes stored domain objects look like an in-memory collection.

**Requirement.** A statement of a capability or quality a system must have.

**Risk.** An uncertain event that would affect project objectives; exposure is probability times impact.

**Rules of engagement.** The written agreement that authorises and limits a security assessment.

**SBOM.** Software bill of materials: a list of the components inside a piece of software.

**Scope (NetWarden).** The set of networks an operator is authorised to assess; targets outside it are refused.

**Scrum.** An agile framework of sprints, three accountabilities, five events and three artifacts.

**Semantic versioning.** MAJOR.MINOR.PATCH version numbers that signal compatibility.

**Sequence diagram.** A UML interaction diagram showing messages between participants over time.

**SOLID.** Five object-oriented design principles: single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion.

**Spiral model.** A risk-driven process model of repeated loops of planning, risk analysis, development and evaluation.

**Sprint.** A fixed-length iteration, one month or less, in Scrum.

**Stakeholder.** Anyone who affects or is affected by a system.

**State machine diagram.** A UML diagram of states and the transitions between them triggered by events.

**Static analysis.** Examining code without running it: linting, type checking, security scanning.

**Story points.** A relative unit for estimating the size of user stories.

**Strangler fig.** Incrementally replacing a system by routing more and more of its work to new code.

**Strategy.** A design pattern that encapsulates interchangeable algorithms behind a common interface.

**STRIDE.** Threat categories: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege.

**Stub.** A test double that returns canned answers.

**Technical debt.** The future cost of design shortcuts, paid as slower and riskier change.

**Test double.** Any object that stands in for a real collaborator in a test.

**Test-driven development (TDD).** Writing a failing test before the code, in red, green, refactor cycles.

**Test pyramid.** Many unit tests, fewer integration tests, few end-to-end tests.

**Threat modelling.** Systematically identifying what can go wrong with a design from a security point of view.

**Traceability.** Links between requirements and their sources, designs, code and tests.

**Trunk-based development.** Integrating into the main branch at least daily through very short-lived branches.

**UML.** Unified Modeling Language, the standard notation for modelling software.

**Unit test.** A test of one function or class in isolation.

**Use case.** A description of how an actor uses a system to achieve a goal, including alternatives.

**User story.** A short statement of a need: as a role, I want a capability, so that a benefit.

**Validation.** Checking that the right product is being built.

**Velocity.** Story points completed per sprint by one team.

**Verification.** Checking that the product is built right, according to its specification.

**V-model.** A plan-driven model pairing each specification with its corresponding test level.

**Waterfall.** A sequential, document-driven process model.

**Work breakdown structure (WBS).** A hierarchical decomposition of a project's deliverables.

**WIP limit.** A cap on the number of items in a stage of work at once.
