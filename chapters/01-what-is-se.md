# Chapter 1: What Is Software Engineering?

The term **software engineering** was chosen deliberately provocatively for a 1968 NATO conference in Garmisch, Germany, at a time when large software projects were routinely late, over budget, unreliable, and sometimes abandoned. Participants spoke of a "software crisis". The proposal was that building software should borrow the discipline of established engineering fields: systematic methods, measurement, and professional responsibility. More than half a century later, software runs banks, hospitals, aircraft and power grids, and the crisis has not so much ended as moved: systems are larger, change faster, and are attacked constantly.

This chapter defines the field, explains why it differs from programming, and introduces the project that runs through the whole book.

## A definition

The IEEE defines software engineering as *the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software*. Three words carry the weight:

- **Systematic**: there is a method, not just talent and heroics.
- **Disciplined**: the method is followed even when deadlines press.
- **Quantifiable**: progress and quality are measured, so decisions rest on evidence.

Notice also that the definition covers **operation and maintenance**, not just development. Most of the cost of successful software is spent after its first release.

## Programming versus software engineering

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Programming compared with software engineering. Programming: one person, a few weeks, the author is the user, and the code is thrown away. Software engineering: teams, years, many users and stakeholders, and code that must be changed safely by people who did not write it." xmlns="http://www.w3.org/2000/svg">
<style>
.s1a{ font-family:var(--sans),sans-serif; }
.s1a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s1a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s1a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s1a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s1a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s1a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s1a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s1a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s1a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s1a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s1a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s1a .s{ fill:var(--text-dim); font-size:13px; }
.s1a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s1a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s1a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s1a .c{ fill:var(--text-faint); font-size:12.5px; }
.s1a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s1a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s1a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s1a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1a-a); }
.s1a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1a-a); marker-start:url(#s1a-s); }
.s1a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s1a-g); }
.s1a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s1a-a); }
.s1a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s1a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s1a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s1a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s1a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s1a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1a-tri); }
.s1a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1a-tri); }
.s1a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1a-open); }
.s1a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1a-open); }
.s1a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1a-dia); }
.s1a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1a-odia); }
.s1a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1a-dia); marker-end:url(#s1a-open); }
.s1a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1a-solid); }
.s1a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s1a-open); }
.s1a .fill{ fill:var(--text); stroke:none; }
.s1a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s1a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s1a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s1a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s1a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s1a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s1a .ks-blue{ fill:#185FA5; font-size:13px; }
.s1a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s1a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s1a .kb-blue, :root[data-theme="dark"] .s1a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s1a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s1a .kh-blue{ fill:#85B7EB; }
.s1a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s1a-blue); }
.s1a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1a-blue); }
.s1a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s1a .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s1a .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s1a .ks-coral{ fill:#993C1D; font-size:13px; }
.s1a .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s1a .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1a .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s1a .kb-coral, :root[data-theme="dark"] .s1a .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s1a .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s1a .kh-coral{ fill:#F0997B; }
.s1a .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s1a-coral); }
.s1a .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1a-coral); }
.s1a .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s1a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s1a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s1a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s1a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s1a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s1a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s1a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s1a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s1a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s1a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s1a">
<rect x="20" y="16" width="330" height="44" rx="7" class="k-blue"/>
<text x="185.0" y="42.5" text-anchor="middle" class="kb-blue">programming</text>
<rect x="370" y="16" width="330" height="44" rx="7" class="k-coral"/>
<text x="535.0" y="42.5" text-anchor="middle" class="kb-coral">software engineering</text>
<text x="360" y="97" text-anchor="middle" class="c">people</text>
<rect x="20" y="74" width="300" height="34" rx="5" class="pnl"/>
<text x="170.0" y="95.5" text-anchor="middle" class="s">one</text>
<rect x="400" y="74" width="300" height="34" rx="5" class="pnl"/>
<text x="550.0" y="95.5" text-anchor="middle" class="s">teams, often changing</text>
<text x="360" y="139" text-anchor="middle" class="c">time</text>
<rect x="20" y="116" width="300" height="34" rx="5" class="pnl"/>
<text x="170.0" y="137.5" text-anchor="middle" class="s">days to weeks</text>
<rect x="400" y="116" width="300" height="34" rx="5" class="pnl"/>
<text x="550.0" y="137.5" text-anchor="middle" class="s">years to decades</text>
<text x="360" y="181" text-anchor="middle" class="c">users</text>
<rect x="20" y="158" width="300" height="34" rx="5" class="pnl"/>
<text x="170.0" y="179.5" text-anchor="middle" class="s">the author</text>
<rect x="400" y="158" width="300" height="34" rx="5" class="pnl"/>
<text x="550.0" y="179.5" text-anchor="middle" class="s">many, with conflicting needs</text>
<text x="360" y="223" text-anchor="middle" class="c">change</text>
<rect x="20" y="200" width="300" height="34" rx="5" class="pnl"/>
<text x="170.0" y="221.5" text-anchor="middle" class="s">rewrite it</text>
<rect x="400" y="200" width="300" height="34" rx="5" class="pnl"/>
<text x="550.0" y="221.5" text-anchor="middle" class="s">change it safely, often</text>
<text x="360" y="265" text-anchor="middle" class="c">success</text>
<rect x="20" y="242" width="300" height="34" rx="5" class="pnl"/>
<text x="170.0" y="263.5" text-anchor="middle" class="s">it runs</text>
<rect x="400" y="242" width="300" height="34" rx="5" class="pnl"/>
<text x="550.0" y="263.5" text-anchor="middle" class="s">it is useful, reliable, maintainable</text>
</g>
</svg>
<figcaption>Software engineering is programming integrated over time, people and change.</figcaption>
</figure>

A useful way to see the difference, popularised by engineers at Google, is that software engineering is **programming integrated over time**. A script you write for an assignment has one author, one user, and a life of a few weeks. A product has many authors, many users with conflicting needs, and a life of years, during which the people who wrote it leave and new people must change it safely. Almost every practice in this book exists to cope with **time, people, and change**:

- Requirements and models help many people agree on what to build.
- Design principles and patterns keep code changeable.
- Version control, reviews and tests let a team change code without breaking it.
- Continuous integration and delivery make releasing routine instead of risky.
- Project management keeps the effort pointed at the goal and within its budget.

## Why it is hard

Fred Brooks, who managed the IBM System/360 operating system project, argued in his essay *No Silver Bullet* (1986) that software has **essential** difficulties that no tool will remove:

| Difficulty | Meaning | NetWarden example |
|---|---|---|
| **Complexity** | Software has more distinct states and parts than almost any other human construction | Every combination of host, port, banner and version is a different case |
| **Conformity** | It must fit arbitrary external interfaces and rules | Banners from dozens of products, each in its own format |
| **Changeability** | Because it is easy to change, it is always asked to change | New vulnerabilities are published every day |
| **Invisibility** | It has no natural geometric shape to draw | Hence the many diagrams in Chapter 4 |

Brooks also gave us **Brooks's law**: adding people to a late software project makes it later, because new people need training and every extra person adds communication paths. Chapter 16 returns to this.

## The cost of finding problems late

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The relative cost of fixing a defect rises the later it is found: cheapest during requirements, more during design and coding, much more during testing, and most after release. The bars are illustrative of the trend reported in many studies, not exact figures." xmlns="http://www.w3.org/2000/svg">
<style>
.s1b{ font-family:var(--sans),sans-serif; }
.s1b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s1b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s1b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s1b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s1b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s1b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s1b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s1b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s1b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s1b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s1b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s1b .s{ fill:var(--text-dim); font-size:13px; }
.s1b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s1b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .c{ fill:var(--text-faint); font-size:12.5px; }
.s1b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s1b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s1b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s1b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1b-a); }
.s1b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1b-a); marker-start:url(#s1b-s); }
.s1b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s1b-g); }
.s1b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-a); }
.s1b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s1b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s1b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s1b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s1b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s1b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1b-tri); }
.s1b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-tri); }
.s1b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1b-open); }
.s1b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-open); }
.s1b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1b-dia); }
.s1b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1b-odia); }
.s1b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1b-dia); marker-end:url(#s1b-open); }
.s1b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1b-solid); }
.s1b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s1b-open); }
.s1b .fill{ fill:var(--text); stroke:none; }
.s1b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s1b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s1b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s1b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s1b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s1b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s1b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s1b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s1b .kb-teal, :root[data-theme="dark"] .s1b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s1b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s1b .kh-teal{ fill:#5DCAA5; }
.s1b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s1b-teal); }
.s1b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-teal); }
.s1b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s1b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s1b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s1b .ks-amber{ fill:#854F0B; font-size:13px; }
.s1b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s1b .kb-amber, :root[data-theme="dark"] .s1b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s1b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s1b .kh-amber{ fill:#EF9F27; }
.s1b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s1b-amber); }
.s1b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-amber); }
.s1b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s1b .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s1b .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s1b .ks-coral{ fill:#993C1D; font-size:13px; }
.s1b .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1b .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s1b .kb-coral, :root[data-theme="dark"] .s1b .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s1b .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s1b .kh-coral{ fill:#F0997B; }
.s1b .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s1b-coral); }
.s1b .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-coral); }
.s1b .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s1b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s1b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s1b .ks-green{ fill:#3B6D11; font-size:13px; }
.s1b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s1b .kb-green, :root[data-theme="dark"] .s1b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s1b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s1b .kh-green{ fill:#97C459; }
.s1b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s1b-green); }
.s1b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-green); }
.s1b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s1b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s1b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s1b .ks-red{ fill:#A32D2D; font-size:13px; }
.s1b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s1b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s1b .kb-red, :root[data-theme="dark"] .s1b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s1b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s1b .kh-red{ fill:#F09595; }
.s1b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s1b-red); }
.s1b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1b-red); }
.s1b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s1b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s1b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s1b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s1b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s1b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s1b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s1b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s1b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s1b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s1b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s1b-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s1b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s1b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s1b">
<rect x="60" y="245.8" width="90" height="4.2" rx="3" class="k-green"/>
<text x="105" y="270" text-anchor="middle" class="s">requirements</text>
<rect x="190" y="237.4" width="90" height="12.600000000000001" rx="3" class="k-teal"/>
<text x="235" y="270" text-anchor="middle" class="s">design</text>
<rect x="320" y="220.6" width="90" height="29.400000000000002" rx="3" class="k-amber"/>
<text x="365" y="270" text-anchor="middle" class="s">coding</text>
<rect x="450" y="174.39999999999998" width="90" height="75.60000000000001" rx="3" class="k-coral"/>
<text x="495" y="270" text-anchor="middle" class="s">testing</text>
<rect x="580" y="40.0" width="90" height="210.0" rx="3" class="k-red"/>
<text x="625" y="270" text-anchor="middle" class="s">after release</text>
<line x1="40" y1="250" x2="700" y2="250" class="ln"/>
<line x1="40" y1="30" x2="40" y2="250" class="ln"/>
<text x="30" y="40" text-anchor="end" class="c">cost</text>
<path d="M105 240 C 300 236, 470 200, 625 48" class="ad-red"/>
<text x="360" y="60" text-anchor="middle" class="kh-red">find problems early: reviews, prototypes, tests</text>
</g>
</svg>
<figcaption>Illustrative only: the exact ratios vary widely between studies, but the direction does not.</figcaption>
</figure>

A recurring observation since the 1970s is that a mistake costs more to fix the later it is discovered. A misunderstood requirement caught in a review costs a conversation; the same misunderstanding discovered after release may cost a redesign, a data migration, and a security incident. The exact multipliers quoted in textbooks vary widely and some are poorly supported, but the direction is not in dispute. It is the main argument for early reviews, prototypes, tests written alongside the code, and short feedback loops.

## Activities of the lifecycle

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The software lifecycle as a cycle of activities: requirements, design, construction, testing, deployment, and operation and maintenance, which feeds new requirements back into the cycle. Project management, quality assurance and configuration management run alongside all of them." xmlns="http://www.w3.org/2000/svg">
<style>
.s1c{ font-family:var(--sans),sans-serif; }
.s1c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s1c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s1c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s1c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s1c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s1c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s1c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s1c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s1c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s1c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s1c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s1c .s{ fill:var(--text-dim); font-size:13px; }
.s1c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s1c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .c{ fill:var(--text-faint); font-size:12.5px; }
.s1c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s1c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s1c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s1c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1c-a); }
.s1c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1c-a); marker-start:url(#s1c-s); }
.s1c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s1c-g); }
.s1c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-a); }
.s1c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s1c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s1c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s1c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s1c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s1c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1c-tri); }
.s1c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-tri); }
.s1c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1c-open); }
.s1c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-open); }
.s1c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1c-dia); }
.s1c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1c-odia); }
.s1c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1c-dia); marker-end:url(#s1c-open); }
.s1c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1c-solid); }
.s1c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s1c-open); }
.s1c .fill{ fill:var(--text); stroke:none; }
.s1c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s1c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s1c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s1c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s1c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s1c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s1c .ks-blue{ fill:#185FA5; font-size:13px; }
.s1c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s1c .kb-blue, :root[data-theme="dark"] .s1c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s1c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s1c .kh-blue{ fill:#85B7EB; }
.s1c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s1c-blue); }
.s1c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-blue); }
.s1c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s1c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s1c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s1c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s1c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s1c .kb-teal, :root[data-theme="dark"] .s1c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s1c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s1c .kh-teal{ fill:#5DCAA5; }
.s1c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s1c-teal); }
.s1c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-teal); }
.s1c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s1c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s1c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s1c .ks-amber{ fill:#854F0B; font-size:13px; }
.s1c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s1c .kb-amber, :root[data-theme="dark"] .s1c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s1c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s1c .kh-amber{ fill:#EF9F27; }
.s1c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s1c-amber); }
.s1c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-amber); }
.s1c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s1c .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s1c .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s1c .ks-coral{ fill:#993C1D; font-size:13px; }
.s1c .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s1c .kb-coral, :root[data-theme="dark"] .s1c .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s1c .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s1c .kh-coral{ fill:#F0997B; }
.s1c .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s1c-coral); }
.s1c .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-coral); }
.s1c .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s1c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s1c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s1c .ks-purple{ fill:#534AB7; font-size:13px; }
.s1c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s1c .kb-purple, :root[data-theme="dark"] .s1c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s1c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s1c .kh-purple{ fill:#AFA9EC; }
.s1c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s1c-purple); }
.s1c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-purple); }
.s1c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s1c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s1c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s1c .ks-green{ fill:#3B6D11; font-size:13px; }
.s1c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s1c .kb-green, :root[data-theme="dark"] .s1c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s1c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s1c .kh-green{ fill:#97C459; }
.s1c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s1c-green); }
.s1c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-green); }
.s1c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s1c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s1c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s1c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s1c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s1c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s1c .kb-gray, :root[data-theme="dark"] .s1c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s1c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s1c .kh-gray{ fill:#B4B2A9; }
.s1c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s1c-gray); }
.s1c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1c-gray); }
.s1c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s1c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s1c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s1c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s1c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s1c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s1c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s1c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s1c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s1c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s1c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s1c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s1c-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s1c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s1c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s1c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s1c">
<rect x="184" y="20" width="132" height="44" rx="7" class="k-blue"/>
<text x="250.0" y="46.5" text-anchor="middle" class="kb-blue">requirements</text>
<path d="M290 55 A 112 112 0 0 1 321 73" class="ar"/>
<rect x="286" y="79" width="132" height="44" rx="7" class="k-purple"/>
<text x="352.0" y="105.5" text-anchor="middle" class="kb-purple">design</text>
<path d="M361 142 A 112 112 0 0 1 361 178" class="ar"/>
<rect x="286" y="197" width="132" height="44" rx="7" class="k-teal"/>
<text x="352.0" y="223.5" text-anchor="middle" class="kb-teal">construction</text>
<path d="M321 247 A 112 112 0 0 1 290 265" class="ar"/>
<rect x="184" y="256" width="132" height="44" rx="7" class="k-amber"/>
<text x="250.0" y="282.5" text-anchor="middle" class="kb-amber">testing</text>
<path d="M210 265 A 112 112 0 0 1 179 247" class="ar"/>
<rect x="82" y="197" width="132" height="44" rx="7" class="k-coral"/>
<text x="148.0" y="223.5" text-anchor="middle" class="kb-coral">deployment</text>
<path d="M139 178 A 112 112 0 0 1 139 142" class="ar"/>
<rect x="82" y="79" width="132" height="44" rx="7" class="k-green"/>
<text x="148.0" y="96.5" text-anchor="middle" class="kb-green">operation and</text>
<text x="148.0" y="114.5" text-anchor="middle" class="kb-green">maintenance</text>
<path d="M179 73 A 112 112 0 0 1 210 55" class="ar"/>
<text x="250" y="156" text-anchor="middle" class="b">NetWarden</text>
<text x="250" y="174" text-anchor="middle" class="c">v1.0, v1.1 ...</text>
<rect x="470" y="60" width="230" height="54" rx="7" class="k-gray"/>
<text x="585.0" y="82.5" text-anchor="middle" class="kb-gray">project management</text>
<text x="585.0" y="100.5" text-anchor="middle" class="ks-gray">across every activity</text>
<rect x="470" y="134" width="230" height="54" rx="7" class="k-gray"/>
<text x="585.0" y="156.5" text-anchor="middle" class="kb-gray">quality assurance</text>
<text x="585.0" y="174.5" text-anchor="middle" class="ks-gray">across every activity</text>
<rect x="470" y="208" width="230" height="54" rx="7" class="k-gray"/>
<text x="585.0" y="230.5" text-anchor="middle" class="kb-gray">configuration management</text>
<text x="585.0" y="248.5" text-anchor="middle" class="ks-gray">across every activity</text>
</g>
</svg>
<figcaption>Every process model in Chapter 2 arranges these same activities differently.</figcaption>
</figure>

Whatever process a team follows, the same kinds of work have to happen:

| Activity | Question it answers | Chapters |
|---|---|---|
| Requirements | What should the system do, and how well? | 3 |
| Design and architecture | How will it be structured? | 4 to 7 |
| Construction | How do we build it well, together? | 8 to 10 |
| Testing and quality assurance | Does it do the right thing, correctly and safely? | 11, 12 |
| Deployment and operation | How does it reach users and keep running? | 13, 14 |
| Maintenance and evolution | How does it keep up with change? | 15 |

**Supporting activities** run throughout: project management (Chapter 16), quality assurance, and **configuration management**, which tracks every version of every artifact (Chapter 8). How these activities are ordered and repeated is the subject of Chapter 2.

## Software quality

What makes software "good"? The international standard **ISO/IEC 25010:2023** splits product quality into nine characteristics.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The nine product quality characteristics of ISO/IEC 25010:2023: functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility and safety, each with a NetWarden example." xmlns="http://www.w3.org/2000/svg">
<style>
.s1d{ font-family:var(--sans),sans-serif; }
.s1d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s1d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s1d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s1d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s1d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s1d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s1d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s1d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s1d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s1d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s1d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s1d .s{ fill:var(--text-dim); font-size:13px; }
.s1d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s1d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .c{ fill:var(--text-faint); font-size:12.5px; }
.s1d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s1d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s1d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s1d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1d-a); }
.s1d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1d-a); marker-start:url(#s1d-s); }
.s1d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s1d-g); }
.s1d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-a); }
.s1d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s1d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s1d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s1d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s1d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s1d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1d-tri); }
.s1d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-tri); }
.s1d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1d-open); }
.s1d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-open); }
.s1d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1d-dia); }
.s1d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1d-odia); }
.s1d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1d-dia); marker-end:url(#s1d-open); }
.s1d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1d-solid); }
.s1d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s1d-open); }
.s1d .fill{ fill:var(--text); stroke:none; }
.s1d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s1d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s1d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s1d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s1d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s1d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s1d .ks-blue{ fill:#185FA5; font-size:13px; }
.s1d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s1d .kb-blue, :root[data-theme="dark"] .s1d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s1d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s1d .kh-blue{ fill:#85B7EB; }
.s1d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s1d-blue); }
.s1d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-blue); }
.s1d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s1d .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s1d .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s1d .ks-teal{ fill:#0F6E56; font-size:13px; }
.s1d .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s1d .kb-teal, :root[data-theme="dark"] .s1d .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s1d .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s1d .kh-teal{ fill:#5DCAA5; }
.s1d .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s1d-teal); }
.s1d .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-teal); }
.s1d .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s1d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s1d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s1d .ks-amber{ fill:#854F0B; font-size:13px; }
.s1d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s1d .kb-amber, :root[data-theme="dark"] .s1d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s1d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s1d .kh-amber{ fill:#EF9F27; }
.s1d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s1d-amber); }
.s1d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-amber); }
.s1d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s1d .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s1d .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s1d .ks-coral{ fill:#993C1D; font-size:13px; }
.s1d .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s1d .kb-coral, :root[data-theme="dark"] .s1d .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s1d .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s1d .kh-coral{ fill:#F0997B; }
.s1d .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s1d-coral); }
.s1d .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-coral); }
.s1d .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s1d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s1d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s1d .ks-purple{ fill:#534AB7; font-size:13px; }
.s1d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s1d .kb-purple, :root[data-theme="dark"] .s1d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s1d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s1d .kh-purple{ fill:#AFA9EC; }
.s1d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s1d-purple); }
.s1d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-purple); }
.s1d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s1d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s1d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s1d .ks-green{ fill:#3B6D11; font-size:13px; }
.s1d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s1d .kb-green, :root[data-theme="dark"] .s1d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s1d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s1d .kh-green{ fill:#97C459; }
.s1d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s1d-green); }
.s1d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-green); }
.s1d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s1d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s1d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s1d .ks-red{ fill:#A32D2D; font-size:13px; }
.s1d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s1d .kb-red, :root[data-theme="dark"] .s1d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s1d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s1d .kh-red{ fill:#F09595; }
.s1d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s1d-red); }
.s1d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-red); }
.s1d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s1d .k-pink{ fill:#FBEAF0; stroke:#D4537E; stroke-width:1.6; }
.s1d .kb-pink{ fill:#72243E; font-size:13px; font-weight:700; }
.s1d .ks-pink{ fill:#993556; font-size:13px; }
.s1d .km-pink{ fill:#72243E; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-pink{ fill:#993556; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-pink{ fill:#72243E; stroke:#ED93B1; }
:root[data-theme="dark"] .s1d .kb-pink, :root[data-theme="dark"] .s1d .km-pink{ fill:#FBEAF0; }
:root[data-theme="dark"] .s1d .ks-pink{ fill:#F4C0D1; }
:root[data-theme="dark"] .s1d .kh-pink{ fill:#ED93B1; }
.s1d .ar-pink{ stroke:#D4537E; stroke-width:2; fill:none; marker-end:url(#s1d-pink); }
.s1d .ad-pink{ stroke:#D4537E; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-pink); }
.s1d .ln-pink{ stroke:#D4537E; stroke-width:2; fill:none; }
.s1d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s1d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s1d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s1d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s1d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s1d .kb-gray, :root[data-theme="dark"] .s1d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s1d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s1d .kh-gray{ fill:#B4B2A9; }
.s1d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s1d-gray); }
.s1d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1d-gray); }
.s1d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s1d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s1d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s1d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s1d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s1d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s1d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s1d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s1d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s1d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s1d-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s1d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s1d-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s1d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s1d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s1d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s1d-pink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D4537E"/></marker><marker id="s1d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s1d">
<rect x="20" y="16" width="218" height="64" rx="7" class="k-blue"/>
<text x="129.0" y="43.5" text-anchor="middle" class="kb-blue">functional suitability</text>
<text x="129.0" y="61.5" text-anchor="middle" class="ks-blue">finds the right CVEs</text>
<rect x="250" y="16" width="218" height="64" rx="7" class="k-teal"/>
<text x="359.0" y="43.5" text-anchor="middle" class="kb-teal">performance efficiency</text>
<text x="359.0" y="61.5" text-anchor="middle" class="ks-teal">a /24 in under 60 s</text>
<rect x="480" y="16" width="218" height="64" rx="7" class="k-purple"/>
<text x="589.0" y="43.5" text-anchor="middle" class="kb-purple">compatibility</text>
<text x="589.0" y="61.5" text-anchor="middle" class="ks-purple">JSON for other tools</text>
<rect x="20" y="96" width="218" height="64" rx="7" class="k-pink"/>
<text x="129.0" y="123.5" text-anchor="middle" class="kb-pink">interaction capability</text>
<text x="129.0" y="141.5" text-anchor="middle" class="ks-pink">clear CLI and reports</text>
<rect x="250" y="96" width="218" height="64" rx="7" class="k-green"/>
<text x="359.0" y="123.5" text-anchor="middle" class="kb-green">reliability</text>
<text x="359.0" y="141.5" text-anchor="middle" class="ks-green">survives silent hosts</text>
<rect x="480" y="96" width="218" height="64" rx="7" class="k-red"/>
<text x="589.0" y="123.5" text-anchor="middle" class="kb-red">security</text>
<text x="589.0" y="141.5" text-anchor="middle" class="ks-red">refuses out-of-scope</text>
<rect x="20" y="176" width="218" height="64" rx="7" class="k-amber"/>
<text x="129.0" y="203.5" text-anchor="middle" class="kb-amber">maintainability</text>
<text x="129.0" y="221.5" text-anchor="middle" class="ks-amber">new check = one class</text>
<rect x="250" y="176" width="218" height="64" rx="7" class="k-coral"/>
<text x="359.0" y="203.5" text-anchor="middle" class="kb-coral">flexibility</text>
<text x="359.0" y="221.5" text-anchor="middle" class="ks-coral">Linux, macOS, Windows</text>
<rect x="480" y="176" width="218" height="64" rx="7" class="k-gray"/>
<text x="589.0" y="203.5" text-anchor="middle" class="kb-gray">safety</text>
<text x="589.0" y="221.5" text-anchor="middle" class="ks-gray">never floods a network</text>
</g>
</svg>
<figcaption>Quality is not one thing. Requirements must say which characteristics matter and how much.</figcaption>
</figure>

Two lessons follow. First, quality is **multi-dimensional**: a fast tool can be insecure, and a secure tool can be unusable. Second, the characteristics **compete**: more security checks slow a scan; more flexibility adds complexity. Engineering is largely the art of making these trade-offs deliberately, which is why requirements must state which qualities matter and how much (Chapter 3).

## The running example: NetWarden

To make the ideas concrete, this book follows one project from idea to release. **NetWarden** is a small, defensive network assessment tool.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="What NetWarden does: it reads an authorised scope, discovers open services on the targets, fingerprints the software and versions, runs security checks against a vulnerability knowledge base, writes a report with remediation advice, and stores the results to compare with later scans." xmlns="http://www.w3.org/2000/svg">
<style>
.s1e{ font-family:var(--sans),sans-serif; }
.s1e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s1e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s1e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s1e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s1e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s1e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s1e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s1e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s1e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s1e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s1e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s1e .s{ fill:var(--text-dim); font-size:13px; }
.s1e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s1e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .c{ fill:var(--text-faint); font-size:12.5px; }
.s1e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s1e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s1e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s1e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1e-a); }
.s1e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1e-a); marker-start:url(#s1e-s); }
.s1e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s1e-g); }
.s1e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-a); }
.s1e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s1e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s1e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s1e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s1e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s1e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1e-tri); }
.s1e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-tri); }
.s1e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1e-open); }
.s1e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-open); }
.s1e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1e-dia); }
.s1e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1e-odia); }
.s1e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1e-dia); marker-end:url(#s1e-open); }
.s1e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1e-solid); }
.s1e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s1e-open); }
.s1e .fill{ fill:var(--text); stroke:none; }
.s1e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s1e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s1e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s1e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s1e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s1e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s1e .ks-blue{ fill:#185FA5; font-size:13px; }
.s1e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s1e .kb-blue, :root[data-theme="dark"] .s1e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s1e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s1e .kh-blue{ fill:#85B7EB; }
.s1e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s1e-blue); }
.s1e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-blue); }
.s1e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s1e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s1e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s1e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s1e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s1e .kb-teal, :root[data-theme="dark"] .s1e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s1e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s1e .kh-teal{ fill:#5DCAA5; }
.s1e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s1e-teal); }
.s1e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-teal); }
.s1e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s1e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s1e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s1e .ks-amber{ fill:#854F0B; font-size:13px; }
.s1e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s1e .kb-amber, :root[data-theme="dark"] .s1e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s1e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s1e .kh-amber{ fill:#EF9F27; }
.s1e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s1e-amber); }
.s1e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-amber); }
.s1e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s1e .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s1e .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s1e .ks-coral{ fill:#993C1D; font-size:13px; }
.s1e .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s1e .kb-coral, :root[data-theme="dark"] .s1e .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s1e .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s1e .kh-coral{ fill:#F0997B; }
.s1e .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s1e-coral); }
.s1e .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-coral); }
.s1e .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s1e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s1e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s1e .ks-purple{ fill:#534AB7; font-size:13px; }
.s1e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s1e .kb-purple, :root[data-theme="dark"] .s1e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s1e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s1e .kh-purple{ fill:#AFA9EC; }
.s1e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s1e-purple); }
.s1e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-purple); }
.s1e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s1e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s1e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s1e .ks-green{ fill:#3B6D11; font-size:13px; }
.s1e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s1e .kb-green, :root[data-theme="dark"] .s1e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s1e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s1e .kh-green{ fill:#97C459; }
.s1e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s1e-green); }
.s1e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-green); }
.s1e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s1e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s1e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s1e .ks-red{ fill:#A32D2D; font-size:13px; }
.s1e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s1e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s1e .kb-red, :root[data-theme="dark"] .s1e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s1e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s1e .kh-red{ fill:#F09595; }
.s1e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s1e-red); }
.s1e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1e-red); }
.s1e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s1e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s1e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s1e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s1e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s1e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s1e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s1e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s1e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s1e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s1e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s1e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s1e-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s1e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s1e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s1e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s1e">
<rect x="20" y="40" width="122" height="60" rx="7" class="k-red"/>
<text x="81.0" y="65.5" text-anchor="middle" class="kb-red">scope</text>
<text x="81.0" y="83.5" text-anchor="middle" class="ks-red">authorised?</text>
<rect x="160" y="40" width="122" height="60" rx="7" class="k-blue"/>
<text x="221.0" y="65.5" text-anchor="middle" class="kb-blue">discover</text>
<text x="221.0" y="83.5" text-anchor="middle" class="ks-blue">open ports</text>
<line x1="144" y1="70" x2="158" y2="70" class="ar"/>
<rect x="300" y="40" width="122" height="60" rx="7" class="k-purple"/>
<text x="361.0" y="65.5" text-anchor="middle" class="kb-purple">fingerprint</text>
<text x="361.0" y="83.5" text-anchor="middle" class="ks-purple">product, version</text>
<line x1="284" y1="70" x2="298" y2="70" class="ar"/>
<rect x="440" y="40" width="122" height="60" rx="7" class="k-amber"/>
<text x="501.0" y="65.5" text-anchor="middle" class="kb-amber">check</text>
<text x="501.0" y="83.5" text-anchor="middle" class="ks-amber">known CVEs, risks</text>
<line x1="424" y1="70" x2="438" y2="70" class="ar"/>
<rect x="580" y="40" width="122" height="60" rx="7" class="k-teal"/>
<text x="641.0" y="65.5" text-anchor="middle" class="kb-teal">report</text>
<text x="641.0" y="83.5" text-anchor="middle" class="ks-teal">fix advice</text>
<line x1="564" y1="70" x2="578" y2="70" class="ar"/>
<rect x="320" y="150" width="160" height="50" rx="7" class="k-green"/>
<text x="400.0" y="170.5" text-anchor="middle" class="kb-green">history</text>
<text x="400.0" y="188.5" text-anchor="middle" class="ks-green">compare scans</text>
<path d="M641 102 C 641 170, 560 175, 482 175" class="ar"/>
<path d="M318 175 C 160 175, 80 150, 80 104" class="ad"/>
<text x="150" y="200" text-anchor="middle" class="c">next month: what was fixed?</text>
<text x="360" y="236" text-anchor="middle" class="kh-coral">a real tool for defenders: Python, about 900 lines, 46 automated tests</text>
</g>
</svg>
<figcaption>NetWarden: the running example. Every chapter adds a piece of its engineering, not just its code.</figcaption>
</figure>

An administrator gives NetWarden a list of networks they are **authorised** to assess and a set of targets. NetWarden:

1. refuses any target outside the authorised scope;
2. discovers open TCP ports on the targets;
3. reads each service's banner to identify the product and version, for example `OpenSSH 8.9p1`;
4. runs checks: known vulnerabilities (CVE identifiers and CVSS scores), cleartext protocols such as Telnet, exposed databases, missing web security headers;
5. writes a report in Markdown, JSON or HTML, with a remediation step for every finding;
6. stores the results, so the next scan can show what was fixed and what is new.

The code, tests, documents and pipeline are real and run. The project story around them, the stakeholders, interviews, sprints and the prototype that came before, is a realistic teaching scenario, written so that every chapter has something concrete to discuss.

NetWarden is a good teaching project because it has everything a real system has: users with different goals, safety and ethical constraints, performance limits, external data that goes out of date, untrusted input, and a need to be extended over time. It is also small, about 900 lines of Python, so you can read all of it.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="How the parts of the book follow NetWarden through its life: Part I sets out the vision and process, Part II produces requirements, UML models, design and architecture, Part III builds it with version control and clean code, Part IV tests and secures it, Part V delivers and maintains it, and Part VI plans and runs the project." xmlns="http://www.w3.org/2000/svg">
<style>
.s1f{ font-family:var(--sans),sans-serif; }
.s1f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s1f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s1f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s1f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s1f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s1f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s1f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s1f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s1f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s1f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s1f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s1f .s{ fill:var(--text-dim); font-size:13px; }
.s1f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s1f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .c{ fill:var(--text-faint); font-size:12.5px; }
.s1f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s1f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s1f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s1f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1f-a); }
.s1f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s1f-a); marker-start:url(#s1f-s); }
.s1f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s1f-g); }
.s1f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-a); }
.s1f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s1f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s1f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s1f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s1f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s1f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1f-tri); }
.s1f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-tri); }
.s1f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1f-open); }
.s1f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-open); }
.s1f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1f-dia); }
.s1f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1f-odia); }
.s1f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s1f-dia); marker-end:url(#s1f-open); }
.s1f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s1f-solid); }
.s1f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s1f-open); }
.s1f .fill{ fill:var(--text); stroke:none; }
.s1f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s1f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s1f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s1f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s1f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s1f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s1f .ks-blue{ fill:#185FA5; font-size:13px; }
.s1f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s1f .kb-blue, :root[data-theme="dark"] .s1f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s1f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s1f .kh-blue{ fill:#85B7EB; }
.s1f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s1f-blue); }
.s1f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-blue); }
.s1f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s1f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s1f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s1f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s1f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s1f .kb-teal, :root[data-theme="dark"] .s1f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s1f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s1f .kh-teal{ fill:#5DCAA5; }
.s1f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s1f-teal); }
.s1f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-teal); }
.s1f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s1f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s1f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s1f .ks-amber{ fill:#854F0B; font-size:13px; }
.s1f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s1f .kb-amber, :root[data-theme="dark"] .s1f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s1f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s1f .kh-amber{ fill:#EF9F27; }
.s1f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s1f-amber); }
.s1f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-amber); }
.s1f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s1f .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s1f .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s1f .ks-coral{ fill:#993C1D; font-size:13px; }
.s1f .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1f .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s1f .kb-coral, :root[data-theme="dark"] .s1f .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s1f .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s1f .kh-coral{ fill:#F0997B; }
.s1f .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s1f-coral); }
.s1f .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-coral); }
.s1f .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s1f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s1f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s1f .ks-purple{ fill:#534AB7; font-size:13px; }
.s1f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s1f .kb-purple, :root[data-theme="dark"] .s1f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s1f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s1f .kh-purple{ fill:#AFA9EC; }
.s1f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s1f-purple); }
.s1f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-purple); }
.s1f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s1f .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s1f .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s1f .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s1f .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s1f .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s1f .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s1f .kb-gray, :root[data-theme="dark"] .s1f .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s1f .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s1f .kh-gray{ fill:#B4B2A9; }
.s1f .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s1f-gray); }
.s1f .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s1f-gray); }
.s1f .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s1f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s1f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s1f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s1f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s1f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s1f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s1f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s1f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s1f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s1f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s1f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s1f-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s1f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s1f-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s1f">
<rect x="20" y="30" width="105" height="40" rx="7" class="k-gray"/>
<text x="72.5" y="54.5" text-anchor="middle" class="kb-gray">Part I</text>
<rect x="20" y="82" width="105" height="70" rx="5" class="pnl"/>
<text x="72.5" y="121.5" text-anchor="middle" class="s">foundations</text>
<rect x="20" y="166" width="105" height="58" rx="5" class="pnl"/>
<text x="72.5" y="190.5" text-anchor="middle" class="c">vision</text>
<text x="72.5" y="208.5" text-anchor="middle" class="c">process</text>
<rect x="135" y="30" width="105" height="40" rx="7" class="k-blue"/>
<text x="187.5" y="54.5" text-anchor="middle" class="kb-blue">Part II</text>
<rect x="135" y="82" width="105" height="70" rx="5" class="pnl"/>
<text x="187.5" y="112.5" text-anchor="middle" class="s">requirements</text>
<text x="187.5" y="130.5" text-anchor="middle" class="s">design</text>
<rect x="135" y="166" width="105" height="58" rx="5" class="pnl"/>
<text x="187.5" y="181.5" text-anchor="middle" class="c">SRS</text>
<text x="187.5" y="199.5" text-anchor="middle" class="c">UML</text>
<text x="187.5" y="217.5" text-anchor="middle" class="c">ADRs</text>
<rect x="250" y="30" width="105" height="40" rx="7" class="k-teal"/>
<text x="302.5" y="54.5" text-anchor="middle" class="kb-teal">Part III</text>
<rect x="250" y="82" width="105" height="70" rx="5" class="pnl"/>
<text x="302.5" y="121.5" text-anchor="middle" class="s">construction</text>
<rect x="250" y="166" width="105" height="58" rx="5" class="pnl"/>
<text x="302.5" y="190.5" text-anchor="middle" class="c">Git</text>
<text x="302.5" y="208.5" text-anchor="middle" class="c">clean code</text>
<rect x="365" y="30" width="105" height="40" rx="7" class="k-amber"/>
<text x="417.5" y="54.5" text-anchor="middle" class="kb-amber">Part IV</text>
<rect x="365" y="82" width="105" height="70" rx="5" class="pnl"/>
<text x="417.5" y="121.5" text-anchor="middle" class="s">quality</text>
<rect x="365" y="166" width="105" height="58" rx="5" class="pnl"/>
<text x="417.5" y="190.5" text-anchor="middle" class="c">tests</text>
<text x="417.5" y="208.5" text-anchor="middle" class="c">threat model</text>
<rect x="480" y="30" width="105" height="40" rx="7" class="k-coral"/>
<text x="532.5" y="54.5" text-anchor="middle" class="kb-coral">Part V</text>
<rect x="480" y="82" width="105" height="70" rx="5" class="pnl"/>
<text x="532.5" y="112.5" text-anchor="middle" class="s">delivery</text>
<text x="532.5" y="130.5" text-anchor="middle" class="s">ops</text>
<rect x="480" y="166" width="105" height="58" rx="5" class="pnl"/>
<text x="532.5" y="190.5" text-anchor="middle" class="c">CI/CD</text>
<text x="532.5" y="208.5" text-anchor="middle" class="c">container</text>
<rect x="595" y="30" width="105" height="40" rx="7" class="k-purple"/>
<text x="647.5" y="54.5" text-anchor="middle" class="kb-purple">Part VI</text>
<rect x="595" y="82" width="105" height="70" rx="5" class="pnl"/>
<text x="647.5" y="112.5" text-anchor="middle" class="s">people</text>
<text x="647.5" y="130.5" text-anchor="middle" class="s">projects</text>
<rect x="595" y="166" width="105" height="58" rx="5" class="pnl"/>
<text x="647.5" y="181.5" text-anchor="middle" class="c">plan</text>
<text x="647.5" y="199.5" text-anchor="middle" class="c">risks</text>
<text x="647.5" y="217.5" text-anchor="middle" class="c">ethics</text>
<text x="360" y="256" text-anchor="middle" class="c">top row: book part; middle: topic; bottom: NetWarden artifacts you will see</text>
<text x="360" y="280" text-anchor="middle" class="c">all artifacts live in the netwarden/ folder of the book's repository</text>
</g>
</svg>
<figcaption>Read the chapters in order the first time; later, use this map to jump to what you need.</figcaption>
</figure>

### Hands on: run it

After setting up the project as described on the home page, start the practice targets in one terminal. They are fake services on your own machine that only **claim** to be old software; nothing is actually vulnerable:

```bash
netwarden demo
```

In a second terminal, scan them:

```bash
netwarden scan 127.0.0.1 --scope examples/lab-scope.txt --ports 2121,2222,2323,8080,13306
```

```text
scanning 1 host(s), 5 port(s) each
  127.0.0.1: 5 open port(s)
    [CRITICAL] vsftpd 2.3.4 backdoor gives a root shell
    [MEDIUM] Cleartext protocol: ftp
    [HIGH] regreSSHion: unauthenticated remote code execution in sshd
    [MEDIUM] Cleartext protocol: telnet
    [HIGH] Path traversal and file disclosure in Apache HTTP Server 2.4.49
    [CRITICAL] Path traversal and remote code execution in Apache HTTP Server 2.4.49 and 2.4.50
    [HIGH] MySQL reachable over the network
    ...
saved as scan 1 in netwarden.db
```

followed by a Markdown report with a summary table and remediation advice for each of the 12 findings. Now try a target outside the scope, such as `10.0.0.1`: NetWarden refuses before sending a single packet. That refusal is a **requirement**, and Chapter 3 shows where it came from.

## Software engineering as a profession

Software engineers make decisions that affect people who never see the code: patients, drivers, voters, and the owners of every network a scanner touches. The ACM and IEEE Computer Society publish a joint **Software Engineering Code of Ethics**, and many jurisdictions regulate the title "engineer". In Canada, for example, "software engineer" is a regulated title in some provinces, reserved for licensed professional engineers. Chapter 17 discusses professional responsibility in detail; for now, notice that NetWarden's first feature is a restriction on what it may do.

## Summary

- Software engineering is a **systematic, disciplined, quantifiable** approach to developing, operating and maintaining software.
- It is **programming integrated over time**: its practices exist to cope with people, change and long lifetimes.
- Software is inherently **complex, conformant, changeable and invisible**; no single tool removes these difficulties.
- Mistakes cost more the **later** they are found.
- Every process includes requirements, design, construction, testing, deployment and maintenance, supported by management, quality assurance and configuration management.
- Quality has many dimensions (ISO/IEC 25010) that must be **traded off** deliberately.
- **NetWarden**, a defensive network assessment tool, is the running example.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-1-what-is-software-engineering).

**1. Which three words describe the approach in the standard definition of software engineering?**

- A. Systematic, disciplined and quantifiable
- B. Fast, cheap and good
- C. Agile, lean and iterative
- D. Creative, flexible and informal

**2. What does 'programming integrated over time' mean?**

- A. Programming done in long sessions
- B. Writing code with timestamps
- C. Software engineering's practices exist to cope with many authors, users, changes and long lifetimes
- D. Using a scheduler in programs

**3. Which of Brooks's essential difficulties says software must fit arbitrary external interfaces and rules?**

- A. Complexity
- B. Conformity
- C. Changeability
- D. Invisibility

**4. What does Brooks's law state?**

- A. Software costs double every year
- B. Every program contains at least one bug
- C. Work expands to fill the time available
- D. Adding people to a late software project makes it later

**5. Why does the book stress finding problems early?**

- A. Early problems are more interesting
- B. A mistake costs more to fix the later in the lifecycle it is found
- C. Testers are cheaper early
- D. Late problems cannot be fixed

**6. What does ISO/IEC 25010 describe?**

- A. A process model
- B. A coding style
- C. A UML diagram type
- D. Software product quality, split into characteristics such as security and performance efficiency

**7. Which lesson about quality characteristics does the chapter draw?**

- A. They compete: more security checks can slow a scan, and engineering trades them off
- B. They are independent
- C. Only functional suitability matters
- D. They apply only to safety-critical software

**8. Why does NetWarden refuse a target outside its scope before sending any packet?**

- A. To save bandwidth
- B. The scanner cannot reach other networks
- C. It is a requirement: assessing networks you are not authorised to assess is harmful and often illegal
- D. To make testing easier
