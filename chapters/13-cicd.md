# Chapter 13: Build Automation and CI/CD

Every step between a commit and a running release that a person does by hand is a step that will eventually be done wrong, skipped under pressure, or done differently by different people. **Build automation** makes the path from source code to a tested, packaged artifact repeatable. **Continuous integration** (CI) runs that path on every change. **Continuous delivery** (CD) extends it all the way to a releasable product. This chapter builds NetWarden's pipeline step by step.

## Building software

For a compiled language, "build" means compiling and linking. For Python it means producing installable **artifacts**: a **wheel** (`.whl`, a ready-to-install archive), a source distribution, and often a container image. NetWarden describes how to build itself in `pyproject.toml`, the standard Python project file (PEP 517, 518 and 621):

```toml
[build-system]
requires = ["setuptools>=77"]
build-backend = "setuptools.build_meta"

[project]
name = "netwarden"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = []          # standard library only (ADR-0001)

[project.optional-dependencies]
dev = ["pytest==9.2.0", "pytest-cov==7.1.0", "ruff==0.17.5", "mypy==2.4.1"]

[project.scripts]
netwarden = "netwarden.cli:main"
```

One command builds it, and the wheel installs anywhere with a suitable Python:

```bash
pip install build
python -m build
# Successfully built netwarden-1.0.0.tar.gz and netwarden-1.0.0-py3-none-any.whl
```

The same file configures the tools (`[tool.pytest.ini_options]`, `[tool.ruff]`, `[tool.mypy]`), so every developer and the CI server run them identically. Other ecosystems have equivalents: Maven or Gradle for Java, npm for JavaScript, Cargo for Rust, Make and CMake for C and C++.

### Managing dependencies

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Dependency management. pyproject.toml declares NetWarden&#x27;s dependencies: none at run time and pinned development tools. Dependabot checks monthly for new versions of the tools and GitHub Actions and opens a pull request for each update; CI tests the update; a human reviews and merges it." xmlns="http://www.w3.org/2000/svg">
<style>
.s13f{ font-family:var(--sans),sans-serif; }
.s13f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s13f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s13f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s13f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s13f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s13f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s13f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s13f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s13f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s13f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s13f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s13f .s{ fill:var(--text-dim); font-size:13px; }
.s13f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s13f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .c{ fill:var(--text-faint); font-size:12.5px; }
.s13f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s13f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s13f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s13f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13f-a); }
.s13f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13f-a); marker-start:url(#s13f-s); }
.s13f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s13f-g); }
.s13f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-a); }
.s13f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s13f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s13f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s13f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s13f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s13f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13f-tri); }
.s13f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-tri); }
.s13f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13f-open); }
.s13f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-open); }
.s13f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13f-dia); }
.s13f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13f-odia); }
.s13f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13f-dia); marker-end:url(#s13f-open); }
.s13f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13f-solid); }
.s13f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s13f-open); }
.s13f .fill{ fill:var(--text); stroke:none; }
.s13f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s13f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s13f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s13f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s13f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s13f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s13f .ks-blue{ fill:#185FA5; font-size:13px; }
.s13f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s13f .kb-blue, :root[data-theme="dark"] .s13f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s13f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s13f .kh-blue{ fill:#85B7EB; }
.s13f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s13f-blue); }
.s13f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-blue); }
.s13f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s13f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s13f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s13f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s13f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s13f .kb-teal, :root[data-theme="dark"] .s13f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s13f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s13f .kh-teal{ fill:#5DCAA5; }
.s13f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s13f-teal); }
.s13f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-teal); }
.s13f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s13f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s13f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s13f .ks-amber{ fill:#854F0B; font-size:13px; }
.s13f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s13f .kb-amber, :root[data-theme="dark"] .s13f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s13f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s13f .kh-amber{ fill:#EF9F27; }
.s13f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s13f-amber); }
.s13f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-amber); }
.s13f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s13f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s13f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s13f .ks-purple{ fill:#534AB7; font-size:13px; }
.s13f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s13f .kb-purple, :root[data-theme="dark"] .s13f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s13f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s13f .kh-purple{ fill:#AFA9EC; }
.s13f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s13f-purple); }
.s13f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-purple); }
.s13f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s13f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s13f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s13f .ks-green{ fill:#3B6D11; font-size:13px; }
.s13f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s13f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s13f .kb-green, :root[data-theme="dark"] .s13f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s13f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s13f .kh-green{ fill:#97C459; }
.s13f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s13f-green); }
.s13f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13f-green); }
.s13f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s13f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s13f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s13f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s13f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s13f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s13f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s13f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s13f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s13f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s13f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s13f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s13f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s13f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s13f">
<rect x="20" y="30" width="220" height="110" rx="7" class="k-teal"/>
<text x="130.0" y="59.5" text-anchor="middle" class="kb-teal">pyproject.toml</text>
<text x="130.0" y="79.5" text-anchor="middle" class="km-teal">dependencies = []</text>
<text x="130.0" y="99.5" text-anchor="middle" class="km-teal">dev = [pytest==9.2.0,</text>
<text x="130.0" y="119.5" text-anchor="middle" class="km-teal">  ruff==0.17.5, ...]</text>
<rect x="300" y="40" width="150" height="70" rx="7" class="k-blue"/>
<text x="375.0" y="70.5" text-anchor="middle" class="kb-blue">Dependabot</text>
<text x="375.0" y="88.5" text-anchor="middle" class="ks-blue">monthly check</text>
<line x1="242" y1="80" x2="298" y2="76" class="ar"/>
<rect x="510" y="20" width="190" height="50" rx="7" class="k-amber"/>
<text x="605.0" y="40.5" text-anchor="middle" class="kb-amber">PR: bump ruff</text>
<text x="605.0" y="58.5" text-anchor="middle" class="km-amber">0.17.5 -&gt; 0.18.0</text>
<rect x="510" y="90" width="190" height="40" rx="7" class="k-purple"/>
<text x="605.0" y="114.5" text-anchor="middle" class="kb-purple">CI runs all tests</text>
<rect x="510" y="150" width="190" height="40" rx="7" class="k-green"/>
<text x="605.0" y="174.5" text-anchor="middle" class="kb-green">review and merge</text>
<line x1="452" y1="70" x2="508" y2="46" class="ar"/>
<line x1="605" y1="72" x2="605" y2="88" class="ar"/>
<line x1="605" y1="132" x2="605" y2="148" class="ar"/>
<text x="260" y="200" text-anchor="middle" class="c">pin exact versions: builds are reproducible;</text>
<text x="260" y="220" text-anchor="middle" class="c">update deliberately: through PRs, tested by CI</text>
</g>
</svg>
<figcaption>Unpinned dependencies make yesterday's green build fail today for no visible reason.</figcaption>
</figure>

A **dependency** is code you did not write but rely on. Good practice:

- **Declare** every dependency in one place, separating run-time from development dependencies.
- **Pin** exact versions (or use a lock file, such as one produced by `pip-tools`, `uv` or Poetry) so builds are **reproducible**.
- **Update deliberately**: NetWarden's `.github/dependabot.yml` asks Dependabot to propose updates monthly, as pull requests that CI tests before anyone merges them.
- **Audit** for known vulnerabilities (`pip-audit`, Chapter 12).

## Continuous integration

Martin Fowler describes **continuous integration** as a practice where each member of a team merges their changes into a shared mainline frequently, at least daily, and each integration is verified by an automated build with tests.

<figure class="diagram">
<svg viewBox="0 0 720 268" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Continuous integration: developers push small changes to the shared main branch at least daily; a CI server automatically builds and tests every change and reports back within minutes. A failing build is fixed before anything else, so main always works." xmlns="http://www.w3.org/2000/svg">
<style>
.s13a{ font-family:var(--sans),sans-serif; }
.s13a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s13a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s13a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s13a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s13a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s13a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s13a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s13a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s13a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s13a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s13a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s13a .s{ fill:var(--text-dim); font-size:13px; }
.s13a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s13a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .c{ fill:var(--text-faint); font-size:12.5px; }
.s13a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s13a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s13a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s13a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13a-a); }
.s13a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13a-a); marker-start:url(#s13a-s); }
.s13a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s13a-g); }
.s13a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-a); }
.s13a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s13a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s13a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s13a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s13a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s13a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13a-tri); }
.s13a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-tri); }
.s13a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13a-open); }
.s13a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-open); }
.s13a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13a-dia); }
.s13a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13a-odia); }
.s13a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13a-dia); marker-end:url(#s13a-open); }
.s13a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13a-solid); }
.s13a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s13a-open); }
.s13a .fill{ fill:var(--text); stroke:none; }
.s13a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s13a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s13a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s13a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s13a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s13a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s13a .ks-blue{ fill:#185FA5; font-size:13px; }
.s13a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s13a .kb-blue, :root[data-theme="dark"] .s13a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s13a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s13a .kh-blue{ fill:#85B7EB; }
.s13a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s13a-blue); }
.s13a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-blue); }
.s13a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s13a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s13a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s13a .ks-amber{ fill:#854F0B; font-size:13px; }
.s13a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s13a .kb-amber, :root[data-theme="dark"] .s13a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s13a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s13a .kh-amber{ fill:#EF9F27; }
.s13a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s13a-amber); }
.s13a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-amber); }
.s13a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s13a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s13a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s13a .ks-purple{ fill:#534AB7; font-size:13px; }
.s13a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s13a .kb-purple, :root[data-theme="dark"] .s13a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s13a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s13a .kh-purple{ fill:#AFA9EC; }
.s13a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s13a-purple); }
.s13a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-purple); }
.s13a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s13a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s13a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s13a .ks-green{ fill:#3B6D11; font-size:13px; }
.s13a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s13a .kb-green, :root[data-theme="dark"] .s13a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s13a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s13a .kh-green{ fill:#97C459; }
.s13a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s13a-green); }
.s13a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-green); }
.s13a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s13a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s13a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s13a .ks-red{ fill:#A32D2D; font-size:13px; }
.s13a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s13a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s13a .kb-red, :root[data-theme="dark"] .s13a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s13a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s13a .kh-red{ fill:#F09595; }
.s13a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s13a-red); }
.s13a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13a-red); }
.s13a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s13a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s13a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s13a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s13a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s13a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s13a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s13a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s13a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s13a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s13a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s13a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s13a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s13a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s13a">
<rect x="20" y="20" width="110" height="44" rx="7" class="k-blue"/>
<text x="75.0" y="46.5" text-anchor="middle" class="kb-blue">dev A</text>
<line x1="132" y1="42" x2="218" y2="112" class="ar"/>
<rect x="20" y="90" width="110" height="44" rx="7" class="k-blue"/>
<text x="75.0" y="116.5" text-anchor="middle" class="kb-blue">dev B</text>
<line x1="132" y1="112" x2="218" y2="112" class="ar"/>
<rect x="20" y="160" width="110" height="44" rx="7" class="k-blue"/>
<text x="75.0" y="186.5" text-anchor="middle" class="kb-blue">dev C</text>
<line x1="132" y1="182" x2="218" y2="112" class="ar"/>
<rect x="220" y="80" width="140" height="64" rx="7" class="k-purple"/>
<text x="290.0" y="107.5" text-anchor="middle" class="kb-purple">main</text>
<text x="290.0" y="125.5" text-anchor="middle" class="ks-purple">shared repo</text>
<line x1="362" y1="112" x2="418" y2="112" class="ar"/>
<rect x="420" y="70" width="160" height="84" rx="7" class="k-amber"/>
<text x="500.0" y="98.5" text-anchor="middle" class="kb-amber">CI server</text>
<text x="500.0" y="116.5" text-anchor="middle" class="ks-amber">build, lint,</text>
<text x="500.0" y="134.5" text-anchor="middle" class="ks-amber">type check, test</text>
<rect x="600" y="40" width="100" height="40" rx="7" class="k-green"/>
<text x="650.0" y="64.5" text-anchor="middle" class="kb-green">green</text>
<rect x="600" y="144" width="100" height="40" rx="7" class="k-red"/>
<text x="650.0" y="168.5" text-anchor="middle" class="ks-red">red: fix first</text>
<line x1="582" y1="100" x2="598" y2="62" class="ar-green"/>
<line x1="582" y1="126" x2="598" y2="162" class="ar-red"/>
<path d="M650 186 C 650 236, 75 236, 75 200" class="ad"/>
<text x="360" y="258" text-anchor="middle" class="c">feedback in minutes, to the person who made the change</text>
</g>
</svg>
<figcaption>Integrate continuously and integration stops being an event. The longer you wait, the more it hurts.</figcaption>
</figure>

The tool is the easy part. The practice requires:

- a single shared mainline (Chapter 8) and small, frequent merges;
- a **self-testing build**: one command runs all checks;
- a **fast build**: ten minutes is a common ceiling, so feedback arrives while the change is fresh in the author's mind;
- a team rule that **a broken build is fixed first**, before any new work;
- everyone can see the build status.

### NetWarden's pipeline

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden&#x27;s GitHub Actions pipeline. Triggered by a push to main or a pull request that touches netwarden. Job lint: checkout, set up Python 3.13, install, ruff check, mypy. Job test, after lint, runs in a matrix on Python 3.11, 3.12 and 3.13: pytest with coverage, failing under 90 percent. Job package, after test: build the wheel, upload it as an artifact, build the container image and run a smoke test." xmlns="http://www.w3.org/2000/svg">
<style>
.s13b{ font-family:var(--sans),sans-serif; }
.s13b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s13b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s13b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s13b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s13b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s13b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s13b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s13b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s13b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s13b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s13b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s13b .s{ fill:var(--text-dim); font-size:13px; }
.s13b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s13b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s13b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s13b .c{ fill:var(--text-faint); font-size:12.5px; }
.s13b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s13b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s13b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s13b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13b-a); }
.s13b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13b-a); marker-start:url(#s13b-s); }
.s13b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s13b-g); }
.s13b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-a); }
.s13b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s13b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s13b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s13b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s13b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s13b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13b-tri); }
.s13b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-tri); }
.s13b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13b-open); }
.s13b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-open); }
.s13b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13b-dia); }
.s13b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13b-odia); }
.s13b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13b-dia); marker-end:url(#s13b-open); }
.s13b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13b-solid); }
.s13b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s13b-open); }
.s13b .fill{ fill:var(--text); stroke:none; }
.s13b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s13b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s13b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s13b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s13b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s13b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s13b .ks-blue{ fill:#185FA5; font-size:13px; }
.s13b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s13b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s13b .kb-blue, :root[data-theme="dark"] .s13b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s13b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s13b .kh-blue{ fill:#85B7EB; }
.s13b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s13b-blue); }
.s13b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-blue); }
.s13b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s13b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s13b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s13b .ks-amber{ fill:#854F0B; font-size:13px; }
.s13b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s13b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s13b .kb-amber, :root[data-theme="dark"] .s13b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s13b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s13b .kh-amber{ fill:#EF9F27; }
.s13b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s13b-amber); }
.s13b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-amber); }
.s13b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s13b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s13b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s13b .ks-green{ fill:#3B6D11; font-size:13px; }
.s13b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s13b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s13b .kb-green, :root[data-theme="dark"] .s13b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s13b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s13b .kh-green{ fill:#97C459; }
.s13b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s13b-green); }
.s13b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-green); }
.s13b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s13b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s13b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s13b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s13b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s13b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s13b .kb-gray, :root[data-theme="dark"] .s13b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s13b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s13b .kh-gray{ fill:#B4B2A9; }
.s13b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s13b-gray); }
.s13b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13b-gray); }
.s13b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s13b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s13b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s13b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s13b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s13b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s13b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s13b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s13b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s13b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s13b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s13b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s13b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s13b">
<rect x="20" y="20" width="680" height="36" rx="4" class="k-gray"/>
<text x="360.0" y="42.5" text-anchor="middle" class="km-gray">on: push to main, pull_request  (paths: netwarden/**)</text>
<rect x="20" y="76" width="210" height="36" rx="7" class="k-amber"/>
<text x="125.0" y="98.5" text-anchor="middle" class="kb-amber">lint</text>
<rect x="20" y="124" width="210" height="30" rx="4" class="pnl"/>
<text x="125.0" y="143.5" text-anchor="middle" class="m">checkout</text>
<rect x="20" y="160" width="210" height="30" rx="4" class="pnl"/>
<text x="125.0" y="179.5" text-anchor="middle" class="m">setup-python 3.13</text>
<rect x="20" y="196" width="210" height="30" rx="4" class="pnl"/>
<text x="125.0" y="215.5" text-anchor="middle" class="m">pip install -e .[dev]</text>
<rect x="20" y="232" width="210" height="30" rx="4" class="pnl"/>
<text x="125.0" y="251.5" text-anchor="middle" class="m">ruff check</text>
<rect x="20" y="268" width="210" height="30" rx="4" class="pnl"/>
<text x="125.0" y="287.5" text-anchor="middle" class="m">mypy (strict)</text>
<rect x="255" y="76" width="210" height="36" rx="7" class="k-blue"/>
<text x="360.0" y="98.5" text-anchor="middle" class="kb-blue">test  (matrix)</text>
<rect x="255" y="124" width="66" height="30" rx="4" class="pnl"/>
<text x="288.0" y="143.5" text-anchor="middle" class="m">3.11</text>
<rect x="327" y="124" width="66" height="30" rx="4" class="pnl"/>
<text x="360.0" y="143.5" text-anchor="middle" class="m">3.12</text>
<rect x="399" y="124" width="66" height="30" rx="4" class="pnl"/>
<text x="432.0" y="143.5" text-anchor="middle" class="m">3.13</text>
<rect x="255" y="160" width="210" height="30" rx="4" class="pnl"/>
<text x="360.0" y="179.5" text-anchor="middle" class="m">pytest --cov</text>
<rect x="255" y="196" width="210" height="30" rx="4" class="pnl"/>
<text x="360.0" y="215.5" text-anchor="middle" class="m">--cov-fail-under=90</text>
<rect x="490" y="76" width="210" height="36" rx="7" class="k-green"/>
<text x="595.0" y="98.5" text-anchor="middle" class="kb-green">package</text>
<rect x="490" y="124" width="210" height="30" rx="4" class="pnl"/>
<text x="595.0" y="143.5" text-anchor="middle" class="m">python -m build</text>
<rect x="490" y="160" width="210" height="30" rx="4" class="pnl"/>
<text x="595.0" y="179.5" text-anchor="middle" class="m">upload-artifact</text>
<rect x="490" y="196" width="210" height="30" rx="4" class="pnl"/>
<text x="595.0" y="215.5" text-anchor="middle" class="m">docker build</text>
<rect x="490" y="232" width="210" height="30" rx="4" class="pnl"/>
<text x="595.0" y="251.5" text-anchor="middle" class="m">docker run --version</text>
<line x1="232" y1="94" x2="253" y2="94" class="ar"/>
<text x="243" y="70" text-anchor="middle" class="c">needs</text>
<line x1="467" y1="94" x2="488" y2="94" class="ar"/>
<text x="478" y="70" text-anchor="middle" class="c">needs</text>
<text x="360" y="318" text-anchor="middle" class="c">file: .github/workflows/netwarden.yml   about 2 minutes per run</text>
</g>
</svg>
<figcaption>Jobs run on fresh virtual machines. The matrix runs the same tests on three Python versions in parallel.</figcaption>
</figure>

GitHub Actions runs **workflows** defined in YAML files in `.github/workflows/`. A workflow has **triggers** (`on:`), **jobs** that run on fresh virtual machines, and **steps** within each job, which either run shell commands or use reusable **actions**. NetWarden's workflow, `netwarden.yml`, in full:

```yaml
name: NetWarden CI

on:
  push:
    branches: [main]
    paths: ["netwarden/**", ".github/workflows/netwarden.yml"]
  pull_request:
    paths: ["netwarden/**", ".github/workflows/netwarden.yml"]

defaults:
  run:
    working-directory: netwarden

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
          cache: pip
      - run: pip install -e ".[dev]"
      - run: ruff check src tests
      - run: mypy

  test:
    needs: lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}
          cache: pip
      - run: pip install -e ".[dev]"
      - run: pytest --cov --cov-report=term-missing --cov-fail-under=90

  package:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
      - run: pip install build && python -m build
      - uses: actions/upload-artifact@v4
        with:
          name: netwarden-dist
          path: netwarden/dist/
      - run: docker build -t netwarden:${{ github.sha }} .
      - run: docker run --rm netwarden:${{ github.sha }} --version
```

Points to notice:

- **`paths`** limits the workflow to changes that affect NetWarden, not the book's chapters.
- **`needs`** orders the jobs: cheap, fast checks first, so a lint error fails in seconds without spending minutes on tests.
- The **matrix** tests every supported Python version in parallel, which verifies requirement NW-NFR-2.
- **Quality gates** are explicit: lint and type errors, any failing test, or coverage under 90% stop the pipeline.
- The last step is a **smoke test**: does the built image start at all?

With **branch protection** requiring these checks to pass before merging, `main` is always in a releasable state.

## Continuous delivery and deployment

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Continuous integration, delivery and deployment. Continuous integration automatically builds and tests every change. Continuous delivery also packages it and deploys it automatically to test and staging environments, so it is always ready to release, with a manual decision to go to production. Continuous deployment removes the manual step: every change that passes goes to production." xmlns="http://www.w3.org/2000/svg">
<style>
.s13c{ font-family:var(--sans),sans-serif; }
.s13c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s13c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s13c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s13c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s13c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s13c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s13c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s13c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s13c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s13c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s13c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s13c .s{ fill:var(--text-dim); font-size:13px; }
.s13c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s13c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s13c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s13c .c{ fill:var(--text-faint); font-size:12.5px; }
.s13c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s13c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s13c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s13c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13c-a); }
.s13c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13c-a); marker-start:url(#s13c-s); }
.s13c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s13c-g); }
.s13c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-a); }
.s13c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s13c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s13c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s13c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s13c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s13c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13c-tri); }
.s13c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-tri); }
.s13c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13c-open); }
.s13c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-open); }
.s13c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13c-dia); }
.s13c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13c-odia); }
.s13c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13c-dia); marker-end:url(#s13c-open); }
.s13c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13c-solid); }
.s13c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s13c-open); }
.s13c .fill{ fill:var(--text); stroke:none; }
.s13c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s13c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s13c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s13c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s13c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s13c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s13c .ks-blue{ fill:#185FA5; font-size:13px; }
.s13c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s13c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s13c .kb-blue, :root[data-theme="dark"] .s13c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s13c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s13c .kh-blue{ fill:#85B7EB; }
.s13c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s13c-blue); }
.s13c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-blue); }
.s13c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s13c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s13c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s13c .ks-amber{ fill:#854F0B; font-size:13px; }
.s13c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s13c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s13c .kb-amber, :root[data-theme="dark"] .s13c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s13c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s13c .kh-amber{ fill:#EF9F27; }
.s13c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s13c-amber); }
.s13c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-amber); }
.s13c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s13c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s13c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s13c .ks-green{ fill:#3B6D11; font-size:13px; }
.s13c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s13c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s13c .kb-green, :root[data-theme="dark"] .s13c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s13c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s13c .kh-green{ fill:#97C459; }
.s13c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s13c-green); }
.s13c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-green); }
.s13c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s13c .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s13c .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s13c .ks-red{ fill:#A32D2D; font-size:13px; }
.s13c .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s13c .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13c .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s13c .kb-red, :root[data-theme="dark"] .s13c .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s13c .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s13c .kh-red{ fill:#F09595; }
.s13c .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s13c-red); }
.s13c .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13c-red); }
.s13c .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s13c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s13c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s13c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s13c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s13c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s13c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s13c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s13c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s13c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s13c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s13c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s13c-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s13c">
<text x="220" y="26" text-anchor="middle" class="c">commit</text>
<text x="326" y="26" text-anchor="middle" class="c">build + test</text>
<text x="432" y="26" text-anchor="middle" class="c">package</text>
<text x="538" y="26" text-anchor="middle" class="c">staging</text>
<text x="644" y="26" text-anchor="middle" class="c">production</text>
<text x="20" y="70" text-anchor="start" class="kh-amber">continuous integration</text>
<rect x="172" y="44" width="96" height="40" rx="4" class="k-amber"/>
<text x="220.0" y="68.5" text-anchor="middle" class="ks-amber">auto</text>
<rect x="278" y="44" width="96" height="40" rx="4" class="k-amber"/>
<text x="326.0" y="68.5" text-anchor="middle" class="ks-amber">auto</text>
<rect x="384" y="44" width="96" height="40" rx="4" class="pnl"/>
<text x="432.0" y="68.5" text-anchor="middle" class="c">-</text>
<rect x="490" y="44" width="96" height="40" rx="4" class="pnl"/>
<text x="538.0" y="68.5" text-anchor="middle" class="c">-</text>
<rect x="596" y="44" width="96" height="40" rx="4" class="pnl"/>
<text x="644.0" y="68.5" text-anchor="middle" class="c">-</text>
<text x="20" y="134" text-anchor="start" class="kh-blue">continuous delivery</text>
<rect x="172" y="108" width="96" height="40" rx="4" class="k-blue"/>
<text x="220.0" y="132.5" text-anchor="middle" class="ks-blue">auto</text>
<rect x="278" y="108" width="96" height="40" rx="4" class="k-blue"/>
<text x="326.0" y="132.5" text-anchor="middle" class="ks-blue">auto</text>
<rect x="384" y="108" width="96" height="40" rx="4" class="k-blue"/>
<text x="432.0" y="132.5" text-anchor="middle" class="ks-blue">auto</text>
<rect x="490" y="108" width="96" height="40" rx="4" class="k-blue"/>
<text x="538.0" y="132.5" text-anchor="middle" class="ks-blue">auto</text>
<rect x="596" y="108" width="96" height="40" rx="4" class="k-red"/>
<text x="644.0" y="132.5" text-anchor="middle" class="ks-red">manual</text>
<text x="20" y="198" text-anchor="start" class="kh-green">continuous deployment</text>
<rect x="172" y="172" width="96" height="40" rx="4" class="k-green"/>
<text x="220.0" y="196.5" text-anchor="middle" class="ks-green">auto</text>
<rect x="278" y="172" width="96" height="40" rx="4" class="k-green"/>
<text x="326.0" y="196.5" text-anchor="middle" class="ks-green">auto</text>
<rect x="384" y="172" width="96" height="40" rx="4" class="k-green"/>
<text x="432.0" y="196.5" text-anchor="middle" class="ks-green">auto</text>
<rect x="490" y="172" width="96" height="40" rx="4" class="k-green"/>
<text x="538.0" y="196.5" text-anchor="middle" class="ks-green">auto</text>
<rect x="596" y="172" width="96" height="40" rx="4" class="k-green"/>
<text x="644.0" y="196.5" text-anchor="middle" class="ks-green">auto</text>
<text x="360" y="240" text-anchor="middle" class="c">delivery: always releasable, a human presses the button; deployment: the pipeline presses it</text>
</g>
</svg>
<figcaption>All three rely on the same thing: a fast, trustworthy, automated pipeline.</figcaption>
</figure>

**Continuous delivery** means every change that passes the pipeline is **releasable**: packaged, deployed automatically to test environments, and one decision away from production. **Continuous deployment** goes further and releases every passing change automatically. Jez Humble and David Farley's book *Continuous Delivery* (2010) set out the principles; the central one is that releasing should be boring.

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Build once, deploy many. The pipeline builds one immutable artifact, the netwarden wheel and container image tagged with the commit hash, and promotes the same artifact through test, staging and production. Only configuration differs between environments." xmlns="http://www.w3.org/2000/svg">
<style>
.s13e{ font-family:var(--sans),sans-serif; }
.s13e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s13e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s13e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s13e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s13e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s13e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s13e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s13e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s13e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s13e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s13e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s13e .s{ fill:var(--text-dim); font-size:13px; }
.s13e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s13e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .c{ fill:var(--text-faint); font-size:12.5px; }
.s13e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s13e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s13e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s13e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13e-a); }
.s13e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13e-a); marker-start:url(#s13e-s); }
.s13e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s13e-g); }
.s13e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-a); }
.s13e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s13e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s13e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s13e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s13e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s13e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13e-tri); }
.s13e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-tri); }
.s13e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13e-open); }
.s13e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-open); }
.s13e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13e-dia); }
.s13e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13e-odia); }
.s13e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13e-dia); marker-end:url(#s13e-open); }
.s13e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13e-solid); }
.s13e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s13e-open); }
.s13e .fill{ fill:var(--text); stroke:none; }
.s13e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s13e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s13e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s13e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s13e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s13e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s13e .ks-blue{ fill:#185FA5; font-size:13px; }
.s13e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s13e .kb-blue, :root[data-theme="dark"] .s13e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s13e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s13e .kh-blue{ fill:#85B7EB; }
.s13e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s13e-blue); }
.s13e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-blue); }
.s13e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s13e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s13e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s13e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s13e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s13e .kb-teal, :root[data-theme="dark"] .s13e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s13e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s13e .kh-teal{ fill:#5DCAA5; }
.s13e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s13e-teal); }
.s13e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-teal); }
.s13e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s13e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s13e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s13e .ks-amber{ fill:#854F0B; font-size:13px; }
.s13e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s13e .kb-amber, :root[data-theme="dark"] .s13e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s13e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s13e .kh-amber{ fill:#EF9F27; }
.s13e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s13e-amber); }
.s13e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-amber); }
.s13e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s13e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s13e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s13e .ks-purple{ fill:#534AB7; font-size:13px; }
.s13e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s13e .kb-purple, :root[data-theme="dark"] .s13e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s13e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s13e .kh-purple{ fill:#AFA9EC; }
.s13e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s13e-purple); }
.s13e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-purple); }
.s13e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s13e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s13e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s13e .ks-green{ fill:#3B6D11; font-size:13px; }
.s13e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s13e .kb-green, :root[data-theme="dark"] .s13e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s13e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s13e .kh-green{ fill:#97C459; }
.s13e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s13e-green); }
.s13e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-green); }
.s13e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s13e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s13e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s13e .ks-red{ fill:#A32D2D; font-size:13px; }
.s13e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s13e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s13e .kb-red, :root[data-theme="dark"] .s13e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s13e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s13e .kh-red{ fill:#F09595; }
.s13e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s13e-red); }
.s13e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13e-red); }
.s13e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s13e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s13e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s13e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s13e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s13e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s13e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s13e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s13e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s13e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s13e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s13e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s13e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s13e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s13e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s13e">
<rect x="20" y="80" width="130" height="60" rx="7" class="k-amber"/>
<text x="85.0" y="105.5" text-anchor="middle" class="kb-amber">build once</text>
<text x="85.0" y="123.5" text-anchor="middle" class="km-amber">commit 3f2a9c1</text>
<rect x="190" y="70" width="160" height="80" rx="7" class="k-purple"/>
<text x="270.0" y="96.5" text-anchor="middle" class="kb-purple">artifact</text>
<text x="270.0" y="114.5" text-anchor="middle" class="km-purple">netwarden:3f2a9c1</text>
<text x="270.0" y="132.5" text-anchor="middle" class="ks-purple">+ wheel, SBOM</text>
<line x1="152" y1="110" x2="188" y2="110" class="ar"/>
<rect x="400" y="80" width="96" height="60" rx="7" class="k-blue"/>
<text x="448.0" y="105.5" text-anchor="middle" class="kb-blue">test</text>
<text x="448.0" y="123.5" text-anchor="middle" class="ks-blue">config: env</text>
<line x1="352" y1="110" x2="398" y2="110" class="ar"/>
<rect x="504" y="80" width="96" height="60" rx="7" class="k-teal"/>
<text x="552.0" y="105.5" text-anchor="middle" class="kb-teal">staging</text>
<text x="552.0" y="123.5" text-anchor="middle" class="ks-teal">config: env</text>
<line x1="496" y1="110" x2="502" y2="110" class="ar"/>
<rect x="608" y="80" width="96" height="60" rx="7" class="k-green"/>
<text x="656.0" y="105.5" text-anchor="middle" class="kb-green">production</text>
<text x="656.0" y="123.5" text-anchor="middle" class="ks-green">config: env</text>
<line x1="600" y1="110" x2="606" y2="110" class="ar"/>
<text x="360" y="190" text-anchor="middle" class="kh-red">never rebuild for production: what you tested is exactly what you ship</text>
</g>
</svg>
<figcaption>Rebuilding per environment risks shipping something slightly different from what was tested.</figcaption>
</figure>

**Build once, deploy many**: the pipeline builds one artifact, tagged with the commit it came from, and promotes that same artifact through environments. Only configuration changes between environments (Chapter 14).

## Versioning and releases

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Semantic versioning: MAJOR.MINOR.PATCH. Increment PATCH for backward-compatible bug fixes, such as 1.0.1 fixing ProFTPD letter versions; MINOR for backward-compatible new features, such as 1.1.0 adding a CSV report; MAJOR for incompatible changes, such as 2.0.0 changing the JSON report format." xmlns="http://www.w3.org/2000/svg">
<style>
.s13d{ font-family:var(--sans),sans-serif; }
.s13d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s13d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s13d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s13d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s13d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s13d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s13d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s13d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s13d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s13d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s13d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s13d .s{ fill:var(--text-dim); font-size:13px; }
.s13d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s13d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s13d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s13d .c{ fill:var(--text-faint); font-size:12.5px; }
.s13d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s13d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s13d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s13d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13d-a); }
.s13d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s13d-a); marker-start:url(#s13d-s); }
.s13d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s13d-g); }
.s13d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s13d-a); }
.s13d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s13d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s13d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s13d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s13d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s13d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13d-tri); }
.s13d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13d-tri); }
.s13d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13d-open); }
.s13d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s13d-open); }
.s13d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13d-dia); }
.s13d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13d-odia); }
.s13d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s13d-dia); marker-end:url(#s13d-open); }
.s13d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s13d-solid); }
.s13d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s13d-open); }
.s13d .fill{ fill:var(--text); stroke:none; }
.s13d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s13d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s13d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s13d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s13d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s13d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s13d .ks-blue{ fill:#185FA5; font-size:13px; }
.s13d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s13d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s13d .kb-blue, :root[data-theme="dark"] .s13d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s13d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s13d .kh-blue{ fill:#85B7EB; }
.s13d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s13d-blue); }
.s13d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13d-blue); }
.s13d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s13d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s13d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s13d .ks-green{ fill:#3B6D11; font-size:13px; }
.s13d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s13d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s13d .kb-green, :root[data-theme="dark"] .s13d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s13d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s13d .kh-green{ fill:#97C459; }
.s13d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s13d-green); }
.s13d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13d-green); }
.s13d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s13d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s13d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s13d .ks-red{ fill:#A32D2D; font-size:13px; }
.s13d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s13d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s13d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s13d .kb-red, :root[data-theme="dark"] .s13d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s13d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s13d .kh-red{ fill:#F09595; }
.s13d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s13d-red); }
.s13d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s13d-red); }
.s13d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s13d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s13d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s13d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s13d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s13d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s13d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s13d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s13d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s13d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s13d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s13d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s13d">
<rect x="210" y="20" width="80" height="70" rx="7" class="k-red"/>
<text x="250.0" y="59.5" text-anchor="middle" class="kb-red">1</text>
<rect x="320" y="20" width="80" height="70" rx="7" class="k-blue"/>
<text x="360.0" y="59.5" text-anchor="middle" class="kb-blue">1</text>
<text x="315" y="70" text-anchor="middle" class="h">.</text>
<rect x="430" y="20" width="80" height="70" rx="7" class="k-green"/>
<text x="470.0" y="59.5" text-anchor="middle" class="kb-green">0</text>
<text x="425" y="70" text-anchor="middle" class="h">.</text>
<text x="250" y="110" text-anchor="middle" class="kh-red">MAJOR</text>
<text x="360" y="110" text-anchor="middle" class="kh-blue">MINOR</text>
<text x="470" y="110" text-anchor="middle" class="kh-green">PATCH</text>
<rect x="20" y="130" width="220" height="32" rx="4" class="k-green"/>
<text x="130.0" y="150.5" text-anchor="middle" class="kb-green">PATCH: compatible bug fix</text>
<text x="256" y="151" text-anchor="start" class="m">1.0.0 -&gt; 1.0.1  fix: ProFTPD letter versions</text>
<rect x="20" y="168" width="220" height="32" rx="4" class="k-blue"/>
<text x="130.0" y="188.5" text-anchor="middle" class="kb-blue">MINOR: compatible feature</text>
<text x="256" y="189" text-anchor="start" class="m">1.0.1 -&gt; 1.1.0  feat: CSV report</text>
<rect x="20" y="206" width="220" height="32" rx="4" class="k-red"/>
<text x="130.0" y="226.5" text-anchor="middle" class="kb-red">MAJOR: breaking change</text>
<text x="256" y="227" text-anchor="start" class="m">1.1.0 -&gt; 2.0.0  JSON report format changed</text>
</g>
</svg>
<figcaption>A version number is a promise about compatibility. Conventional Commits let tools compute the next one.</figcaption>
</figure>

**Semantic Versioning** (SemVer) encodes compatibility in the version number. NetWarden's "public API" for SemVer purposes is its command-line interface and its JSON report format; a change that breaks a script parsing the JSON is a major change. Releases are recorded in `CHANGELOG.md` using the **Keep a Changelog** format, with sections such as Added, Changed, Fixed and Removed per version.

A release is then a short, scripted sequence:

```bash
# update version in pyproject.toml and src/netwarden/__init__.py, and CHANGELOG.md
git commit -am "chore(release): 1.0.0"
git tag -a v1.0.0 -m "NetWarden 1.0.0"
git push origin main --tags
```

A further workflow, triggered by the tag, can build and publish the wheel to PyPI using **trusted publishing** (no stored passwords), push the image to a container registry, attach an SBOM, and create a GitHub release with notes generated from the Conventional Commits since the previous tag. Tools such as `release-please` or `python-semantic-release` automate the version calculation and changelog.

## Securing the pipeline

The pipeline has the keys to the kingdom: it can change production. Treat it as a critical system:

- Give workflows **least privilege**: `permissions: contents: read` unless they need more.
- Keep secrets in the platform's secret store, never in YAML; prefer short-lived credentials (OpenID Connect) to long-lived tokens.
- Be careful with workflows that run on pull requests from **forks**: untrusted code must not see secrets.
- Pin third-party actions to versions you have reviewed; Dependabot can keep the pins current.

## Hands on

1. Fork the book's repository on GitHub, enable Actions, make a small change in `netwarden/`, and open a pull request to your fork's `main`. Watch the three jobs run.
2. Break a test on purpose and push again. Where does the pipeline stop, and how long did it take to tell you?
3. Add Python 3.14 to the matrix. Does everything still pass? This is **adaptive maintenance** (Chapter 15).
4. Build the wheel locally with `python -m build` and install it into a fresh virtual environment. Run `netwarden --version`.

## Summary

- **Build automation** turns source into tested, packaged artifacts with one command; `pyproject.toml` describes Python projects.
- **Declare, pin, update deliberately, and audit** dependencies.
- **Continuous integration**: frequent merges to main, each verified by a fast, self-testing automated build; broken builds are fixed first.
- A **pipeline** runs ordered jobs and **quality gates**; NetWarden's checks lint, types, tests on three Python versions, coverage, packaging and a smoke test.
- **Continuous delivery** keeps every change releasable; **continuous deployment** releases every passing change. **Build once**, promote the same artifact.
- **Semantic versioning** communicates compatibility; changelogs and tags make releases traceable.
- Secure the pipeline: least privilege, managed secrets, care with untrusted pull requests.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-13-build-automation-and-cicd).

**1. What is continuous integration?**

- A. Merging to main frequently, each change verified by a fast, self-testing automated build
- B. Releasing every week
- C. Integrating with other companies
- D. Running tests once before release

**2. Which file describes a modern Python project's build, dependencies and tools?**

- A. setup.cfg only
- B. requirements.txt only
- C. pyproject.toml
- D. Makefile

**3. What does the chapter advise for dependencies?**

- A. Always use the latest version
- B. Declare, pin, update deliberately, and audit them
- C. Copy them into the repository
- D. Avoid all dependencies

**4. Why does NetWarden's pipeline test on three Python versions?**

- A. To make builds slower
- B. Because pytest requires it
- C. To compare speed
- D. To catch incompatibilities across the versions users run

**5. How do continuous delivery and continuous deployment differ?**

- A. They are the same
- B. Delivery keeps every change releasable; deployment releases every passing change automatically
- C. Deployment needs no tests
- D. Delivery is only for mobile apps

**6. What does 'build once, promote the same artifact' prevent?**

- A. Slow builds
- B. Version numbers
- C. Dependency updates
- D. Differences between what was tested and what is released

**7. Under semantic versioning, which part changes for an incompatible API change?**

- A. Major
- B. Patch
- C. Minor
- D. Build

**8. Which is a pipeline security practice from the chapter?**

- A. Give the pipeline admin rights everywhere
- B. Store secrets in the repository
- C. Least privilege, managed secrets, and care with untrusted pull requests
- D. Run every fork's code with secrets
