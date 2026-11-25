# Chapter 7: Software Architecture

**Software architecture** is the set of structures needed to reason about a system: its elements, the relations between them, and their properties (Bass, Clements and Kazman, *Software Architecture in Practice*). Martin Fowler's shorter version is that architecture is "the important stuff, whatever that is", meaning the decisions that are expensive to change later. Chapter 5 was about principles for any piece of design; this chapter is about the large-scale shape of a system and how to choose it deliberately.

## What drives architecture

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Architecture drivers. Functional requirements, quality attribute requirements, constraints and the team&#x27;s context feed the architecture, which is a set of structures plus the decisions and rationale behind them. Quality attributes such as performance, security and modifiability shape it most." xmlns="http://www.w3.org/2000/svg">
<style>
.s7a{ font-family:var(--sans),sans-serif; }
.s7a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7a .s{ fill:var(--text-dim); font-size:13px; }
.s7a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .c{ fill:var(--text-faint); font-size:12.5px; }
.s7a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7a-a); }
.s7a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7a-a); marker-start:url(#s7a-s); }
.s7a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7a-g); }
.s7a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-a); }
.s7a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7a-tri); }
.s7a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-tri); }
.s7a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7a-open); }
.s7a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-open); }
.s7a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7a-dia); }
.s7a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7a-odia); }
.s7a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7a-dia); marker-end:url(#s7a-open); }
.s7a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7a-solid); }
.s7a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7a-open); }
.s7a .fill{ fill:var(--text); stroke:none; }
.s7a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s7a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s7a .ks-blue{ fill:#185FA5; font-size:13px; }
.s7a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s7a .kb-blue, :root[data-theme="dark"] .s7a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s7a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s7a .kh-blue{ fill:#85B7EB; }
.s7a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s7a-blue); }
.s7a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-blue); }
.s7a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s7a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7a .kb-teal, :root[data-theme="dark"] .s7a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7a .kh-teal{ fill:#5DCAA5; }
.s7a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7a-teal); }
.s7a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-teal); }
.s7a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7a .ks-amber{ fill:#854F0B; font-size:13px; }
.s7a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7a .kb-amber, :root[data-theme="dark"] .s7a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7a .kh-amber{ fill:#EF9F27; }
.s7a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7a-amber); }
.s7a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-amber); }
.s7a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7a .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s7a .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s7a .ks-coral{ fill:#993C1D; font-size:13px; }
.s7a .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7a .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s7a .kb-coral, :root[data-theme="dark"] .s7a .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s7a .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s7a .kh-coral{ fill:#F0997B; }
.s7a .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s7a-coral); }
.s7a .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-coral); }
.s7a .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s7a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7a .ks-purple{ fill:#534AB7; font-size:13px; }
.s7a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7a .kb-purple, :root[data-theme="dark"] .s7a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7a .kh-purple{ fill:#AFA9EC; }
.s7a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7a-purple); }
.s7a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-purple); }
.s7a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s7a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s7a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s7a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s7a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s7a .kb-gray, :root[data-theme="dark"] .s7a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s7a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s7a .kh-gray{ fill:#B4B2A9; }
.s7a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s7a-gray); }
.s7a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7a-gray); }
.s7a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s7a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s7a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s7a">
<rect x="20" y="16" width="230" height="48" rx="7" class="k-blue"/>
<text x="135.0" y="35.5" text-anchor="middle" class="kb-blue">functional requirements</text>
<text x="135.0" y="53.5" text-anchor="middle" class="ks-blue">what it must do</text>
<line x1="252" y1="40" x2="318" y2="125" class="ar"/>
<rect x="20" y="74" width="230" height="48" rx="7" class="k-coral"/>
<text x="135.0" y="93.5" text-anchor="middle" class="kb-coral">quality attributes</text>
<text x="135.0" y="111.5" text-anchor="middle" class="ks-coral">how well: the big shapers</text>
<line x1="252" y1="98" x2="318" y2="125" class="ar"/>
<rect x="20" y="132" width="230" height="48" rx="7" class="k-gray"/>
<text x="135.0" y="151.5" text-anchor="middle" class="kb-gray">constraints</text>
<text x="135.0" y="169.5" text-anchor="middle" class="ks-gray">language, budget, law</text>
<line x1="252" y1="156" x2="318" y2="125" class="ar"/>
<rect x="20" y="190" width="230" height="48" rx="7" class="k-purple"/>
<text x="135.0" y="209.5" text-anchor="middle" class="kb-purple">context</text>
<text x="135.0" y="227.5" text-anchor="middle" class="ks-purple">team, skills, deadline</text>
<line x1="252" y1="214" x2="318" y2="125" class="ar"/>
<rect x="320" y="70" width="200" height="110" rx="7" class="k-teal"/>
<text x="420.0" y="102.5" text-anchor="middle" class="kb-teal">architecture</text>
<text x="420.0" y="120.5" text-anchor="middle" class="ks-teal">structures</text>
<text x="420.0" y="138.5" text-anchor="middle" class="ks-teal">+ decisions</text>
<text x="420.0" y="156.5" text-anchor="middle" class="ks-teal">+ rationale</text>
<line x1="522" y1="125" x2="568" y2="125" class="ar"/>
<rect x="570" y="80" width="130" height="90" rx="7" class="k-amber"/>
<text x="635.0" y="111.5" text-anchor="middle" class="ks-amber">ADRs, views,</text>
<text x="635.0" y="129.5" text-anchor="middle" class="ks-amber">prototypes,</text>
<text x="635.0" y="147.5" text-anchor="middle" class="ks-amber">fitness tests</text>
</g>
</svg>
<figcaption>Most systems could meet their functional requirements with many architectures. Quality attributes decide which one.</figcaption>
</figure>

A surprising fact about architecture is that **functional requirements barely constrain it**. NetWarden's features could be built as one script, as a layered program, or as a dozen microservices. What separates those options is **quality attributes**: performance, security, modifiability, availability, usability, and the rest of the ISO 25010 list from Chapter 1. Constraints (language, budget, regulation) and context (team size, skills, deadline) narrow the choice further.

### Quality attribute scenarios

Vague quality requirements cannot guide design. The Software Engineering Institute (SEI) recommends writing them as **scenarios** with six parts.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A quality attribute scenario for performance: source, an administrator; stimulus, starts an assessment of a /24 network on 17 ports; artifact, NetWarden; environment, normal operation on a LAN; response, all hosts scanned and the report written; response measure, within 60 seconds." xmlns="http://www.w3.org/2000/svg">
<style>
.s7b{ font-family:var(--sans),sans-serif; }
.s7b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7b .s{ fill:var(--text-dim); font-size:13px; }
.s7b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .c{ fill:var(--text-faint); font-size:12.5px; }
.s7b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7b-a); }
.s7b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7b-a); marker-start:url(#s7b-s); }
.s7b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7b-g); }
.s7b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-a); }
.s7b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7b-tri); }
.s7b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-tri); }
.s7b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7b-open); }
.s7b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-open); }
.s7b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7b-dia); }
.s7b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7b-odia); }
.s7b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7b-dia); marker-end:url(#s7b-open); }
.s7b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7b-solid); }
.s7b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7b-open); }
.s7b .fill{ fill:var(--text); stroke:none; }
.s7b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s7b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s7b .ks-blue{ fill:#185FA5; font-size:13px; }
.s7b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s7b .kb-blue, :root[data-theme="dark"] .s7b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s7b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s7b .kh-blue{ fill:#85B7EB; }
.s7b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s7b-blue); }
.s7b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-blue); }
.s7b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s7b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7b .kb-teal, :root[data-theme="dark"] .s7b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7b .kh-teal{ fill:#5DCAA5; }
.s7b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7b-teal); }
.s7b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-teal); }
.s7b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7b .ks-purple{ fill:#534AB7; font-size:13px; }
.s7b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7b .kb-purple, :root[data-theme="dark"] .s7b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7b .kh-purple{ fill:#AFA9EC; }
.s7b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7b-purple); }
.s7b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-purple); }
.s7b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s7b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s7b .ks-green{ fill:#3B6D11; font-size:13px; }
.s7b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s7b .kb-green, :root[data-theme="dark"] .s7b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s7b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s7b .kh-green{ fill:#97C459; }
.s7b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s7b-green); }
.s7b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-green); }
.s7b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s7b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s7b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s7b .ks-red{ fill:#A32D2D; font-size:13px; }
.s7b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s7b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s7b .kb-red, :root[data-theme="dark"] .s7b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s7b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s7b .kh-red{ fill:#F09595; }
.s7b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s7b-red); }
.s7b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7b-red); }
.s7b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s7b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s7b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s7b">
<rect x="20" y="50" width="124" height="66" rx="7" class="k-blue"/>
<text x="82.0" y="78.5" text-anchor="middle" class="kb-blue">source</text>
<text x="82.0" y="96.5" text-anchor="middle" class="ks-blue">administrator</text>
<rect x="160" y="50" width="124" height="66" rx="7" class="k-purple"/>
<text x="222.0" y="78.5" text-anchor="middle" class="kb-purple">stimulus</text>
<text x="222.0" y="96.5" text-anchor="middle" class="ks-purple">scan a /24, 17 ports</text>
<line x1="146" y1="83" x2="158" y2="83" class="ar"/>
<rect x="300" y="50" width="124" height="66" rx="7" class="k-teal"/>
<text x="362.0" y="78.5" text-anchor="middle" class="kb-teal">artifact</text>
<text x="362.0" y="96.5" text-anchor="middle" class="ks-teal">NetWarden</text>
<line x1="286" y1="83" x2="298" y2="83" class="ar"/>
<rect x="440" y="50" width="124" height="66" rx="7" class="k-green"/>
<text x="502.0" y="78.5" text-anchor="middle" class="kb-green">response</text>
<text x="502.0" y="96.5" text-anchor="middle" class="ks-green">report produced</text>
<line x1="426" y1="83" x2="438" y2="83" class="ar"/>
<rect x="580" y="50" width="124" height="66" rx="7" class="k-red"/>
<text x="642.0" y="78.5" text-anchor="middle" class="kb-red">measure</text>
<text x="642.0" y="96.5" text-anchor="middle" class="ks-red">&lt; 60 s</text>
<line x1="566" y1="83" x2="578" y2="83" class="ar"/>
<rect x="170" y="150" width="380" height="44" rx="7" class="pnl"/>
<text x="360.0" y="176.5" text-anchor="middle" class="s">environment: normal operation, lab LAN</text>
<text x="360" y="30" text-anchor="middle" class="kh-teal">NW-NFR-1, written as a testable scenario</text>
<text x="360" y="232" text-anchor="middle" class="c">the same template works for security, availability, modifiability, usability</text>
</g>
</svg>
<figcaption>SEI quality attribute scenarios turn "it should be fast" into something an architecture can be checked against.</figcaption>
</figure>

| Part | Security scenario for NetWarden |
|---|---|
| Source | An administrator, possibly mistyping |
| Stimulus | Requests a scan of an address outside the authorised scope |
| Artifact | The scan engine |
| Environment | Normal operation |
| Response | Refuses with an error naming the address; sends no packet |
| Response measure | Zero packets to out-of-scope addresses, verified by a test with a recording fake scanner |

Each scenario can be checked against a proposed architecture: "where in this design is that guaranteed?" For NetWarden the answer is `Scope.expand`, called by `Assessment` before the scanner, shown in the sequence diagram in Chapter 4.

## Architectural styles

An **architectural style** (or pattern) is a named arrangement of components and connectors with known properties, the architecture-scale equivalent of a design pattern.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Six common architectural styles: layered, client-server, model-view-controller, pipe and filter, event-driven with a broker between publishers and subscribers, and microservices, each sketched as a small diagram." xmlns="http://www.w3.org/2000/svg">
<style>
.s7f{ font-family:var(--sans),sans-serif; }
.s7f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7f .s{ fill:var(--text-dim); font-size:13px; }
.s7f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .c{ fill:var(--text-faint); font-size:12.5px; }
.s7f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7f-a); }
.s7f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7f-a); marker-start:url(#s7f-s); }
.s7f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7f-g); }
.s7f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-a); }
.s7f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7f-tri); }
.s7f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-tri); }
.s7f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7f-open); }
.s7f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-open); }
.s7f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7f-dia); }
.s7f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7f-odia); }
.s7f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7f-dia); marker-end:url(#s7f-open); }
.s7f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7f-solid); }
.s7f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7f-open); }
.s7f .fill{ fill:var(--text); stroke:none; }
.s7f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s7f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s7f .ks-blue{ fill:#185FA5; font-size:13px; }
.s7f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s7f .kb-blue, :root[data-theme="dark"] .s7f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s7f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s7f .kh-blue{ fill:#85B7EB; }
.s7f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s7f-blue); }
.s7f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-blue); }
.s7f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s7f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7f .kb-teal, :root[data-theme="dark"] .s7f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7f .kh-teal{ fill:#5DCAA5; }
.s7f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7f-teal); }
.s7f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-teal); }
.s7f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7f .ks-amber{ fill:#854F0B; font-size:13px; }
.s7f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7f .kb-amber, :root[data-theme="dark"] .s7f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7f .kh-amber{ fill:#EF9F27; }
.s7f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7f-amber); }
.s7f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-amber); }
.s7f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7f .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s7f .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s7f .ks-coral{ fill:#993C1D; font-size:13px; }
.s7f .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7f .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s7f .kb-coral, :root[data-theme="dark"] .s7f .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s7f .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s7f .kh-coral{ fill:#F0997B; }
.s7f .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s7f-coral); }
.s7f .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-coral); }
.s7f .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s7f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7f .ks-purple{ fill:#534AB7; font-size:13px; }
.s7f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7f .kb-purple, :root[data-theme="dark"] .s7f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7f .kh-purple{ fill:#AFA9EC; }
.s7f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7f-purple); }
.s7f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-purple); }
.s7f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s7f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s7f .ks-green{ fill:#3B6D11; font-size:13px; }
.s7f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s7f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s7f .kb-green, :root[data-theme="dark"] .s7f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s7f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s7f .kh-green{ fill:#97C459; }
.s7f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s7f-green); }
.s7f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7f-green); }
.s7f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s7f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7f-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s7f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s7f">
<rect x="20" y="10" width="218" height="130" rx="8" class="pnl"/>
<text x="129" y="30" text-anchor="middle" class="kh-teal">layered</text>
<rect x="40" y="38" width="178" height="24" rx="3" class="k-teal"/>
<rect x="40" y="68" width="178" height="24" rx="3" class="k-teal"/>
<rect x="40" y="98" width="178" height="24" rx="3" class="k-teal"/>
<rect x="251" y="10" width="218" height="130" rx="8" class="pnl"/>
<text x="360" y="30" text-anchor="middle" class="kh-blue">client-server</text>
<rect x="270" y="40" width="50" height="22" rx="3" class="k-blue"/>
<line x1="322" y1="51" x2="390" y2="80" class="ln-blue"/>
<rect x="270" y="70" width="50" height="22" rx="3" class="k-blue"/>
<line x1="322" y1="81" x2="390" y2="80" class="ln-blue"/>
<rect x="270" y="100" width="50" height="22" rx="3" class="k-blue"/>
<line x1="322" y1="111" x2="390" y2="80" class="ln-blue"/>
<rect x="392" y="55" width="56" height="50" rx="3" class="k-blue"/>
<rect x="482" y="10" width="218" height="130" rx="8" class="pnl"/>
<text x="591" y="30" text-anchor="middle" class="kh-purple">model-view-controller</text>
<rect x="495" y="40" width="60" height="30" rx="3" class="k-purple"/>
<text x="525.0" y="59.5" text-anchor="middle" class="ks-purple">model</text>
<rect x="580" y="40" width="60" height="30" rx="3" class="k-purple"/>
<text x="610.0" y="59.5" text-anchor="middle" class="ks-purple">view</text>
<rect x="537" y="96" width="74" height="30" rx="3" class="k-purple"/>
<text x="574.0" y="115.5" text-anchor="middle" class="ks-purple">controller</text>
<line x1="557" y1="55" x2="578" y2="55" class="ln-purple"/>
<line x1="530" y1="72" x2="560" y2="94" class="ln-purple"/>
<line x1="610" y1="72" x2="590" y2="94" class="ln-purple"/>
<rect x="20" y="160" width="218" height="130" rx="8" class="pnl"/>
<text x="129" y="180" text-anchor="middle" class="kh-amber">pipe and filter</text>
<rect x="32" y="210" width="40" height="30" rx="3" class="k-amber"/>
<rect x="82" y="210" width="40" height="30" rx="3" class="k-amber"/>
<line x1="72" y1="225" x2="81" y2="225" class="ar-amber"/>
<rect x="132" y="210" width="40" height="30" rx="3" class="k-amber"/>
<line x1="122" y1="225" x2="131" y2="225" class="ar-amber"/>
<rect x="182" y="210" width="40" height="30" rx="3" class="k-amber"/>
<line x1="172" y1="225" x2="181" y2="225" class="ar-amber"/>
<rect x="251" y="160" width="218" height="130" rx="8" class="pnl"/>
<text x="360" y="180" text-anchor="middle" class="kh-coral">event-driven</text>
<rect x="270" y="200" width="50" height="24" rx="3" class="k-coral"/>
<rect x="270" y="240" width="50" height="24" rx="3" class="k-coral"/>
<rect x="335" y="205" width="60" height="54" rx="3" class="k-coral"/>
<text x="365.0" y="236.5" text-anchor="middle" class="ks-coral">broker</text>
<rect x="410" y="195" width="30" height="20" rx="3" class="k-coral"/>
<rect x="410" y="222" width="30" height="20" rx="3" class="k-coral"/>
<rect x="410" y="249" width="30" height="20" rx="3" class="k-coral"/>
<line x1="322" y1="212" x2="334" y2="220" class="ln-coral"/>
<line x1="322" y1="252" x2="334" y2="245" class="ln-coral"/>
<line x1="396" y1="232" x2="409" y2="205" class="ln-coral"/>
<line x1="396" y1="232" x2="409" y2="232" class="ln-coral"/>
<line x1="396" y1="232" x2="409" y2="259" class="ln-coral"/>
<rect x="482" y="160" width="218" height="130" rx="8" class="pnl"/>
<text x="591" y="180" text-anchor="middle" class="kh-green">microservices</text>
<circle cx="591" cy="201" r="12" class="k-green"/>
<line x1="591" y1="235" x2="591" y2="201" class="ln-green"/>
<circle cx="629" cy="224" r="12" class="k-green"/>
<line x1="591" y1="235" x2="629" y2="224" class="ln-green"/>
<circle cx="615" cy="263" r="12" class="k-green"/>
<line x1="591" y1="235" x2="615" y2="263" class="ln-green"/>
<circle cx="567" cy="263" r="12" class="k-green"/>
<line x1="591" y1="235" x2="567" y2="263" class="ln-green"/>
<circle cx="553" cy="224" r="12" class="k-green"/>
<line x1="591" y1="235" x2="553" y2="224" class="ln-green"/>
<circle cx="591" cy="235" r="7" class="k-green"/>
</g>
</svg>
<figcaption>Real systems combine styles: NetWarden is layered, its core is a pipeline, and it uses events internally.</figcaption>
</figure>

| Style | Structure | Strengths | Weaknesses |
|---|---|---|---|
| **Layered** | Stacked layers; each uses the ones below | Easy to understand; separates concerns | Changes can cut through all layers; layers can become pass-through |
| **Client-server** | Clients request services from a server | Central data and control | Server is a bottleneck and single point of failure |
| **Model-view-controller** | Model holds data and rules; views display; controllers handle input | Several views of one model; testable model | Can be overkill for simple interfaces |
| **Pipe and filter** | Independent filters connected by data streams | Reuse, recombination, parallelism | Poor for interactive applications; data format becomes a contract |
| **Event-driven** | Components publish and subscribe to events via a broker | Very loose coupling; scales well | Hard to trace flows; eventual consistency |
| **Microservices** | Small services, deployed independently, communicating over the network | Independent deployment and scaling; team autonomy | Distributed systems complexity; operations cost |

### Layered architecture

<figure class="diagram">
<svg viewBox="0 0 720 320" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden as a layered architecture. Presentation: cli.py. Application: engine.Assessment and events. Domain: models, scope, checks, fingerprint and knowledge. Infrastructure: scanner, report and store. Dependencies point downward or inward; the domain never imports the presentation layer." xmlns="http://www.w3.org/2000/svg">
<style>
.s7c{ font-family:var(--sans),sans-serif; }
.s7c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7c .s{ fill:var(--text-dim); font-size:13px; }
.s7c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7c .c{ fill:var(--text-faint); font-size:12.5px; }
.s7c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7c-a); }
.s7c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7c-a); marker-start:url(#s7c-s); }
.s7c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7c-g); }
.s7c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-a); }
.s7c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7c-tri); }
.s7c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-tri); }
.s7c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7c-open); }
.s7c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-open); }
.s7c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7c-dia); }
.s7c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7c-odia); }
.s7c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7c-dia); marker-end:url(#s7c-open); }
.s7c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7c-solid); }
.s7c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7c-open); }
.s7c .fill{ fill:var(--text); stroke:none; }
.s7c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7c .kb-teal, :root[data-theme="dark"] .s7c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7c .kh-teal{ fill:#5DCAA5; }
.s7c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7c-teal); }
.s7c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-teal); }
.s7c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7c .ks-amber{ fill:#854F0B; font-size:13px; }
.s7c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7c .kb-amber, :root[data-theme="dark"] .s7c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7c .kh-amber{ fill:#EF9F27; }
.s7c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7c-amber); }
.s7c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-amber); }
.s7c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7c .ks-purple{ fill:#534AB7; font-size:13px; }
.s7c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7c .kb-purple, :root[data-theme="dark"] .s7c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7c .kh-purple{ fill:#AFA9EC; }
.s7c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7c-purple); }
.s7c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-purple); }
.s7c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s7c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s7c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s7c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s7c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s7c .kb-gray, :root[data-theme="dark"] .s7c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s7c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s7c .kh-gray{ fill:#B4B2A9; }
.s7c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s7c-gray); }
.s7c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7c-gray); }
.s7c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s7c">
<rect x="20" y="14" width="680" height="62" rx="8" class="k-gray"/>
<text x="30" y="50" text-anchor="start" class="kh-gray">presentation</text>
<rect x="144" y="28" width="111" height="34" rx="4" class="pnl"/>
<text x="199.5" y="49.5" text-anchor="middle" class="m">cli.py</text>
<rect x="20" y="88" width="680" height="62" rx="8" class="k-teal"/>
<text x="30" y="124" text-anchor="start" class="kh-teal">application</text>
<rect x="144" y="102" width="111" height="34" rx="4" class="pnl"/>
<text x="199.5" y="123.5" text-anchor="middle" class="m">engine.py</text>
<rect x="255" y="102" width="111" height="34" rx="4" class="pnl"/>
<text x="310.5" y="123.5" text-anchor="middle" class="m">events.py</text>
<rect x="20" y="162" width="680" height="62" rx="8" class="k-purple"/>
<text x="30" y="198" text-anchor="start" class="kh-purple">domain</text>
<rect x="144" y="176" width="111" height="34" rx="4" class="pnl"/>
<text x="199.5" y="197.5" text-anchor="middle" class="m">models.py</text>
<rect x="255" y="176" width="111" height="34" rx="4" class="pnl"/>
<text x="310.5" y="197.5" text-anchor="middle" class="m">scope.py</text>
<rect x="366" y="176" width="111" height="34" rx="4" class="pnl"/>
<text x="421.5" y="197.5" text-anchor="middle" class="m">checks.py</text>
<rect x="477" y="176" width="111" height="34" rx="4" class="pnl"/>
<text x="532.5" y="197.5" text-anchor="middle" class="m">fingerprint.py</text>
<rect x="588" y="176" width="111" height="34" rx="4" class="pnl"/>
<text x="643.5" y="197.5" text-anchor="middle" class="m">knowledge.py</text>
<rect x="20" y="236" width="680" height="62" rx="8" class="k-amber"/>
<text x="30" y="272" text-anchor="start" class="kh-amber">infrastructure</text>
<rect x="144" y="250" width="111" height="34" rx="4" class="pnl"/>
<text x="199.5" y="271.5" text-anchor="middle" class="m">scanner.py</text>
<rect x="255" y="250" width="111" height="34" rx="4" class="pnl"/>
<text x="310.5" y="271.5" text-anchor="middle" class="m">report.py</text>
<rect x="366" y="250" width="111" height="34" rx="4" class="pnl"/>
<text x="421.5" y="271.5" text-anchor="middle" class="m">store.py</text>
<rect x="477" y="250" width="111" height="34" rx="4" class="pnl"/>
<text x="532.5" y="271.5" text-anchor="middle" class="m">demo.py</text>
<line x1="680" y1="78" x2="680" y2="88" class="ar"/>
<line x1="680" y1="152" x2="680" y2="162" class="ar"/>
<line x1="680" y1="226" x2="680" y2="236" class="ar"/>
<text x="360" y="312" text-anchor="middle" class="c">rule: depend downward only; skipping layers is allowed, upward dependencies are not</text>
</g>
</svg>
<figcaption>Layers organise code by level of abstraction. Each layer can be understood using only the layers below it.</figcaption>
</figure>

NetWarden is organised in four layers. The key rule is the direction of dependencies: `cli.py` may import anything; `models.py` imports nothing from NetWarden at all. The rule can be checked automatically with tools such as `import-linter`, turning an architectural decision into a test that fails in CI if someone breaks it, a so-called **fitness function**.

### Ports and adapters

A refinement of layering, Alistair Cockburn's **hexagonal architecture** (also called **ports and adapters**), and the closely related **clean architecture** of Robert Martin, put the domain at the centre and treat everything else, user interfaces, databases, networks, files, as replaceable details at the edge.

<figure class="diagram">
<svg viewBox="0 0 720 380" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden as ports and adapters, also called hexagonal architecture. At the centre, the core: models, scope rules, checks and the assessment workflow. Driving adapters on the left, the command line and a CI job, call the core through its use cases. On the right, the core defines ports, Scanner, KnowledgeSource, ScanRepository and Reporter, and driven adapters implement them: asyncio TCP, the JSON file, SQLite and the Markdown, JSON and HTML formats. Tests plug fakes into the same ports." xmlns="http://www.w3.org/2000/svg">
<style>
.s7d{ font-family:var(--sans),sans-serif; }
.s7d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7d .s{ fill:var(--text-dim); font-size:13px; }
.s7d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7d .c{ fill:var(--text-faint); font-size:12.5px; }
.s7d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7d-a); }
.s7d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7d-a); marker-start:url(#s7d-s); }
.s7d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7d-g); }
.s7d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-a); }
.s7d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7d-tri); }
.s7d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-tri); }
.s7d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7d-open); }
.s7d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-open); }
.s7d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7d-dia); }
.s7d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7d-odia); }
.s7d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7d-dia); marker-end:url(#s7d-open); }
.s7d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7d-solid); }
.s7d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7d-open); }
.s7d .fill{ fill:var(--text); stroke:none; }
.s7d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7d .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7d .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7d .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7d .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7d .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7d .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7d .kb-teal, :root[data-theme="dark"] .s7d .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7d .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7d .kh-teal{ fill:#5DCAA5; }
.s7d .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7d-teal); }
.s7d .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-teal); }
.s7d .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7d .ks-amber{ fill:#854F0B; font-size:13px; }
.s7d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7d .kb-amber, :root[data-theme="dark"] .s7d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7d .kh-amber{ fill:#EF9F27; }
.s7d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7d-amber); }
.s7d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-amber); }
.s7d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7d .ks-purple{ fill:#534AB7; font-size:13px; }
.s7d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7d .kb-purple, :root[data-theme="dark"] .s7d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7d .kh-purple{ fill:#AFA9EC; }
.s7d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7d-purple); }
.s7d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-purple); }
.s7d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s7d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s7d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s7d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s7d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s7d .kb-gray, :root[data-theme="dark"] .s7d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s7d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s7d .kh-gray{ fill:#B4B2A9; }
.s7d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s7d-gray); }
.s7d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7d-gray); }
.s7d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7d-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s7d">
<polygon points="490,190 425,303 295,303 230,190 295,77 425,77" class="k-teal"/>
<text x="360" y="160" text-anchor="middle" class="kb-teal">core</text>
<text x="360" y="180" text-anchor="middle" class="ks-teal">models, scope rules,</text>
<text x="360" y="198" text-anchor="middle" class="ks-teal">checks, Assessment</text>
<text x="360" y="224" text-anchor="middle" class="kh-teal">no I/O here</text>
<rect x="20" y="110" width="150" height="44" rx="7" class="k-gray"/>
<text x="95.0" y="136.5" text-anchor="middle" class="kb-gray">CLI</text>
<rect x="20" y="180" width="150" height="44" rx="7" class="k-gray"/>
<text x="95.0" y="206.5" text-anchor="middle" class="kb-gray">CI job</text>
<rect x="20" y="250" width="150" height="44" rx="7" class="k-purple"/>
<text x="95.0" y="276.5" text-anchor="middle" class="kb-purple">tests</text>
<line x1="172" y1="132" x2="236" y2="190" class="ar"/>
<line x1="172" y1="202" x2="236" y2="190" class="ar"/>
<line x1="172" y1="272" x2="236" y2="190" class="ar"/>
<text x="95" y="90" text-anchor="middle" class="kh-gray">driving adapters</text>
<rect x="510" y="52" width="190" height="44" rx="4" class="k-amber"/>
<text x="605.0" y="69.5" text-anchor="middle" class="km-amber">Scanner</text>
<text x="605.0" y="87.5" text-anchor="middle" class="ks-amber">asyncio TCP</text>
<line x1="460" y1="124.0" x2="508" y2="74" class="u"/>
<circle cx="460" cy="124" r="6" class="act"/>
<rect x="510" y="132" width="190" height="44" rx="4" class="k-amber"/>
<text x="605.0" y="149.5" text-anchor="middle" class="km-amber">KnowledgeSource</text>
<text x="605.0" y="167.5" text-anchor="middle" class="ks-amber">JSON file</text>
<line x1="460" y1="168.0" x2="508" y2="154" class="u"/>
<circle cx="460" cy="168" r="6" class="act"/>
<rect x="510" y="212" width="190" height="44" rx="4" class="k-amber"/>
<text x="605.0" y="229.5" text-anchor="middle" class="km-amber">ScanRepository</text>
<text x="605.0" y="247.5" text-anchor="middle" class="ks-amber">SQLite</text>
<line x1="460" y1="212.0" x2="508" y2="234" class="u"/>
<circle cx="460" cy="212" r="6" class="act"/>
<rect x="510" y="292" width="190" height="44" rx="4" class="k-amber"/>
<text x="605.0" y="309.5" text-anchor="middle" class="km-amber">Reporter</text>
<text x="605.0" y="327.5" text-anchor="middle" class="ks-amber">MD, JSON, HTML</text>
<line x1="460" y1="256.0" x2="508" y2="314" class="u"/>
<circle cx="460" cy="256" r="6" class="act"/>
<text x="700" y="30" text-anchor="end" class="kh-amber">ports and driven adapters</text>
</g>
</svg>
<figcaption>The core defines the interfaces it needs; the outside world plugs in. Everything at the edge is replaceable.</figcaption>
</figure>

The core defines **ports**, interfaces describing what it needs (a scanner, a source of vulnerability data, a place to store results). **Adapters** implement the ports using real technology. This is the dependency inversion principle (Chapter 5) applied at the scale of the whole system. Its payoff is visible in NetWarden's test suite: `tests/test_engine.py` runs the core with a fake scanner adapter, in milliseconds, with no network.

### Pipe and filter

<figure class="diagram">
<svg viewBox="0 0 720 200" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Pipe and filter. Data flows through independent filters connected by pipes: targets go through scope, which emits addresses; discovery emits hosts with banners; fingerprinting emits identified services; checks emit findings; and reporting emits text. Unix shell pipelines are the classic example." xmlns="http://www.w3.org/2000/svg">
<style>
.s7e{ font-family:var(--sans),sans-serif; }
.s7e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7e .s{ fill:var(--text-dim); font-size:13px; }
.s7e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .c{ fill:var(--text-faint); font-size:12.5px; }
.s7e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7e-a); }
.s7e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7e-a); marker-start:url(#s7e-s); }
.s7e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7e-g); }
.s7e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-a); }
.s7e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7e-tri); }
.s7e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-tri); }
.s7e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7e-open); }
.s7e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-open); }
.s7e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7e-dia); }
.s7e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7e-odia); }
.s7e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7e-dia); marker-end:url(#s7e-open); }
.s7e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7e-solid); }
.s7e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7e-open); }
.s7e .fill{ fill:var(--text); stroke:none; }
.s7e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s7e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s7e .ks-blue{ fill:#185FA5; font-size:13px; }
.s7e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s7e .kb-blue, :root[data-theme="dark"] .s7e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s7e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s7e .kh-blue{ fill:#85B7EB; }
.s7e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s7e-blue); }
.s7e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-blue); }
.s7e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s7e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7e .kb-teal, :root[data-theme="dark"] .s7e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7e .kh-teal{ fill:#5DCAA5; }
.s7e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7e-teal); }
.s7e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-teal); }
.s7e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7e .ks-amber{ fill:#854F0B; font-size:13px; }
.s7e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7e .kb-amber, :root[data-theme="dark"] .s7e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7e .kh-amber{ fill:#EF9F27; }
.s7e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7e-amber); }
.s7e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-amber); }
.s7e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7e .ks-purple{ fill:#534AB7; font-size:13px; }
.s7e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7e .kb-purple, :root[data-theme="dark"] .s7e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7e .kh-purple{ fill:#AFA9EC; }
.s7e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7e-purple); }
.s7e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-purple); }
.s7e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s7e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s7e .ks-red{ fill:#A32D2D; font-size:13px; }
.s7e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s7e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s7e .kb-red, :root[data-theme="dark"] .s7e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s7e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s7e .kh-red{ fill:#F09595; }
.s7e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s7e-red); }
.s7e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7e-red); }
.s7e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s7e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s7e">
<rect x="20" y="70" width="110" height="50" rx="7" class="k-red"/>
<text x="75.0" y="99.5" text-anchor="middle" class="kb-red">scope</text>
<rect x="162" y="70" width="110" height="50" rx="7" class="k-blue"/>
<text x="217.0" y="99.5" text-anchor="middle" class="kb-blue">discover</text>
<line x1="130" y1="95" x2="160" y2="95" class="ar"/>
<text x="146" y="58" text-anchor="middle" class="c">addresses</text>
<rect x="304" y="70" width="110" height="50" rx="7" class="k-purple"/>
<text x="359.0" y="99.5" text-anchor="middle" class="kb-purple">fingerprint</text>
<line x1="272" y1="95" x2="302" y2="95" class="ar"/>
<text x="288" y="58" text-anchor="middle" class="c">hosts</text>
<rect x="446" y="70" width="110" height="50" rx="7" class="k-amber"/>
<text x="501.0" y="99.5" text-anchor="middle" class="kb-amber">check</text>
<line x1="414" y1="95" x2="444" y2="95" class="ar"/>
<text x="430" y="58" text-anchor="middle" class="c">services</text>
<rect x="588" y="70" width="110" height="50" rx="7" class="k-teal"/>
<text x="643.0" y="99.5" text-anchor="middle" class="kb-teal">report</text>
<line x1="556" y1="95" x2="586" y2="95" class="ar"/>
<text x="572" y="58" text-anchor="middle" class="c">findings</text>
<text x="360" y="160" text-anchor="middle" class="m">$ cat access.log | grep 404 | cut -d' ' -f1 | sort | uniq -c</text>
</g>
</svg>
<figcaption>Filters know nothing about each other, only about the data format that flows between them.</figcaption>
</figure>

Inside the core, an assessment is a pipeline: each stage transforms the output of the previous one. The pipeline view explains why NetWarden's stages are easy to test separately: each has a clear input and output type.

## Monolith or microservices?

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden today and at scale. Today: one process, a modular monolith with a command-line interface and a SQLite file. At scale, for a large organisation: a web UI and API service, a scheduler, a message queue feeding many scanner workers placed in different network segments, a results service with PostgreSQL, and a notification service, each deployed independently." xmlns="http://www.w3.org/2000/svg">
<style>
.s7g{ font-family:var(--sans),sans-serif; }
.s7g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7g .s{ fill:var(--text-dim); font-size:13px; }
.s7g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7g .c{ fill:var(--text-faint); font-size:12.5px; }
.s7g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7g-a); }
.s7g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7g-a); marker-start:url(#s7g-s); }
.s7g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7g-g); }
.s7g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-a); }
.s7g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7g-tri); }
.s7g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-tri); }
.s7g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7g-open); }
.s7g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-open); }
.s7g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7g-dia); }
.s7g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7g-odia); }
.s7g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7g-dia); marker-end:url(#s7g-open); }
.s7g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7g-solid); }
.s7g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7g-open); }
.s7g .fill{ fill:var(--text); stroke:none; }
.s7g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7g .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7g .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7g .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7g .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7g .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7g .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7g .kb-teal, :root[data-theme="dark"] .s7g .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7g .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7g .kh-teal{ fill:#5DCAA5; }
.s7g .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7g-teal); }
.s7g .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-teal); }
.s7g .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7g .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7g .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7g .ks-amber{ fill:#854F0B; font-size:13px; }
.s7g .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7g .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7g .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7g .kb-amber, :root[data-theme="dark"] .s7g .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7g .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7g .kh-amber{ fill:#EF9F27; }
.s7g .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7g-amber); }
.s7g .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-amber); }
.s7g .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7g .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s7g .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s7g .ks-coral{ fill:#993C1D; font-size:13px; }
.s7g .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s7g .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7g .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s7g .kb-coral, :root[data-theme="dark"] .s7g .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s7g .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s7g .kh-coral{ fill:#F0997B; }
.s7g .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s7g-coral); }
.s7g .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-coral); }
.s7g .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s7g .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7g .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7g .ks-purple{ fill:#534AB7; font-size:13px; }
.s7g .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7g .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7g .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7g .kb-purple, :root[data-theme="dark"] .s7g .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7g .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7g .kh-purple{ fill:#AFA9EC; }
.s7g .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7g-purple); }
.s7g .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7g-purple); }
.s7g .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7g-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7g-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7g-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s7g-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s7g">
<text x="150" y="20" text-anchor="middle" class="kh-teal">today: modular monolith</text>
<rect x="20" y="34" width="260" height="270" rx="10" class="k-teal"/>
<rect x="40" y="54" width="105" height="44" rx="4" class="pnl"/>
<text x="92.5" y="80.5" text-anchor="middle" class="m">cli</text>
<rect x="155" y="54" width="105" height="44" rx="4" class="pnl"/>
<text x="207.5" y="80.5" text-anchor="middle" class="m">engine</text>
<rect x="40" y="114" width="105" height="44" rx="4" class="pnl"/>
<text x="92.5" y="140.5" text-anchor="middle" class="m">checks</text>
<rect x="155" y="114" width="105" height="44" rx="4" class="pnl"/>
<text x="207.5" y="140.5" text-anchor="middle" class="m">scanner</text>
<rect x="40" y="174" width="105" height="44" rx="4" class="pnl"/>
<text x="92.5" y="200.5" text-anchor="middle" class="m">report</text>
<rect x="155" y="174" width="105" height="44" rx="4" class="pnl"/>
<text x="207.5" y="200.5" text-anchor="middle" class="m">store</text>
<rect x="70" y="240" width="160" height="44" rx="4" class="k-purple"/>
<text x="150.0" y="266.5" text-anchor="middle" class="km-purple">netwarden.db</text>
<text x="500" y="20" text-anchor="middle" class="kh-coral">at scale: services</text>
<rect x="330" y="40" width="160" height="44" rx="4" class="k-coral"/>
<text x="410.0" y="66.5" text-anchor="middle" class="kb-coral">web UI + API</text>
<rect x="520" y="40" width="160" height="44" rx="4" class="k-coral"/>
<text x="600.0" y="66.5" text-anchor="middle" class="kb-coral">scheduler</text>
<rect x="330" y="140" width="160" height="44" rx="4" class="k-coral"/>
<text x="410.0" y="166.5" text-anchor="middle" class="kb-coral">results service</text>
<rect x="520" y="230" width="160" height="44" rx="4" class="k-coral"/>
<text x="600.0" y="256.5" text-anchor="middle" class="kb-coral">scanner worker</text>
<rect x="330" y="240" width="160" height="44" rx="4" class="k-coral"/>
<text x="410.0" y="266.5" text-anchor="middle" class="kb-coral">notifications</text>
<rect x="520" y="130" width="160" height="60" rx="4" class="k-amber"/>
<text x="600.0" y="155.5" text-anchor="middle" class="kb-amber">message queue</text>
<text x="600.0" y="173.5" text-anchor="middle" class="ks-amber">scan jobs, findings</text>
<rect x="540" y="280" width="160" height="34" rx="4" class="pnl"/>
<text x="620.0" y="301.5" text-anchor="middle" class="c">more workers ...</text>
<line x1="600" y1="86" x2="600" y2="128" class="ar"/>
<line x1="600" y1="192" x2="600" y2="228" class="ar"/>
<line x1="518" y1="160" x2="492" y2="160" class="ar"/>
<line x1="410" y1="86" x2="410" y2="138" class="ar"/>
<line x1="410" y1="186" x2="410" y2="238" class="ar"/>
<text x="360" y="322" text-anchor="middle" class="c">independent deployment and scaling, at the price of network calls, distributed failures and operations work</text>
</g>
</svg>
<figcaption>Start with a well-structured monolith; split out services only when a real need, such as scale or team independence, appears.</figcaption>
</figure>

NetWarden is a **modular monolith**: one deployable program, internally divided into well-separated modules. This is the right starting point for almost every new system. A large organisation might eventually need scanner workers in many network segments, scheduled scans, a web dashboard, and notifications, at which point some modules could become **services** communicating through a message queue. The modular structure makes that split possible; it does not make it free. Microservices trade the complexity inside one program for the complexity of a distributed system: network failures, partial outages, data consistency across services, and much more operational work (Chapter 14). Fowler's advice, "monolith first", is widely shared.

## Evaluating architecture

The SEI's **Architecture Tradeoff Analysis Method** (ATAM) evaluates an architecture against prioritised quality attribute scenarios, organised in a **utility tree**.

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A utility tree from the Architecture Tradeoff Analysis Method. Utility splits into quality attributes: security, performance, modifiability and usability. Each is refined and ends in concrete scenarios rated for business importance and technical difficulty, such as: no packet is sent to an out-of-scope address (high, medium); a /24 completes in under 60 seconds (high, medium); a new check takes under one day (medium, low)." xmlns="http://www.w3.org/2000/svg">
<style>
.s7h{ font-family:var(--sans),sans-serif; }
.s7h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7h .s{ fill:var(--text-dim); font-size:13px; }
.s7h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .c{ fill:var(--text-faint); font-size:12.5px; }
.s7h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7h-a); }
.s7h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7h-a); marker-start:url(#s7h-s); }
.s7h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7h-g); }
.s7h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-a); }
.s7h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7h-tri); }
.s7h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-tri); }
.s7h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7h-open); }
.s7h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-open); }
.s7h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7h-dia); }
.s7h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7h-odia); }
.s7h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7h-dia); marker-end:url(#s7h-open); }
.s7h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7h-solid); }
.s7h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7h-open); }
.s7h .fill{ fill:var(--text); stroke:none; }
.s7h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s7h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s7h .ks-blue{ fill:#185FA5; font-size:13px; }
.s7h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s7h .kb-blue, :root[data-theme="dark"] .s7h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s7h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s7h .kh-blue{ fill:#85B7EB; }
.s7h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s7h-blue); }
.s7h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-blue); }
.s7h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s7h .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7h .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7h .ks-purple{ fill:#534AB7; font-size:13px; }
.s7h .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7h .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7h .kb-purple, :root[data-theme="dark"] .s7h .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7h .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7h .kh-purple{ fill:#AFA9EC; }
.s7h .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7h-purple); }
.s7h .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-purple); }
.s7h .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7h .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s7h .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s7h .ks-green{ fill:#3B6D11; font-size:13px; }
.s7h .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7h .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s7h .kb-green, :root[data-theme="dark"] .s7h .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s7h .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s7h .kh-green{ fill:#97C459; }
.s7h .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s7h-green); }
.s7h .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-green); }
.s7h .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s7h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s7h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s7h .ks-red{ fill:#A32D2D; font-size:13px; }
.s7h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s7h .kb-red, :root[data-theme="dark"] .s7h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s7h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s7h .kh-red{ fill:#F09595; }
.s7h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s7h-red); }
.s7h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-red); }
.s7h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s7h .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s7h .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s7h .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s7h .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s7h .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7h .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s7h .kb-gray, :root[data-theme="dark"] .s7h .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s7h .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s7h .kh-gray{ fill:#B4B2A9; }
.s7h .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s7h-gray); }
.s7h .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7h-gray); }
.s7h .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s7h-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7h-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s7h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s7h-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s7h">
<rect x="20" y="140" width="100" height="44" rx="7" class="k-gray"/>
<text x="70.0" y="166.5" text-anchor="middle" class="kb-gray">utility</text>
<rect x="170" y="30" width="140" height="36" rx="4" class="k-red"/>
<text x="240.0" y="52.5" text-anchor="middle" class="kb-red">security</text>
<line x1="122" y1="162" x2="168" y2="48" class="u"/>
<rect x="360" y="30" width="290" height="34" rx="4" class="pnl"/>
<text x="505.0" y="51.5" text-anchor="middle" class="s">no packet to out-of-scope address</text>
<text x="690" y="52" text-anchor="end" class="kh-red">H, M</text>
<line x1="312" y1="48" x2="358" y2="47" class="u"/>
<rect x="360" y="72" width="290" height="34" rx="4" class="pnl"/>
<text x="505.0" y="93.5" text-anchor="middle" class="s">reports escape network data</text>
<text x="690" y="94" text-anchor="end" class="kh-red">H, L</text>
<line x1="312" y1="48" x2="358" y2="89" class="u"/>
<rect x="170" y="120" width="140" height="36" rx="4" class="k-blue"/>
<text x="240.0" y="142.5" text-anchor="middle" class="kb-blue">performance</text>
<line x1="122" y1="162" x2="168" y2="138" class="u"/>
<rect x="360" y="120" width="290" height="34" rx="4" class="pnl"/>
<text x="505.0" y="141.5" text-anchor="middle" class="s">/24 on 17 ports &lt; 60 s</text>
<text x="690" y="142" text-anchor="end" class="kh-blue">H, M</text>
<line x1="312" y1="138" x2="358" y2="137" class="u"/>
<rect x="170" y="190" width="140" height="36" rx="4" class="k-purple"/>
<text x="240.0" y="212.5" text-anchor="middle" class="kb-purple">modifiability</text>
<line x1="122" y1="162" x2="168" y2="208" class="u"/>
<rect x="360" y="190" width="290" height="34" rx="4" class="pnl"/>
<text x="505.0" y="211.5" text-anchor="middle" class="s">new check in &lt; 1 day</text>
<text x="690" y="212" text-anchor="end" class="kh-purple">M, L</text>
<line x1="312" y1="208" x2="358" y2="207" class="u"/>
<rect x="360" y="232" width="290" height="34" rx="4" class="pnl"/>
<text x="505.0" y="253.5" text-anchor="middle" class="s">swap SQLite for PostgreSQL &lt; 1 week</text>
<text x="690" y="254" text-anchor="end" class="kh-purple">L, M</text>
<line x1="312" y1="208" x2="358" y2="249" class="u"/>
<rect x="170" y="280" width="140" height="36" rx="4" class="k-green"/>
<text x="240.0" y="302.5" text-anchor="middle" class="kb-green">usability</text>
<line x1="122" y1="162" x2="168" y2="298" class="u"/>
<rect x="360" y="280" width="290" height="34" rx="4" class="pnl"/>
<text x="505.0" y="301.5" text-anchor="middle" class="s">first demo scan &lt; 5 minutes</text>
<text x="690" y="302" text-anchor="end" class="kh-green">M, L</text>
<line x1="312" y1="298" x2="358" y2="297" class="u"/>
<text x="670" y="14" text-anchor="end" class="c">(importance, difficulty)</text>
</g>
</svg>
<figcaption>High-importance, high-difficulty scenarios get the most architectural attention and the earliest prototypes.</figcaption>
</figure>

Scenarios rated high importance and high difficulty get the most attention. The evaluation identifies **sensitivity points** (decisions that strongly affect one quality), **trade-off points** (decisions that affect several qualities in opposite directions) and **risks**. For NetWarden, the concurrency limit is a trade-off point: raising it improves performance and worsens the risk of disrupting fragile devices.

Full ATAM evaluations take days and many stakeholders. Lighter alternatives, such as an hour-long review walking the top five scenarios through the design, catch most of the same problems.

## Recording decisions

Architecture is the sum of its decisions, and the reasons behind them are lost quickly as people move on. An **architecture decision record** (ADR), proposed by Michael Nygard in 2011, captures one decision in a short document.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The structure of an architecture decision record, using NetWarden&#x27;s ADR-0003: title; status, accepted; context, US-7 needs history and compare; options considered, JSON files, SQLite, PostgreSQL; decision, SQLite behind a repository; consequences, positive and negative, including when to revisit." xmlns="http://www.w3.org/2000/svg">
<style>
.s7i{ font-family:var(--sans),sans-serif; }
.s7i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s7i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s7i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s7i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s7i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s7i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s7i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s7i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s7i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s7i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s7i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s7i .s{ fill:var(--text-dim); font-size:13px; }
.s7i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s7i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .c{ fill:var(--text-faint); font-size:12.5px; }
.s7i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s7i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s7i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s7i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7i-a); }
.s7i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s7i-a); marker-start:url(#s7i-s); }
.s7i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s7i-g); }
.s7i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-a); }
.s7i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s7i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s7i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s7i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s7i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s7i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7i-tri); }
.s7i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-tri); }
.s7i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7i-open); }
.s7i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-open); }
.s7i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7i-dia); }
.s7i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7i-odia); }
.s7i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s7i-dia); marker-end:url(#s7i-open); }
.s7i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s7i-solid); }
.s7i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s7i-open); }
.s7i .fill{ fill:var(--text); stroke:none; }
.s7i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s7i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s7i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s7i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s7i .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s7i .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s7i .ks-blue{ fill:#185FA5; font-size:13px; }
.s7i .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7i .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s7i .kb-blue, :root[data-theme="dark"] .s7i .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s7i .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s7i .kh-blue{ fill:#85B7EB; }
.s7i .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s7i-blue); }
.s7i .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-blue); }
.s7i .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s7i .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s7i .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s7i .ks-teal{ fill:#0F6E56; font-size:13px; }
.s7i .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7i .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s7i .kb-teal, :root[data-theme="dark"] .s7i .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s7i .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s7i .kh-teal{ fill:#5DCAA5; }
.s7i .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s7i-teal); }
.s7i .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-teal); }
.s7i .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s7i .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s7i .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s7i .ks-amber{ fill:#854F0B; font-size:13px; }
.s7i .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7i .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s7i .kb-amber, :root[data-theme="dark"] .s7i .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s7i .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s7i .kh-amber{ fill:#EF9F27; }
.s7i .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s7i-amber); }
.s7i .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-amber); }
.s7i .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s7i .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s7i .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s7i .ks-purple{ fill:#534AB7; font-size:13px; }
.s7i .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7i .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s7i .kb-purple, :root[data-theme="dark"] .s7i .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s7i .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s7i .kh-purple{ fill:#AFA9EC; }
.s7i .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s7i-purple); }
.s7i .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-purple); }
.s7i .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s7i .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s7i .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s7i .ks-green{ fill:#3B6D11; font-size:13px; }
.s7i .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7i .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s7i .kb-green, :root[data-theme="dark"] .s7i .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s7i .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s7i .kh-green{ fill:#97C459; }
.s7i .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s7i-green); }
.s7i .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-green); }
.s7i .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s7i .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s7i .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s7i .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s7i .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s7i .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s7i .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s7i .kb-gray, :root[data-theme="dark"] .s7i .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s7i .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s7i .kh-gray{ fill:#B4B2A9; }
.s7i .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s7i-gray); }
.s7i .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s7i-gray); }
.s7i .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s7i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s7i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s7i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s7i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s7i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s7i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s7i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s7i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s7i-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s7i-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s7i-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s7i-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s7i-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s7i-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s7i">
<rect x="20" y="14" width="130" height="38" rx="4" class="k-gray"/>
<text x="85.0" y="37.5" text-anchor="middle" class="kb-gray">title</text>
<rect x="160" y="14" width="540" height="38" rx="4" class="pnl"/>
<text x="430.0" y="37.5" text-anchor="middle" class="s">ADR-0003: SQLite for scan history, behind a repository</text>
<rect x="20" y="60" width="130" height="38" rx="4" class="k-green"/>
<text x="85.0" y="83.5" text-anchor="middle" class="kb-green">status</text>
<rect x="160" y="60" width="540" height="38" rx="4" class="pnl"/>
<text x="430.0" y="83.5" text-anchor="middle" class="s">Accepted (2026-10-05)   proposed / accepted / superseded</text>
<rect x="20" y="106" width="130" height="38" rx="4" class="k-blue"/>
<text x="85.0" y="129.5" text-anchor="middle" class="kb-blue">context</text>
<rect x="160" y="106" width="540" height="38" rx="4" class="pnl"/>
<text x="430.0" y="129.5" text-anchor="middle" class="s">US-7 needs results kept and compared between runs</text>
<rect x="20" y="152" width="130" height="38" rx="4" class="k-purple"/>
<text x="85.0" y="175.5" text-anchor="middle" class="kb-purple">options</text>
<rect x="160" y="152" width="540" height="38" rx="4" class="pnl"/>
<text x="430.0" y="175.5" text-anchor="middle" class="s">JSON files per scan  |  SQLite  |  PostgreSQL server</text>
<rect x="20" y="198" width="130" height="38" rx="4" class="k-teal"/>
<text x="85.0" y="221.5" text-anchor="middle" class="kb-teal">decision</text>
<rect x="160" y="198" width="540" height="38" rx="4" class="pnl"/>
<text x="430.0" y="221.5" text-anchor="middle" class="s">SQLite through ScanRepository</text>
<rect x="20" y="244" width="130" height="38" rx="4" class="k-amber"/>
<text x="85.0" y="267.5" text-anchor="middle" class="kb-amber">consequences</text>
<rect x="160" y="244" width="540" height="38" rx="4" class="pnl"/>
<text x="430.0" y="267.5" text-anchor="middle" class="s">+ zero admin, transactions   - one writer at a time</text>
</g>
</svg>
<figcaption>ADRs are short, numbered, never deleted, and live in the repository next to the code (docs/adr/).</figcaption>
</figure>

NetWarden has three ADRs in `docs/adr/`: Python with the standard library only (ADR-0001), an offline knowledge base behind an interface (ADR-0002), and SQLite behind a repository (ADR-0003). When a decision is reversed, its ADR is not edited or deleted; it is marked **superseded** and a new ADR explains the change. The record of what was considered and why is often more valuable than the decision itself.

## The architect's role

In agile teams, architecture is not a phase done once by a separate person. It **emerges** from many decisions, but it should not happen by accident. Practical habits:

- Make the **few big decisions** early and explicitly (language, style, storage, deployment), and record them as ADRs.
- Defer decisions that are cheap to change later, and keep them reversible behind interfaces.
- Express important rules as **fitness functions**: tests for layer dependencies, performance budgets, security checks.
- Draw a C4 context and container diagram and keep them current.
- Revisit the architecture when quality attribute scenarios change.

## Summary

- Architecture is the set of **structures** and **decisions** that are expensive to change.
- **Quality attributes**, not functions, drive it; write them as **scenarios** with measurable responses.
- Common styles: **layered**, **client-server**, **MVC**, **pipe and filter**, **event-driven**, **microservices**; real systems combine them.
- **Ports and adapters** keep the core independent of technology, which makes it testable and adaptable.
- Start with a **modular monolith**; split into services only for a real need.
- Evaluate with scenario-based methods such as **ATAM** and a **utility tree**.
- Record decisions in **ADRs** and enforce key rules with **fitness functions**.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-7-software-architecture).

**1. How does the chapter define software architecture?**

- A. The set of structures and decisions that are expensive to change
- B. The list of classes
- C. The deployment diagram
- D. The programming language

**2. What mainly drives architecture?**

- A. The functions the system performs
- B. The team's favourite framework
- C. Quality attributes, such as performance, security and modifiability
- D. The database vendor

**3. How should a quality attribute be written?**

- A. As an adjective, such as fast
- B. As a user story
- C. As a class diagram
- D. As a scenario with a source, stimulus, environment and a measurable response

**4. What do ports and adapters (hexagonal architecture) give you?**

- A. Faster networking
- B. A core independent of technology, which makes it testable and adaptable
- C. Automatic scaling
- D. Fewer classes

**5. What does the chapter recommend as the starting point?**

- A. Microservices from day one
- B. Serverless functions
- C. A modular monolith, splitting into services only for a real need
- D. A distributed event store

**6. What is ATAM?**

- A. A scenario-based method for evaluating architectures, with a utility tree
- B. A deployment tool
- C. A design pattern
- D. A test technique

**7. What is an ADR?**

- A. An architecture decision record: a short document of a decision, its context and consequences
- B. An automated deployment run
- C. A database table
- D. A UML diagram

**8. What is an architectural fitness function?**

- A. A performance benchmark only
- B. A health check endpoint
- C. An automated check that enforces an architectural rule, such as 'the core never imports the network library'
- D. A code formatter
