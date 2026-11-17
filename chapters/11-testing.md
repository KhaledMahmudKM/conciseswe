# Chapter 11: Software Testing

**Testing** is executing software in order to find failures and to gain confidence that it meets its requirements. It is the main way teams check their work, and automated tests are what make refactoring (Chapter 10) and continuous delivery (Chapter 13) safe. This chapter covers the vocabulary, the levels and types of tests, how to design test cases, test doubles, test-driven development and coverage, using NetWarden's 46 tests throughout.

## Vocabulary

<figure class="diagram">
<svg viewBox="0 0 720 220" style="width:100%;height:auto;max-width:720px" role="img" aria-label="From mistake to failure. A developer makes an error, for example comparing versions as strings. The error leaves a fault, also called a defect or bug, in the code. When the faulty code runs with certain inputs, such as OpenSSH 10.0p1, it produces a failure: a wrong result visible to the user, here a false CVE report. Testing finds failures; debugging finds faults." xmlns="http://www.w3.org/2000/svg">
<style>
.s11a{ font-family:var(--sans),sans-serif; }
.s11a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11a .s{ fill:var(--text-dim); font-size:13px; }
.s11a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11a .c{ fill:var(--text-faint); font-size:12.5px; }
.s11a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11a-a); }
.s11a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11a-a); marker-start:url(#s11a-s); }
.s11a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11a-g); }
.s11a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-a); }
.s11a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11a-tri); }
.s11a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-tri); }
.s11a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11a-open); }
.s11a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-open); }
.s11a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11a-dia); }
.s11a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11a-odia); }
.s11a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11a-dia); marker-end:url(#s11a-open); }
.s11a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11a-solid); }
.s11a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11a-open); }
.s11a .fill{ fill:var(--text); stroke:none; }
.s11a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11a .ks-amber{ fill:#854F0B; font-size:13px; }
.s11a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11a .kb-amber, :root[data-theme="dark"] .s11a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11a .kh-amber{ fill:#EF9F27; }
.s11a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11a-amber); }
.s11a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-amber); }
.s11a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s11a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s11a .ks-purple{ fill:#534AB7; font-size:13px; }
.s11a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s11a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s11a .kb-purple, :root[data-theme="dark"] .s11a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s11a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s11a .kh-purple{ fill:#AFA9EC; }
.s11a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s11a-purple); }
.s11a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-purple); }
.s11a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s11a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11a .ks-red{ fill:#A32D2D; font-size:13px; }
.s11a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11a .kb-red, :root[data-theme="dark"] .s11a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11a .kh-red{ fill:#F09595; }
.s11a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11a-red); }
.s11a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-red); }
.s11a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s11a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s11a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s11a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s11a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s11a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s11a .kb-gray, :root[data-theme="dark"] .s11a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s11a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s11a .kh-gray{ fill:#B4B2A9; }
.s11a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s11a-gray); }
.s11a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11a-gray); }
.s11a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s11a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s11a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s11a">
<rect x="20" y="40" width="200" height="90" rx="7" class="k-purple"/>
<text x="120.0" y="67.5" text-anchor="middle" class="kb-purple">error</text>
<text x="120.0" y="89.5" text-anchor="middle" class="ks-purple">a human mistake</text>
<text x="120.0" y="111.5" text-anchor="middle" class="km-purple">"compare as strings"</text>
<rect x="260" y="40" width="200" height="90" rx="7" class="k-amber"/>
<text x="360.0" y="67.5" text-anchor="middle" class="kb-amber">fault (defect)</text>
<text x="360.0" y="89.5" text-anchor="middle" class="ks-amber">in the code</text>
<text x="360.0" y="111.5" text-anchor="middle" class="km-amber">v &gt;= "8.5p1"</text>
<line x1="222" y1="85" x2="258" y2="85" class="ar"/>
<rect x="500" y="40" width="200" height="90" rx="7" class="k-red"/>
<text x="600.0" y="67.5" text-anchor="middle" class="kb-red">failure</text>
<text x="600.0" y="89.5" text-anchor="middle" class="ks-red">wrong behaviour</text>
<text x="600.0" y="111.5" text-anchor="middle" class="km-red">10.0p1 flagged</text>
<line x1="462" y1="85" x2="498" y2="85" class="ar"/>
<text x="260" y="170" text-anchor="middle" class="c">debugging works backwards from a failure to the fault</text>
<text x="260" y="196" text-anchor="middle" class="c">testing tries to provoke failures before users do</text>
<text x="620" y="180" text-anchor="middle" class="kh-gray">not every fault causes a failure</text>
</g>
</svg>
<figcaption>Testing can show the presence of bugs, never their absence (Dijkstra). It reduces risk; it cannot prove correctness.</figcaption>
</figure>

| Term | Meaning |
|---|---|
| **Error** (mistake) | A human action that produces an incorrect result |
| **Fault** (defect, bug) | An imperfection in the code or documents |
| **Failure** | The system behaving differently from what is required |
| **Verification** | Are we building the product right? Does it meet its specification? |
| **Validation** | Are we building the right product? Does it meet users' needs? |
| **Test case** | Inputs, preconditions and expected results for one check |
| **Test oracle** | The source of the expected result |
| **Regression** | Something that used to work and no longer does |

Edsger Dijkstra's remark that testing "can be used to show the presence of bugs, but never to show their absence" is the key limit. Exhaustive testing is impossible: NetWarden's inputs include every possible banner from every possible host. Testing is therefore a **risk-based sampling** problem: choose the tests most likely to reveal the failures that matter most.

## Levels of testing

| Level | Tests | Example in NetWarden |
|---|---|---|
| **Unit** | One function or class in isolation | `test_fingerprint` with nine banners |
| **Component** | A group of units, collaborators replaced | `test_engine.py` with a fake scanner |
| **Integration** | Real interactions between parts and with external systems | `test_integration.py`: real sockets against demo services, real SQLite |
| **System** | The whole system in a realistic environment | Manual scan of a lab VLAN before release |
| **Acceptance** | Does it satisfy users and the acceptance criteria? | Gherkin scenarios for each user story, demonstrated at sprint review |

<figure class="diagram">
<svg viewBox="0 0 720 345" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden&#x27;s test pyramid. At the base, 38 unit tests that run in milliseconds. Above them, 3 component tests of the engine with test doubles. Above those, 5 integration tests with real sockets against the demo targets, taking about half a second each. At the top, a manual system test on a lab network before each release. The ice cream cone anti-pattern, mostly manual and end-to-end tests, is shown for contrast." xmlns="http://www.w3.org/2000/svg">
<style>
.s11b{ font-family:var(--sans),sans-serif; }
.s11b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11b .s{ fill:var(--text-dim); font-size:13px; }
.s11b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11b .c{ fill:var(--text-faint); font-size:12.5px; }
.s11b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11b-a); }
.s11b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11b-a); marker-start:url(#s11b-s); }
.s11b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11b-g); }
.s11b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-a); }
.s11b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11b-tri); }
.s11b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-tri); }
.s11b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11b-open); }
.s11b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-open); }
.s11b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11b-dia); }
.s11b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11b-odia); }
.s11b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11b-dia); marker-end:url(#s11b-open); }
.s11b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11b-solid); }
.s11b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11b-open); }
.s11b .fill{ fill:var(--text); stroke:none; }
.s11b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11b .ks-amber{ fill:#854F0B; font-size:13px; }
.s11b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11b .kb-amber, :root[data-theme="dark"] .s11b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11b .kh-amber{ fill:#EF9F27; }
.s11b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11b-amber); }
.s11b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-amber); }
.s11b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s11b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s11b .ks-purple{ fill:#534AB7; font-size:13px; }
.s11b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s11b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s11b .kb-purple, :root[data-theme="dark"] .s11b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s11b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s11b .kh-purple{ fill:#AFA9EC; }
.s11b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s11b-purple); }
.s11b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-purple); }
.s11b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s11b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s11b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s11b .ks-green{ fill:#3B6D11; font-size:13px; }
.s11b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s11b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s11b .kb-green, :root[data-theme="dark"] .s11b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s11b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s11b .kh-green{ fill:#97C459; }
.s11b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s11b-green); }
.s11b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-green); }
.s11b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s11b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11b .ks-red{ fill:#A32D2D; font-size:13px; }
.s11b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11b .kb-red, :root[data-theme="dark"] .s11b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11b .kh-red{ fill:#F09595; }
.s11b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11b-red); }
.s11b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11b-red); }
.s11b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s11b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s11b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s11b">
<rect x="235.0" y="20" width="170" height="58" rx="7" class="k-red"/>
<text x="320.0" y="44.5" text-anchor="middle" class="kb-red">manual system test</text>
<text x="320.0" y="62.5" text-anchor="middle" class="ks-red">lab VLAN, per release</text>
<rect x="205.0" y="90" width="230" height="58" rx="7" class="k-amber"/>
<text x="320.0" y="114.5" text-anchor="middle" class="kb-amber">integration: 5</text>
<text x="320.0" y="132.5" text-anchor="middle" class="ks-amber">real sockets, ~0.5 s each</text>
<rect x="145.0" y="160" width="350" height="58" rx="7" class="k-purple"/>
<text x="320.0" y="184.5" text-anchor="middle" class="kb-purple">component: 3</text>
<text x="320.0" y="202.5" text-anchor="middle" class="ks-purple">engine + test doubles</text>
<rect x="85.0" y="230" width="470" height="58" rx="7" class="k-green"/>
<text x="320.0" y="254.5" text-anchor="middle" class="kb-green">unit: 38</text>
<text x="320.0" y="272.5" text-anchor="middle" class="ks-green">milliseconds each</text>
<line x1="20" y1="335" x2="20" y2="30" class="ar"/>
<text x="30" y="40" text-anchor="start" class="c">slower, costlier, more realistic</text>
<text x="30" y="334" text-anchor="start" class="c">faster, cheaper, more precise</text>
<text x="700" y="20" text-anchor="end" class="kh-red">anti-pattern: ice cream cone</text>
<rect x="580.0" y="36" width="120" height="38" rx="4" class="k-red"/>
<rect x="595.0" y="82" width="90" height="38" rx="4" class="k-red"/>
<rect x="612.0" y="128" width="56" height="38" rx="4" class="k-amber"/>
<rect x="628.0" y="174" width="24" height="38" rx="4" class="k-green"/>
<text x="640" y="240" text-anchor="middle" class="c">mostly manual,</text>
<text x="640" y="258" text-anchor="middle" class="c">slow, flaky</text>
</g>
</svg>
<figcaption>Many fast, focused tests at the bottom; a few slow, broad ones at the top. pytest runs all 46 in about 4 seconds.</figcaption>
</figure>

Mike Cohn's **test pyramid** recommends many fast unit tests, fewer integration tests, and few slow end-to-end tests. Unit tests pinpoint failures and run in milliseconds; end-to-end tests are realistic but slow, brittle and hard to diagnose. The inverted shape, the **ice cream cone**, is common in organisations that rely on manual testing, and leads to slow releases and fear of change.

## Writing good tests

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Anatomy of a unit test from NetWarden, in the arrange, act, assert pattern: arrange a scope covering 192.168.56.0/24; act by expanding the target 8.8.8.8 inside pytest.raises; assert that a ScopeError mentioning outside the authorised scope is raised. The test name states the behaviour being checked." xmlns="http://www.w3.org/2000/svg">
<style>
.s11c{ font-family:var(--sans),sans-serif; }
.s11c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11c .s{ fill:var(--text-dim); font-size:13px; }
.s11c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11c .c{ fill:var(--text-faint); font-size:12.5px; }
.s11c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11c-a); }
.s11c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11c-a); marker-start:url(#s11c-s); }
.s11c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11c-g); }
.s11c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-a); }
.s11c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11c-tri); }
.s11c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-tri); }
.s11c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11c-open); }
.s11c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-open); }
.s11c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11c-dia); }
.s11c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11c-odia); }
.s11c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11c-dia); marker-end:url(#s11c-open); }
.s11c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11c-solid); }
.s11c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11c-open); }
.s11c .fill{ fill:var(--text); stroke:none; }
.s11c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s11c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s11c .ks-blue{ fill:#185FA5; font-size:13px; }
.s11c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s11c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s11c .kb-blue, :root[data-theme="dark"] .s11c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s11c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s11c .kh-blue{ fill:#85B7EB; }
.s11c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s11c-blue); }
.s11c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-blue); }
.s11c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s11c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11c .ks-amber{ fill:#854F0B; font-size:13px; }
.s11c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11c .kb-amber, :root[data-theme="dark"] .s11c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11c .kh-amber{ fill:#EF9F27; }
.s11c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11c-amber); }
.s11c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-amber); }
.s11c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11c .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11c .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11c .ks-red{ fill:#A32D2D; font-size:13px; }
.s11c .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11c .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11c .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11c .kb-red, :root[data-theme="dark"] .s11c .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11c .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11c .kh-red{ fill:#F09595; }
.s11c .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11c-red); }
.s11c .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-red); }
.s11c .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s11c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s11c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s11c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s11c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s11c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s11c .kb-gray, :root[data-theme="dark"] .s11c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s11c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s11c .kh-gray{ fill:#B4B2A9; }
.s11c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s11c-gray); }
.s11c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11c-gray); }
.s11c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s11c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11c-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s11c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s11c">
<rect x="20" y="20" width="510" height="200" rx="6" class="pnl"/>
<text x="34" y="52" text-anchor="start" class="m">def test_scope_refuses_targets_outside_it():</text>
<text x="64.0" y="88" text-anchor="start" class="km-blue">scope = Scope(["192.168.56.0/24"])</text>
<text x="64.0" y="124" text-anchor="start" class="km-red">with pytest.raises(ScopeError,</text>
<text x="206.5" y="160" text-anchor="start" class="km-red">match="outside the authorised scope"):</text>
<text x="94.0" y="196" text-anchor="start" class="km-amber">scope.expand(["8.8.8.8"])</text>
<rect x="546" y="62" width="154" height="32" rx="4" class="k-blue"/>
<text x="623.0" y="82.5" text-anchor="middle" class="kb-blue">arrange</text>
<rect x="546" y="108" width="154" height="32" rx="4" class="k-red"/>
<text x="623.0" y="128.5" text-anchor="middle" class="kb-red">assert (expect)</text>
<rect x="546" y="174" width="154" height="32" rx="4" class="k-amber"/>
<text x="623.0" y="194.5" text-anchor="middle" class="kb-amber">act</text>
<text x="605" y="40" text-anchor="middle" class="kh-gray">name = behaviour</text>
</g>
</svg>
<figcaption>One behaviour per test, a name that says what it checks, and no logic in the test itself.</figcaption>
</figure>

Good automated tests are **FIRST**: Fast, Isolated (independent of each other and of order), Repeatable (same result every run), Self-validating (pass or fail, no reading output), and Timely (written with the code). The **arrange, act, assert** structure keeps each test readable.

pytest makes tests plain functions with plain `assert` statements, and provides **fixtures** for setup and **parametrize** for running one test over many inputs:

```python
@pytest.mark.parametrize("port, banner, name, product, version", [
    (22, "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6", "ssh", "OpenSSH", "8.9p1"),
    (21, "220 (vsFTPd 2.3.4)", "ftp", "vsftpd", "2.3.4"),
    (21, "220 ProFTPD 1.3.5a Server (Debian)", "ftp", "ProFTPD", "1.3.5a"),
    (80, "HTTP/1.1 200 OK\r\nServer: Apache/2.4.49 (Unix)", "http", "Apache httpd", "2.4.49"),
    (2323, "\xff\xfd\x18login: ", "telnet", None, None),
    (40000, "", "unknown", None, None),
])
def test_fingerprint(port, banner, name, product, version):
    s = Fingerprinter().identify(Service(port, banner))
    assert (s.name, s.product, s.version) == (name, product, version)
```

The session-scoped fixture `demo_ports` in `tests/conftest.py` starts the fake demo services once, on free ports chosen by the operating system, in a background thread, and shuts them down cleanly afterwards. The integration tests use it to scan real sockets on `127.0.0.1` without any external network, so they are repeatable on every developer's machine and in CI.

## Designing test cases

### Black-box techniques

**Black-box** (specification-based) techniques derive tests from requirements without looking at the code.

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Equivalence partitions and boundary values for Severity.from_cvss. The CVSS score range 0 to 10 splits into five partitions: 0 is INFO, 0.1 to 3.9 LOW, 4.0 to 6.9 MEDIUM, 7.0 to 8.9 HIGH, 9.0 to 10.0 CRITICAL. Test values sit on both sides of each boundary: 0.0, 0.1, 3.9, 4.0, 6.9, 7.0, 8.9, 9.0 and 10.0." xmlns="http://www.w3.org/2000/svg">
<style>
.s11f{ font-family:var(--sans),sans-serif; }
.s11f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11f .s{ fill:var(--text-dim); font-size:13px; }
.s11f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .c{ fill:var(--text-faint); font-size:12.5px; }
.s11f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11f-a); }
.s11f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11f-a); marker-start:url(#s11f-s); }
.s11f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11f-g); }
.s11f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-a); }
.s11f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11f-tri); }
.s11f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-tri); }
.s11f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11f-open); }
.s11f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-open); }
.s11f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11f-dia); }
.s11f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11f-odia); }
.s11f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11f-dia); marker-end:url(#s11f-open); }
.s11f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11f-solid); }
.s11f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11f-open); }
.s11f .fill{ fill:var(--text); stroke:none; }
.s11f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s11f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s11f .ks-blue{ fill:#185FA5; font-size:13px; }
.s11f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s11f .kb-blue, :root[data-theme="dark"] .s11f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s11f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s11f .kh-blue{ fill:#85B7EB; }
.s11f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s11f-blue); }
.s11f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-blue); }
.s11f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s11f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11f .ks-amber{ fill:#854F0B; font-size:13px; }
.s11f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11f .kb-amber, :root[data-theme="dark"] .s11f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11f .kh-amber{ fill:#EF9F27; }
.s11f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11f-amber); }
.s11f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-amber); }
.s11f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11f .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s11f .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s11f .ks-coral{ fill:#993C1D; font-size:13px; }
.s11f .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11f .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s11f .kb-coral, :root[data-theme="dark"] .s11f .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s11f .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s11f .kh-coral{ fill:#F0997B; }
.s11f .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s11f-coral); }
.s11f .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-coral); }
.s11f .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s11f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11f .ks-red{ fill:#A32D2D; font-size:13px; }
.s11f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11f .kb-red, :root[data-theme="dark"] .s11f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11f .kh-red{ fill:#F09595; }
.s11f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11f-red); }
.s11f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-red); }
.s11f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s11f .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s11f .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s11f .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s11f .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s11f .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11f .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s11f .kb-gray, :root[data-theme="dark"] .s11f .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s11f .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s11f .kh-gray{ fill:#B4B2A9; }
.s11f .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s11f-gray); }
.s11f .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11f-gray); }
.s11f .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s11f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11f-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s11f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s11f-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s11f">
<rect x="40.0" y="60" width="14" height="44" rx="2" class="k-gray"/>
<rect x="46.4" y="60" width="249.6" height="44" rx="2" class="k-blue"/>
<text x="171.2" y="88" text-anchor="middle" class="kb-blue">LOW</text>
<rect x="296.0" y="60" width="192.0" height="44" rx="2" class="k-amber"/>
<text x="392.0" y="88" text-anchor="middle" class="kb-amber">MEDIUM</text>
<rect x="488.0" y="60" width="128.0" height="44" rx="2" class="k-coral"/>
<text x="552.0" y="88" text-anchor="middle" class="kb-coral">HIGH</text>
<rect x="616.0" y="60" width="64.0" height="44" rx="2" class="k-red"/>
<text x="36.0" y="48" text-anchor="start" class="kh-gray">INFO</text>
<text x="680.0" y="48" text-anchor="end" class="kh-red">CRITICAL</text>
<line x1="40.0" y1="108" x2="40.0" y2="124" class="ln-red"/>
<circle cx="40.0" cy="128" r="4" class="k-red"/>
<line x1="46.4" y1="108" x2="46.4" y2="124" class="ln-red"/>
<circle cx="46.4" cy="128" r="4" class="k-red"/>
<line x1="289.6" y1="108" x2="289.6" y2="124" class="ln-red"/>
<circle cx="289.6" cy="128" r="4" class="k-red"/>
<line x1="296.0" y1="108" x2="296.0" y2="124" class="ln-red"/>
<circle cx="296.0" cy="128" r="4" class="k-red"/>
<line x1="481.6" y1="108" x2="481.6" y2="124" class="ln-red"/>
<circle cx="481.6" cy="128" r="4" class="k-red"/>
<line x1="488.0" y1="108" x2="488.0" y2="124" class="ln-red"/>
<circle cx="488.0" cy="128" r="4" class="k-red"/>
<line x1="609.6" y1="108" x2="609.6" y2="124" class="ln-red"/>
<circle cx="609.6" cy="128" r="4" class="k-red"/>
<line x1="616.0" y1="108" x2="616.0" y2="124" class="ln-red"/>
<circle cx="616.0" cy="128" r="4" class="k-red"/>
<line x1="680.0" y1="108" x2="680.0" y2="124" class="ln-red"/>
<circle cx="680.0" cy="128" r="4" class="k-red"/>
<text x="26.0" y="152" text-anchor="middle" class="m">0.0</text>
<text x="60.4" y="152" text-anchor="middle" class="m">0.1</text>
<text x="275.6" y="152" text-anchor="middle" class="m">3.9</text>
<text x="310.0" y="152" text-anchor="middle" class="m">4.0</text>
<text x="467.6" y="152" text-anchor="middle" class="m">6.9</text>
<text x="502.0" y="152" text-anchor="middle" class="m">7.0</text>
<text x="595.6" y="152" text-anchor="middle" class="m">8.9</text>
<text x="630.0" y="152" text-anchor="middle" class="m">9.0</text>
<text x="694.0" y="152" text-anchor="middle" class="m">10.0</text>
<text x="360" y="196" text-anchor="middle" class="kh-red">9 tests from one @pytest.mark.parametrize: every boundary, both sides</text>
</g>
</svg>
<figcaption>Bugs cluster at boundaries: &gt;= versus &gt;, 3.9 versus 4.0. Testing every value is impossible; testing every edge is cheap.</figcaption>
</figure>

**Equivalence partitioning** divides inputs into classes the software should treat the same way, and tests one value from each. **Boundary value analysis** adds values at and next to each boundary, because off-by-one errors (`>` instead of `>=`) cluster there. NetWarden's `test_severity_from_cvss_boundaries` tests nine values, covering every boundary of the CVSS rating scale from both sides. The version ranges in the knowledge base get the same treatment: `test_regresshion_range` checks `8.4p1` (not affected), `8.5p1` (first affected), `9.7p1` (last affected) and `9.8p1` (fixed).

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A decision table for NetWarden&#x27;s exit status. Conditions: an error occurred; findings meet the fail-on threshold. Rules: error, any findings, exit 2. No error and findings at or above the threshold, exit 1. No error and no such findings, exit 0. Each rule becomes at least one test." xmlns="http://www.w3.org/2000/svg">
<style>
.s11g{ font-family:var(--sans),sans-serif; }
.s11g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11g .s{ fill:var(--text-dim); font-size:13px; }
.s11g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11g .c{ fill:var(--text-faint); font-size:12.5px; }
.s11g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11g-a); }
.s11g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11g-a); marker-start:url(#s11g-s); }
.s11g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11g-g); }
.s11g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11g-a); }
.s11g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11g-tri); }
.s11g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11g-tri); }
.s11g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11g-open); }
.s11g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11g-open); }
.s11g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11g-dia); }
.s11g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11g-odia); }
.s11g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11g-dia); marker-end:url(#s11g-open); }
.s11g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11g-solid); }
.s11g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11g-open); }
.s11g .fill{ fill:var(--text); stroke:none; }
.s11g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11g .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s11g .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s11g .ks-purple{ fill:#534AB7; font-size:13px; }
.s11g .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s11g .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11g .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s11g .kb-purple, :root[data-theme="dark"] .s11g .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s11g .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s11g .kh-purple{ fill:#AFA9EC; }
.s11g .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s11g-purple); }
.s11g .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11g-purple); }
.s11g .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s11g .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s11g .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s11g .ks-green{ fill:#3B6D11; font-size:13px; }
.s11g .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s11g .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11g .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s11g .kb-green, :root[data-theme="dark"] .s11g .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s11g .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s11g .kh-green{ fill:#97C459; }
.s11g .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s11g-green); }
.s11g .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11g-green); }
.s11g .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s11g .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s11g .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s11g .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s11g .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s11g .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11g .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s11g .kb-gray, :root[data-theme="dark"] .s11g .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s11g .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s11g .kh-gray{ fill:#B4B2A9; }
.s11g .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s11g-gray); }
.s11g .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11g-gray); }
.s11g .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11g-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s11g-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s11g-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s11g">
<rect x="330" y="16" width="116" height="32" rx="4" class="k-gray"/>
<text x="388.0" y="36.5" text-anchor="middle" class="kb-gray">rule 1</text>
<rect x="454" y="16" width="116" height="32" rx="4" class="k-gray"/>
<text x="512.0" y="36.5" text-anchor="middle" class="kb-gray">rule 2</text>
<rect x="578" y="16" width="116" height="32" rx="4" class="k-gray"/>
<text x="636.0" y="36.5" text-anchor="middle" class="kb-gray">rule 3</text>
<rect x="20" y="58" width="300" height="36" rx="4" class="k-purple"/>
<text x="170.0" y="80.5" text-anchor="middle" class="ks-purple">error (scope, bad ports, file)?</text>
<rect x="330" y="58" width="116" height="36" rx="4" class="pnl"/>
<text x="388.0" y="80.5" text-anchor="middle" class="m">Y</text>
<rect x="454" y="58" width="116" height="36" rx="4" class="pnl"/>
<text x="512.0" y="80.5" text-anchor="middle" class="m">N</text>
<rect x="578" y="58" width="116" height="36" rx="4" class="pnl"/>
<text x="636.0" y="80.5" text-anchor="middle" class="m">N</text>
<rect x="20" y="102" width="300" height="36" rx="4" class="k-purple"/>
<text x="170.0" y="124.5" text-anchor="middle" class="ks-purple">findings &gt;= --fail-on?</text>
<rect x="330" y="102" width="116" height="36" rx="4" class="pnl"/>
<text x="388.0" y="124.5" text-anchor="middle" class="m">any</text>
<rect x="454" y="102" width="116" height="36" rx="4" class="pnl"/>
<text x="512.0" y="124.5" text-anchor="middle" class="m">Y</text>
<rect x="578" y="102" width="116" height="36" rx="4" class="pnl"/>
<text x="636.0" y="124.5" text-anchor="middle" class="m">N</text>
<rect x="20" y="146" width="300" height="36" rx="4" class="k-green"/>
<text x="170.0" y="168.5" text-anchor="middle" class="ks-green">exit status</text>
<rect x="330" y="146" width="116" height="36" rx="4" class="pnl"/>
<text x="388.0" y="168.5" text-anchor="middle" class="m">2</text>
<rect x="454" y="146" width="116" height="36" rx="4" class="pnl"/>
<text x="512.0" y="168.5" text-anchor="middle" class="m">1</text>
<rect x="578" y="146" width="116" height="36" rx="4" class="pnl"/>
<text x="636.0" y="168.5" text-anchor="middle" class="m">0</text>
<text x="360" y="210" text-anchor="middle" class="c">tested in test_cli_scan_exit_codes and test_cli_report_file_and_diff</text>
</g>
</svg>
<figcaption>Decision tables make sure every combination of conditions has been thought about, and tested.</figcaption>
</figure>

**Decision tables** list combinations of conditions and the expected action for each. They are ideal for business rules and command-line behaviour like exit codes. Other black-box techniques include **state transition testing**, deriving tests from a state machine such as the finding lifecycle in Chapter 4, and **use case testing**, one test per scenario and extension.

### White-box techniques

**White-box** (structure-based) techniques use the code itself.

<figure class="diagram">
<svg viewBox="0 0 720 360" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Control flow graph of Severity.from_cvss. Four decisions, score at least 9, at least 7, at least 4, greater than 0, each with a true branch returning CRITICAL, HIGH, MEDIUM or LOW, and a final return of INFO. Cyclomatic complexity is decisions plus one, which is five, so at least five tests are needed to cover every branch; the parametrized test has nine." xmlns="http://www.w3.org/2000/svg">
<style>
.s11h{ font-family:var(--sans),sans-serif; }
.s11h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11h .s{ fill:var(--text-dim); font-size:13px; }
.s11h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .c{ fill:var(--text-faint); font-size:12.5px; }
.s11h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11h-a); }
.s11h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11h-a); marker-start:url(#s11h-s); }
.s11h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11h-g); }
.s11h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-a); }
.s11h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11h-tri); }
.s11h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-tri); }
.s11h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11h-open); }
.s11h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-open); }
.s11h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11h-dia); }
.s11h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11h-odia); }
.s11h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11h-dia); marker-end:url(#s11h-open); }
.s11h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11h-solid); }
.s11h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11h-open); }
.s11h .fill{ fill:var(--text); stroke:none; }
.s11h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s11h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s11h .ks-blue{ fill:#185FA5; font-size:13px; }
.s11h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s11h .kb-blue, :root[data-theme="dark"] .s11h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s11h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s11h .kh-blue{ fill:#85B7EB; }
.s11h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s11h-blue); }
.s11h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-blue); }
.s11h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s11h .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11h .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11h .ks-amber{ fill:#854F0B; font-size:13px; }
.s11h .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11h .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11h .kb-amber, :root[data-theme="dark"] .s11h .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11h .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11h .kh-amber{ fill:#EF9F27; }
.s11h .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11h-amber); }
.s11h .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-amber); }
.s11h .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11h .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s11h .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s11h .ks-coral{ fill:#993C1D; font-size:13px; }
.s11h .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11h .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s11h .kb-coral, :root[data-theme="dark"] .s11h .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s11h .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s11h .kh-coral{ fill:#F0997B; }
.s11h .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s11h-coral); }
.s11h .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-coral); }
.s11h .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s11h .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s11h .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s11h .ks-purple{ fill:#534AB7; font-size:13px; }
.s11h .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11h .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s11h .kb-purple, :root[data-theme="dark"] .s11h .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s11h .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s11h .kh-purple{ fill:#AFA9EC; }
.s11h .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s11h-purple); }
.s11h .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-purple); }
.s11h .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s11h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11h .ks-red{ fill:#A32D2D; font-size:13px; }
.s11h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11h .kb-red, :root[data-theme="dark"] .s11h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11h .kh-red{ fill:#F09595; }
.s11h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11h-red); }
.s11h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-red); }
.s11h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s11h .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s11h .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s11h .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s11h .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s11h .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11h .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s11h .kb-gray, :root[data-theme="dark"] .s11h .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s11h .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s11h .kh-gray{ fill:#B4B2A9; }
.s11h .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s11h-gray); }
.s11h .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11h-gray); }
.s11h .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s11h-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11h-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s11h-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s11h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s11h-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s11h">
<circle cx="160" cy="20" r="9" class="fill"/>
<line x1="160" y1="29" x2="160" y2="44" class="msg"/>
<path d="M160 46 L184 70 L160 94 L136 70 z" class="k-purple"/>
<text x="128" y="74" text-anchor="end" class="m">&gt;= 9.0?</text>
<line x1="184" y1="70" x2="330" y2="70" class="msg"/>
<text x="258" y="64" text-anchor="middle" class="c">true</text>
<rect x="340" y="52" width="130" height="36" rx="4" class="k-red"/>
<text x="405.0" y="74.5" text-anchor="middle" class="ks-red">return CRITICAL</text>
<line x1="160" y1="94" x2="160" y2="110" class="msg"/>
<text x="168" y="108" text-anchor="start" class="c">false</text>
<path d="M160 112 L184 136 L160 160 L136 136 z" class="k-purple"/>
<text x="128" y="140" text-anchor="end" class="m">&gt;= 7.0?</text>
<line x1="184" y1="136" x2="330" y2="136" class="msg"/>
<text x="258" y="130" text-anchor="middle" class="c">true</text>
<rect x="340" y="118" width="130" height="36" rx="4" class="k-coral"/>
<text x="405.0" y="140.5" text-anchor="middle" class="ks-coral">return HIGH</text>
<line x1="160" y1="160" x2="160" y2="176" class="msg"/>
<text x="168" y="174" text-anchor="start" class="c">false</text>
<path d="M160 178 L184 202 L160 226 L136 202 z" class="k-purple"/>
<text x="128" y="206" text-anchor="end" class="m">&gt;= 4.0?</text>
<line x1="184" y1="202" x2="330" y2="202" class="msg"/>
<text x="258" y="196" text-anchor="middle" class="c">true</text>
<rect x="340" y="184" width="130" height="36" rx="4" class="k-amber"/>
<text x="405.0" y="206.5" text-anchor="middle" class="ks-amber">return MEDIUM</text>
<line x1="160" y1="226" x2="160" y2="242" class="msg"/>
<text x="168" y="240" text-anchor="start" class="c">false</text>
<path d="M160 244 L184 268 L160 292 L136 268 z" class="k-purple"/>
<text x="128" y="272" text-anchor="end" class="m">&gt; 0.0?</text>
<line x1="184" y1="268" x2="330" y2="268" class="msg"/>
<text x="258" y="262" text-anchor="middle" class="c">true</text>
<rect x="340" y="250" width="130" height="36" rx="4" class="k-blue"/>
<text x="405.0" y="272.5" text-anchor="middle" class="ks-blue">return LOW</text>
<line x1="160" y1="292" x2="160" y2="308" class="msg"/>
<text x="168" y="306" text-anchor="start" class="c">false</text>
<rect x="95" y="312" width="130" height="36" rx="4" class="k-gray"/>
<text x="160.0" y="334.5" text-anchor="middle" class="ks-gray">return INFO</text>
<rect x="520" y="120" width="180" height="120" rx="7" class="k-purple"/>
<text x="610.0" y="151.5" text-anchor="middle" class="kb-purple">cyclomatic</text>
<text x="610.0" y="173.5" text-anchor="middle" class="kb-purple">complexity</text>
<text x="610.0" y="195.5" text-anchor="middle" class="ks-purple">= decisions + 1</text>
<text x="610.0" y="217.5" text-anchor="middle" class="km-purple">= 4 + 1 = 5</text>
</g>
</svg>
<figcaption>White-box testing uses the code's structure: here, five independent paths, so at least five tests for full branch coverage.</figcaption>
</figure>

**Statement coverage** asks whether every line ran; **branch coverage** whether every decision went both ways. **Cyclomatic complexity** (McCabe) gives the number of independent paths, and so a lower bound on the tests needed for branch coverage.

### Experience-based techniques

**Error guessing** uses experience of what tends to go wrong: empty inputs, `None`, huge inputs, unusual characters, time zones, concurrency. NetWarden's `test_scope_rejects_bad_targets` tries `"not-an-ip"`, `"300.1.1.1"` and an empty string. **Exploratory testing** is simultaneous learning, test design and execution by a skilled tester, and finds problems scripted tests miss; it is how the team discovered that a silent service on a non-standard port was never identified as HTTP, which led to probing every silent port with an HTTP request.

## Test doubles

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Test doubles stand in for real collaborators. Dummy: passed but never used. Stub: returns canned answers, like NetWarden&#x27;s FakeScanner returning fixed hosts. Spy: records how it was called, like the Mock subscribed to the event bus. Mock: pre-programmed with expectations and verifies them. Fake: a working but simplified implementation, like the demo services or an in-memory SQLite database." xmlns="http://www.w3.org/2000/svg">
<style>
.s11d{ font-family:var(--sans),sans-serif; }
.s11d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11d .s{ fill:var(--text-dim); font-size:13px; }
.s11d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .c{ fill:var(--text-faint); font-size:12.5px; }
.s11d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11d-a); }
.s11d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11d-a); marker-start:url(#s11d-s); }
.s11d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11d-g); }
.s11d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-a); }
.s11d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11d-tri); }
.s11d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-tri); }
.s11d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11d-open); }
.s11d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-open); }
.s11d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11d-dia); }
.s11d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11d-odia); }
.s11d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11d-dia); marker-end:url(#s11d-open); }
.s11d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11d-solid); }
.s11d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11d-open); }
.s11d .fill{ fill:var(--text); stroke:none; }
.s11d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s11d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s11d .ks-blue{ fill:#185FA5; font-size:13px; }
.s11d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s11d .kb-blue, :root[data-theme="dark"] .s11d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s11d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s11d .kh-blue{ fill:#85B7EB; }
.s11d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s11d-blue); }
.s11d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-blue); }
.s11d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s11d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11d .ks-amber{ fill:#854F0B; font-size:13px; }
.s11d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11d .kb-amber, :root[data-theme="dark"] .s11d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11d .kh-amber{ fill:#EF9F27; }
.s11d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11d-amber); }
.s11d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-amber); }
.s11d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s11d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s11d .ks-purple{ fill:#534AB7; font-size:13px; }
.s11d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s11d .kb-purple, :root[data-theme="dark"] .s11d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s11d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s11d .kh-purple{ fill:#AFA9EC; }
.s11d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s11d-purple); }
.s11d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-purple); }
.s11d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s11d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s11d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s11d .ks-green{ fill:#3B6D11; font-size:13px; }
.s11d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s11d .kb-green, :root[data-theme="dark"] .s11d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s11d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s11d .kh-green{ fill:#97C459; }
.s11d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s11d-green); }
.s11d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-green); }
.s11d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s11d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s11d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s11d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s11d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s11d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s11d .kb-gray, :root[data-theme="dark"] .s11d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s11d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s11d .kh-gray{ fill:#B4B2A9; }
.s11d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s11d-gray); }
.s11d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11d-gray); }
.s11d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s11d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s11d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s11d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s11d">
<rect x="20" y="14" width="110" height="44" rx="7" class="k-gray"/>
<text x="75.0" y="40.5" text-anchor="middle" class="kb-gray">dummy</text>
<text x="146" y="41" text-anchor="start" class="s">fills a parameter, never used</text>
<rect x="400" y="18" width="300" height="36" rx="4" class="pnl"/>
<text x="550.0" y="40.5" text-anchor="middle" class="m">None for an unused bus</text>
<rect x="20" y="70" width="110" height="44" rx="7" class="k-blue"/>
<text x="75.0" y="96.5" text-anchor="middle" class="kb-blue">stub</text>
<text x="146" y="97" text-anchor="start" class="s">returns canned answers</text>
<rect x="400" y="74" width="300" height="36" rx="4" class="pnl"/>
<text x="550.0" y="96.5" text-anchor="middle" class="m">FakeScanner.scan() -&gt; fixed hosts</text>
<rect x="20" y="126" width="110" height="44" rx="7" class="k-purple"/>
<text x="75.0" y="152.5" text-anchor="middle" class="kb-purple">spy</text>
<text x="146" y="153" text-anchor="start" class="s">records calls for later checks</text>
<rect x="400" y="130" width="300" height="36" rx="4" class="pnl"/>
<text x="550.0" y="152.5" text-anchor="middle" class="m">Mock() subscribed to EventBus</text>
<rect x="20" y="182" width="110" height="44" rx="7" class="k-amber"/>
<text x="75.0" y="208.5" text-anchor="middle" class="kb-amber">mock</text>
<text x="146" y="209" text-anchor="start" class="s">expects calls, fails otherwise</text>
<rect x="400" y="186" width="300" height="36" rx="4" class="pnl"/>
<text x="550.0" y="208.5" text-anchor="middle" class="m">mock.assert_called_once_with(...)</text>
<rect x="20" y="238" width="110" height="44" rx="7" class="k-green"/>
<text x="75.0" y="264.5" text-anchor="middle" class="kb-green">fake</text>
<text x="146" y="265" text-anchor="start" class="s">simplified working version</text>
<rect x="400" y="242" width="300" height="36" rx="4" class="pnl"/>
<text x="550.0" y="264.5" text-anchor="middle" class="m">demo services; SQLite in tmp_path</text>
</g>
</svg>
<figcaption>Doubles make tests fast and deterministic. Too many mocks, though, test the implementation instead of the behaviour.</figcaption>
</figure>

When the unit under test depends on something slow, non-deterministic or external, such as a network, a clock, a database or another team's service, tests replace it with a **test double** (Gerard Meszaros's term). NetWarden's engine tests use two:

```python
def test_out_of_scope_target_never_reaches_the_scanner():
    assessment, scanner = make_assessment([])          # FakeScanner: a stub that also records calls
    with pytest.raises(ScopeError):
        assessment.run(["192.168.1.1"], [22])
    assert scanner.calls == []                          # NW-SR-1: no traffic was attempted


def test_events_are_published_to_observers():
    bus = EventBus()
    spy = Mock()
    bus.subscribe(FindingRaised, spy)
    bus.subscribe(ScanFinished, spy)
    assessment, _ = make_assessment([Host("10.0.0.5", [Service(23, "\xff\xfd")])], bus)
    assessment.run(["10.0.0.5"], [23])
    kinds = [type(c.args[0]).__name__ for c in spy.call_args_list]
    assert kinds == ["FindingRaised", "ScanFinished"]
```

The first test is the executable form of the most important requirement in the system. Doubles are only possible because `Assessment` receives its collaborators through its constructor (dependency injection, Chapter 6): **testable design and good design are mostly the same thing**.

Use doubles with restraint. A test that mocks everything checks that the code calls what it calls, and breaks whenever the implementation changes, even when the behaviour does not. Prefer real objects when they are fast and deterministic, fakes for infrastructure, and mocks mainly for verifying interactions that are themselves the requirement, as in the two tests above.

## Test-driven development

<figure class="diagram">
<svg viewBox="0 0 720 275" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Test-driven development: write a failing test (red), write just enough code to pass it (green), then refactor while staying green, and repeat in cycles of a few minutes. Example: a test that Scope rejects more than 1024 hosts fails, a check is added, then the constant MAX_HOSTS is extracted." xmlns="http://www.w3.org/2000/svg">
<style>
.s11e{ font-family:var(--sans),sans-serif; }
.s11e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11e .s{ fill:var(--text-dim); font-size:13px; }
.s11e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11e .c{ fill:var(--text-faint); font-size:12.5px; }
.s11e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11e-a); }
.s11e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11e-a); marker-start:url(#s11e-s); }
.s11e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11e-g); }
.s11e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11e-a); }
.s11e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11e-tri); }
.s11e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11e-tri); }
.s11e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11e-open); }
.s11e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11e-open); }
.s11e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11e-dia); }
.s11e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11e-odia); }
.s11e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11e-dia); marker-end:url(#s11e-open); }
.s11e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11e-solid); }
.s11e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11e-open); }
.s11e .fill{ fill:var(--text); stroke:none; }
.s11e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s11e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s11e .ks-blue{ fill:#185FA5; font-size:13px; }
.s11e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s11e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s11e .kb-blue, :root[data-theme="dark"] .s11e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s11e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s11e .kh-blue{ fill:#85B7EB; }
.s11e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s11e-blue); }
.s11e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11e-blue); }
.s11e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s11e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s11e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s11e .ks-green{ fill:#3B6D11; font-size:13px; }
.s11e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s11e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s11e .kb-green, :root[data-theme="dark"] .s11e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s11e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s11e .kh-green{ fill:#97C459; }
.s11e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s11e-green); }
.s11e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11e-green); }
.s11e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s11e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11e .ks-red{ fill:#A32D2D; font-size:13px; }
.s11e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11e .kb-red, :root[data-theme="dark"] .s11e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11e .kh-red{ fill:#F09595; }
.s11e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11e-red); }
.s11e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11e-red); }
.s11e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s11e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s11e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s11e">
<rect x="235" y="12" width="250" height="72" rx="7" class="k-red"/>
<text x="360.0" y="32.5" text-anchor="middle" class="kb-red">red</text>
<text x="360.0" y="52.5" text-anchor="middle" class="ks-red">write a failing test</text>
<text x="360.0" y="72.5" text-anchor="middle" class="km-red">test_scope_refuses_huge_requests</text>
<rect x="426" y="150" width="250" height="72" rx="7" class="k-green"/>
<text x="551.0" y="170.5" text-anchor="middle" class="kb-green">green</text>
<text x="551.0" y="190.5" text-anchor="middle" class="ks-green">make it pass, simply</text>
<text x="551.0" y="210.5" text-anchor="middle" class="km-green">if len(addresses) &gt; 1024: raise</text>
<rect x="44" y="150" width="250" height="72" rx="7" class="k-blue"/>
<text x="169.0" y="170.5" text-anchor="middle" class="kb-blue">refactor</text>
<text x="169.0" y="190.5" text-anchor="middle" class="ks-blue">clean up, stay green</text>
<text x="169.0" y="210.5" text-anchor="middle" class="km-blue">1024 -&gt; MAX_HOSTS</text>
<path d="M492 60 C 600 60, 660 110, 655 172" class="ar"/>
<path d="M430 252 L290 252" class="ar"/>
<path d="M80 172 C 80 110, 140 62, 233 60" class="ar"/>
</g>
</svg>
<figcaption>TDD is a design technique as much as a testing one: writing the test first forces you to decide the interface first.</figcaption>
</figure>

**Test-driven development** (TDD), from Extreme Programming, writes the test **before** the code, in short cycles:

1. **Red**: write a small test for behaviour that does not exist yet; watch it fail.
2. **Green**: write the simplest code that passes.
3. **Refactor**: improve the code and the test, keeping everything green.

TDD gives a fast feedback loop, a test suite as a by-product, and designs that are testable by construction, because the interface is used before it is written. Research results on its effect on quality and productivity are mixed, and it suits some code (logic, parsers, rules) better than other code (user interfaces, exploratory prototypes). Many developers use it selectively. **Behaviour-driven development** (BDD) extends the idea to acceptance tests written in the Given, When, Then language of Chapter 3.

## Coverage

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden&#x27;s statement coverage per module from pytest --cov: checks, engine, events, models and scope 100 percent; knowledge 97, store 97, fingerprint 93, report 93, scanner 91, cli 84 and demo 78 percent; 95 percent overall. The CI pipeline fails below 90 percent." xmlns="http://www.w3.org/2000/svg">
<style>
.s11i{ font-family:var(--sans),sans-serif; }
.s11i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s11i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s11i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s11i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s11i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s11i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s11i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s11i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s11i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s11i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s11i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s11i .s{ fill:var(--text-dim); font-size:13px; }
.s11i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s11i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s11i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s11i .c{ fill:var(--text-faint); font-size:12.5px; }
.s11i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s11i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s11i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s11i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11i-a); }
.s11i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s11i-a); marker-start:url(#s11i-s); }
.s11i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s11i-g); }
.s11i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s11i-a); }
.s11i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s11i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s11i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s11i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s11i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s11i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11i-tri); }
.s11i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11i-tri); }
.s11i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11i-open); }
.s11i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s11i-open); }
.s11i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11i-dia); }
.s11i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11i-odia); }
.s11i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s11i-dia); marker-end:url(#s11i-open); }
.s11i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s11i-solid); }
.s11i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s11i-open); }
.s11i .fill{ fill:var(--text); stroke:none; }
.s11i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s11i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s11i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s11i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s11i .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s11i .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s11i .ks-amber{ fill:#854F0B; font-size:13px; }
.s11i .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s11i .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11i .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s11i .kb-amber, :root[data-theme="dark"] .s11i .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s11i .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s11i .kh-amber{ fill:#EF9F27; }
.s11i .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s11i-amber); }
.s11i .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11i-amber); }
.s11i .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s11i .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s11i .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s11i .ks-green{ fill:#3B6D11; font-size:13px; }
.s11i .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s11i .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11i .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s11i .kb-green, :root[data-theme="dark"] .s11i .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s11i .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s11i .kh-green{ fill:#97C459; }
.s11i .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s11i-green); }
.s11i .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11i-green); }
.s11i .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s11i .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s11i .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s11i .ks-red{ fill:#A32D2D; font-size:13px; }
.s11i .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s11i .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s11i .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s11i .kb-red, :root[data-theme="dark"] .s11i .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s11i .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s11i .kh-red{ fill:#F09595; }
.s11i .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s11i-red); }
.s11i .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s11i-red); }
.s11i .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s11i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s11i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s11i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s11i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s11i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s11i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s11i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s11i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s11i-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s11i-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s11i-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s11i">
<text x="120" y="28" text-anchor="end" class="m">checks</text>
<rect x="130" y="16" width="500" height="16" rx="2" class="k-green"/>
<text x="700" y="28" text-anchor="end" class="c">100%</text>
<text x="120" y="50" text-anchor="end" class="m">engine</text>
<rect x="130" y="38" width="500" height="16" rx="2" class="k-green"/>
<text x="700" y="50" text-anchor="end" class="c">100%</text>
<text x="120" y="72" text-anchor="end" class="m">events</text>
<rect x="130" y="60" width="500" height="16" rx="2" class="k-green"/>
<text x="700" y="72" text-anchor="end" class="c">100%</text>
<text x="120" y="94" text-anchor="end" class="m">models</text>
<rect x="130" y="82" width="500" height="16" rx="2" class="k-green"/>
<text x="700" y="94" text-anchor="end" class="c">100%</text>
<text x="120" y="116" text-anchor="end" class="m">scope</text>
<rect x="130" y="104" width="500" height="16" rx="2" class="k-green"/>
<text x="700" y="116" text-anchor="end" class="c">100%</text>
<text x="120" y="138" text-anchor="end" class="m">knowledge</text>
<rect x="130" y="126" width="485" height="16" rx="2" class="k-green"/>
<text x="700" y="138" text-anchor="end" class="c">97%</text>
<text x="120" y="160" text-anchor="end" class="m">store</text>
<rect x="130" y="148" width="485" height="16" rx="2" class="k-green"/>
<text x="700" y="160" text-anchor="end" class="c">97%</text>
<text x="120" y="182" text-anchor="end" class="m">fingerprint</text>
<rect x="130" y="170" width="465" height="16" rx="2" class="k-amber"/>
<text x="700" y="182" text-anchor="end" class="c">93%</text>
<text x="120" y="204" text-anchor="end" class="m">report</text>
<rect x="130" y="192" width="465" height="16" rx="2" class="k-amber"/>
<text x="700" y="204" text-anchor="end" class="c">93%</text>
<text x="120" y="226" text-anchor="end" class="m">scanner</text>
<rect x="130" y="214" width="455" height="16" rx="2" class="k-amber"/>
<text x="700" y="226" text-anchor="end" class="c">91%</text>
<text x="120" y="248" text-anchor="end" class="m">cli</text>
<rect x="130" y="236" width="420" height="16" rx="2" class="k-red"/>
<text x="700" y="248" text-anchor="end" class="c">84%</text>
<text x="120" y="270" text-anchor="end" class="m">demo</text>
<rect x="130" y="258" width="390" height="16" rx="2" class="k-red"/>
<text x="700" y="270" text-anchor="end" class="c">78%</text>
<line x1="580" y1="10" x2="580" y2="282" class="ad-red"/>
<text x="586" y="290" text-anchor="start" class="kh-red">CI threshold 90%</text>
</g>
</svg>
<figcaption>Coverage shows what the tests did not run. It cannot show whether the tests that did run check the right things.</figcaption>
</figure>

```bash
pytest --cov --cov-report=term-missing
```

prints, for each module, the percentage of statements executed and the line numbers that were not. NetWarden's CI fails if total coverage drops below 90% (`--cov-fail-under=90`).

Treat coverage as a **flashlight, not a target**. Low coverage reliably shows untested code; high coverage does not show good tests, because a test can execute a line without checking its result. **Mutation testing** goes further: a tool such as `mutmut` makes small changes to the code (`>=` to `>`) and checks that some test fails; a surviving mutant reveals a weak test.

## Other kinds of testing

| Type | Question | Tools and examples |
|---|---|---|
| **Performance and load** | Fast enough under expected load? | Time a /24 scan against NW-NFR-1; Locust, k6 for services |
| **Security** | Can it be misused? | Chapter 12: out-of-scope tests, HTML escaping tests, fuzzing |
| **Usability** | Can real users succeed? | Five users try the README demo (NW-NFR-5) |
| **Compatibility** | Works on all supported platforms? | CI matrix: Python 3.11, 3.12, 3.13 |
| **Regression** | Did a change break something? | The whole automated suite, on every commit |
| **Property-based** | Does a property hold for all generated inputs? | Hypothesis: `version_key` ordering for random versions |
| **Fuzzing** | Does malformed input crash it? | Random banners into `Fingerprinter` |

## Test management

Larger projects plan testing explicitly. A **test plan** (NetWarden's is `docs/test-plan.md`) records scope, levels, techniques, environments, entry and exit criteria, and responsibilities. The international standard **ISO/IEC/IEEE 29119** describes test processes and documentation; the **ISTQB** certification scheme uses the same vocabulary as this chapter.

## Hands on

```bash
pytest -v                               # every test and its result
pytest -k scope -v                      # only tests with "scope" in the name
pytest --durations=5                    # the five slowest tests
pytest --cov --cov-report=term-missing  # coverage with missing lines
```

Then:

1. Write a boundary-value test for `parse_ports` covering `1`, `65535`, `0` and `65536`.
2. Introduce a bug on purpose, changing `>=` to `>` in `Severity.from_cvss`, and see which tests catch it. Restore it.
3. Use TDD to add support for an `nginx` banner without a version (`Server: nginx`): test first, then code.

## Summary

- An **error** causes a **fault**, which may cause a **failure**; testing finds failures, it cannot prove their absence.
- Test at several **levels**, shaped like a **pyramid**: many fast unit tests, few slow end-to-end tests.
- Good tests are **FIRST** and follow **arrange, act, assert**; pytest **fixtures** and **parametrize** keep them short.
- Design tests with **equivalence partitions, boundary values, decision tables**, state transitions, **coverage criteria** and error guessing.
- **Test doubles** (dummy, stub, spy, mock, fake) isolate units; injected dependencies make them possible.
- **TDD**: red, green, refactor. **Coverage** shows what is untested, not what is well tested.
