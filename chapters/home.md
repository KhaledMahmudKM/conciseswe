# Concise Book on Software Engineering

A concise, diagram-rich guide to engineering software that lasts, built around one real project.

<img src="cover.svg" alt="Cover Image" width="100%" >

Writing a program that works once is the easy part. Building software that a team can understand, test, ship, secure, and keep changing for years, while the requirements, the people and the technology all change around it, is a different discipline. That discipline is **software engineering**.

This book covers the whole lifecycle: process models and agile methods, requirements, UML and architecture models, design principles and patterns, version control, clean code, refactoring, testing, quality and security, continuous integration and delivery, DevOps, maintenance, project management, and the professional and ethical side of the job. It is written for third-year undergraduates who can program in Python and have met basic networking.

---

## The running example: NetWarden

Every chapter applies its ideas to one project, **NetWarden**, a small but real defensive security tool. NetWarden scans hosts **you are authorised to assess**, discovers their network services, identifies the software versions behind them, matches those versions against known vulnerabilities, and writes a report with remediation advice. It keeps a history, so you can see what was fixed since the last scan.

You will see NetWarden's vision, requirements and user stories, its UML models and architecture decisions, its code and design patterns, its 46 automated tests, its threat model, its CI pipeline and container, and its project plan and risk register. Everything is in the [`netwarden/` folder](https://github.com/khaledmahmudkm/conciseswe/tree/main/netwarden) of this book's repository, and it all runs. The project story around the code, its stakeholders, interviews and sprints, is a realistic teaching scenario.

> **Scan only what you are allowed to scan.** NetWarden refuses targets outside an authorised scope file, and it comes with harmless practice targets that run on your own machine.

---

## How this book is organized

**Part I, Foundations.** What software engineering is and why it exists; process models from waterfall to Scrum and Kanban.

**Part II, Requirements and Design.** Requirements engineering; modelling with UML and C4; design principles; design patterns; software architecture.

**Part III, Construction.** Version control and collaboration with Git; clean code; refactoring and technical debt.

**Part IV, Quality.** Software testing; quality assurance and secure development.

**Part V, Delivery and Operations.** Build automation and CI/CD; deployment and DevOps; maintenance and evolution.

**Part VI, People and Projects.** Estimation, planning and risk; teams, professional ethics and AI-assisted development.

The **Appendix** has quick-reference sheets for UML notation, Git, pytest and the NetWarden commands, and the **Glossary** defines every term.

---

## How to read it

Read Part I first. Part II is best read in order, because each chapter builds on the models of the one before. After that, the parts can be read in any order.

Each chapter ends with a summary. Sections marked **Hands on** use NetWarden. Set it up once:

```bash
git clone https://github.com/khaledmahmudkm/conciseswe.git
cd conciseswe/netwarden
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

---

© 2026 Khaled Mahmud
