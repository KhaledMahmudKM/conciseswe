# Chapter 16: Project Management

Most software projects that fail do not fail for technical reasons. They fail because nobody knew how big the work was, the plan was fiction, risks were ignored until they happened, or progress was invisible until it was too late. **Software project management** is the discipline of planning, estimating, organising, tracking and steering the work so that the right software is delivered with the time, money and people available. This chapter covers both the plan-driven tools and their agile counterparts, using NetWarden's three-sprint plan as the example.

## Constraints and trade-offs

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The project management triangle. Plan-driven projects fix scope and estimate time and cost from it. Agile projects invert the triangle: time, the sprints, and cost, the team, are fixed, and scope varies, with the most valuable features delivered first. Quality sits in the middle and should not be the variable that gives." xmlns="http://www.w3.org/2000/svg">
<style>
.s16a{ font-family:var(--sans),sans-serif; }
.s16a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16a .s{ fill:var(--text-dim); font-size:13px; }
.s16a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16a .c{ fill:var(--text-faint); font-size:12.5px; }
.s16a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16a-a); }
.s16a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16a-a); marker-start:url(#s16a-s); }
.s16a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16a-g); }
.s16a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16a-a); }
.s16a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16a-tri); }
.s16a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16a-tri); }
.s16a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16a-open); }
.s16a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16a-open); }
.s16a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16a-dia); }
.s16a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16a-odia); }
.s16a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16a-dia); marker-end:url(#s16a-open); }
.s16a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16a-solid); }
.s16a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16a-open); }
.s16a .fill{ fill:var(--text); stroke:none; }
.s16a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s16a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s16a .ks-blue{ fill:#185FA5; font-size:13px; }
.s16a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s16a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s16a .kb-blue, :root[data-theme="dark"] .s16a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s16a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s16a .kh-blue{ fill:#85B7EB; }
.s16a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s16a-blue); }
.s16a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16a-blue); }
.s16a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s16a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s16a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s16a .ks-green{ fill:#3B6D11; font-size:13px; }
.s16a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s16a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s16a .kb-green, :root[data-theme="dark"] .s16a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s16a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s16a .kh-green{ fill:#97C459; }
.s16a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s16a-green); }
.s16a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16a-green); }
.s16a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s16a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s16a">
<polygon points="190,40 320,230 60,230" class="k-blue" style="fill-opacity:0.5"/>
<text x="190" y="24" text-anchor="middle" class="kh-blue">plan-driven</text>
<text x="190" y="118" text-anchor="middle" class="kb-blue">scope</text>
<text x="190" y="138" text-anchor="middle" class="ks-blue">fixed</text>
<text x="80" y="254" text-anchor="middle" class="s">time: estimated</text>
<text x="300" y="254" text-anchor="middle" class="s">cost: estimated</text>
<text x="190" y="196" text-anchor="middle" class="b">quality</text>
<polygon points="400,40 660,40 530,230" class="k-green" style="fill-opacity:0.5"/>
<text x="530" y="24" text-anchor="middle" class="kh-green">agile</text>
<text x="430" y="62" text-anchor="start" class="kb-green">time: fixed</text>
<text x="630" y="62" text-anchor="end" class="kb-green">cost: fixed</text>
<text x="530" y="250" text-anchor="middle" class="kh-green">scope: varies, by value</text>
<text x="530" y="120" text-anchor="middle" class="b">quality</text>
</g>
</svg>
<figcaption>Something must flex. Agile chooses scope, and protects quality with the definition of done.</figcaption>
</figure>

Every project balances **scope**, **time** and **cost**, with **quality** in the middle. A plan-driven project fixes the scope and estimates the time and cost; when estimates prove optimistic, deadlines slip or budgets grow. Agile projects invert the triangle: the team and the sprint cadence are fixed, and scope flexes, with the product owner deciding what the most valuable next increment is. In both, letting quality give silently is the worst option, because it creates technical debt (Chapter 10) that slows every later step.

## Planning

### Work breakdown

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Work breakdown structure for NetWarden release 1.0. The release splits into requirements, design, implementation, quality, delivery and management. Implementation splits into scope and discovery, fingerprinting, checks and knowledge base, reports, history and command line. Each leaf is small enough to estimate and assign." xmlns="http://www.w3.org/2000/svg">
<style>
.s16c{ font-family:var(--sans),sans-serif; }
.s16c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16c .s{ fill:var(--text-dim); font-size:13px; }
.s16c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .c{ fill:var(--text-faint); font-size:12.5px; }
.s16c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16c-a); }
.s16c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16c-a); marker-start:url(#s16c-s); }
.s16c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16c-g); }
.s16c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-a); }
.s16c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16c-tri); }
.s16c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-tri); }
.s16c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16c-open); }
.s16c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-open); }
.s16c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16c-dia); }
.s16c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16c-odia); }
.s16c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16c-dia); marker-end:url(#s16c-open); }
.s16c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16c-solid); }
.s16c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16c-open); }
.s16c .fill{ fill:var(--text); stroke:none; }
.s16c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s16c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s16c .ks-blue{ fill:#185FA5; font-size:13px; }
.s16c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s16c .kb-blue, :root[data-theme="dark"] .s16c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s16c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s16c .kh-blue{ fill:#85B7EB; }
.s16c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s16c-blue); }
.s16c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-blue); }
.s16c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s16c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s16c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s16c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s16c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s16c .kb-teal, :root[data-theme="dark"] .s16c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s16c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s16c .kh-teal{ fill:#5DCAA5; }
.s16c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s16c-teal); }
.s16c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-teal); }
.s16c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s16c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s16c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s16c .ks-amber{ fill:#854F0B; font-size:13px; }
.s16c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s16c .kb-amber, :root[data-theme="dark"] .s16c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s16c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s16c .kh-amber{ fill:#EF9F27; }
.s16c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s16c-amber); }
.s16c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-amber); }
.s16c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s16c .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s16c .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s16c .ks-coral{ fill:#993C1D; font-size:13px; }
.s16c .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s16c .kb-coral, :root[data-theme="dark"] .s16c .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s16c .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s16c .kh-coral{ fill:#F0997B; }
.s16c .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s16c-coral); }
.s16c .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-coral); }
.s16c .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s16c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s16c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s16c .ks-purple{ fill:#534AB7; font-size:13px; }
.s16c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s16c .kb-purple, :root[data-theme="dark"] .s16c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s16c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s16c .kh-purple{ fill:#AFA9EC; }
.s16c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s16c-purple); }
.s16c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-purple); }
.s16c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s16c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s16c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s16c .ks-green{ fill:#3B6D11; font-size:13px; }
.s16c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s16c .kb-green, :root[data-theme="dark"] .s16c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s16c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s16c .kh-green{ fill:#97C459; }
.s16c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s16c-green); }
.s16c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-green); }
.s16c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s16c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s16c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s16c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s16c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s16c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s16c .kb-gray, :root[data-theme="dark"] .s16c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s16c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s16c .kh-gray{ fill:#B4B2A9; }
.s16c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s16c-gray); }
.s16c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16c-gray); }
.s16c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s16c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s16c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s16c-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s16c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s16c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s16c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s16c">
<rect x="260" y="10" width="200" height="40" rx="7" class="k-coral"/>
<text x="360.0" y="34.5" text-anchor="middle" class="kb-coral">NetWarden 1.0</text>
<rect x="20" y="80" width="104" height="36" rx="4" class="k-blue"/>
<text x="72.0" y="102.5" text-anchor="middle" class="ks-blue">requirements</text>
<path d="M360 52 L360 66 L72 66 L72 78" class="u"/>
<rect x="136" y="80" width="104" height="36" rx="4" class="k-purple"/>
<text x="188.0" y="102.5" text-anchor="middle" class="ks-purple">design</text>
<path d="M360 52 L360 66 L188 66 L188 78" class="u"/>
<rect x="252" y="80" width="104" height="36" rx="4" class="k-teal"/>
<text x="304.0" y="102.5" text-anchor="middle" class="ks-teal">implementation</text>
<path d="M360 52 L360 66 L304 66 L304 78" class="u"/>
<rect x="368" y="80" width="104" height="36" rx="4" class="k-amber"/>
<text x="420.0" y="102.5" text-anchor="middle" class="ks-amber">quality</text>
<path d="M360 52 L360 66 L420 66 L420 78" class="u"/>
<rect x="484" y="80" width="104" height="36" rx="4" class="k-green"/>
<text x="536.0" y="102.5" text-anchor="middle" class="ks-green">delivery</text>
<path d="M360 52 L360 66 L536 66 L536 78" class="u"/>
<rect x="600" y="80" width="104" height="36" rx="4" class="k-gray"/>
<text x="652.0" y="102.5" text-anchor="middle" class="ks-gray">management</text>
<path d="M360 52 L360 66 L652 66 L652 78" class="u"/>
<rect x="30" y="132" width="94" height="24" rx="3" class="pnl"/>
<text x="77.0" y="148.5" text-anchor="middle" class="c">vision</text>
<path d="M24 118 L24 144 L30 144" class="u"/>
<rect x="30" y="162" width="94" height="24" rx="3" class="pnl"/>
<text x="77.0" y="178.5" text-anchor="middle" class="c">SRS</text>
<path d="M24 118 L24 174 L30 174" class="u"/>
<rect x="30" y="192" width="94" height="24" rx="3" class="pnl"/>
<text x="77.0" y="208.5" text-anchor="middle" class="c">stories</text>
<path d="M24 118 L24 204 L30 204" class="u"/>
<rect x="146" y="132" width="94" height="24" rx="3" class="pnl"/>
<text x="193.0" y="148.5" text-anchor="middle" class="c">UML</text>
<path d="M140 118 L140 144 L146 144" class="u"/>
<rect x="146" y="162" width="94" height="24" rx="3" class="pnl"/>
<text x="193.0" y="178.5" text-anchor="middle" class="c">ADRs</text>
<path d="M140 118 L140 174 L146 174" class="u"/>
<rect x="146" y="192" width="94" height="24" rx="3" class="pnl"/>
<text x="193.0" y="208.5" text-anchor="middle" class="c">C4</text>
<path d="M140 118 L140 204 L146 204" class="u"/>
<rect x="262" y="132" width="94" height="24" rx="3" class="pnl"/>
<text x="309.0" y="148.5" text-anchor="middle" class="c">scope, scan</text>
<path d="M256 118 L256 144 L262 144" class="u"/>
<rect x="262" y="162" width="94" height="24" rx="3" class="pnl"/>
<text x="309.0" y="178.5" text-anchor="middle" class="c">fingerprint</text>
<path d="M256 118 L256 174 L262 174" class="u"/>
<rect x="262" y="192" width="94" height="24" rx="3" class="pnl"/>
<text x="309.0" y="208.5" text-anchor="middle" class="c">checks, KB</text>
<path d="M256 118 L256 204 L262 204" class="u"/>
<rect x="262" y="222" width="94" height="24" rx="3" class="pnl"/>
<text x="309.0" y="238.5" text-anchor="middle" class="c">reports</text>
<path d="M256 118 L256 234 L262 234" class="u"/>
<rect x="262" y="252" width="94" height="24" rx="3" class="pnl"/>
<text x="309.0" y="268.5" text-anchor="middle" class="c">history, CLI</text>
<path d="M256 118 L256 264 L262 264" class="u"/>
<rect x="378" y="132" width="94" height="24" rx="3" class="pnl"/>
<text x="425.0" y="148.5" text-anchor="middle" class="c">test plan</text>
<path d="M372 118 L372 144 L378 144" class="u"/>
<rect x="378" y="162" width="94" height="24" rx="3" class="pnl"/>
<text x="425.0" y="178.5" text-anchor="middle" class="c">tests</text>
<path d="M372 118 L372 174 L378 174" class="u"/>
<rect x="378" y="192" width="94" height="24" rx="3" class="pnl"/>
<text x="425.0" y="208.5" text-anchor="middle" class="c">threat model</text>
<path d="M372 118 L372 204 L378 204" class="u"/>
<rect x="494" y="132" width="94" height="24" rx="3" class="pnl"/>
<text x="541.0" y="148.5" text-anchor="middle" class="c">CI</text>
<path d="M488 118 L488 144 L494 144" class="u"/>
<rect x="494" y="162" width="94" height="24" rx="3" class="pnl"/>
<text x="541.0" y="178.5" text-anchor="middle" class="c">container</text>
<path d="M488 118 L488 174 L494 174" class="u"/>
<rect x="494" y="192" width="94" height="24" rx="3" class="pnl"/>
<text x="541.0" y="208.5" text-anchor="middle" class="c">docs</text>
<path d="M488 118 L488 204 L494 204" class="u"/>
<rect x="610" y="132" width="94" height="24" rx="3" class="pnl"/>
<text x="657.0" y="148.5" text-anchor="middle" class="c">plan</text>
<path d="M604 118 L604 144 L610 144" class="u"/>
<rect x="610" y="162" width="94" height="24" rx="3" class="pnl"/>
<text x="657.0" y="178.5" text-anchor="middle" class="c">risks</text>
<path d="M604 118 L604 174 L610 174" class="u"/>
<rect x="610" y="192" width="94" height="24" rx="3" class="pnl"/>
<text x="657.0" y="208.5" text-anchor="middle" class="c">reviews</text>
<path d="M604 118 L604 204 L610 204" class="u"/>
</g>
</svg>
<figcaption>A WBS decomposes deliverables, not activities over time. The 100% rule: the children add up to exactly the parent.</figcaption>
</figure>

A **work breakdown structure** (WBS) decomposes the project's deliverables hierarchically until each piece is small enough to estimate, assign and track. The **100% rule** says the children of each node must cover all of its work and nothing more. In an agile project, the product backlog plays the same role: epics break into stories, stories into tasks.

### Release and sprint planning

NetWarden's release 1.0 was planned as three two-week sprints with a team of three, using the backlog from Chapter 3 (`docs/user-stories.md`):

| Sprint | Goal | Stories | Points |
|---|---|---|---|
| 1 | Safely discover services and identify software | US-1 scope, US-2 discovery, US-3 fingerprint | 3 + 5 + 5 = 13 |
| 2 | Report known vulnerabilities with fixes | US-4 CVEs, US-5 remediation, US-6 HTML report | 8 + 3 + 3 = 14 |
| 3 | Make it operational | US-7 history and diff, US-8 exit codes, US-9 demo targets | 5 + 2 + 3 = 10 |

US-10 (live feed, 13 points) and US-11 (backports, 8 points) stayed in the backlog: **won't have this time**. Each sprint began with planning (what and how), and ended with a review (demo to the security manager) and a retrospective. The release plan was revised after each review.

## Estimation

Estimates are predictions under uncertainty, and the uncertainty is largest exactly when estimates are most wanted, at the start.

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The cone of uncertainty: at the initial concept, actual effort can range from about one quarter to four times an estimate; the range narrows through approved requirements, design and detailed design, and closes only when the software is complete. Estimates should be given as ranges and refined as the project proceeds." xmlns="http://www.w3.org/2000/svg">
<style>
.s16b{ font-family:var(--sans),sans-serif; }
.s16b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16b .s{ fill:var(--text-dim); font-size:13px; }
.s16b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16b .c{ fill:var(--text-faint); font-size:12.5px; }
.s16b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16b-a); }
.s16b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16b-a); marker-start:url(#s16b-s); }
.s16b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16b-g); }
.s16b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16b-a); }
.s16b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16b-tri); }
.s16b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16b-tri); }
.s16b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16b-open); }
.s16b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16b-open); }
.s16b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16b-dia); }
.s16b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16b-odia); }
.s16b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16b-dia); marker-end:url(#s16b-open); }
.s16b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16b-solid); }
.s16b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16b-open); }
.s16b .fill{ fill:var(--text); stroke:none; }
.s16b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s16b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s16b .ks-red{ fill:#A32D2D; font-size:13px; }
.s16b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s16b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s16b .kb-red, :root[data-theme="dark"] .s16b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s16b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s16b .kh-red{ fill:#F09595; }
.s16b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s16b-red); }
.s16b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16b-red); }
.s16b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s16b">
<line x1="80" y1="140.0" x2="690" y2="140.0" class="gd"/>
<path d="M80 40 L210 111 L340 124 L470 133 L600 140" class="ln-red"/>
<path d="M80 240 L210 169 L340 156 L470 147 L600 140" class="ln-red"/>
<circle cx="80" cy="40" r="4" class="k-red"/>
<circle cx="80" cy="240" r="4" class="k-red"/>
<text x="80" y="266" text-anchor="middle" class="c">concept</text>
<circle cx="210" cy="111" r="4" class="k-red"/>
<circle cx="210" cy="169" r="4" class="k-red"/>
<text x="210" y="266" text-anchor="middle" class="c">requirements</text>
<circle cx="340" cy="124" r="4" class="k-red"/>
<circle cx="340" cy="156" r="4" class="k-red"/>
<text x="340" y="266" text-anchor="middle" class="c">design</text>
<circle cx="470" cy="133" r="4" class="k-red"/>
<circle cx="470" cy="147" r="4" class="k-red"/>
<text x="470" y="266" text-anchor="middle" class="c">detail design</text>
<circle cx="600" cy="140" r="4" class="k-red"/>
<circle cx="600" cy="140" r="4" class="k-red"/>
<text x="600" y="266" text-anchor="middle" class="c">complete</text>
<text x="60" y="44.0" text-anchor="end" class="m">4x</text>
<text x="60" y="244.0" text-anchor="end" class="m">0.25x</text>
<text x="60" y="144.0" text-anchor="end" class="m">1x</text>
<text x="360" y="40" text-anchor="middle" class="c">actual effort relative to the estimate</text>
</g>
</svg>
<figcaption>From Boehm, popularised by McConnell. Early estimates are guesses with error bars; treat them that way.</figcaption>
</figure>

Good practice: estimate in **ranges**, re-estimate as you learn, use **several methods** and compare them, and never let an estimate be silently turned into a commitment.

| Technique | How | Best for |
|---|---|---|
| **Expert judgement** | Experienced people estimate | Quick, early estimates |
| **Analogy** | Compare with similar past work | Organisations with historical data |
| **Decomposition** (bottom-up) | Estimate small pieces of the WBS and add them | Detailed plans; finds forgotten work |
| **Three-point** (PERT) | Optimistic O, most likely M, pessimistic P; estimate = (O + 4M + P) / 6 | Expressing uncertainty |
| **Wideband Delphi, planning poker** | Independent estimates, discussion, re-estimate | Team estimates of stories |
| **Parametric models** (COCOMO, function points) | Formula from size and cost drivers | Large projects; cross-checks |

### Story points and planning poker

Agile teams often estimate **relative size** in **story points** rather than hours: a 5-point story is about as big as other 5-point stories, and bigger than a 3. Size includes effort, complexity and uncertainty.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Planning poker for user story US-7. Each developer privately picks a card from the modified Fibonacci sequence 1, 2, 3, 5, 8, 13, 20 and 40; all reveal at once. Estimates of 3, 5, 5 and 13 differ, so the highest and lowest estimators explain their reasoning and the team votes again, converging on 5." xmlns="http://www.w3.org/2000/svg">
<style>
.s16d{ font-family:var(--sans),sans-serif; }
.s16d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16d .s{ fill:var(--text-dim); font-size:13px; }
.s16d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16d .c{ fill:var(--text-faint); font-size:12.5px; }
.s16d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16d-a); }
.s16d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16d-a); marker-start:url(#s16d-s); }
.s16d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16d-g); }
.s16d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16d-a); }
.s16d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16d-tri); }
.s16d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16d-tri); }
.s16d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16d-open); }
.s16d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16d-open); }
.s16d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16d-dia); }
.s16d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16d-odia); }
.s16d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16d-dia); marker-end:url(#s16d-open); }
.s16d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16d-solid); }
.s16d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16d-open); }
.s16d .fill{ fill:var(--text); stroke:none; }
.s16d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s16d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s16d .ks-amber{ fill:#854F0B; font-size:13px; }
.s16d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s16d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s16d .kb-amber, :root[data-theme="dark"] .s16d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s16d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s16d .kh-amber{ fill:#EF9F27; }
.s16d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s16d-amber); }
.s16d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16d-amber); }
.s16d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s16d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s16d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s16d .ks-red{ fill:#A32D2D; font-size:13px; }
.s16d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s16d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s16d .kb-red, :root[data-theme="dark"] .s16d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s16d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s16d .kh-red{ fill:#F09595; }
.s16d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s16d-red); }
.s16d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16d-red); }
.s16d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s16d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s16d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s16d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s16d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s16d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s16d .kb-gray, :root[data-theme="dark"] .s16d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s16d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s16d .kh-gray{ fill:#B4B2A9; }
.s16d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s16d-gray); }
.s16d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16d-gray); }
.s16d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s16d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s16d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s16d">
<rect x="20" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="52.0" y="66.5" text-anchor="middle" class="kb-amber">1</text>
<rect x="96" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="128.0" y="66.5" text-anchor="middle" class="kb-amber">2</text>
<rect x="172" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="204.0" y="66.5" text-anchor="middle" class="kb-amber">3</text>
<rect x="248" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="280.0" y="66.5" text-anchor="middle" class="kb-amber">5</text>
<rect x="324" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="356.0" y="66.5" text-anchor="middle" class="kb-amber">8</text>
<rect x="400" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="432.0" y="66.5" text-anchor="middle" class="kb-amber">13</text>
<rect x="476" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="508.0" y="66.5" text-anchor="middle" class="kb-amber">20</text>
<rect x="552" y="20" width="64" height="84" rx="6" class="k-amber"/>
<text x="584.0" y="66.5" text-anchor="middle" class="kb-amber">40</text>
<rect x="628" y="20" width="64" height="84" rx="6" class="k-gray"/>
<text x="660.0" y="66.5" text-anchor="middle" class="kb-gray">?</text>
<text x="20" y="140" text-anchor="start" class="b">US-7 compare two scans, round 1:</text>
<rect x="270" y="124" width="80" height="30" rx="4" class="k-red"/>
<text x="310.0" y="143.5" text-anchor="middle" class="ks-red">Ana: 3</text>
<rect x="360" y="124" width="80" height="30" rx="4" class="pnl"/>
<text x="400.0" y="143.5" text-anchor="middle" class="s">Ben: 5</text>
<rect x="450" y="124" width="80" height="30" rx="4" class="pnl"/>
<text x="490.0" y="143.5" text-anchor="middle" class="s">Chen: 5</text>
<rect x="540" y="124" width="80" height="30" rx="4" class="k-red"/>
<text x="580.0" y="143.5" text-anchor="middle" class="ks-red">Dev: 13</text>
<text x="20" y="190" text-anchor="start" class="b">Ana and Dev explain; round 2: 5, 5, 5, 8  -&gt;  5 points</text>
<text x="20" y="226" text-anchor="start" class="c">relative sizes in story points; the discussion matters more than the number</text>
</g>
</svg>
<figcaption>Wideband Delphi, gamified: independent estimates avoid anchoring, and disagreement surfaces hidden assumptions.</figcaption>
</figure>

The value of planning poker is the conversation when estimates differ. In the example, Ana assumed `diff` would reuse the scan comparison logic; Dev knew that `ScanRepository.get()` did not exist yet and that findings needed a stable identity, the `Finding.key` property. One discussion surfaced a hidden piece of work before the sprint, not during it.

### A parametric cross-check

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Basic COCOMO for NetWarden, organic mode. Effort in person-months equals 2.4 times size in thousands of lines to the power 1.05; with 0.9 thousand lines, effort is about 2.2 person-months. Schedule in months equals 2.5 times effort to the power 0.38, about 3.4 months. The model was calibrated on 1970s projects, so treat the result as a rough cross-check only." xmlns="http://www.w3.org/2000/svg">
<style>
.s16e{ font-family:var(--sans),sans-serif; }
.s16e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16e .s{ fill:var(--text-dim); font-size:13px; }
.s16e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16e .c{ fill:var(--text-faint); font-size:12.5px; }
.s16e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16e-a); }
.s16e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16e-a); marker-start:url(#s16e-s); }
.s16e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16e-g); }
.s16e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16e-a); }
.s16e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16e-tri); }
.s16e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16e-tri); }
.s16e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16e-open); }
.s16e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16e-open); }
.s16e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16e-dia); }
.s16e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16e-odia); }
.s16e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16e-dia); marker-end:url(#s16e-open); }
.s16e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16e-solid); }
.s16e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16e-open); }
.s16e .fill{ fill:var(--text); stroke:none; }
.s16e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s16e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s16e .ks-blue{ fill:#185FA5; font-size:13px; }
.s16e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s16e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s16e .kb-blue, :root[data-theme="dark"] .s16e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s16e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s16e .kh-blue{ fill:#85B7EB; }
.s16e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s16e-blue); }
.s16e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16e-blue); }
.s16e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s16e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s16e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s16e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s16e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s16e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s16e .kb-teal, :root[data-theme="dark"] .s16e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s16e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s16e .kh-teal{ fill:#5DCAA5; }
.s16e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s16e-teal); }
.s16e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16e-teal); }
.s16e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s16e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s16e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s16e .ks-red{ fill:#A32D2D; font-size:13px; }
.s16e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s16e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s16e .kb-red, :root[data-theme="dark"] .s16e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s16e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s16e .kh-red{ fill:#F09595; }
.s16e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s16e-red); }
.s16e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16e-red); }
.s16e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s16e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s16e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s16e">
<rect x="20" y="20" width="330" height="90" rx="7" class="k-blue"/>
<text x="185.0" y="47.5" text-anchor="middle" class="km-blue">effort = 2.4 x KLOC^1.05</text>
<text x="185.0" y="69.5" text-anchor="middle" class="km-blue">= 2.4 x 0.9^1.05</text>
<text x="185.0" y="91.5" text-anchor="middle" class="kb-blue">~ 2.2 person-months</text>
<rect x="370" y="20" width="330" height="90" rx="7" class="k-teal"/>
<text x="535.0" y="47.5" text-anchor="middle" class="km-teal">schedule = 2.5 x effort^0.38</text>
<text x="535.0" y="69.5" text-anchor="middle" class="km-teal">= 2.5 x 2.2^0.38</text>
<text x="535.0" y="91.5" text-anchor="middle" class="kb-teal">~ 3.4 months</text>
<text x="360" y="150" text-anchor="middle" class="c">basic COCOMO (Boehm, 1981), organic mode; COCOMO II adds cost drivers and scale factors</text>
<text x="360" y="178" text-anchor="middle" class="c">NetWarden's plan: three people x three 2-week sprints = 4.5 person-months, including docs and process</text>
<text x="360" y="206" text-anchor="middle" class="kh-red">different methods disagree: that is useful information, not a failure</text>
</g>
</svg>
<figcaption>Parametric models turn size into effort. They need calibration with your own historical data to be trustworthy.</figcaption>
</figure>

Barry Boehm's **COCOMO** (Constructive Cost Model, 1981; COCOMO II, 2000) estimates effort from size. Applied to NetWarden's code size, the basic model gives roughly two person-months over about three months. The team's actual plan was larger, because it also produced requirements, models, documentation and a pipeline, which a model calibrated on code size does not see. The disagreement is the useful result: it prompts the question "what is in our plan that the model does not count, and vice versa?"

## Scheduling

Plan-driven projects schedule work with **Gantt charts** and **network diagrams**.

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Critical path network for a plan-driven version of NetWarden 1.0. Tasks with durations in days: A requirements 3, B architecture 2 after A, C scanner 4 after B, D checks and knowledge base 5 after B, E reports 3 after D, F CI pipeline 2 after B, G integration testing 2 after C, E and F, H release 1 after G. The critical path A, B, D, E, G, H takes 16 days; C has 4 days of slack and F 6 days." xmlns="http://www.w3.org/2000/svg">
<style>
.s16h{ font-family:var(--sans),sans-serif; }
.s16h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16h .s{ fill:var(--text-dim); font-size:13px; }
.s16h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16h .c{ fill:var(--text-faint); font-size:12.5px; }
.s16h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16h-a); }
.s16h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16h-a); marker-start:url(#s16h-s); }
.s16h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16h-g); }
.s16h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16h-a); }
.s16h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16h-tri); }
.s16h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16h-tri); }
.s16h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16h-open); }
.s16h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16h-open); }
.s16h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16h-dia); }
.s16h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16h-odia); }
.s16h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16h-dia); marker-end:url(#s16h-open); }
.s16h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16h-solid); }
.s16h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16h-open); }
.s16h .fill{ fill:var(--text); stroke:none; }
.s16h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s16h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s16h .ks-blue{ fill:#185FA5; font-size:13px; }
.s16h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s16h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s16h .kb-blue, :root[data-theme="dark"] .s16h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s16h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s16h .kh-blue{ fill:#85B7EB; }
.s16h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s16h-blue); }
.s16h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16h-blue); }
.s16h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s16h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s16h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s16h .ks-red{ fill:#A32D2D; font-size:13px; }
.s16h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s16h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s16h .kb-red, :root[data-theme="dark"] .s16h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s16h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s16h .kh-red{ fill:#F09595; }
.s16h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s16h-red); }
.s16h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16h-red); }
.s16h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s16h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s16h">
<rect x="20" y="130" width="96" height="70" rx="4" class="k-red"/>
<text x="68.0" y="149.5" text-anchor="middle" class="kb-red">A: 3 days</text>
<text x="68.0" y="169.5" text-anchor="middle" class="ks-red">requirements</text>
<text x="68.0" y="189.5" text-anchor="middle" class="ks-red">critical</text>
<rect x="130" y="130" width="96" height="70" rx="4" class="k-red"/>
<text x="178.0" y="149.5" text-anchor="middle" class="kb-red">B: 2 days</text>
<text x="178.0" y="169.5" text-anchor="middle" class="ks-red">architecture</text>
<text x="178.0" y="189.5" text-anchor="middle" class="ks-red">critical</text>
<rect x="260" y="30" width="96" height="70" rx="4" class="k-blue"/>
<text x="308.0" y="49.5" text-anchor="middle" class="kb-blue">C: 4 days</text>
<text x="308.0" y="69.5" text-anchor="middle" class="ks-blue">scanner</text>
<text x="308.0" y="89.5" text-anchor="middle" class="ks-blue">slack 4</text>
<rect x="260" y="130" width="96" height="70" rx="4" class="k-red"/>
<text x="308.0" y="149.5" text-anchor="middle" class="kb-red">D: 5 days</text>
<text x="308.0" y="169.5" text-anchor="middle" class="ks-red">checks + KB</text>
<text x="308.0" y="189.5" text-anchor="middle" class="ks-red">critical</text>
<rect x="380" y="130" width="96" height="70" rx="4" class="k-red"/>
<text x="428.0" y="149.5" text-anchor="middle" class="kb-red">E: 3 days</text>
<text x="428.0" y="169.5" text-anchor="middle" class="ks-red">reports</text>
<text x="428.0" y="189.5" text-anchor="middle" class="ks-red">critical</text>
<rect x="260" y="230" width="96" height="70" rx="4" class="k-blue"/>
<text x="308.0" y="249.5" text-anchor="middle" class="kb-blue">F: 2 days</text>
<text x="308.0" y="269.5" text-anchor="middle" class="ks-blue">CI</text>
<text x="308.0" y="289.5" text-anchor="middle" class="ks-blue">slack 6</text>
<rect x="500" y="130" width="96" height="70" rx="4" class="k-red"/>
<text x="548.0" y="149.5" text-anchor="middle" class="kb-red">G: 2 days</text>
<text x="548.0" y="169.5" text-anchor="middle" class="ks-red">integration</text>
<text x="548.0" y="189.5" text-anchor="middle" class="ks-red">critical</text>
<rect x="610" y="130" width="96" height="70" rx="4" class="k-red"/>
<text x="658.0" y="149.5" text-anchor="middle" class="kb-red">H: 1 day</text>
<text x="658.0" y="169.5" text-anchor="middle" class="ks-red">release</text>
<text x="658.0" y="189.5" text-anchor="middle" class="ks-red">critical</text>
<line x1="118" y1="165" x2="128" y2="165" class="ar-red"/>
<line x1="228" y1="165" x2="258" y2="65" class="ar"/>
<line x1="228" y1="165" x2="258" y2="165" class="ar-red"/>
<line x1="228" y1="165" x2="258" y2="265" class="ar"/>
<line x1="358" y1="165" x2="378" y2="165" class="ar-red"/>
<line x1="358" y1="65" x2="498" y2="165" class="ar"/>
<line x1="478" y1="165" x2="498" y2="165" class="ar-red"/>
<line x1="358" y1="265" x2="498" y2="165" class="ar"/>
<line x1="598" y1="165" x2="608" y2="165" class="ar-red"/>
<text x="360" y="318" text-anchor="middle" class="kh-red">critical path A-B-D-E-G-H = 16 days: any delay on it delays the release</text>
</g>
</svg>
<figcaption>The critical path method finds the chain of tasks with zero slack. Managing a project means watching that chain.</figcaption>
</figure>

The **critical path method** (CPM) computes the earliest start of each task from its dependencies and finds the longest path through the network. Tasks on the **critical path** have zero **slack**: any delay to them delays the whole project. Tasks off the path can slip by their slack without harm. Managers watch the critical path, put their strongest people on it, and look for ways to shorten it by running tasks in parallel. Agile teams avoid most of this complexity by planning short, fixed-length sprints, but dependencies between teams still need managing, often on a shared roadmap or **program board**.

## Tracking progress

### Agile tracking

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Release burn-up chart for NetWarden 1.0. The scope line stays at 37 story points. Completed work rises to 13 points after sprint 1, 27 after sprint 2 and 37 after sprint 3. Velocity per sprint was 13, 14 and 10 points." xmlns="http://www.w3.org/2000/svg">
<style>
.s16f{ font-family:var(--sans),sans-serif; }
.s16f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16f .s{ fill:var(--text-dim); font-size:13px; }
.s16f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16f .c{ fill:var(--text-faint); font-size:12.5px; }
.s16f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16f-a); }
.s16f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16f-a); marker-start:url(#s16f-s); }
.s16f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16f-g); }
.s16f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16f-a); }
.s16f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16f-tri); }
.s16f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16f-tri); }
.s16f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16f-open); }
.s16f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16f-open); }
.s16f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16f-dia); }
.s16f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16f-odia); }
.s16f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16f-dia); marker-end:url(#s16f-open); }
.s16f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16f-solid); }
.s16f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16f-open); }
.s16f .fill{ fill:var(--text); stroke:none; }
.s16f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s16f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s16f .ks-blue{ fill:#185FA5; font-size:13px; }
.s16f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s16f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s16f .kb-blue, :root[data-theme="dark"] .s16f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s16f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s16f .kh-blue{ fill:#85B7EB; }
.s16f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s16f-blue); }
.s16f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16f-blue); }
.s16f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s16f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s16f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s16f .ks-green{ fill:#3B6D11; font-size:13px; }
.s16f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s16f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s16f .kb-green, :root[data-theme="dark"] .s16f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s16f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s16f .kh-green{ fill:#97C459; }
.s16f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s16f-green); }
.s16f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16f-green); }
.s16f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s16f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s16f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s16f .ks-red{ fill:#A32D2D; font-size:13px; }
.s16f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s16f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s16f .kb-red, :root[data-theme="dark"] .s16f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s16f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s16f .kh-red{ fill:#F09595; }
.s16f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s16f-red); }
.s16f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16f-red); }
.s16f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s16f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s16f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s16f">
<line x1="80" y1="250" x2="500" y2="250" class="ar"/>
<line x1="80" y1="250" x2="80" y2="20" class="ar"/>
<text x="80.0" y="270" text-anchor="middle" class="c">start</text>
<text x="213.33333333333334" y="270" text-anchor="middle" class="c">S1</text>
<text x="346.6666666666667" y="270" text-anchor="middle" class="c">S2</text>
<text x="480.0" y="270" text-anchor="middle" class="c">S3</text>
<text x="72" y="199.0" text-anchor="end" class="c">10</text>
<line x1="80" y1="195.0" x2="480" y2="195.0" class="gd"/>
<text x="72" y="144.0" text-anchor="end" class="c">20</text>
<line x1="80" y1="140.0" x2="480" y2="140.0" class="gd"/>
<text x="72" y="89.0" text-anchor="end" class="c">30</text>
<line x1="80" y1="85.0" x2="480" y2="85.0" class="gd"/>
<text x="72" y="34.0" text-anchor="end" class="c">40</text>
<line x1="80" y1="30.0" x2="480" y2="30.0" class="gd"/>
<line x1="80.0" y1="46.5" x2="480.0" y2="46.5" class="ln-red"/>
<text x="486.0" y="50.5" text-anchor="start" class="kh-red">scope 37</text>
<path d="M80 250 L213 178 L347 102 L480 46" class="ln-green"/>
<circle cx="80" cy="250" r="4" class="k-green"/>
<circle cx="213" cy="178" r="4" class="k-green"/>
<circle cx="347" cy="102" r="4" class="k-green"/>
<circle cx="480" cy="46" r="4" class="k-green"/>
<text x="356.6666666666667" y="117.5" text-anchor="start" class="kh-green">done</text>
<text x="600" y="40" text-anchor="middle" class="b">velocity</text>
<rect x="540" y="100" width="36" height="130" rx="2" class="k-blue"/>
<text x="558" y="94" text-anchor="middle" class="c">13</text>
<text x="558" y="248" text-anchor="middle" class="c">S1</text>
<rect x="590" y="90" width="36" height="140" rx="2" class="k-blue"/>
<text x="608" y="84" text-anchor="middle" class="c">14</text>
<text x="608" y="248" text-anchor="middle" class="c">S2</text>
<rect x="640" y="130" width="36" height="100" rx="2" class="k-blue"/>
<text x="658" y="124" text-anchor="middle" class="c">10</text>
<text x="658" y="248" text-anchor="middle" class="c">S3</text>
</g>
</svg>
<figcaption>Burn-up charts show both progress and scope changes. Velocity is for planning, never for comparing teams.</figcaption>
</figure>

**Velocity**, the number of points completed per sprint, measures a team's capacity. After three sprints NetWarden's average velocity was about 12 points, so the 21 points remaining in the backlog (US-10 and US-11) forecast about two more sprints. A **burn-up** chart shows completed work against total scope; when scope grows, the scope line rises, which a burn-down chart hides.

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Sprint 2 burn-down chart. The ideal line falls from 14 points to zero over ten working days. The actual line stays flat for the first three days while US-4 is in progress, drops when stories are finished, and reaches zero on day 10." xmlns="http://www.w3.org/2000/svg">
<style>
.s16g{ font-family:var(--sans),sans-serif; }
.s16g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16g .s{ fill:var(--text-dim); font-size:13px; }
.s16g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16g .c{ fill:var(--text-faint); font-size:12.5px; }
.s16g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16g-a); }
.s16g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16g-a); marker-start:url(#s16g-s); }
.s16g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16g-g); }
.s16g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16g-a); }
.s16g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16g-tri); }
.s16g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16g-tri); }
.s16g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16g-open); }
.s16g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16g-open); }
.s16g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16g-dia); }
.s16g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16g-odia); }
.s16g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16g-dia); marker-end:url(#s16g-open); }
.s16g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16g-solid); }
.s16g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16g-open); }
.s16g .fill{ fill:var(--text); stroke:none; }
.s16g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16g .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s16g .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s16g .ks-coral{ fill:#993C1D; font-size:13px; }
.s16g .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s16g .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16g .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s16g .kb-coral, :root[data-theme="dark"] .s16g .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s16g .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s16g .kh-coral{ fill:#F0997B; }
.s16g .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s16g-coral); }
.s16g .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16g-coral); }
.s16g .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s16g .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s16g .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s16g .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s16g .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s16g .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16g .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s16g .kb-gray, :root[data-theme="dark"] .s16g .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s16g .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s16g .kh-gray{ fill:#B4B2A9; }
.s16g .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s16g-gray); }
.s16g .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16g-gray); }
.s16g .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16g-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s16g-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s16g">
<line x1="70" y1="240" x2="650" y2="240" class="ar"/>
<line x1="70" y1="240" x2="70" y2="28" class="ar"/>
<text x="70.0" y="258" text-anchor="middle" class="c">day 0</text>
<text x="182.0" y="258" text-anchor="middle" class="c">day 2</text>
<text x="294.0" y="258" text-anchor="middle" class="c">day 4</text>
<text x="406.0" y="258" text-anchor="middle" class="c">day 6</text>
<text x="518.0" y="258" text-anchor="middle" class="c">day 8</text>
<text x="630.0" y="258" text-anchor="middle" class="c">day 10</text>
<text x="62" y="244.0" text-anchor="end" class="c">0</text>
<text x="62" y="144.0" text-anchor="end" class="c">7</text>
<text x="62" y="44.0" text-anchor="end" class="c">14</text>
<line x1="70.0" y1="40.0" x2="630.0" y2="240.0" class="ad-gray"/>
<text x="316.4" y="118.57142857142857" text-anchor="start" class="kh-gray">ideal</text>
<path d="M70 40 L126 40 L182 40 L238 40 L294 154 L350 154 L406 154 L462 197 L518 197 L574 240 L630 240" class="ln-coral"/>
<text x="700" y="30" text-anchor="end" class="kh-coral">drops: day 4 US-4 (8), day 7 US-5 (3), day 9 US-6 (3)</text>
</g>
</svg>
<figcaption>Flat stretches mean work in progress but nothing finished: a hint to swarm on fewer stories at once.</figcaption>
</figure>

Within a sprint, a **burn-down** chart shows remaining work day by day. Its shape tells a story: long flat stretches mean many stories in progress and none finished, a signal to limit work in progress (Chapter 2).

Velocity is a planning tool for one team. Comparing velocities between teams is meaningless, because points are relative to each team, and using velocity as a performance target leads to point inflation (Goodhart's law, Chapter 12).

### Plan-driven tracking

**Earned value management** (EVM) compares three numbers at each reporting date: the **planned value** (budgeted cost of work scheduled), the **earned value** (budgeted cost of work actually completed) and the **actual cost**. The **schedule performance index** SPI = EV / PV and **cost performance index** CPI = EV / AC show whether the project is behind schedule or over budget. If, after three weeks, NetWarden had completed work budgeted at 9 person-days of the 12 planned, at an actual cost of 10 person-days, then SPI = 0.75 (behind schedule) and CPI = 0.9 (over budget).

## Risk management

A **risk** is an uncertain event that, if it happens, affects the project's objectives. Risk management is proactive: it deals with problems before they occur.

1. **Identify** risks: brainstorming, checklists, assumptions, lessons from past projects.
2. **Analyse**: estimate probability and impact; **exposure** = probability x impact.
3. **Plan responses**: **avoid** (change the plan so the risk cannot occur), **transfer** (insurance, contracts), **mitigate** (reduce probability or impact), or **accept** (with a contingency plan).
4. **Monitor**: review the register regularly; watch for triggers; add new risks.

<figure class="diagram">
<svg viewBox="0 0 720 336" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Risk matrix with NetWarden&#x27;s risks plotted by probability and impact on a one to five scale: R1 unauthorised use, probability 2, impact 5; R2 false positives from backports, 4 and 3; R3 outdated knowledge base, 5 and 3; R4 disrupting fragile devices, 2 and 4; R5 losing a key developer, 2 and 3; R6 scope creep, 3 and 3. Cells are coloured from green for low exposure to red for high." xmlns="http://www.w3.org/2000/svg">
<style>
.s16i{ font-family:var(--sans),sans-serif; }
.s16i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s16i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s16i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s16i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s16i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s16i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s16i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s16i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s16i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s16i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s16i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s16i .s{ fill:var(--text-dim); font-size:13px; }
.s16i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s16i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s16i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s16i .c{ fill:var(--text-faint); font-size:12.5px; }
.s16i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s16i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s16i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s16i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16i-a); }
.s16i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s16i-a); marker-start:url(#s16i-s); }
.s16i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s16i-g); }
.s16i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s16i-a); }
.s16i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s16i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s16i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s16i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s16i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s16i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16i-tri); }
.s16i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16i-tri); }
.s16i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16i-open); }
.s16i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s16i-open); }
.s16i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16i-dia); }
.s16i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16i-odia); }
.s16i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s16i-dia); marker-end:url(#s16i-open); }
.s16i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s16i-solid); }
.s16i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s16i-open); }
.s16i .fill{ fill:var(--text); stroke:none; }
.s16i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s16i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s16i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s16i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s16i .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s16i .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s16i .ks-amber{ fill:#854F0B; font-size:13px; }
.s16i .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s16i .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16i .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s16i .kb-amber, :root[data-theme="dark"] .s16i .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s16i .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s16i .kh-amber{ fill:#EF9F27; }
.s16i .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s16i-amber); }
.s16i .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16i-amber); }
.s16i .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s16i .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s16i .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s16i .ks-green{ fill:#3B6D11; font-size:13px; }
.s16i .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s16i .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16i .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s16i .kb-green, :root[data-theme="dark"] .s16i .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s16i .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s16i .kh-green{ fill:#97C459; }
.s16i .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s16i-green); }
.s16i .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16i-green); }
.s16i .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s16i .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s16i .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s16i .ks-red{ fill:#A32D2D; font-size:13px; }
.s16i .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s16i .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s16i .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s16i .kb-red, :root[data-theme="dark"] .s16i .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s16i .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s16i .kh-red{ fill:#F09595; }
.s16i .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s16i-red); }
.s16i .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s16i-red); }
.s16i .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s16i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s16i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s16i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s16i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s16i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s16i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s16i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s16i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s16i-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s16i-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s16i-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s16i">
<rect x="110" y="20" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="162" y="20" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="214" y="20" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="266" y="20" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="318" y="20" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="110" y="72" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="162" y="72" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="214" y="72" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="266" y="72" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="318" y="72" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="110" y="124" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="162" y="124" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="214" y="124" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="266" y="124" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="318" y="124" width="50" height="50" rx="3" class="k-red" style="fill-opacity:0.6"/>
<rect x="110" y="176" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="162" y="176" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="214" y="176" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="266" y="176" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="318" y="176" width="50" height="50" rx="3" class="k-amber" style="fill-opacity:0.6"/>
<rect x="110" y="228" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="162" y="228" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="214" y="228" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="266" y="228" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<rect x="318" y="228" width="50" height="50" rx="3" class="k-green" style="fill-opacity:0.6"/>
<text x="136.0" y="296" text-anchor="middle" class="c">1</text>
<text x="100" y="258.0" text-anchor="end" class="c">1</text>
<text x="188.0" y="296" text-anchor="middle" class="c">2</text>
<text x="100" y="206.0" text-anchor="end" class="c">2</text>
<text x="240.0" y="296" text-anchor="middle" class="c">3</text>
<text x="100" y="154.0" text-anchor="end" class="c">3</text>
<text x="292.0" y="296" text-anchor="middle" class="c">4</text>
<text x="100" y="102.0" text-anchor="end" class="c">4</text>
<text x="344.0" y="296" text-anchor="middle" class="c">5</text>
<text x="100" y="50.0" text-anchor="end" class="c">5</text>
<text x="240.0" y="316" text-anchor="middle" class="c">impact</text>
<text x="70" y="150.0" text-anchor="end" class="c">probability</text>
<rect x="324" y="188" width="38" height="24" rx="10" class="pnl"/>
<text x="343.0" y="204.5" text-anchor="middle" class="b">R1</text>
<rect x="220" y="84" width="38" height="24" rx="10" class="pnl"/>
<text x="239.0" y="100.5" text-anchor="middle" class="b">R2</text>
<rect x="220" y="32" width="38" height="24" rx="10" class="pnl"/>
<text x="239.0" y="48.5" text-anchor="middle" class="b">R3</text>
<rect x="272" y="188" width="38" height="24" rx="10" class="pnl"/>
<text x="291.0" y="204.5" text-anchor="middle" class="b">R4</text>
<rect x="220" y="188" width="38" height="24" rx="10" class="pnl"/>
<text x="239.0" y="204.5" text-anchor="middle" class="b">R5</text>
<rect x="220" y="136" width="38" height="24" rx="10" class="pnl"/>
<text x="239.0" y="152.5" text-anchor="middle" class="b">R6</text>
<text x="400" y="34" text-anchor="start" class="b">R1 unauthorised use</text>
<text x="400" y="52" text-anchor="start" class="c">avoid: scope enforcement</text>
<text x="400" y="78" text-anchor="start" class="b">R2 backport false positives</text>
<text x="400" y="96" text-anchor="start" class="c">mitigate: US-11</text>
<text x="400" y="122" text-anchor="start" class="b">R3 outdated knowledge</text>
<text x="400" y="140" text-anchor="start" class="c">mitigate: live feed US-10</text>
<text x="400" y="166" text-anchor="start" class="b">R4 fragile devices</text>
<text x="400" y="184" text-anchor="start" class="c">mitigate: limits, windows</text>
<text x="400" y="210" text-anchor="start" class="b">R5 key person leaves</text>
<text x="400" y="228" text-anchor="start" class="c">mitigate: pairing, docs</text>
<text x="400" y="254" text-anchor="start" class="b">R6 scope creep</text>
<text x="400" y="272" text-anchor="start" class="c">avoid: non-goals</text>
</g>
</svg>
<figcaption>Exposure = probability x impact. Responses: avoid, transfer, mitigate, or accept, and review the register every sprint.</figcaption>
</figure>

NetWarden's risk register (`docs/risk-register.md`) has six risks. The highest exposure, an outdated knowledge base, is mitigated by a backlog item; the one with the highest impact, unauthorised use, is avoided by design through scope enforcement. Note that several risk responses became **requirements**: risk management and requirements engineering feed each other.

## People and communication

Projects are delivered by people, so management is mostly about communication:

- **Stakeholder communication** matched to the power and interest grid (Chapter 3): weekly demos for the security manager, a monthly summary for the IT director.
- **Transparency**: a visible board, burn-up chart and risk register, so problems surface early.
- **Sustainable pace**: overtime as a habit reduces quality and increases turnover, the risk R5 in the register.
- **Escalation**: agree in advance how decisions beyond the team's authority are made.

## Why projects fail

The causes in the literature repeat: unclear or changing requirements without change control, unrealistic estimates turned into commitments, lack of user involvement, poor risk management, weak sponsorship, and technical debt that slows everything. Most of them are visible early to anyone who looks. The practices in this chapter, short iterations, visible progress, honest estimates, and a living risk register, exist so that someone does look.

## Hands on

1. Estimate US-10 (live vulnerability feed) using a three-point estimate in days. Compare with the 13 story points the team gave it.
2. Redraw the critical path network if the reports task (E) takes 5 days instead of 3. What is the new project length? What if instead the scanner (C) takes 8 days?
3. Add a risk to NetWarden's register: a new operating system release changes its SSH banner format. Estimate probability and impact and choose a response.

## Summary

- Projects balance **scope, time, cost** and **quality**; agile fixes time and cost and varies scope.
- Plan with a **WBS** or **backlog**, and in **releases and sprints**.
- Estimate in **ranges** with several techniques; early estimates sit in the **cone of uncertainty**. **Story points** and **planning poker** make team estimation quick and surface assumptions; **COCOMO** provides a parametric cross-check.
- Schedule with **critical path** analysis in plan-driven projects; agile teams use fixed sprints.
- Track with **velocity, burn-up and burn-down** charts, or **earned value**; never use velocity to compare teams.
- Manage **risks** proactively: identify, analyse exposure, respond (avoid, transfer, mitigate, accept), monitor.
- Most project failures are visible early to anyone who keeps progress and risks transparent.
