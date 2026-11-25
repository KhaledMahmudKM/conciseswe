# Chapter 2: Software Process Models

A **software process** is the set of activities, in some order, that turns an idea into working software and keeps it working. A **process model** is a simplified description of a process: which activities happen, in what sequence, who does them, and what they produce. This chapter surveys the classic plan-driven models, then the agile methods that most teams use today, and ends with how to choose.

## Plan-driven models

**Plan-driven** processes plan the work in detail up front and measure progress against that plan. They work best when requirements are well understood and stable, and when the cost of failure is high.

### Waterfall

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The waterfall model: requirements, design, implementation, verification and maintenance in sequence, each phase finishing and signing off a document before the next begins. Dashed arrows show the feedback that Royce himself said was needed but that the model makes expensive." xmlns="http://www.w3.org/2000/svg">
<style>
.s2a{ font-family:var(--sans),sans-serif; }
.s2a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2a .s{ fill:var(--text-dim); font-size:13px; }
.s2a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .c{ fill:var(--text-faint); font-size:12.5px; }
.s2a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2a-a); }
.s2a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2a-a); marker-start:url(#s2a-s); }
.s2a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2a-g); }
.s2a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-a); }
.s2a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2a-tri); }
.s2a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-tri); }
.s2a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2a-open); }
.s2a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-open); }
.s2a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2a-dia); }
.s2a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2a-odia); }
.s2a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2a-dia); marker-end:url(#s2a-open); }
.s2a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2a-solid); }
.s2a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2a-open); }
.s2a .fill{ fill:var(--text); stroke:none; }
.s2a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2a .ks-blue{ fill:#185FA5; font-size:13px; }
.s2a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2a .kb-blue, :root[data-theme="dark"] .s2a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2a .kh-blue{ fill:#85B7EB; }
.s2a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2a-blue); }
.s2a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-blue); }
.s2a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s2a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s2a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s2a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s2a .kb-teal, :root[data-theme="dark"] .s2a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s2a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s2a .kh-teal{ fill:#5DCAA5; }
.s2a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s2a-teal); }
.s2a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-teal); }
.s2a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s2a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s2a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s2a .ks-amber{ fill:#854F0B; font-size:13px; }
.s2a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s2a .kb-amber, :root[data-theme="dark"] .s2a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s2a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s2a .kh-amber{ fill:#EF9F27; }
.s2a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s2a-amber); }
.s2a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-amber); }
.s2a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s2a .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s2a .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s2a .ks-coral{ fill:#993C1D; font-size:13px; }
.s2a .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2a .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s2a .kb-coral, :root[data-theme="dark"] .s2a .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s2a .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s2a .kh-coral{ fill:#F0997B; }
.s2a .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s2a-coral); }
.s2a .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-coral); }
.s2a .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s2a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s2a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s2a .ks-purple{ fill:#534AB7; font-size:13px; }
.s2a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s2a .kb-purple, :root[data-theme="dark"] .s2a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s2a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s2a .kh-purple{ fill:#AFA9EC; }
.s2a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s2a-purple); }
.s2a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-purple); }
.s2a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s2a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s2a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s2a .ks-red{ fill:#A32D2D; font-size:13px; }
.s2a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s2a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s2a .kb-red, :root[data-theme="dark"] .s2a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s2a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s2a .kh-red{ fill:#F09595; }
.s2a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s2a-red); }
.s2a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2a-red); }
.s2a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s2a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s2a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s2a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s2a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s2a">
<rect x="20" y="20" width="150" height="40" rx="7" class="k-blue"/>
<text x="95.0" y="44.5" text-anchor="middle" class="kb-blue">requirements</text>
<path d="M172 40 L195 40 L195 68" class="ar"/>
<path d="M270 68 C 270 54, 220 52, 174 52" class="ad-red"/>
<rect x="150" y="70" width="150" height="40" rx="7" class="k-purple"/>
<text x="225.0" y="94.5" text-anchor="middle" class="kb-purple">design</text>
<path d="M302 90 L325 90 L325 118" class="ar"/>
<path d="M400 118 C 400 104, 350 102, 304 102" class="ad-red"/>
<rect x="280" y="120" width="150" height="40" rx="7" class="k-teal"/>
<text x="355.0" y="144.5" text-anchor="middle" class="kb-teal">implementation</text>
<path d="M432 140 L455 140 L455 168" class="ar"/>
<path d="M530 168 C 530 154, 480 152, 434 152" class="ad-red"/>
<rect x="410" y="170" width="150" height="40" rx="7" class="k-amber"/>
<text x="485.0" y="194.5" text-anchor="middle" class="kb-amber">verification</text>
<path d="M562 190 L585 190 L585 218" class="ar"/>
<path d="M660 218 C 660 204, 610 202, 564 202" class="ad-red"/>
<rect x="540" y="220" width="150" height="40" rx="7" class="k-coral"/>
<text x="615.0" y="244.5" text-anchor="middle" class="kb-coral">maintenance</text>
<text x="20" y="288" text-anchor="start" class="c">each phase ends with a signed-off document: requirements spec, design spec, code, test report</text>
</g>
</svg>
<figcaption>Simple to plan and control, but it assumes requirements are known and stable at the start.</figcaption>
</figure>

The **waterfall** model runs the lifecycle activities in sequence, each producing a document that is reviewed and signed off before the next phase starts. It is usually attributed to Winston Royce's 1970 paper, which, ironically, presented the strict sequence as risky and recommended feedback loops and prototyping.

| Strengths | Weaknesses |
|---|---|
| Easy to plan, staff and track | Requirements must be known at the start |
| Clear documents and sign-offs, useful for contracts and audits | Working software appears very late |
| Suits stable, well-understood problems | Errors in early phases are found late, when they are most expensive |

### The V-model

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The V-model pairs each development phase on the left with a testing phase on the right: requirements with acceptance testing, system specification with system testing, architecture with integration testing, and detailed design with unit testing. Coding sits at the bottom of the V." xmlns="http://www.w3.org/2000/svg">
<style>
.s2b{ font-family:var(--sans),sans-serif; }
.s2b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2b .s{ fill:var(--text-dim); font-size:13px; }
.s2b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .c{ fill:var(--text-faint); font-size:12.5px; }
.s2b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2b-a); }
.s2b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2b-a); marker-start:url(#s2b-s); }
.s2b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2b-g); }
.s2b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-a); }
.s2b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2b-tri); }
.s2b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-tri); }
.s2b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2b-open); }
.s2b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-open); }
.s2b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2b-dia); }
.s2b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2b-odia); }
.s2b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2b-dia); marker-end:url(#s2b-open); }
.s2b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2b-solid); }
.s2b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2b-open); }
.s2b .fill{ fill:var(--text); stroke:none; }
.s2b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2b .ks-blue{ fill:#185FA5; font-size:13px; }
.s2b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2b .kb-blue, :root[data-theme="dark"] .s2b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2b .kh-blue{ fill:#85B7EB; }
.s2b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2b-blue); }
.s2b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-blue); }
.s2b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s2b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s2b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s2b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s2b .kb-teal, :root[data-theme="dark"] .s2b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s2b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s2b .kh-teal{ fill:#5DCAA5; }
.s2b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s2b-teal); }
.s2b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-teal); }
.s2b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s2b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s2b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s2b .ks-amber{ fill:#854F0B; font-size:13px; }
.s2b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s2b .kb-amber, :root[data-theme="dark"] .s2b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s2b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s2b .kh-amber{ fill:#EF9F27; }
.s2b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s2b-amber); }
.s2b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-amber); }
.s2b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s2b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s2b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s2b .ks-purple{ fill:#534AB7; font-size:13px; }
.s2b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s2b .kb-purple, :root[data-theme="dark"] .s2b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s2b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s2b .kh-purple{ fill:#AFA9EC; }
.s2b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s2b-purple); }
.s2b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-purple); }
.s2b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s2b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s2b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s2b .ks-green{ fill:#3B6D11; font-size:13px; }
.s2b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s2b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s2b .kb-green, :root[data-theme="dark"] .s2b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s2b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s2b .kh-green{ fill:#97C459; }
.s2b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s2b-green); }
.s2b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2b-green); }
.s2b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s2b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s2b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s2b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s2b">
<rect x="20" y="20" width="150" height="40" rx="7" class="k-blue"/>
<text x="95.0" y="44.5" text-anchor="middle" class="kb-blue">requirements</text>
<rect x="550" y="20" width="150" height="40" rx="7" class="k-green"/>
<text x="625.0" y="44.5" text-anchor="middle" class="kb-green">acceptance test</text>
<line x1="172" y1="40" x2="548" y2="40" class="ad"/>
<line x1="95" y1="62" x2="120" y2="74" class="ar"/>
<line x1="600" y1="74" x2="625" y2="62" class="ar"/>
<rect x="70" y="76" width="150" height="40" rx="7" class="k-blue"/>
<text x="145.0" y="100.5" text-anchor="middle" class="kb-blue">system spec</text>
<rect x="500" y="76" width="150" height="40" rx="7" class="k-green"/>
<text x="575.0" y="100.5" text-anchor="middle" class="kb-green">system test</text>
<line x1="222" y1="96" x2="498" y2="96" class="ad"/>
<line x1="145" y1="118" x2="170" y2="130" class="ar"/>
<line x1="550" y1="130" x2="575" y2="118" class="ar"/>
<rect x="120" y="132" width="150" height="40" rx="7" class="k-purple"/>
<text x="195.0" y="156.5" text-anchor="middle" class="kb-purple">architecture</text>
<rect x="450" y="132" width="150" height="40" rx="7" class="k-amber"/>
<text x="525.0" y="156.5" text-anchor="middle" class="kb-amber">integration test</text>
<line x1="272" y1="152" x2="448" y2="152" class="ad"/>
<line x1="195" y1="174" x2="220" y2="186" class="ar"/>
<line x1="500" y1="186" x2="525" y2="174" class="ar"/>
<rect x="170" y="188" width="150" height="40" rx="7" class="k-purple"/>
<text x="245.0" y="212.5" text-anchor="middle" class="kb-purple">module design</text>
<rect x="400" y="188" width="150" height="40" rx="7" class="k-amber"/>
<text x="475.0" y="212.5" text-anchor="middle" class="kb-amber">unit test</text>
<line x1="322" y1="208" x2="398" y2="208" class="ad"/>
<rect x="285" y="240" width="150" height="40" rx="7" class="k-teal"/>
<text x="360.0" y="264.5" text-anchor="middle" class="kb-teal">coding</text>
<line x1="245" y1="222" x2="300" y2="238" class="ar"/>
<line x1="420" y1="238" x2="475" y2="222" class="ar"/>
<text x="360" y="12" text-anchor="middle" class="c">dashed: the left side's documents are the test basis for the right side</text>
</g>
</svg>
<figcaption>Tests are planned when each specification is written, long before there is code to run.</figcaption>
</figure>

The **V-model** is a refinement of waterfall that pairs every specification with the test level that will verify it. Acceptance tests are designed from the requirements, system tests from the system specification, integration tests from the architecture, and unit tests from the detailed design. It is common in safety-critical domains such as automotive, aerospace and medical devices, where standards demand traceability from every requirement to the test that proves it.

### Incremental and iterative development

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Incremental versus iterative development. Incremental: deliver the product in slices, each one finished, like painting a picture one finished section at a time. Iterative: build a rough version of the whole and refine it in each pass. Agile methods combine both: each iteration delivers a small, working, improved increment." xmlns="http://www.w3.org/2000/svg">
<style>
.s2c{ font-family:var(--sans),sans-serif; }
.s2c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2c .s{ fill:var(--text-dim); font-size:13px; }
.s2c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2c .c{ fill:var(--text-faint); font-size:12.5px; }
.s2c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2c-a); }
.s2c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2c-a); marker-start:url(#s2c-s); }
.s2c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2c-g); }
.s2c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2c-a); }
.s2c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2c-tri); }
.s2c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2c-tri); }
.s2c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2c-open); }
.s2c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2c-open); }
.s2c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2c-dia); }
.s2c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2c-odia); }
.s2c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2c-dia); marker-end:url(#s2c-open); }
.s2c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2c-solid); }
.s2c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2c-open); }
.s2c .fill{ fill:var(--text); stroke:none; }
.s2c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2c .ks-blue{ fill:#185FA5; font-size:13px; }
.s2c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2c .kb-blue, :root[data-theme="dark"] .s2c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2c .kh-blue{ fill:#85B7EB; }
.s2c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2c-blue); }
.s2c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2c-blue); }
.s2c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2c .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s2c .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s2c .ks-coral{ fill:#993C1D; font-size:13px; }
.s2c .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s2c .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2c .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s2c .kb-coral, :root[data-theme="dark"] .s2c .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s2c .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s2c .kh-coral{ fill:#F0997B; }
.s2c .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s2c-coral); }
.s2c .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2c-coral); }
.s2c .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s2c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s2c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s2c .ks-purple{ fill:#534AB7; font-size:13px; }
.s2c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s2c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s2c .kb-purple, :root[data-theme="dark"] .s2c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s2c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s2c .kh-purple{ fill:#AFA9EC; }
.s2c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s2c-purple); }
.s2c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2c-purple); }
.s2c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2c-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s2c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s2c">
<text x="20" y="26" text-anchor="start" class="kh-blue">incremental: finished slices</text>
<rect x="20" y="40" width="76" height="70" rx="4" class="k-blue"/>
<text x="58" y="80" text-anchor="middle" class="kb-blue">1</text>
<rect x="100" y="40" width="76" height="70" rx="4" class="k-blue"/>
<text x="138" y="80" text-anchor="middle" class="kb-blue">2</text>
<rect x="180" y="40" width="76" height="70" rx="4" class="k-blue"/>
<text x="218" y="80" text-anchor="middle" class="kb-blue">3</text>
<rect x="260" y="40" width="76" height="70" rx="4" class="pnl"/>
<text x="298" y="80" text-anchor="middle" class="c">?</text>
<text x="380" y="26" text-anchor="start" class="kh-purple">iterative: whole, then refined</text>
<rect x="380" y="40" width="100" height="70" rx="4" class="k-purple" style="fill-opacity:0.35"/>
<text x="430" y="80" text-anchor="middle" class="kb-purple">sketch</text>
<rect x="490" y="40" width="100" height="70" rx="4" class="k-purple" style="fill-opacity:0.65"/>
<text x="540" y="80" text-anchor="middle" class="kb-purple">draft</text>
<rect x="600" y="40" width="100" height="70" rx="4" class="k-purple" style="fill-opacity:1.0"/>
<text x="650" y="80" text-anchor="middle" class="kb-purple">finished</text>
<rect x="20" y="150" width="680" height="60" rx="7" class="k-coral"/>
<text x="360.0" y="175.5" text-anchor="middle" class="kb-coral">agile: iterative and incremental</text>
<text x="360.0" y="193.5" text-anchor="middle" class="ks-coral">each 2-week sprint adds a working slice and improves what exists</text>
<text x="360" y="248" text-anchor="middle" class="c">NetWarden: sprint 1 scope + discovery, sprint 2 vulnerabilities + reports, sprint 3 history + CI</text>
</g>
</svg>
<figcaption>Both reduce risk by producing something real early. Most modern processes do both at once.</figcaption>
</figure>

**Incremental** development delivers the system in slices, each adding functionality on top of the last. **Iterative** development builds a rough version of the whole and refines it in repeated passes. Both bring working software forward, so users can give feedback early, and both reduce the risk of discovering at the end that the product is wrong. The Rational Unified Process (RUP), popular in the 2000s, organised iterations into four phases: inception, elaboration, construction and transition.

### The spiral model

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Boehm&#x27;s spiral model: each loop of the spiral passes through four quadrants: determine objectives, identify and resolve risks (often with a prototype), develop and test, and plan the next iteration. The spiral widens as cost and commitment grow." xmlns="http://www.w3.org/2000/svg">
<style>
.s2d{ font-family:var(--sans),sans-serif; }
.s2d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2d .s{ fill:var(--text-dim); font-size:13px; }
.s2d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2d .c{ fill:var(--text-faint); font-size:12.5px; }
.s2d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2d-a); }
.s2d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2d-a); marker-start:url(#s2d-s); }
.s2d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2d-g); }
.s2d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-a); }
.s2d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2d-tri); }
.s2d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-tri); }
.s2d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2d-open); }
.s2d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-open); }
.s2d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2d-dia); }
.s2d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2d-odia); }
.s2d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2d-dia); marker-end:url(#s2d-open); }
.s2d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2d-solid); }
.s2d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2d-open); }
.s2d .fill{ fill:var(--text); stroke:none; }
.s2d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2d .ks-blue{ fill:#185FA5; font-size:13px; }
.s2d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2d .kb-blue, :root[data-theme="dark"] .s2d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2d .kh-blue{ fill:#85B7EB; }
.s2d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2d-blue); }
.s2d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-blue); }
.s2d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2d .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s2d .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s2d .ks-teal{ fill:#0F6E56; font-size:13px; }
.s2d .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s2d .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2d .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s2d .kb-teal, :root[data-theme="dark"] .s2d .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s2d .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s2d .kh-teal{ fill:#5DCAA5; }
.s2d .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s2d-teal); }
.s2d .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-teal); }
.s2d .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s2d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s2d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s2d .ks-amber{ fill:#854F0B; font-size:13px; }
.s2d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s2d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s2d .kb-amber, :root[data-theme="dark"] .s2d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s2d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s2d .kh-amber{ fill:#EF9F27; }
.s2d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s2d-amber); }
.s2d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-amber); }
.s2d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s2d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s2d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s2d .ks-red{ fill:#A32D2D; font-size:13px; }
.s2d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s2d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s2d .kb-red, :root[data-theme="dark"] .s2d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s2d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s2d .kh-red{ fill:#F09595; }
.s2d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s2d-red); }
.s2d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2d-red); }
.s2d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2d-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s2d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s2d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s2d">
<line x1="60" y1="168" x2="660" y2="168" class="ln"/>
<line x1="360" y1="18" x2="360" y2="318" class="ln"/>
<path d="M342 168 L340 171 L340 174 L339 177 L340 180 L342 184 L345 187 L349 190 L354 193 L360 194 L366 195 L373 195 L380 195 L387 193 L394 190 L400 185 L405 180 L410 175 L412 168 L413 161 L413 154 L410 146 L406 139 L400 133 L392 127 L382 122 L372 118 L360 116 L348 115 L335 116 L323 119 L311 124 L300 130 L290 138 L282 147 L277 157 L274 168 L273 179 L275 191 L280 203 L288 213 L298 223 L311 232 L326 238 L342 243 L360 246 L378 246 L397 244 L415 239 L431 232 L447 222 L460 211 L470 198 L477 183 L481 168 L481 152 L477 136 L469 121 L458 106 L444 93 L426 82 L406 74 L384 68 L360 65 L336 65 L312 68 L288 75 L267 85 L247 97 L231 112 L218 129 L209 148 L205 168" class="ar"/>
<text x="80" y="40" text-anchor="start" class="kh-blue">1. objectives, alternatives</text>
<text x="640" y="40" text-anchor="end" class="kh-red">2. evaluate risks, prototype</text>
<text x="640" y="304" text-anchor="end" class="kh-teal">3. develop and test</text>
<text x="80" y="304" text-anchor="start" class="kh-amber">4. plan next iteration</text>
<text x="366" y="162" text-anchor="start" class="c">start</text>
</g>
</svg>
<figcaption>Risk drives the process: each loop tackles the biggest remaining risk before committing more money.</figcaption>
</figure>

Barry Boehm's **spiral model** (1986) organises development as a series of loops. Each loop sets objectives, identifies the biggest remaining **risks** and resolves them, often by building a prototype, then develops and tests a version, and plans the next loop. It is less a recipe than a principle that still matters: **let risk decide what to do next**. For NetWarden, the biggest early risk was whether banner-based version detection would be accurate enough, so the first prototype did only that.

## Agile development

By the late 1990s many practitioners felt that heavyweight processes produced documents rather than software. In 2001, seventeen of them met in Utah and wrote the **Manifesto for Agile Software Development**.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The four values of the Agile Manifesto (2001): individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan. The items on the right still have value; the items on the left are valued more." xmlns="http://www.w3.org/2000/svg">
<style>
.s2e{ font-family:var(--sans),sans-serif; }
.s2e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2e .s{ fill:var(--text-dim); font-size:13px; }
.s2e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2e .c{ fill:var(--text-faint); font-size:12.5px; }
.s2e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2e-a); }
.s2e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2e-a); marker-start:url(#s2e-s); }
.s2e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2e-g); }
.s2e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2e-a); }
.s2e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2e-tri); }
.s2e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2e-tri); }
.s2e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2e-open); }
.s2e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2e-open); }
.s2e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2e-dia); }
.s2e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2e-odia); }
.s2e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2e-dia); marker-end:url(#s2e-open); }
.s2e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2e-solid); }
.s2e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2e-open); }
.s2e .fill{ fill:var(--text); stroke:none; }
.s2e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2e .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s2e .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s2e .ks-coral{ fill:#993C1D; font-size:13px; }
.s2e .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s2e .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2e .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s2e .kb-coral, :root[data-theme="dark"] .s2e .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s2e .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s2e .kh-coral{ fill:#F0997B; }
.s2e .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s2e-coral); }
.s2e .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2e-coral); }
.s2e .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2e-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s2e">
<rect x="20" y="16" width="290" height="40" rx="7" class="k-coral"/>
<text x="165.0" y="40.5" text-anchor="middle" class="kb-coral">individuals and interactions</text>
<text x="360" y="41" text-anchor="middle" class="c">over</text>
<rect x="410" y="16" width="290" height="40" rx="7" class="pnl"/>
<text x="555.0" y="40.5" text-anchor="middle" class="s">processes and tools</text>
<rect x="20" y="68" width="290" height="40" rx="7" class="k-coral"/>
<text x="165.0" y="92.5" text-anchor="middle" class="kb-coral">working software</text>
<text x="360" y="93" text-anchor="middle" class="c">over</text>
<rect x="410" y="68" width="290" height="40" rx="7" class="pnl"/>
<text x="555.0" y="92.5" text-anchor="middle" class="s">comprehensive documentation</text>
<rect x="20" y="120" width="290" height="40" rx="7" class="k-coral"/>
<text x="165.0" y="144.5" text-anchor="middle" class="kb-coral">customer collaboration</text>
<text x="360" y="145" text-anchor="middle" class="c">over</text>
<rect x="410" y="120" width="290" height="40" rx="7" class="pnl"/>
<text x="555.0" y="144.5" text-anchor="middle" class="s">contract negotiation</text>
<rect x="20" y="172" width="290" height="40" rx="7" class="k-coral"/>
<text x="165.0" y="196.5" text-anchor="middle" class="kb-coral">responding to change</text>
<text x="360" y="197" text-anchor="middle" class="c">over</text>
<rect x="410" y="172" width="290" height="40" rx="7" class="pnl"/>
<text x="555.0" y="196.5" text-anchor="middle" class="s">following a plan</text>
<text x="360" y="240" text-anchor="middle" class="c">"while there is value in the items on the right, we value the items on the left more"</text>
</g>
</svg>
<figcaption>A statement of priorities, not a ban on documents or plans. NetWarden still has an SRS, just a lean one.</figcaption>
</figure>

The manifesto is backed by twelve principles, including: deliver working software frequently, from a couple of weeks to a couple of months; welcome changing requirements, even late; business people and developers work together daily; build projects around motivated individuals; the best measure of progress is working software; maintain a sustainable pace; and at regular intervals the team reflects on how to become more effective.

Agile is a set of values, not a single method. The most widely used frameworks are Scrum, Kanban and Extreme Programming.

### Scrum

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The Scrum framework: the product owner orders the product backlog; sprint planning selects items into the sprint backlog; the developers work for a sprint of up to one month, meeting daily for 15 minutes; the sprint produces an increment that meets the definition of done; the sprint review inspects the increment with stakeholders and the retrospective improves the way the team works." xmlns="http://www.w3.org/2000/svg">
<style>
.s2f{ font-family:var(--sans),sans-serif; }
.s2f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2f .s{ fill:var(--text-dim); font-size:13px; }
.s2f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .c{ fill:var(--text-faint); font-size:12.5px; }
.s2f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2f-a); }
.s2f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2f-a); marker-start:url(#s2f-s); }
.s2f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2f-g); }
.s2f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-a); }
.s2f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2f-tri); }
.s2f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-tri); }
.s2f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2f-open); }
.s2f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-open); }
.s2f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2f-dia); }
.s2f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2f-odia); }
.s2f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2f-dia); marker-end:url(#s2f-open); }
.s2f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2f-solid); }
.s2f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2f-open); }
.s2f .fill{ fill:var(--text); stroke:none; }
.s2f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2f .ks-blue{ fill:#185FA5; font-size:13px; }
.s2f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2f .kb-blue, :root[data-theme="dark"] .s2f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2f .kh-blue{ fill:#85B7EB; }
.s2f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2f-blue); }
.s2f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-blue); }
.s2f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s2f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s2f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s2f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s2f .kb-teal, :root[data-theme="dark"] .s2f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s2f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s2f .kh-teal{ fill:#5DCAA5; }
.s2f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s2f-teal); }
.s2f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-teal); }
.s2f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s2f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s2f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s2f .ks-amber{ fill:#854F0B; font-size:13px; }
.s2f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s2f .kb-amber, :root[data-theme="dark"] .s2f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s2f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s2f .kh-amber{ fill:#EF9F27; }
.s2f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s2f-amber); }
.s2f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-amber); }
.s2f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s2f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s2f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s2f .ks-purple{ fill:#534AB7; font-size:13px; }
.s2f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s2f .kb-purple, :root[data-theme="dark"] .s2f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s2f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s2f .kh-purple{ fill:#AFA9EC; }
.s2f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s2f-purple); }
.s2f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-purple); }
.s2f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s2f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s2f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s2f .ks-green{ fill:#3B6D11; font-size:13px; }
.s2f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s2f .kb-green, :root[data-theme="dark"] .s2f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s2f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s2f .kh-green{ fill:#97C459; }
.s2f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s2f-green); }
.s2f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-green); }
.s2f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s2f .k-pink{ fill:#FBEAF0; stroke:#D4537E; stroke-width:1.6; }
.s2f .kb-pink{ fill:#72243E; font-size:13px; font-weight:700; }
.s2f .ks-pink{ fill:#993556; font-size:13px; }
.s2f .km-pink{ fill:#72243E; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-pink{ fill:#993556; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-pink{ fill:#72243E; stroke:#ED93B1; }
:root[data-theme="dark"] .s2f .kb-pink, :root[data-theme="dark"] .s2f .km-pink{ fill:#FBEAF0; }
:root[data-theme="dark"] .s2f .ks-pink{ fill:#F4C0D1; }
:root[data-theme="dark"] .s2f .kh-pink{ fill:#ED93B1; }
.s2f .ar-pink{ stroke:#D4537E; stroke-width:2; fill:none; marker-end:url(#s2f-pink); }
.s2f .ad-pink{ stroke:#D4537E; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-pink); }
.s2f .ln-pink{ stroke:#D4537E; stroke-width:2; fill:none; }
.s2f .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s2f .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s2f .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s2f .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s2f .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2f .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s2f .kb-gray, :root[data-theme="dark"] .s2f .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s2f .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s2f .kh-gray{ fill:#B4B2A9; }
.s2f .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s2f-gray); }
.s2f .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2f-gray); }
.s2f .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s2f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s2f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s2f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s2f-pink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D4537E"/></marker><marker id="s2f-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s2f">
<rect x="20" y="120" width="120" height="80" rx="7" class="k-blue"/>
<text x="80.0" y="146.5" text-anchor="middle" class="kb-blue">product</text>
<text x="80.0" y="164.5" text-anchor="middle" class="kb-blue">backlog</text>
<text x="80.0" y="182.5" text-anchor="middle" class="ks-blue">ordered by PO</text>
<line x1="142" y1="160" x2="168" y2="160" class="ar"/>
<rect x="170" y="135" width="100" height="50" rx="7" class="k-gray"/>
<text x="220.0" y="155.5" text-anchor="middle" class="kb-gray">sprint</text>
<text x="220.0" y="173.5" text-anchor="middle" class="kb-gray">planning</text>
<line x1="272" y1="160" x2="298" y2="160" class="ar"/>
<rect x="300" y="120" width="110" height="80" rx="7" class="k-purple"/>
<text x="355.0" y="146.5" text-anchor="middle" class="kb-purple">sprint</text>
<text x="355.0" y="164.5" text-anchor="middle" class="kb-purple">backlog</text>
<text x="355.0" y="182.5" text-anchor="middle" class="ks-purple">+ sprint goal</text>
<circle cx="500" cy="160" r="62" class="k-amber"/>
<text x="500" y="154" text-anchor="middle" class="kb-amber">sprint</text>
<text x="500" y="172" text-anchor="middle" class="ks-amber">1 to 4 weeks</text>
<path d="M500 76 C 540 50, 580 60, 570 98" class="ar-amber"/>
<text x="560" y="46" text-anchor="middle" class="kh-amber">daily scrum, 15 min</text>
<line x1="412" y1="160" x2="436" y2="160" class="ar"/>
<line x1="564" y1="160" x2="576" y2="160" class="ar"/>
<rect x="578" y="120" width="122" height="80" rx="7" class="k-green"/>
<text x="639.0" y="146.5" text-anchor="middle" class="kb-green">increment</text>
<text x="639.0" y="164.5" text-anchor="middle" class="ks-green">meets the</text>
<text x="639.0" y="182.5" text-anchor="middle" class="ks-green">definition of done</text>
<rect x="430" y="250" width="130" height="50" rx="7" class="k-teal"/>
<text x="495.0" y="270.5" text-anchor="middle" class="kb-teal">sprint review</text>
<text x="495.0" y="288.5" text-anchor="middle" class="ks-teal">what we built</text>
<rect x="250" y="250" width="150" height="50" rx="7" class="k-pink"/>
<text x="325.0" y="270.5" text-anchor="middle" class="kb-pink">retrospective</text>
<text x="325.0" y="288.5" text-anchor="middle" class="ks-pink">how we worked</text>
<path d="M645 202 C 645 240, 600 275, 562 275" class="ar"/>
<line x1="428" y1="275" x2="402" y2="275" class="ar"/>
<path d="M248 275 C 120 275, 80 240, 80 202" class="ad"/>
<text x="150" y="316" text-anchor="middle" class="c">feedback updates the backlog</text>
<text x="20" y="40" text-anchor="start" class="b">roles: product owner (what), scrum master (how well), developers (how)</text>
</g>
</svg>
<figcaption>Scrum is deliberately small: three accountabilities, five events, three artifacts.</figcaption>
</figure>

**Scrum**, described by Ken Schwaber and Jeff Sutherland in the *Scrum Guide* (the official edition is still the 2020 one; a 2025 *Expansion Pack* by Sutherland and colleagues adds optional guidance), organises work into **sprints** of one month or less, usually two weeks.

| Element | What it is | NetWarden example |
|---|---|---|
| **Product owner** | Accountable for maximising value; orders the product backlog | The security team lead |
| **Scrum master** | Accountable for the team's effectiveness; coaches and removes impediments | A senior developer, part-time |
| **Developers** | Build the increment; decide how to do the work | Three students |
| **Product backlog** | Ordered list of everything that might be needed | User stories US-1 to US-11 |
| **Sprint backlog** | Sprint goal plus the items selected for this sprint, with a plan | Sprint 2: "report known vulnerabilities with fixes" |
| **Increment** | A usable step towards the goal that meets the **definition of done** | Version 0.2.0 |
| **Sprint planning** | What can be done this sprint, and how? | 8 hours at most for a one-month sprint |
| **Daily scrum** | 15 minutes to inspect progress towards the sprint goal | Every morning at 9:30 |
| **Sprint review** | Inspect the increment with stakeholders; adapt the backlog | Demo to the security manager |
| **Sprint retrospective** | Inspect and improve how the team works | "Reviews take too long: limit PR size" |

The **definition of done** is a shared checklist that every increment must satisfy, for example: tests written and passing, coverage at least 90%, code reviewed, documentation updated. NetWarden's is in its `CONTRIBUTING.md`. Without it, "done" means something different to each person.

### Kanban

<figure class="diagram">
<svg viewBox="0 0 720 285" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A Kanban board for NetWarden with columns backlog, ready, in progress with a work-in-progress limit of 3, review with a limit of 2, and done. Cards move right as work progresses; a column at its limit cannot accept more work, which exposes bottlenecks." xmlns="http://www.w3.org/2000/svg">
<style>
.s2g{ font-family:var(--sans),sans-serif; }
.s2g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2g .s{ fill:var(--text-dim); font-size:13px; }
.s2g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2g .c{ fill:var(--text-faint); font-size:12.5px; }
.s2g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2g-a); }
.s2g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2g-a); marker-start:url(#s2g-s); }
.s2g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2g-g); }
.s2g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-a); }
.s2g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2g-tri); }
.s2g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-tri); }
.s2g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2g-open); }
.s2g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-open); }
.s2g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2g-dia); }
.s2g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2g-odia); }
.s2g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2g-dia); marker-end:url(#s2g-open); }
.s2g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2g-solid); }
.s2g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2g-open); }
.s2g .fill{ fill:var(--text); stroke:none; }
.s2g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2g .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2g .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2g .ks-blue{ fill:#185FA5; font-size:13px; }
.s2g .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2g .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2g .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2g .kb-blue, :root[data-theme="dark"] .s2g .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2g .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2g .kh-blue{ fill:#85B7EB; }
.s2g .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2g-blue); }
.s2g .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-blue); }
.s2g .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2g .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s2g .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s2g .ks-amber{ fill:#854F0B; font-size:13px; }
.s2g .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s2g .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2g .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s2g .kb-amber, :root[data-theme="dark"] .s2g .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s2g .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s2g .kh-amber{ fill:#EF9F27; }
.s2g .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s2g-amber); }
.s2g .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-amber); }
.s2g .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s2g .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s2g .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s2g .ks-green{ fill:#3B6D11; font-size:13px; }
.s2g .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s2g .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2g .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s2g .kb-green, :root[data-theme="dark"] .s2g .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s2g .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s2g .kh-green{ fill:#97C459; }
.s2g .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s2g-green); }
.s2g .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-green); }
.s2g .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s2g .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s2g .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s2g .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s2g .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s2g .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2g .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s2g .kb-gray, :root[data-theme="dark"] .s2g .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s2g .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s2g .kh-gray{ fill:#B4B2A9; }
.s2g .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s2g-gray); }
.s2g .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2g-gray); }
.s2g .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2g-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2g-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s2g-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s2g-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s2g">
<rect x="20" y="16" width="128" height="34" rx="4" class="k-gray"/>
<text x="84.0" y="37.5" text-anchor="middle" class="kb-gray">backlog</text>
<rect x="20" y="56" width="128" height="196" rx="4" class="pnl"/>
<rect x="28" y="66" width="112" height="36" rx="4" class="k-blue"/>
<text x="84.0" y="88.5" text-anchor="middle" class="ks-blue">US-10 live feed</text>
<rect x="28" y="112" width="112" height="36" rx="4" class="k-blue"/>
<text x="84.0" y="134.5" text-anchor="middle" class="ks-blue">US-11 backports</text>
<rect x="158" y="16" width="128" height="34" rx="4" class="k-gray"/>
<text x="222.0" y="37.5" text-anchor="middle" class="kb-gray">ready</text>
<rect x="158" y="56" width="128" height="196" rx="4" class="pnl"/>
<rect x="166" y="66" width="112" height="36" rx="4" class="k-blue"/>
<text x="222.0" y="88.5" text-anchor="middle" class="ks-blue">export CSV</text>
<rect x="296" y="16" width="128" height="34" rx="4" class="k-amber"/>
<text x="360.0" y="37.5" text-anchor="middle" class="kb-amber">in progress  (WIP 3)</text>
<rect x="296" y="56" width="128" height="196" rx="4" class="pnl"/>
<rect x="304" y="66" width="112" height="36" rx="4" class="k-blue"/>
<text x="360.0" y="88.5" text-anchor="middle" class="ks-blue">SMB check</text>
<rect x="304" y="112" width="112" height="36" rx="4" class="k-blue"/>
<text x="360.0" y="134.5" text-anchor="middle" class="ks-blue">IPv6 scan</text>
<rect x="304" y="158" width="112" height="36" rx="4" class="k-blue"/>
<text x="360.0" y="180.5" text-anchor="middle" class="ks-blue">fix #42</text>
<rect x="434" y="16" width="128" height="34" rx="4" class="k-amber"/>
<text x="498.0" y="37.5" text-anchor="middle" class="kb-amber">review  (WIP 2)</text>
<rect x="434" y="56" width="128" height="196" rx="4" class="pnl"/>
<rect x="442" y="66" width="112" height="36" rx="4" class="k-blue"/>
<text x="498.0" y="88.5" text-anchor="middle" class="ks-blue">HTML colours</text>
<rect x="572" y="16" width="128" height="34" rx="4" class="k-gray"/>
<text x="636.0" y="37.5" text-anchor="middle" class="kb-gray">done</text>
<rect x="572" y="56" width="128" height="196" rx="4" class="pnl"/>
<rect x="580" y="66" width="112" height="36" rx="4" class="k-green"/>
<text x="636.0" y="88.5" text-anchor="middle" class="ks-green">US-9 demo</text>
<rect x="580" y="112" width="112" height="36" rx="4" class="k-green"/>
<text x="636.0" y="134.5" text-anchor="middle" class="ks-green">US-8 exit codes</text>
<text x="360" y="276" text-anchor="middle" class="c">pull work when there is capacity; limit work in progress; measure lead time</text>
</g>
</svg>
<figcaption>Kanban has no sprints: work flows continuously, and WIP limits keep it flowing.</figcaption>
</figure>

**Kanban**, adapted from Toyota's production system, visualises work on a board and limits **work in progress** (WIP). There are no sprints and no prescribed roles; items are pulled when there is capacity. WIP limits make bottlenecks visible: if "review" is full, developers stop starting new work and help review instead. Teams measure **lead time** (from request to delivery) and **throughput** (items finished per week). Kanban suits work that arrives continuously and unpredictably, such as operations, support, and maintenance of a released product like NetWarden 1.x.

### Extreme Programming

**Extreme Programming** (XP), developed by Kent Beck in the late 1990s, contributed many of the technical practices that agile teams rely on: test-driven development (Chapter 11), pair programming, continuous integration (Chapter 13), small releases, simple design, refactoring (Chapter 10), collective code ownership, and a sustainable pace. Scrum says how to organise the work; XP says how to do the engineering. Many teams combine them.

### Scaling and hybrids

Large organisations use frameworks such as SAFe (Scaled Agile Framework) or LeSS (Large-Scale Scrum) to coordinate many teams, though these are debated. Many real projects are **hybrids**: plan-driven at the level of contracts, budgets and safety cases, agile inside each team.

## DevOps, briefly

Agile shortened the loop between customers and developers. **DevOps** extends it to operations: the same team builds, deploys and runs the software, using automation so that releasing is frequent and safe. Chapters 13 and 14 cover it in depth.

## Choosing a process

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Choosing a process: plan-driven approaches suit stable, well-understood requirements, safety-critical or regulated systems, large distributed teams and fixed contracts. Agile approaches suit uncertain or changing requirements, small co-located teams, frequent releases and an available customer. Most organisations use a hybrid." xmlns="http://www.w3.org/2000/svg">
<style>
.s2h{ font-family:var(--sans),sans-serif; }
.s2h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s2h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s2h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s2h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s2h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s2h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s2h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s2h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s2h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s2h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s2h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s2h .s{ fill:var(--text-dim); font-size:13px; }
.s2h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s2h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s2h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s2h .c{ fill:var(--text-faint); font-size:12.5px; }
.s2h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s2h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s2h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s2h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2h-a); }
.s2h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s2h-a); marker-start:url(#s2h-s); }
.s2h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s2h-g); }
.s2h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s2h-a); }
.s2h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s2h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s2h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s2h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s2h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s2h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2h-tri); }
.s2h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2h-tri); }
.s2h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2h-open); }
.s2h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s2h-open); }
.s2h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2h-dia); }
.s2h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2h-odia); }
.s2h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s2h-dia); marker-end:url(#s2h-open); }
.s2h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s2h-solid); }
.s2h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s2h-open); }
.s2h .fill{ fill:var(--text); stroke:none; }
.s2h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s2h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s2h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s2h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s2h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s2h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s2h .ks-blue{ fill:#185FA5; font-size:13px; }
.s2h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s2h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s2h .kb-blue, :root[data-theme="dark"] .s2h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s2h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s2h .kh-blue{ fill:#85B7EB; }
.s2h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s2h-blue); }
.s2h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2h-blue); }
.s2h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s2h .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s2h .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s2h .ks-coral{ fill:#993C1D; font-size:13px; }
.s2h .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s2h .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s2h .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s2h .kb-coral, :root[data-theme="dark"] .s2h .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s2h .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s2h .kh-coral{ fill:#F0997B; }
.s2h .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s2h-coral); }
.s2h .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s2h-coral); }
.s2h .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s2h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s2h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s2h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s2h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s2h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s2h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s2h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s2h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s2h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s2h-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s2h">
<rect x="20" y="16" width="300" height="40" rx="7" class="k-blue"/>
<text x="170.0" y="40.5" text-anchor="middle" class="kb-blue">plan-driven (waterfall, V)</text>
<rect x="400" y="16" width="300" height="40" rx="7" class="k-coral"/>
<text x="550.0" y="40.5" text-anchor="middle" class="kb-coral">agile (Scrum, Kanban, XP)</text>
<text x="360" y="86" text-anchor="middle" class="c">requirements</text>
<rect x="20" y="66" width="300" height="30" rx="4" class="pnl"/>
<text x="170.0" y="85.5" text-anchor="middle" class="s">stable, known</text>
<rect x="400" y="66" width="300" height="30" rx="4" class="pnl"/>
<text x="550.0" y="85.5" text-anchor="middle" class="s">uncertain, changing</text>
<text x="360" y="122" text-anchor="middle" class="c">criticality</text>
<rect x="20" y="102" width="300" height="30" rx="4" class="pnl"/>
<text x="170.0" y="121.5" text-anchor="middle" class="s">safety, regulation</text>
<rect x="400" y="102" width="300" height="30" rx="4" class="pnl"/>
<text x="550.0" y="121.5" text-anchor="middle" class="s">lower, recoverable</text>
<text x="360" y="158" text-anchor="middle" class="c">team</text>
<rect x="20" y="138" width="300" height="30" rx="4" class="pnl"/>
<text x="170.0" y="157.5" text-anchor="middle" class="s">large, distributed</text>
<rect x="400" y="138" width="300" height="30" rx="4" class="pnl"/>
<text x="550.0" y="157.5" text-anchor="middle" class="s">small, co-located</text>
<text x="360" y="194" text-anchor="middle" class="c">customer</text>
<rect x="20" y="174" width="300" height="30" rx="4" class="pnl"/>
<text x="170.0" y="193.5" text-anchor="middle" class="s">contract, sign-offs</text>
<rect x="400" y="174" width="300" height="30" rx="4" class="pnl"/>
<text x="550.0" y="193.5" text-anchor="middle" class="s">available, involved</text>
<text x="360" y="230" text-anchor="middle" class="c">releases</text>
<rect x="20" y="210" width="300" height="30" rx="4" class="pnl"/>
<text x="170.0" y="229.5" text-anchor="middle" class="s">few, big</text>
<rect x="400" y="210" width="300" height="30" rx="4" class="pnl"/>
<text x="550.0" y="229.5" text-anchor="middle" class="s">frequent, small</text>
<path d="M30 262 L690 262" class="ar2"/>
</g>
</svg>
<figcaption>Boehm and Turner's home grounds: choose by risk, and mix where a project has features of both.</figcaption>
</figure>

Boehm and Turner's *Balancing Agility and Discipline* (2003) suggests looking at a project's characteristics. Uncertain requirements, a small team and an available customer favour agile methods. Safety-critical systems, regulatory audits, large distributed teams and fixed-price contracts favour more planning and documentation. Most projects have some of each, so the honest answer is usually "agile, with as much discipline as the risks require".

NetWarden was developed with **Scrum** in three two-week sprints, because the requirements were expected to change as users saw early versions. Its safety requirements, however, were fixed before the first line of code, in the plan-driven spirit, because the cost of getting them wrong was unacceptable.

## Summary

- A **process model** describes the order of activities, roles and artifacts.
- **Waterfall** is sequential and document-driven; the **V-model** pairs each specification with a test level.
- **Incremental** and **iterative** development deliver working software early; the **spiral** model lets **risk** drive each iteration.
- The **Agile Manifesto** values individuals, working software, collaboration and responding to change.
- **Scrum** uses sprints, three accountabilities, five events and three artifacts, plus a **definition of done**.
- **Kanban** visualises flow and limits **work in progress**; **XP** supplies engineering practices.
- Choose by the project's risks; most organisations use **hybrids**.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-2-software-process-models).

**1. When does a plan-driven process such as waterfall work best?**

- A. When requirements change weekly
- B. When there is no customer
- C. For small prototypes
- D. When requirements are well understood and stable, and the cost of failure is high

**2. What does the V-model add to waterfall?**

- A. Sprints
- B. It pairs each specification with the test level that will verify it
- C. WIP limits
- D. Daily stand-ups

**3. What drives each loop of Boehm's spiral model?**

- A. The calendar
- B. The number of developers
- C. Customer complaints
- D. The biggest remaining risks, often resolved by building a prototype

**4. Which is one of the four values of the Agile Manifesto?**

- A. Responding to change over following a plan
- B. Comprehensive documentation over working software
- C. Processes and tools over individuals
- D. Contract negotiation over customer collaboration

**5. In Scrum, who orders the product backlog?**

- A. The scrum master
- B. The developers
- C. The product owner
- D. The stakeholders

**6. What is the definition of done?**

- A. The sprint end date
- B. The product owner's approval
- C. The last item in the backlog
- D. A shared checklist every increment must satisfy, such as tests passing and code reviewed

**7. What does Kanban limit to make bottlenecks visible?**

- A. Sprint length
- B. Work in progress
- C. Team size
- D. Backlog size

**8. Why was NetWarden developed with Scrum but its safety requirements fixed up front?**

- A. Scrum forbids safety requirements
- B. The team did not know Scrum well
- C. Requirements were expected to change, but safety rules were too important to leave to change: a hybrid
- D. Waterfall was cheaper
