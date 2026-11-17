# Chapter 18: Quick Reference

Compact reminders of the notation, commands and templates used in this book.

## UML notation

<figure class="diagram">
<svg viewBox="0 0 720 390" style="width:100%;height:auto;max-width:720px" role="img" aria-label="UML notation summary. Class box with name, attributes and operations. Relationship lines: association with open arrow, aggregation with hollow diamond, composition with filled diamond, generalization with hollow triangle, realization with dashed line and hollow triangle, dependency with dashed open arrow. Behaviour symbols: initial node, final node, action, decision, fork bar, state, actor, use case, lifeline with activation, synchronous message, and return message." xmlns="http://www.w3.org/2000/svg">
<style>
.s18a{ font-family:var(--sans),sans-serif; }
.s18a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s18a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s18a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s18a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s18a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s18a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s18a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s18a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s18a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s18a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s18a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s18a .s{ fill:var(--text-dim); font-size:13px; }
.s18a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s18a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .c{ fill:var(--text-faint); font-size:12.5px; }
.s18a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s18a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s18a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s18a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s18a-a); }
.s18a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s18a-a); marker-start:url(#s18a-s); }
.s18a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s18a-g); }
.s18a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-a); }
.s18a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s18a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s18a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s18a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s18a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s18a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s18a-tri); }
.s18a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-tri); }
.s18a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s18a-open); }
.s18a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-open); }
.s18a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s18a-dia); }
.s18a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s18a-odia); }
.s18a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s18a-dia); marker-end:url(#s18a-open); }
.s18a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s18a-solid); }
.s18a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s18a-open); }
.s18a .fill{ fill:var(--text); stroke:none; }
.s18a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s18a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s18a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s18a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s18a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s18a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s18a .ks-blue{ fill:#185FA5; font-size:13px; }
.s18a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s18a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s18a .kb-blue, :root[data-theme="dark"] .s18a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s18a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s18a .kh-blue{ fill:#85B7EB; }
.s18a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s18a-blue); }
.s18a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-blue); }
.s18a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s18a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s18a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s18a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s18a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s18a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s18a .kb-teal, :root[data-theme="dark"] .s18a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s18a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s18a .kh-teal{ fill:#5DCAA5; }
.s18a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s18a-teal); }
.s18a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-teal); }
.s18a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s18a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s18a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s18a .ks-amber{ fill:#854F0B; font-size:13px; }
.s18a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s18a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s18a .kb-amber, :root[data-theme="dark"] .s18a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s18a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s18a .kh-amber{ fill:#EF9F27; }
.s18a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s18a-amber); }
.s18a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-amber); }
.s18a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s18a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s18a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s18a .ks-purple{ fill:#534AB7; font-size:13px; }
.s18a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s18a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s18a .kb-purple, :root[data-theme="dark"] .s18a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s18a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s18a .kh-purple{ fill:#AFA9EC; }
.s18a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s18a-purple); }
.s18a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-purple); }
.s18a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s18a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s18a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s18a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s18a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s18a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s18a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s18a .kb-gray, :root[data-theme="dark"] .s18a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s18a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s18a .kh-gray{ fill:#B4B2A9; }
.s18a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s18a-gray); }
.s18a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s18a-gray); }
.s18a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s18a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s18a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s18a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s18a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s18a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s18a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s18a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s18a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s18a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s18a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s18a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s18a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s18a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s18a">
<rect x="20" y="16" width="170" height="86" rx="3" class="k-blue"/>
<text x="105.0" y="36" text-anchor="middle" class="kb-blue">ClassName</text>
<line x1="20" y1="46" x2="190" y2="46" class="ln-blue"/>
<text x="28" y="64" text-anchor="start" class="km-blue">- attribute: Type</text>
<line x1="20" y1="74" x2="190" y2="74" class="ln-blue"/>
<text x="28" y="92" text-anchor="start" class="km-blue">+ operation(): Type</text>
<line x1="220" y1="30" x2="320" y2="30" class="assoc"/>
<text x="332" y="34" text-anchor="start" class="s">association</text>
<line x1="220" y1="60" x2="320" y2="60" class="agg"/>
<text x="332" y="64" text-anchor="start" class="s">aggregation</text>
<line x1="220" y1="90" x2="320" y2="90" class="comp"/>
<text x="332" y="94" text-anchor="start" class="s">composition</text>
<line x1="220" y1="120" x2="320" y2="120" class="gen"/>
<text x="332" y="124" text-anchor="start" class="s">generalization</text>
<line x1="220" y1="150" x2="320" y2="150" class="real"/>
<text x="332" y="154" text-anchor="start" class="s">realization</text>
<line x1="220" y1="180" x2="320" y2="180" class="dep"/>
<text x="332" y="184" text-anchor="start" class="s">dependency</text>
<circle cx="470" cy="30" r="9" class="fill"/>
<text x="490" y="34" text-anchor="start" class="s">initial node</text>
<circle cx="470" cy="62" r="11" class="act"/>
<circle cx="470" cy="62" r="6.5" class="fill"/>
<text x="490" y="66" text-anchor="start" class="s">final node</text>
<rect x="440" y="84" width="60" height="26" rx="13" class="k-teal"/>
<text x="470.0" y="101.5" text-anchor="middle" class="ks-teal">action</text>
<text x="510" y="101" text-anchor="start" class="s">action / activity</text>
<path d="M470 121 L483 134 L470 147 L457 134 z" class="k-amber"/>
<text x="490" y="138" text-anchor="start" class="s">decision / merge</text>
<rect x="440" y="160" width="60" height="7" rx="2" class="fill"/>
<text x="510" y="168" text-anchor="start" class="s">fork / join</text>
<rect x="20" y="210" width="120" height="36" rx="16" class="k-purple"/>
<text x="80.0" y="232.5" text-anchor="middle" class="kb-purple">State</text>
<text x="150" y="232" text-anchor="start" class="s">state</text>
<circle cx="250" cy="205" r="9" class="act"/>
<line x1="250" y1="214" x2="250" y2="240" class="stick"/>
<line x1="236" y1="224" x2="264" y2="224" class="stick"/>
<line x1="250" y1="240" x2="238" y2="258" class="stick"/>
<line x1="250" y1="240" x2="262" y2="258" class="stick"/>
<text x="250" y="276" text-anchor="middle" class="b">actor</text>
<ellipse cx="380" cy="230" rx="60" ry="20" class="k-teal"/>
<text x="380" y="234.5" text-anchor="middle" class="kb-teal">use case</text>
<rect x="500" y="196" width="100" height="30" rx="3" class="k-gray"/>
<text x="550.0" y="215.5" text-anchor="middle" class="kb-gray">:Object</text>
<line x1="550" y1="226" x2="550" y2="370" class="gd"/>
<rect x="545" y="250" width="10" height="80" class="act"/>
<line x1="560" y1="270" x2="685" y2="270" class="msg"/>
<text x="622" y="264" text-anchor="middle" class="s">call()</text>
<line x1="685" y1="310" x2="560" y2="310" class="ret"/>
<text x="622" y="304" text-anchor="middle" class="c">result</text>
<line x1="690" y1="250" x2="690" y2="370" class="gd"/>
<rect x="20" y="290" width="300" height="80" rx="4" class="zone" style="fill-opacity:0.35"/>
<path d="M20 290 L119.6 290 L119.6 306 L111.6 314 L20 314 z" class="zone"/>
<text x="28" y="307" text-anchor="start" class="b">alt [guard]</text>
<line x1="20" y1="330" x2="320" y2="330" class="ud"/>
<text x="330" y="340" text-anchor="start" class="s">combined fragment</text>
</g>
</svg>
<figcaption>A one-page reminder of the UML notation used in this book.</figcaption>
</figure>

| Element | Notation | Meaning |
|---|---|---|
| Visibility | `+` `-` `#` `~` | public, private, protected, package |
| Multiplicity | `1`, `0..1`, `*`, `1..*` | how many objects take part |
| Stereotype | `«interface»`, `«enumeration»`, `«component»` | a specialised kind of element |
| Abstract | *italic name* | cannot be instantiated |
| Static | underlined member | belongs to the class, not instances |
| Combined fragments | `alt`, `opt`, `loop`, `par`, `ref` | alternatives, optional, repetition, parallel, reference |
| Transition | `event [guard] / action` | state machine arrow label |

## NetWarden commands

| Task | Command |
|---|---|
| Install for development | `pip install -e ".[dev]"` |
| Start practice targets | `netwarden demo` |
| Scan | `netwarden scan 127.0.0.1 --scope examples/lab-scope.txt --ports 2121,2222,2323,8080,13306` |
| HTML report to a file | `... --format html --output report.html` |
| JSON for scripts | `... --format json` |
| Fail only on critical findings | `... --fail-on critical` |
| Do not record history | `... --no-save` |
| List previous scans | `netwarden history` |
| Compare two scans | `netwarden diff 1 2` |
| Exit status | `0` fine, `1` findings at or above `--fail-on`, `2` error |

## Git

| Task | Command |
|---|---|
| New branch | `git switch -c feature/US-7-scan-diff` |
| What changed | `git status`, `git diff`, `git diff --staged` |
| Stage and commit | `git add FILE`, `git commit -m "feat(scope): ..."` |
| Publish a branch | `git push -u origin BRANCH` |
| Update from remote | `git pull --rebase` |
| History | `git log --oneline --graph`, `git log -p -S TEXT`, `git blame FILE` |
| Undo local changes to a file | `git restore FILE` |
| Unstage | `git restore --staged FILE` |
| Undo a pushed commit safely | `git revert COMMIT` |
| Tag a release | `git tag -a v1.0.0 -m "..."`, `git push --tags` |

Conventional Commit types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`, `ci`, `chore`; add `!` or a `BREAKING CHANGE:` footer for incompatible changes.

## pytest and quality tools

| Task | Command |
|---|---|
| Run all tests | `pytest` |
| Verbose, filtered | `pytest -v -k scope` |
| Stop at first failure | `pytest -x` |
| Slowest tests | `pytest --durations=5` |
| Coverage with missing lines | `pytest --cov --cov-report=term-missing` |
| Fail on resource leaks | `pytest -W error::ResourceWarning` |
| Lint, including security rules | `ruff check src tests` |
| Format | `ruff format src tests` |
| Type check | `mypy` |
| Complexity | `radon cc -s -a src/netwarden` |
| Known-vulnerable dependencies | `pip-audit` |
| Build wheel | `python -m build` |
| Build and run container | `docker build -t netwarden netwarden/`, `docker run --rm netwarden --version` |

## Templates

### User story

```text
US-n: As a <role>, I want <capability>, so that <benefit>.   (points)
Acceptance criteria:
  Given <context>
  When <action>
  Then <observable outcome>
```

### Requirement

```text
NW-XX-n  The system shall <behaviour> <measurable condition>.   Priority: Must / Should / Could
Source: <stakeholder or story>   Verified by: <test name>
```

### Quality attribute scenario

```text
Source | Stimulus | Artifact | Environment | Response | Response measure
```

### Architecture decision record

```markdown
# ADR-NNNN: <decision title>
* Status: proposed | accepted | superseded by ADR-MMMM
* Date: YYYY-MM-DD
## Context      what forces are at play
## Options      what was considered
## Decision     what we chose
## Consequences good, bad, and when to revisit
```

### Defect report

```text
Summary | Steps to reproduce | Expected | Actual | Environment | Evidence | Severity | Priority
```

### Blameless postmortem

```text
Summary | Impact | Timeline | Root causes | What went well | What went badly | Actions (owner, date)
```

## Formulas

| Quantity | Formula |
|---|---|
| Cyclomatic complexity | decisions + 1 (for one function) |
| Communication paths | n (n - 1) / 2 |
| Risk exposure | probability x impact |
| Three-point estimate | (O + 4M + P) / 6 |
| Basic COCOMO, organic | effort = 2.4 KLOC^1.05 person-months; time = 2.5 effort^0.38 months |
| Schedule and cost performance | SPI = EV / PV; CPI = EV / AC |
| CVSS v3 rating | 0 none (INFO in NetWarden); 0.1 to 3.9 low; 4.0 to 6.9 medium; 7.0 to 8.9 high; 9.0 to 10.0 critical |

## Standards and sources mentioned

| Reference | Topic |
|---|---|
| ISO/IEC 25010:2023 | Product quality model |
| ISO/IEC/IEEE 29148 | Requirements engineering |
| ISO/IEC/IEEE 29119 | Software testing |
| ISO/IEC/IEEE 14764 | Software maintenance |
| UML 2.5.1 (OMG) | Modelling language |
| SWEBOK Guide | Software engineering body of knowledge (IEEE Computer Society) |
| Scrum Guide (2020) | Scrum framework |
| NIST SP 800-218 (SSDF) | Secure software development |
| OWASP Top 10, CWE Top 25 | Common security weaknesses |
| ACM/IEEE-CS Code of Ethics | Professional conduct |
| Semantic Versioning 2.0.0 | Version numbers |
| Conventional Commits 1.0.0 | Commit messages |

## Further reading

- Fred Brooks, *The Mythical Man-Month* (anniversary edition, 1995).
- Ian Sommerville, *Software Engineering*, and Roger Pressman and Bruce Maxim, *Software Engineering: A Practitioner's Approach*, two widely used textbooks.
- Martin Fowler, *UML Distilled* and *Refactoring*.
- Gamma, Helm, Johnson and Vlissides, *Design Patterns*.
- Len Bass, Paul Clements and Rick Kazman, *Software Architecture in Practice*.
- Robert C. Martin, *Clean Code*; David Thomas and Andrew Hunt, *The Pragmatic Programmer*.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*.
- Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate*.
- Adam Shostack, *Threat Modeling: Designing for Security*.
