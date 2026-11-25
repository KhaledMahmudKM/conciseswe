# Chapter 4: Modelling with UML and C4

A **model** is a simplified representation of something, built to answer particular questions. A map of a subway leaves out streets, distances and buildings because its users only need to know the order of stations and where lines connect. Software models work the same way: a class diagram leaves out algorithms to show structure; a sequence diagram leaves out structure to show who calls whom, in what order. Because software is invisible (Chapter 1), models are how engineers see it, discuss it, and check it before and after building it.

This chapter introduces the **Unified Modeling Language** (UML) and the lighter **C4 model**, and uses both to describe NetWarden.

## Why model?

Models are used in three ways, and it helps to be clear which one you are doing:

| Use | Purpose | Level of detail |
|---|---|---|
| **Sketch** | Think and communicate, on a whiteboard | Low; incomplete on purpose |
| **Blueprint** | Specify a design for others to build, or document one | Medium to high |
| **Executable** | Generate code from models (model-driven engineering) | Complete and formal |

Most teams sketch a lot, keep a small number of blueprint diagrams up to date, and rarely execute models. The diagrams in this chapter are blueprints: each one was drawn from NetWarden's actual code and kept in sync with it.

## UML in brief

UML was created in the mid-1990s by Grady Booch, James Rumbaugh and Ivar Jacobson, who merged their competing notations. It is maintained by the Object Management Group (OMG); the current version, **UML 2.5.1**, was published in 2017 and is also an ISO standard.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The 14 diagram types of UML 2.5, in two families. Structure diagrams: class, object, component, composite structure, package, deployment and profile. Behaviour diagrams: use case, activity and state machine, plus the interaction diagrams: sequence, communication, timing and interaction overview. Diagrams used in this book are highlighted." xmlns="http://www.w3.org/2000/svg">
<style>
.s4a{ font-family:var(--sans),sans-serif; }
.s4a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4a .s{ fill:var(--text-dim); font-size:13px; }
.s4a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4a .c{ fill:var(--text-faint); font-size:12.5px; }
.s4a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4a-a); }
.s4a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4a-a); marker-start:url(#s4a-s); }
.s4a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4a-g); }
.s4a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4a-a); }
.s4a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4a-tri); }
.s4a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4a-tri); }
.s4a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4a-open); }
.s4a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4a-open); }
.s4a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4a-dia); }
.s4a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4a-odia); }
.s4a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4a-dia); marker-end:url(#s4a-open); }
.s4a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4a-solid); }
.s4a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4a-open); }
.s4a .fill{ fill:var(--text); stroke:none; }
.s4a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4a .ks-blue{ fill:#185FA5; font-size:13px; }
.s4a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4a .kb-blue, :root[data-theme="dark"] .s4a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4a .kh-blue{ fill:#85B7EB; }
.s4a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4a-blue); }
.s4a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4a-blue); }
.s4a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4a .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s4a .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s4a .ks-coral{ fill:#993C1D; font-size:13px; }
.s4a .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s4a .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4a .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s4a .kb-coral, :root[data-theme="dark"] .s4a .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s4a .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s4a .kh-coral{ fill:#F0997B; }
.s4a .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s4a-coral); }
.s4a .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4a-coral); }
.s4a .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s4a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s4a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s4a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s4a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s4a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s4a .kb-gray, :root[data-theme="dark"] .s4a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s4a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s4a .kh-gray{ fill:#B4B2A9; }
.s4a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s4a-gray); }
.s4a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4a-gray); }
.s4a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s4a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s4a">
<rect x="260" y="10" width="200" height="36" rx="7" class="k-gray"/>
<text x="360.0" y="32.5" text-anchor="middle" class="kb-gray">UML diagram</text>
<rect x="40" y="70" width="260" height="36" rx="7" class="k-blue"/>
<text x="170.0" y="92.5" text-anchor="middle" class="kb-blue">structure (static)</text>
<rect x="420" y="70" width="260" height="36" rx="7" class="k-coral"/>
<text x="550.0" y="92.5" text-anchor="middle" class="kb-coral">behaviour (dynamic)</text>
<line x1="330" y1="46" x2="170" y2="68" class="gen"/>
<line x1="390" y1="46" x2="550" y2="68" class="gen"/>
<rect x="20" y="124" width="140" height="32" rx="5" class="k-blue"/>
<text x="90.0" y="144.5" text-anchor="middle" class="ks-blue">class</text>
<rect x="170" y="124" width="140" height="32" rx="5" class="k-blue"/>
<text x="240.0" y="144.5" text-anchor="middle" class="ks-blue">object</text>
<rect x="20" y="164" width="140" height="32" rx="5" class="k-blue"/>
<text x="90.0" y="184.5" text-anchor="middle" class="ks-blue">component</text>
<rect x="170" y="164" width="140" height="32" rx="5" class="k-blue"/>
<text x="240.0" y="184.5" text-anchor="middle" class="ks-blue">package</text>
<rect x="20" y="204" width="140" height="32" rx="5" class="k-blue"/>
<text x="90.0" y="224.5" text-anchor="middle" class="ks-blue">deployment</text>
<rect x="170" y="204" width="140" height="32" rx="5" class="pnl"/>
<text x="240.0" y="224.5" text-anchor="middle" class="s">composite structure</text>
<rect x="20" y="244" width="140" height="32" rx="5" class="pnl"/>
<text x="90.0" y="264.5" text-anchor="middle" class="s">profile</text>
<rect x="400" y="124" width="140" height="32" rx="5" class="k-coral"/>
<text x="470.0" y="144.5" text-anchor="middle" class="ks-coral">use case</text>
<rect x="400" y="164" width="140" height="32" rx="5" class="k-coral"/>
<text x="470.0" y="184.5" text-anchor="middle" class="ks-coral">activity</text>
<rect x="400" y="204" width="140" height="32" rx="5" class="k-coral"/>
<text x="470.0" y="224.5" text-anchor="middle" class="ks-coral">state machine</text>
<rect x="560" y="124" width="140" height="32" rx="5" class="pnl"/>
<text x="630.0" y="144.5" text-anchor="middle" class="b">interaction</text>
<rect x="560" y="164" width="140" height="26" rx="4" class="k-coral"/>
<text x="630.0" y="181.5" text-anchor="middle" class="ks-coral">sequence</text>
<rect x="560" y="194" width="140" height="26" rx="4" class="pnl"/>
<text x="630.0" y="211.5" text-anchor="middle" class="c">communication</text>
<rect x="560" y="224" width="140" height="26" rx="4" class="pnl"/>
<text x="630.0" y="241.5" text-anchor="middle" class="c">timing</text>
<rect x="560" y="254" width="140" height="26" rx="4" class="pnl"/>
<text x="630.0" y="271.5" text-anchor="middle" class="c">interaction overview</text>
<text x="360" y="284" text-anchor="middle" class="c">coloured: used in this book; the others are rarer in everyday practice</text>
</g>
</svg>
<figcaption>You do not need all 14. Class, sequence, activity, state and use case diagrams cover most needs.</figcaption>
</figure>

UML defines 14 diagram types. **Structure diagrams** show what the system is made of; **behaviour diagrams** show what it does. In practice a handful cover most needs, and they map onto Philippe Kruchten's **4+1 view model**, which reminds us that different stakeholders need different views.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Kruchten&#x27;s 4+1 view model of architecture: the logical view (class and state diagrams) for end users and analysts, the development view (package and component diagrams) for programmers, the process view (sequence and activity diagrams) for integrators, and the physical view (deployment diagrams) for operators, all tied together by scenarios (use cases)." xmlns="http://www.w3.org/2000/svg">
<style>
.s4b{ font-family:var(--sans),sans-serif; }
.s4b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4b .s{ fill:var(--text-dim); font-size:13px; }
.s4b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .c{ fill:var(--text-faint); font-size:12.5px; }
.s4b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4b-a); }
.s4b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4b-a); marker-start:url(#s4b-s); }
.s4b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4b-g); }
.s4b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-a); }
.s4b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4b-tri); }
.s4b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-tri); }
.s4b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4b-open); }
.s4b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-open); }
.s4b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4b-dia); }
.s4b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4b-odia); }
.s4b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4b-dia); marker-end:url(#s4b-open); }
.s4b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4b-solid); }
.s4b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4b-open); }
.s4b .fill{ fill:var(--text); stroke:none; }
.s4b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4b .ks-blue{ fill:#185FA5; font-size:13px; }
.s4b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4b .kb-blue, :root[data-theme="dark"] .s4b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4b .kh-blue{ fill:#85B7EB; }
.s4b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4b-blue); }
.s4b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-blue); }
.s4b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4b .kb-teal, :root[data-theme="dark"] .s4b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4b .kh-teal{ fill:#5DCAA5; }
.s4b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4b-teal); }
.s4b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-teal); }
.s4b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4b .ks-amber{ fill:#854F0B; font-size:13px; }
.s4b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4b .kb-amber, :root[data-theme="dark"] .s4b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4b .kh-amber{ fill:#EF9F27; }
.s4b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4b-amber); }
.s4b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-amber); }
.s4b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s4b .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s4b .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s4b .ks-coral{ fill:#993C1D; font-size:13px; }
.s4b .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4b .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s4b .kb-coral, :root[data-theme="dark"] .s4b .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s4b .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s4b .kh-coral{ fill:#F0997B; }
.s4b .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s4b-coral); }
.s4b .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-coral); }
.s4b .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s4b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4b .ks-purple{ fill:#534AB7; font-size:13px; }
.s4b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4b .kb-purple, :root[data-theme="dark"] .s4b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4b .kh-purple{ fill:#AFA9EC; }
.s4b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4b-purple); }
.s4b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4b-purple); }
.s4b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s4b-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s4b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s4b">
<rect x="20" y="20" width="260" height="90" rx="7" class="k-blue"/>
<text x="150.0" y="60.5" text-anchor="middle" class="kb-blue">logical view</text>
<text x="150.0" y="78.5" text-anchor="middle" class="ks-blue">classes, states</text>
<rect x="440" y="20" width="260" height="90" rx="7" class="k-teal"/>
<text x="570.0" y="60.5" text-anchor="middle" class="kb-teal">development view</text>
<text x="570.0" y="78.5" text-anchor="middle" class="ks-teal">packages, components</text>
<rect x="20" y="170" width="260" height="90" rx="7" class="k-amber"/>
<text x="150.0" y="210.5" text-anchor="middle" class="kb-amber">process view</text>
<text x="150.0" y="228.5" text-anchor="middle" class="ks-amber">sequence, activity</text>
<rect x="440" y="170" width="260" height="90" rx="7" class="k-purple"/>
<text x="570.0" y="210.5" text-anchor="middle" class="kb-purple">physical view</text>
<text x="570.0" y="228.5" text-anchor="middle" class="ks-purple">deployment</text>
<ellipse cx="360" cy="140" rx="100" ry="56" class="k-coral"/>
<text x="360" y="136" text-anchor="middle" class="kb-coral">scenarios</text>
<text x="360" y="154" text-anchor="middle" class="ks-coral">use cases</text>
<line x1="282" y1="80" x2="317.1" y2="107.0" class="u"/>
<line x1="438" y1="80" x2="402.9" y2="107.0" class="u"/>
<line x1="282" y1="200" x2="317.1" y2="173.0" class="u"/>
<line x1="438" y1="200" x2="402.9" y2="173.0" class="u"/>
</g>
</svg>
<figcaption>Each view answers different stakeholders' questions; scenarios check that the views fit together.</figcaption>
</figure>

## Class diagrams

The class diagram is the most widely used UML diagram. Each class is a box with up to three compartments.

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Anatomy of a UML class, using NetWarden&#x27;s Assessment class: the name compartment, the attribute compartment with visibility, name and type, and the operation compartment with parameters and return type. Visibility symbols: plus public, minus private, hash protected, tilde package. Static members are underlined; abstract ones are in italics." xmlns="http://www.w3.org/2000/svg">
<style>
.s4c{ font-family:var(--sans),sans-serif; }
.s4c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4c .s{ fill:var(--text-dim); font-size:13px; }
.s4c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4c .c{ fill:var(--text-faint); font-size:12.5px; }
.s4c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4c-a); }
.s4c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4c-a); marker-start:url(#s4c-s); }
.s4c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4c-g); }
.s4c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4c-a); }
.s4c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4c-tri); }
.s4c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4c-tri); }
.s4c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4c-open); }
.s4c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4c-open); }
.s4c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4c-dia); }
.s4c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4c-odia); }
.s4c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4c-dia); marker-end:url(#s4c-open); }
.s4c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4c-solid); }
.s4c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4c-open); }
.s4c .fill{ fill:var(--text); stroke:none; }
.s4c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4c .kb-teal, :root[data-theme="dark"] .s4c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4c .kh-teal{ fill:#5DCAA5; }
.s4c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4c-teal); }
.s4c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4c-teal); }
.s4c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker></defs>
<g class="s4c">
<rect x="220" y="20" width="280" height="158" rx="3" class="k-teal"/>
<text x="360.0" y="40" text-anchor="middle" class="kb-teal">Assessment</text>
<line x1="220" y1="50" x2="500" y2="50" class="ln-teal"/>
<text x="228" y="68" text-anchor="start" class="km-teal">- scope: Scope</text>
<text x="228" y="86" text-anchor="start" class="km-teal">- scanner: TcpScanner</text>
<text x="228" y="104" text-anchor="start" class="km-teal">- checks: list[Check]</text>
<text x="228" y="122" text-anchor="start" class="km-teal">- bus: EventBus</text>
<line x1="220" y1="132" x2="500" y2="132" class="ln-teal"/>
<text x="228" y="150" text-anchor="start" class="km-teal">+ run(targets, ports): ScanResult</text>
<text x="228" y="168" text-anchor="start" class="km-teal">+ run_async(targets, ports)</text>
<line x1="500" y1="40" x2="540" y2="40" class="u"/>
<text x="548" y="44" text-anchor="start" class="s">name</text>
<line x1="500" y1="110" x2="540" y2="110" class="u"/>
<text x="548" y="106" text-anchor="start" class="s">attributes:</text>
<text x="548" y="124" text-anchor="start" class="c">visibility name: type</text>
<line x1="500" y1="190" x2="540" y2="190" class="u"/>
<text x="548" y="194" text-anchor="start" class="s">operations</text>
<text x="30" y="50" text-anchor="start" class="m">+</text>
<text x="54" y="50" text-anchor="start" class="s">public</text>
<text x="30" y="76" text-anchor="start" class="m">-</text>
<text x="54" y="76" text-anchor="start" class="s">private</text>
<text x="30" y="102" text-anchor="start" class="m">#</text>
<text x="54" y="102" text-anchor="start" class="s">protected</text>
<text x="30" y="128" text-anchor="start" class="m">~</text>
<text x="54" y="128" text-anchor="start" class="s">package</text>
<text x="30" y="170" text-anchor="start" class="s">underlined: static</text>
<text x="30" y="194" text-anchor="start" class="i">italic: abstract</text>
</g>
</svg>
<figcaption>Detail is optional: early sketches show only names; later ones add types where they help.</figcaption>
</figure>

### Relationships

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="UML relationships between classes: association, a structural link, optionally with navigation arrow and multiplicities; aggregation, a whole-part link where parts can exist alone; composition, a whole-part link where parts live and die with the whole; generalization, inheritance; realization, a class implementing an interface; dependency, one class uses another temporarily." xmlns="http://www.w3.org/2000/svg">
<style>
.s4d{ font-family:var(--sans),sans-serif; }
.s4d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4d .s{ fill:var(--text-dim); font-size:13px; }
.s4d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4d .c{ fill:var(--text-faint); font-size:12.5px; }
.s4d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4d-a); }
.s4d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4d-a); marker-start:url(#s4d-s); }
.s4d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4d-g); }
.s4d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4d-a); }
.s4d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4d-tri); }
.s4d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4d-tri); }
.s4d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4d-open); }
.s4d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4d-open); }
.s4d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4d-dia); }
.s4d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4d-odia); }
.s4d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4d-dia); marker-end:url(#s4d-open); }
.s4d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4d-solid); }
.s4d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4d-open); }
.s4d .fill{ fill:var(--text); stroke:none; }
.s4d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4d .ks-blue{ fill:#185FA5; font-size:13px; }
.s4d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4d .kb-blue, :root[data-theme="dark"] .s4d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4d .kh-blue{ fill:#85B7EB; }
.s4d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4d-blue); }
.s4d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4d-blue); }
.s4d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker></defs>
<g class="s4d">
<text x="20" y="38" text-anchor="start" class="b">association</text>
<rect x="150" y="20" width="140" height="30" rx="3" class="k-blue"/>
<text x="220.0" y="39.5" text-anchor="middle" class="km-blue">Assessment</text>
<rect x="380" y="20" width="140" height="30" rx="3" class="k-blue"/>
<text x="450.0" y="39.5" text-anchor="middle" class="km-blue">Scope</text>
<line x1="290" y1="35" x2="380" y2="35" class="assoc"/>
<text x="540" y="39" text-anchor="start" class="c">holds a reference</text>
<text x="20" y="90" text-anchor="start" class="b">aggregation</text>
<rect x="150" y="72" width="140" height="30" rx="3" class="k-blue"/>
<text x="220.0" y="91.5" text-anchor="middle" class="km-blue">Team</text>
<rect x="380" y="72" width="140" height="30" rx="3" class="k-blue"/>
<text x="450.0" y="91.5" text-anchor="middle" class="km-blue">Developer</text>
<line x1="290" y1="87" x2="380" y2="87" class="agg"/>
<text x="540" y="91" text-anchor="start" class="c">parts can exist alone</text>
<text x="20" y="142" text-anchor="start" class="b">composition</text>
<rect x="150" y="124" width="140" height="30" rx="3" class="k-blue"/>
<text x="220.0" y="143.5" text-anchor="middle" class="km-blue">ScanResult</text>
<rect x="380" y="124" width="140" height="30" rx="3" class="k-blue"/>
<text x="450.0" y="143.5" text-anchor="middle" class="km-blue">Finding</text>
<line x1="290" y1="139" x2="380" y2="139" class="comp"/>
<text x="540" y="143" text-anchor="start" class="c">parts die with whole</text>
<text x="20" y="194" text-anchor="start" class="b">generalization</text>
<rect x="150" y="176" width="140" height="30" rx="3" class="k-blue"/>
<text x="220.0" y="195.5" text-anchor="middle" class="km-blue">Severity</text>
<rect x="380" y="176" width="140" height="30" rx="3" class="k-blue"/>
<text x="450.0" y="195.5" text-anchor="middle" class="km-blue">IntEnum</text>
<line x1="290" y1="191" x2="380" y2="191" class="gen"/>
<text x="540" y="195" text-anchor="start" class="c">is a kind of</text>
<text x="20" y="246" text-anchor="start" class="b">realization</text>
<rect x="150" y="228" width="140" height="30" rx="3" class="k-blue"/>
<text x="220.0" y="247.5" text-anchor="middle" class="km-blue">HttpHeadersCheck</text>
<rect x="380" y="228" width="140" height="30" rx="3" class="k-blue"/>
<text x="450.0" y="247.5" text-anchor="middle" class="km-blue">Check</text>
<line x1="290" y1="243" x2="380" y2="243" class="real"/>
<text x="540" y="247" text-anchor="start" class="c">implements interface</text>
<text x="20" y="298" text-anchor="start" class="b">dependency</text>
<rect x="150" y="280" width="140" height="30" rx="3" class="k-blue"/>
<text x="220.0" y="299.5" text-anchor="middle" class="km-blue">cli</text>
<rect x="380" y="280" width="140" height="30" rx="3" class="k-blue"/>
<text x="450.0" y="299.5" text-anchor="middle" class="km-blue">Reporter</text>
<line x1="290" y1="295" x2="380" y2="295" class="dep"/>
<text x="540" y="299" text-anchor="start" class="c">uses temporarily</text>
</g>
</svg>
<figcaption>Read the diamond end as "has"; the hollow triangle as "is a"; the dashed arrow as "uses" or "depends on".</figcaption>
</figure>

| Relationship | Meaning | Python equivalent |
|---|---|---|
| **Association** | Objects of one class hold references to the other | An attribute: `self.scope = scope` |
| **Aggregation** | Whole and part; the part can exist independently | A list of references to shared objects |
| **Composition** | Whole and part; the part is created and destroyed with the whole | `self.findings = []` filled with new objects |
| **Generalization** | Inheritance | `class Severity(IntEnum)` |
| **Realization** | A class implements an interface | A class that satisfies a `Protocol` |
| **Dependency** | Uses temporarily | A parameter, a local variable, a function call |

**Multiplicity** says how many objects take part: `1`, `0..1`, `*` (same as `0..*`), `1..*`. Labels at line ends name the role, often matching an attribute name.

### NetWarden's domain model

<figure class="diagram">
<svg viewBox="0 0 720 430" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Class diagram of NetWarden&#x27;s domain model. A ScanResult is composed of zero or more Hosts and zero or more Findings. Each Host is composed of zero or more Services. Each Finding has one Severity, an enumeration with values INFO, LOW, MEDIUM, HIGH and CRITICAL and an operation from_cvss." xmlns="http://www.w3.org/2000/svg">
<style>
.s4e{ font-family:var(--sans),sans-serif; }
.s4e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4e .s{ fill:var(--text-dim); font-size:13px; }
.s4e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4e .c{ fill:var(--text-faint); font-size:12.5px; }
.s4e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4e-a); }
.s4e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4e-a); marker-start:url(#s4e-s); }
.s4e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4e-g); }
.s4e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-a); }
.s4e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4e-tri); }
.s4e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-tri); }
.s4e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4e-open); }
.s4e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-open); }
.s4e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4e-dia); }
.s4e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4e-odia); }
.s4e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4e-dia); marker-end:url(#s4e-open); }
.s4e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4e-solid); }
.s4e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4e-open); }
.s4e .fill{ fill:var(--text); stroke:none; }
.s4e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4e .ks-blue{ fill:#185FA5; font-size:13px; }
.s4e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4e .kb-blue, :root[data-theme="dark"] .s4e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4e .kh-blue{ fill:#85B7EB; }
.s4e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4e-blue); }
.s4e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-blue); }
.s4e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4e .kb-teal, :root[data-theme="dark"] .s4e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4e .kh-teal{ fill:#5DCAA5; }
.s4e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4e-teal); }
.s4e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-teal); }
.s4e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4e .ks-amber{ fill:#854F0B; font-size:13px; }
.s4e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4e .kb-amber, :root[data-theme="dark"] .s4e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4e .kh-amber{ fill:#EF9F27; }
.s4e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4e-amber); }
.s4e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-amber); }
.s4e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s4e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4e .ks-purple{ fill:#534AB7; font-size:13px; }
.s4e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4e .kb-purple, :root[data-theme="dark"] .s4e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4e .kh-purple{ fill:#AFA9EC; }
.s4e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4e-purple); }
.s4e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4e-purple); }
.s4e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s4e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s4e">
<rect x="20" y="20" width="230" height="158" rx="3" class="k-teal"/>
<text x="135.0" y="40" text-anchor="middle" class="kb-teal">ScanResult</text>
<line x1="20" y1="50" x2="250" y2="50" class="ln-teal"/>
<text x="28" y="68" text-anchor="start" class="km-teal">+ targets: list[str]</text>
<text x="28" y="86" text-anchor="start" class="km-teal">+ started: datetime</text>
<text x="28" y="104" text-anchor="start" class="km-teal">+ finished: datetime</text>
<text x="28" y="122" text-anchor="start" class="km-teal">+ scan_id: int</text>
<line x1="20" y1="132" x2="250" y2="132" class="ln-teal"/>
<text x="28" y="150" text-anchor="start" class="km-teal">+ counts(): dict</text>
<text x="28" y="168" text-anchor="start" class="km-teal">+ worst(): Severity</text>
<rect x="320" y="20" width="170" height="68" rx="3" class="k-blue"/>
<text x="405.0" y="40" text-anchor="middle" class="kb-blue">Host</text>
<line x1="320" y1="50" x2="490" y2="50" class="ln-blue"/>
<text x="328" y="68" text-anchor="start" class="km-blue">+ address: str</text>
<line x1="320" y1="78" x2="490" y2="78" class="ln-blue"/>
<rect x="540" y="20" width="160" height="140" rx="3" class="k-blue"/>
<text x="620.0" y="40" text-anchor="middle" class="kb-blue">Service</text>
<line x1="540" y1="50" x2="700" y2="50" class="ln-blue"/>
<text x="548" y="68" text-anchor="start" class="km-blue">+ port: int</text>
<text x="548" y="86" text-anchor="start" class="km-blue">+ banner: str</text>
<text x="548" y="104" text-anchor="start" class="km-blue">+ name: str</text>
<text x="548" y="122" text-anchor="start" class="km-blue">+ product: str</text>
<text x="548" y="140" text-anchor="start" class="km-blue">+ version: str</text>
<line x1="540" y1="150" x2="700" y2="150" class="ln-blue"/>
<rect x="320" y="210" width="200" height="194" rx="3" class="k-amber"/>
<text x="420.0" y="230" text-anchor="middle" class="kb-amber">Finding</text>
<line x1="320" y1="240" x2="520" y2="240" class="ln-amber"/>
<text x="328" y="258" text-anchor="start" class="km-amber">+ host: str</text>
<text x="328" y="276" text-anchor="start" class="km-amber">+ port: int</text>
<text x="328" y="294" text-anchor="start" class="km-amber">+ check_id: str</text>
<text x="328" y="312" text-anchor="start" class="km-amber">+ title: str</text>
<text x="328" y="330" text-anchor="start" class="km-amber">+ cvss: float</text>
<text x="328" y="348" text-anchor="start" class="km-amber">+ cve: str</text>
<text x="328" y="366" text-anchor="start" class="km-amber">+ remediation: str</text>
<line x1="320" y1="376" x2="520" y2="376" class="ln-amber"/>
<text x="328" y="394" text-anchor="start" class="km-amber">+ key(): tuple</text>
<rect x="560" y="230" width="140" height="176" rx="3" class="k-purple"/>
<text x="630.0" y="250" text-anchor="middle" class="ks-purple">«enumeration»</text>
<text x="630.0" y="268" text-anchor="middle" class="kb-purple">Severity</text>
<line x1="560" y1="278" x2="700" y2="278" class="ln-purple"/>
<text x="568" y="296" text-anchor="start" class="km-purple">INFO</text>
<text x="568" y="314" text-anchor="start" class="km-purple">LOW</text>
<text x="568" y="332" text-anchor="start" class="km-purple">MEDIUM</text>
<text x="568" y="350" text-anchor="start" class="km-purple">HIGH</text>
<text x="568" y="368" text-anchor="start" class="km-purple">CRITICAL</text>
<line x1="560" y1="378" x2="700" y2="378" class="ln-purple"/>
<text x="568" y="396" text-anchor="start" class="km-purple">+ from_cvss()</text>
<line x1="252" y1="52" x2="318" y2="52" class="comp"/>
<text x="268" y="44" text-anchor="middle" class="c">1</text>
<text x="300" y="44" text-anchor="middle" class="c">0..*</text>
<text x="286" y="70" text-anchor="middle" class="c">hosts</text>
<line x1="492" y1="52" x2="538" y2="52" class="comp"/>
<text x="504" y="44" text-anchor="middle" class="c">1</text>
<text x="522" y="70" text-anchor="middle" class="c">0..*</text>
<path d="M135 180 L135 300 L318 300" class="comp"/>
<text x="145" y="200" text-anchor="start" class="c">1</text>
<text x="290" y="292" text-anchor="middle" class="c">0..*</text>
<text x="230" y="318" text-anchor="middle" class="c">findings</text>
<line x1="522" y1="320" x2="558" y2="320" class="assoc"/>
<text x="548" y="312" text-anchor="middle" class="c">1</text>
<text x="540" y="338" text-anchor="middle" class="c">severity</text>
</g>
</svg>
<figcaption>A domain model shows the concepts and how they relate. It is drawn straight from models.py.</figcaption>
</figure>

A **domain model** captures the concepts of the problem, usually before code exists. This one matches `models.py`: a `ScanResult` owns its `Host` objects and its `Finding` objects (composition: deleting the result deletes them), each `Host` owns its `Service` objects, and each `Finding` has a `Severity`. In the code, `Severity` is an `IntEnum`, so severities compare naturally: `Severity.HIGH > Severity.LOW`.

### Interfaces and implementations

<figure class="diagram">
<svg viewBox="0 0 720 370" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Class diagram of NetWarden&#x27;s checks. Assessment holds a list of Check objects. Check is an interface with an id attribute and a run operation. Five classes realise it: CleartextProtocolCheck, ExposedDatabaseCheck, KnownVulnerabilityCheck, HttpHeadersCheck and VersionDisclosureCheck. KnownVulnerabilityCheck uses a KnowledgeBase." xmlns="http://www.w3.org/2000/svg">
<style>
.s4f{ font-family:var(--sans),sans-serif; }
.s4f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4f .s{ fill:var(--text-dim); font-size:13px; }
.s4f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4f .c{ fill:var(--text-faint); font-size:12.5px; }
.s4f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4f-a); }
.s4f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4f-a); marker-start:url(#s4f-s); }
.s4f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4f-g); }
.s4f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4f-a); }
.s4f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4f-tri); }
.s4f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4f-tri); }
.s4f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4f-open); }
.s4f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4f-open); }
.s4f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4f-dia); }
.s4f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4f-odia); }
.s4f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4f-dia); marker-end:url(#s4f-open); }
.s4f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4f-solid); }
.s4f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4f-open); }
.s4f .fill{ fill:var(--text); stroke:none; }
.s4f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4f .ks-blue{ fill:#185FA5; font-size:13px; }
.s4f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4f .kb-blue, :root[data-theme="dark"] .s4f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4f .kh-blue{ fill:#85B7EB; }
.s4f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4f-blue); }
.s4f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4f-blue); }
.s4f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4f .kb-teal, :root[data-theme="dark"] .s4f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4f .kh-teal{ fill:#5DCAA5; }
.s4f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4f-teal); }
.s4f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4f-teal); }
.s4f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4f .ks-purple{ fill:#534AB7; font-size:13px; }
.s4f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4f .kb-purple, :root[data-theme="dark"] .s4f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4f .kh-purple{ fill:#AFA9EC; }
.s4f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4f-purple); }
.s4f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4f-purple); }
.s4f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s4f">
<rect x="20" y="20" width="180" height="86" rx="3" class="k-teal"/>
<text x="110.0" y="40" text-anchor="middle" class="kb-teal">Assessment</text>
<line x1="20" y1="50" x2="200" y2="50" class="ln-teal"/>
<text x="28" y="68" text-anchor="start" class="km-teal">- checks: list[Check]</text>
<line x1="20" y1="78" x2="200" y2="78" class="ln-teal"/>
<text x="28" y="96" text-anchor="start" class="km-teal">+ run(targets, ports)</text>
<rect x="250" y="20" width="200" height="104" rx="3" class="k-purple"/>
<text x="350.0" y="40" text-anchor="middle" class="ks-purple">«interface»</text>
<text x="350.0" y="58" text-anchor="middle" class="kb-purple">Check</text>
<line x1="250" y1="68" x2="450" y2="68" class="ln-purple"/>
<text x="258" y="86" text-anchor="start" class="km-purple">+ id: str</text>
<line x1="250" y1="96" x2="450" y2="96" class="ln-purple"/>
<text x="258" y="114" text-anchor="start" class="km-purple">+ run(host, service)</text>
<rect x="480" y="20" width="220" height="86" rx="3" class="k-teal"/>
<text x="590.0" y="40" text-anchor="middle" class="kb-teal">KnowledgeBase</text>
<line x1="480" y1="50" x2="700" y2="50" class="ln-teal"/>
<text x="488" y="68" text-anchor="start" class="km-teal">- vulnerabilities</text>
<line x1="480" y1="78" x2="700" y2="78" class="ln-teal"/>
<text x="488" y="96" text-anchor="start" class="km-teal">+ lookup(product, version)</text>
<line x1="202" y1="60" x2="248" y2="60" class="assoc"/>
<text x="238" y="52" text-anchor="middle" class="c">*</text>
<line x1="350" y1="152" x2="350" y2="124" class="real"/>
<line x1="120" y1="152" x2="580" y2="152" class="ud"/>
<rect x="20" y="180" width="200" height="68" rx="3" class="k-blue"/>
<text x="120.0" y="200" text-anchor="middle" class="kb-blue">CleartextProtocolCheck</text>
<line x1="20" y1="210" x2="220" y2="210" class="ln-blue"/>
<line x1="20" y1="220" x2="220" y2="220" class="ln-blue"/>
<text x="28" y="238" text-anchor="start" class="km-blue">+ run(host, service)</text>
<line x1="120" y1="180" x2="120" y2="152" class="ud"/>
<rect x="250" y="180" width="200" height="68" rx="3" class="k-blue"/>
<text x="350.0" y="200" text-anchor="middle" class="kb-blue">ExposedDatabaseCheck</text>
<line x1="250" y1="210" x2="450" y2="210" class="ln-blue"/>
<line x1="250" y1="220" x2="450" y2="220" class="ln-blue"/>
<text x="258" y="238" text-anchor="start" class="km-blue">+ run(host, service)</text>
<line x1="350" y1="180" x2="350" y2="152" class="ud"/>
<rect x="480" y="180" width="200" height="86" rx="3" class="k-blue"/>
<text x="580.0" y="200" text-anchor="middle" class="kb-blue">KnownVulnerabilityCheck</text>
<line x1="480" y1="210" x2="680" y2="210" class="ln-blue"/>
<text x="488" y="228" text-anchor="start" class="km-blue">- kb: KnowledgeBase</text>
<line x1="480" y1="238" x2="680" y2="238" class="ln-blue"/>
<text x="488" y="256" text-anchor="start" class="km-blue">+ run(host, service)</text>
<line x1="580" y1="180" x2="580" y2="152" class="ud"/>
<rect x="135" y="280" width="200" height="68" rx="3" class="k-blue"/>
<text x="235.0" y="300" text-anchor="middle" class="kb-blue">HttpHeadersCheck</text>
<line x1="135" y1="310" x2="335" y2="310" class="ln-blue"/>
<line x1="135" y1="320" x2="335" y2="320" class="ln-blue"/>
<text x="143" y="338" text-anchor="start" class="km-blue">+ run(host, service)</text>
<line x1="235" y1="280" x2="235" y2="152" class="ud"/>
<rect x="365" y="280" width="200" height="68" rx="3" class="k-blue"/>
<text x="465.0" y="300" text-anchor="middle" class="kb-blue">VersionDisclosureCheck</text>
<line x1="365" y1="310" x2="565" y2="310" class="ln-blue"/>
<line x1="365" y1="320" x2="565" y2="320" class="ln-blue"/>
<text x="373" y="338" text-anchor="start" class="km-blue">+ run(host, service)</text>
<line x1="465" y1="280" x2="465" y2="152" class="ud"/>
<line x1="650" y1="180" x2="650" y2="108" class="assoc"/>
<text x="658" y="150" text-anchor="start" class="c">uses</text>
</g>
</svg>
<figcaption>Adding a check means adding one class that realises Check. Nothing above the dashed lines changes.</figcaption>
</figure>

This diagram shows a design decision. `Assessment` depends only on the `Check` **interface**, written in Python as a `Protocol`. Each concrete check **realises** it. The engine never needs to know which checks exist, so adding one changes nothing above the dashed lines. Chapter 5 names the principle (open/closed) and Chapter 6 the pattern (strategy).

```python
class Check(Protocol):
    """The interface every check implements."""
    id: str
    def run(self, host: Host, service: Service) -> list[Finding]: ...
```

### Object diagrams

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="An object diagram: a snapshot of objects after the demo scan. result1 of class ScanResult links to host1 with address 127.0.0.1, which links to ssh of class Service with port 2222, product OpenSSH and version 8.9p1. result1 also links to f3 of class Finding with cve CVE-2024-6387 and severity HIGH." xmlns="http://www.w3.org/2000/svg">
<style>
.s4g{ font-family:var(--sans),sans-serif; }
.s4g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4g .s{ fill:var(--text-dim); font-size:13px; }
.s4g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4g .c{ fill:var(--text-faint); font-size:12.5px; }
.s4g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4g-a); }
.s4g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4g-a); marker-start:url(#s4g-s); }
.s4g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4g-g); }
.s4g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4g-a); }
.s4g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4g-tri); }
.s4g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4g-tri); }
.s4g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4g-open); }
.s4g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4g-open); }
.s4g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4g-dia); }
.s4g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4g-odia); }
.s4g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4g-dia); marker-end:url(#s4g-open); }
.s4g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4g-solid); }
.s4g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4g-open); }
.s4g .fill{ fill:var(--text); stroke:none; }
.s4g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4g .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4g .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4g .ks-amber{ fill:#854F0B; font-size:13px; }
.s4g .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4g .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4g .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4g .kb-amber, :root[data-theme="dark"] .s4g .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4g .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4g .kh-amber{ fill:#EF9F27; }
.s4g .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4g-amber); }
.s4g .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4g-amber); }
.s4g .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4g-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker></defs>
<g class="s4g">
<rect x="20" y="20" width="220" height="76" rx="3" class="k-amber"/>
<text x="130" y="40" text-anchor="middle" class="kb-amber" style="text-decoration:underline">result1 : ScanResult</text>
<line x1="20" y1="50" x2="240" y2="50" class="ln-amber"/>
<text x="28" y="68" text-anchor="start" class="km-amber">scan_id = 1</text>
<text x="28" y="86" text-anchor="start" class="km-amber">targets = ["127.0.0.1"]</text>
<rect x="300" y="20" width="220" height="58" rx="3" class="k-amber"/>
<text x="410" y="40" text-anchor="middle" class="kb-amber" style="text-decoration:underline">host1 : Host</text>
<line x1="300" y1="50" x2="520" y2="50" class="ln-amber"/>
<text x="308" y="68" text-anchor="start" class="km-amber">address = "127.0.0.1"</text>
<rect x="500" y="120" width="200" height="94" rx="3" class="k-amber"/>
<text x="600" y="140" text-anchor="middle" class="kb-amber" style="text-decoration:underline">ssh : Service</text>
<line x1="500" y1="150" x2="700" y2="150" class="ln-amber"/>
<text x="508" y="168" text-anchor="start" class="km-amber">port = 2222</text>
<text x="508" y="186" text-anchor="start" class="km-amber">product = "OpenSSH"</text>
<text x="508" y="204" text-anchor="start" class="km-amber">version = "8.9p1"</text>
<rect x="20" y="140" width="220" height="94" rx="3" class="k-amber"/>
<text x="130" y="160" text-anchor="middle" class="kb-amber" style="text-decoration:underline">f3 : Finding</text>
<line x1="20" y1="170" x2="240" y2="170" class="ln-amber"/>
<text x="28" y="188" text-anchor="start" class="km-amber">port = 2222</text>
<text x="28" y="206" text-anchor="start" class="km-amber">cve = "CVE-2024-6387"</text>
<text x="28" y="224" text-anchor="start" class="km-amber">severity = HIGH</text>
<line x1="240" y1="45" x2="298" y2="45" class="u"/>
<path d="M410 76 L410 150 L498 150" class="u"/>
<line x1="120" y1="96" x2="120" y2="138" class="u"/>
</g>
</svg>
<figcaption>Object names are underlined and have values instead of types. Snapshots like this help explain and test class diagrams.</figcaption>
</figure>

An **object diagram** is a snapshot: specific objects and their values at one moment. It is useful for explaining a class diagram with a concrete example, and for designing test fixtures.

## Interaction: sequence diagrams

Class diagrams show structure; **sequence diagrams** show how objects collaborate over time to carry out one scenario.

<figure class="diagram">
<svg viewBox="0 0 720 480" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Sequence diagram for netwarden scan. The cli calls run on Assessment, which calls expand on Scope and receives addresses. In the alternative where all targets are in scope, Assessment calls scan on TcpScanner and receives hosts, identifies the services, and in a loop over each check calls run on a Check and receives findings; it returns the ScanResult to cli, which saves it to history. Otherwise Assessment raises ScopeError to cli and no traffic is sent." xmlns="http://www.w3.org/2000/svg">
<style>
.s4h{ font-family:var(--sans),sans-serif; }
.s4h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4h .s{ fill:var(--text-dim); font-size:13px; }
.s4h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .c{ fill:var(--text-faint); font-size:12.5px; }
.s4h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4h-a); }
.s4h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4h-a); marker-start:url(#s4h-s); }
.s4h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4h-g); }
.s4h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-a); }
.s4h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4h-tri); }
.s4h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-tri); }
.s4h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4h-open); }
.s4h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-open); }
.s4h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4h-dia); }
.s4h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4h-odia); }
.s4h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4h-dia); marker-end:url(#s4h-open); }
.s4h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4h-solid); }
.s4h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4h-open); }
.s4h .fill{ fill:var(--text); stroke:none; }
.s4h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4h .ks-blue{ fill:#185FA5; font-size:13px; }
.s4h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4h .kb-blue, :root[data-theme="dark"] .s4h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4h .kh-blue{ fill:#85B7EB; }
.s4h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4h-blue); }
.s4h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-blue); }
.s4h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4h .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4h .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4h .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4h .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4h .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4h .kb-teal, :root[data-theme="dark"] .s4h .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4h .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4h .kh-teal{ fill:#5DCAA5; }
.s4h .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4h-teal); }
.s4h .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-teal); }
.s4h .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4h .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4h .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4h .ks-purple{ fill:#534AB7; font-size:13px; }
.s4h .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4h .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4h .kb-purple, :root[data-theme="dark"] .s4h .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4h .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4h .kh-purple{ fill:#AFA9EC; }
.s4h .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4h-purple); }
.s4h .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-purple); }
.s4h .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s4h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s4h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s4h .ks-red{ fill:#A32D2D; font-size:13px; }
.s4h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s4h .kb-red, :root[data-theme="dark"] .s4h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s4h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s4h .kh-red{ fill:#F09595; }
.s4h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s4h-red); }
.s4h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-red); }
.s4h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s4h .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s4h .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s4h .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s4h .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s4h .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4h .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s4h .kb-gray, :root[data-theme="dark"] .s4h .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s4h .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s4h .kh-gray{ fill:#B4B2A9; }
.s4h .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s4h-gray); }
.s4h .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4h-gray); }
.s4h .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4h-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4h-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s4h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s4h-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s4h">
<rect x="10.0" y="12" width="120" height="36" rx="4" class="k-gray"/>
<text x="70.0" y="34.5" text-anchor="middle" class="kb-gray">:cli</text>
<line x1="70" y1="48" x2="70" y2="472" class="gd"/>
<rect x="155.0" y="12" width="120" height="36" rx="4" class="k-teal"/>
<text x="215.0" y="34.5" text-anchor="middle" class="kb-teal">:Assessment</text>
<line x1="215" y1="48" x2="215" y2="472" class="gd"/>
<rect x="300.0" y="12" width="120" height="36" rx="4" class="k-red"/>
<text x="360.0" y="34.5" text-anchor="middle" class="kb-red">:Scope</text>
<line x1="360" y1="48" x2="360" y2="472" class="gd"/>
<rect x="445.0" y="12" width="120" height="36" rx="4" class="k-blue"/>
<text x="505.0" y="34.5" text-anchor="middle" class="kb-blue">:TcpScanner</text>
<line x1="505" y1="48" x2="505" y2="472" class="gd"/>
<rect x="590.0" y="12" width="120" height="36" rx="4" class="k-purple"/>
<text x="650.0" y="34.5" text-anchor="middle" class="kb-purple">:Check</text>
<line x1="650" y1="48" x2="650" y2="472" class="gd"/>
<rect x="65" y="70" width="10" height="396" class="act"/>
<rect x="210" y="82" width="10" height="378" class="act"/>
<line x1="75" y1="86" x2="210" y2="86" class="msg"/>
<text x="142" y="80" text-anchor="middle" class="s">run(targets)</text>
<line x1="220" y1="112" x2="355" y2="112" class="msg"/>
<text x="287" y="106" text-anchor="middle" class="s">expand(targets)</text>
<rect x="355" y="106" width="10" height="26" class="act"/>
<line x1="355" y1="136" x2="220" y2="136" class="ret"/>
<text x="287" y="130" text-anchor="middle" class="c">addresses</text>
<rect x="100" y="150" width="610" height="316" rx="4" class="zone" style="fill-opacity:0.35"/>
<path d="M100 150 L138.8 150 L138.8 166 L130.8 174 L100 174 z" class="zone"/>
<text x="108" y="167" text-anchor="start" class="b">alt</text>
<text x="226" y="170" text-anchor="start" class="c">[in scope]</text>
<line x1="220" y1="196" x2="500" y2="196" class="msg"/>
<text x="287" y="190" text-anchor="middle" class="s">scan(addresses)</text>
<rect x="500" y="190" width="10" height="28" class="act"/>
<line x1="500" y1="222" x2="220" y2="222" class="ret"/>
<text x="432" y="216" text-anchor="middle" class="c">hosts</text>
<path d="M220 240 L250 240 L250 256 L222 256" class="msg"/>
<text x="258" y="252" text-anchor="start" class="s">identify services</text>
<rect x="150" y="270" width="540" height="84" rx="4" class="zone" style="fill-opacity:0.35"/>
<path d="M150 270 L196.4 270 L196.4 286 L188.4 294 L150 294 z" class="zone"/>
<text x="158" y="287" text-anchor="start" class="b">loop</text>
<text x="244" y="292" text-anchor="start" class="c">[each check]</text>
<line x1="220" y1="316" x2="645" y2="316" class="msg"/>
<text x="287" y="310" text-anchor="middle" class="s">run(host, service)</text>
<rect x="645" y="310" width="10" height="26" class="act"/>
<line x1="645" y1="340" x2="220" y2="340" class="ret"/>
<text x="577" y="334" text-anchor="middle" class="c">findings</text>
<line x1="210" y1="374" x2="75" y2="374" class="ret"/>
<text x="142" y="368" text-anchor="middle" class="c">ScanResult</text>
<path d="M75 392 L105 392 L105 408 L77 408" class="msg"/>
<text x="112" y="404" text-anchor="start" class="s">save(result)</text>
<line x1="100" y1="420" x2="710" y2="420" class="ud"/>
<text x="226" y="440" text-anchor="start" class="c">[else]</text>
<line x1="210" y1="454" x2="75" y2="454" class="ret"/>
<text x="142" y="448" text-anchor="middle" class="c">ScopeError</text>
<text x="432" y="458" text-anchor="middle" class="kh-red">no traffic sent</text>
</g>
</svg>
<figcaption>Time runs downwards. Frames show alternatives (alt) and repetition (loop); dashed arrows are returns.</figcaption>
</figure>

Read it from top to bottom. Each participant has a **lifeline** (dashed); thin rectangles are **activations**, when a participant is busy. Solid arrows with filled heads are calls; dashed arrows are returns. **Combined fragments** add logic: `alt` for alternatives with guards in square brackets, `opt` for optional behaviour, `loop` for repetition, `par` for parallel execution.

This diagram documents requirement NW-SR-1 precisely: the scope check happens **before** the scanner is called, so an out-of-scope request never produces network traffic. The test `test_out_of_scope_target_never_reaches_the_scanner` in `tests/test_engine.py` checks exactly this ordering, using a fake scanner that records its calls.

## Activity diagrams

<figure class="diagram">
<svg viewBox="0 0 720 420" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Activity diagram for one assessment. Start, read scope and targets, then a decision: if any target is out of scope, report the error and stop. Otherwise a fork starts probing all hosts and ports concurrently; a join waits for all probes. Then fingerprint banners, run checks, and write the report. A decision asks whether to save; if yes, save to history. Then stop." xmlns="http://www.w3.org/2000/svg">
<style>
.s4i{ font-family:var(--sans),sans-serif; }
.s4i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4i .s{ fill:var(--text-dim); font-size:13px; }
.s4i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .c{ fill:var(--text-faint); font-size:12.5px; }
.s4i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4i-a); }
.s4i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4i-a); marker-start:url(#s4i-s); }
.s4i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4i-g); }
.s4i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-a); }
.s4i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4i-tri); }
.s4i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-tri); }
.s4i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4i-open); }
.s4i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-open); }
.s4i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4i-dia); }
.s4i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4i-odia); }
.s4i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4i-dia); marker-end:url(#s4i-open); }
.s4i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4i-solid); }
.s4i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4i-open); }
.s4i .fill{ fill:var(--text); stroke:none; }
.s4i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4i .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4i .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4i .ks-blue{ fill:#185FA5; font-size:13px; }
.s4i .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4i .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4i .kb-blue, :root[data-theme="dark"] .s4i .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4i .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4i .kh-blue{ fill:#85B7EB; }
.s4i .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4i-blue); }
.s4i .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-blue); }
.s4i .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4i .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4i .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4i .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4i .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4i .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4i .kb-teal, :root[data-theme="dark"] .s4i .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4i .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4i .kh-teal{ fill:#5DCAA5; }
.s4i .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4i-teal); }
.s4i .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-teal); }
.s4i .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4i .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4i .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4i .ks-amber{ fill:#854F0B; font-size:13px; }
.s4i .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4i .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4i .kb-amber, :root[data-theme="dark"] .s4i .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4i .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4i .kh-amber{ fill:#EF9F27; }
.s4i .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4i-amber); }
.s4i .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-amber); }
.s4i .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s4i .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4i .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4i .ks-purple{ fill:#534AB7; font-size:13px; }
.s4i .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4i .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4i .kb-purple, :root[data-theme="dark"] .s4i .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4i .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4i .kh-purple{ fill:#AFA9EC; }
.s4i .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4i-purple); }
.s4i .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-purple); }
.s4i .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s4i .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s4i .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s4i .ks-red{ fill:#A32D2D; font-size:13px; }
.s4i .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s4i .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4i .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s4i .kb-red, :root[data-theme="dark"] .s4i .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s4i .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s4i .kh-red{ fill:#F09595; }
.s4i .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s4i-red); }
.s4i .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4i-red); }
.s4i .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4i-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4i-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4i-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s4i-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s4i-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s4i">
<circle cx="120" cy="24" r="9" class="fill"/>
<line x1="120" y1="34" x2="120" y2="52" class="msg"/>
<rect x="20.0" y="54" width="200" height="36" rx="16" class="k-teal"/>
<text x="120.0" y="76.5" text-anchor="middle" class="kb-teal">read scope and targets</text>
<line x1="120" y1="90" x2="120" y2="106" class="msg"/>
<path d="M120 106 L138 124 L120 142 L102 124 z" class="k-amber"/>
<line x1="138" y1="124" x2="338" y2="124" class="msg"/>
<text x="240" y="116" text-anchor="middle" class="c">[target out of scope]</text>
<rect x="340.0" y="106" width="180" height="36" rx="16" class="k-red"/>
<text x="430.0" y="128.5" text-anchor="middle" class="kb-red">report ScopeError</text>
<line x1="520" y1="124" x2="586" y2="124" class="msg"/>
<circle cx="600" cy="124" r="11" class="act"/>
<circle cx="600" cy="124" r="6.5" class="fill"/>
<line x1="120" y1="142" x2="120" y2="162" class="msg"/>
<text x="128" y="156" text-anchor="start" class="c">[all in scope]</text>
<rect x="20" y="166" width="200" height="7" rx="2" class="fill"/>
<line x1="50" y1="174" x2="50" y2="190" class="msg"/>
<rect x="18.0" y="192" width="64" height="36" rx="16" class="k-blue"/>
<text x="50.0" y="214.5" text-anchor="middle" class="kb-blue">host 1</text>
<line x1="50" y1="228" x2="50" y2="244" class="msg"/>
<line x1="120" y1="174" x2="120" y2="190" class="msg"/>
<rect x="88.0" y="192" width="64" height="36" rx="16" class="k-blue"/>
<text x="120.0" y="214.5" text-anchor="middle" class="kb-blue">host 2</text>
<line x1="120" y1="228" x2="120" y2="244" class="msg"/>
<line x1="190" y1="174" x2="190" y2="190" class="msg"/>
<rect x="158.0" y="192" width="64" height="36" rx="16" class="k-blue"/>
<text x="190.0" y="214.5" text-anchor="middle" class="kb-blue">host n</text>
<line x1="190" y1="228" x2="190" y2="244" class="msg"/>
<rect x="20" y="246" width="200" height="7" rx="2" class="fill"/>
<line x1="120" y1="254" x2="120" y2="268" class="msg"/>
<rect x="20.0" y="270" width="200" height="36" rx="16" class="k-teal"/>
<text x="120.0" y="292.5" text-anchor="middle" class="kb-teal">fingerprint banners</text>
<line x1="220" y1="288" x2="268" y2="288" class="msg"/>
<rect x="270.0" y="270" width="180" height="36" rx="16" class="k-teal"/>
<text x="360.0" y="292.5" text-anchor="middle" class="kb-teal">run checks</text>
<line x1="450" y1="288" x2="500" y2="288" class="msg"/>
<rect x="500.0" y="270" width="180" height="36" rx="16" class="k-teal"/>
<text x="590.0" y="292.5" text-anchor="middle" class="kb-teal">write report</text>
<line x1="590" y1="306" x2="590" y2="326" class="msg"/>
<path d="M590 326 L608 344 L590 362 L572 344 z" class="k-amber"/>
<line x1="572" y1="344" x2="452" y2="344" class="msg"/>
<text x="512" y="336" text-anchor="middle" class="c">[save]</text>
<rect x="270.0" y="326" width="180" height="36" rx="16" class="k-purple"/>
<text x="360.0" y="348.5" text-anchor="middle" class="kb-purple">save to history</text>
<path d="M360 362 L360 396 L576 396" class="msg"/>
<path d="M590 362 L590 382" class="msg"/>
<text x="600" y="376" text-anchor="start" class="c">[--no-save]</text>
<circle cx="590" cy="396" r="11" class="act"/>
<circle cx="590" cy="396" r="6.5" class="fill"/>
<text x="240" y="210" text-anchor="start" class="c">fork: concurrent probes</text>
<text x="240" y="254" text-anchor="start" class="c">join: wait for all</text>
</g>
</svg>
<figcaption>Rounded boxes are actions, diamonds are decisions with guards, and bars fork and join concurrent flows.</figcaption>
</figure>

**Activity diagrams** are flowcharts with extras: decisions with **guards**, and **fork** and **join** bars for concurrency. They suit workflows and algorithms, including business processes that involve people. The fork here reflects NetWarden's design: all probes run concurrently with `asyncio`, limited to 100 at a time (NW-NFR-3), and the join waits for every probe to finish before fingerprinting begins.

## State machine diagrams

When an object's response to an event depends on its history, model it as a **state machine**.

<figure class="diagram">
<svg viewBox="0 0 720 350" style="width:100%;height:auto;max-width:720px" role="img" aria-label="State machine for a finding across scans. A finding seen for the first time is New. Seen again, it becomes Open. Not seen in a later scan, it becomes Resolved; if it reappears it becomes Reopened, then Open when confirmed. From Open, the owner may record Accepted risk, which returns to Open when the review date passes, or a reviewer may mark it a False positive, which ends its life." xmlns="http://www.w3.org/2000/svg">
<style>
.s4j{ font-family:var(--sans),sans-serif; }
.s4j .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4j .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4j .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4j .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4j .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4j .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4j .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4j .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4j .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4j .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4j .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4j .s{ fill:var(--text-dim); font-size:13px; }
.s4j .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4j .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .c{ fill:var(--text-faint); font-size:12.5px; }
.s4j .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4j .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4j .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4j .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4j-a); }
.s4j .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4j-a); marker-start:url(#s4j-s); }
.s4j .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4j-g); }
.s4j .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-a); }
.s4j .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4j .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4j .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4j .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4j .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4j .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4j-tri); }
.s4j .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-tri); }
.s4j .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4j-open); }
.s4j .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-open); }
.s4j .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4j-dia); }
.s4j .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4j-odia); }
.s4j .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4j-dia); marker-end:url(#s4j-open); }
.s4j .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4j-solid); }
.s4j .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4j-open); }
.s4j .fill{ fill:var(--text); stroke:none; }
.s4j .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4j .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4j .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4j .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4j .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4j .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4j .ks-amber{ fill:#854F0B; font-size:13px; }
.s4j .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4j .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4j .kb-amber, :root[data-theme="dark"] .s4j .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4j .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4j .kh-amber{ fill:#EF9F27; }
.s4j .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4j-amber); }
.s4j .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-amber); }
.s4j .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s4j .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4j .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4j .ks-purple{ fill:#534AB7; font-size:13px; }
.s4j .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4j .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4j .kb-purple, :root[data-theme="dark"] .s4j .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4j .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4j .kh-purple{ fill:#AFA9EC; }
.s4j .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4j-purple); }
.s4j .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-purple); }
.s4j .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s4j .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s4j .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s4j .ks-green{ fill:#3B6D11; font-size:13px; }
.s4j .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4j .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s4j .kb-green, :root[data-theme="dark"] .s4j .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s4j .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s4j .kh-green{ fill:#97C459; }
.s4j .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s4j-green); }
.s4j .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-green); }
.s4j .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s4j .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s4j .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s4j .ks-red{ fill:#A32D2D; font-size:13px; }
.s4j .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4j .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s4j .kb-red, :root[data-theme="dark"] .s4j .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s4j .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s4j .kh-red{ fill:#F09595; }
.s4j .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s4j-red); }
.s4j .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-red); }
.s4j .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s4j .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s4j .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s4j .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s4j .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s4j .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4j .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s4j .kb-gray, :root[data-theme="dark"] .s4j .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s4j .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s4j .kh-gray{ fill:#B4B2A9; }
.s4j .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s4j-gray); }
.s4j .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4j-gray); }
.s4j .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4j-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4j-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4j-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4j-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4j-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4j-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4j-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4j-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4j-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s4j-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s4j-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s4j-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s4j-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s4j">
<circle cx="30" cy="190" r="9" class="fill"/>
<rect x="60" y="170" width="110" height="40" rx="16" class="k-purple"/>
<text x="115.0" y="194.5" text-anchor="middle" class="kb-purple">New</text>
<rect x="270" y="170" width="120" height="40" rx="16" class="k-red"/>
<text x="330.0" y="194.5" text-anchor="middle" class="kb-red">Open</text>
<rect x="540" y="170" width="140" height="40" rx="16" class="k-green"/>
<text x="610.0" y="194.5" text-anchor="middle" class="kb-green">Resolved</text>
<rect x="230" y="60" width="200" height="40" rx="16" class="k-gray"/>
<text x="330.0" y="84.5" text-anchor="middle" class="kb-gray">Accepted risk</text>
<rect x="230" y="290" width="200" height="40" rx="16" class="k-gray"/>
<text x="330.0" y="314.5" text-anchor="middle" class="kb-gray">False positive</text>
<rect x="540" y="290" width="140" height="40" rx="16" class="k-amber"/>
<text x="610.0" y="314.5" text-anchor="middle" class="kb-amber">Reopened</text>
<circle cx="500" cy="310" r="11" class="act"/>
<circle cx="500" cy="310" r="6.5" class="fill"/>
<line x1="39" y1="190" x2="58" y2="190" class="msg"/>
<text x="20" y="228" text-anchor="start" class="c">first seen</text>
<line x1="170" y1="190" x2="268" y2="190" class="msg"/>
<text x="220" y="182" text-anchor="middle" class="c">seen again</text>
<line x1="390" y1="190" x2="538" y2="190" class="msg"/>
<text x="465" y="182" text-anchor="middle" class="c">not seen</text>
<path d="M115 168 C 115 -20, 610 -20, 610 168" class="msg"/>
<text x="590" y="110" text-anchor="end" class="c">not seen in next scan</text>
<line x1="305" y1="168" x2="305" y2="102" class="msg"/>
<text x="298" y="140" text-anchor="end" class="c">owner accepts</text>
<line x1="355" y1="102" x2="355" y2="168" class="msg"/>
<text x="362" y="140" text-anchor="start" class="c">review date passed</text>
<line x1="330" y1="212" x2="330" y2="288" class="msg"/>
<text x="322" y="255" text-anchor="end" class="c">reviewer rejects</text>
<line x1="610" y1="212" x2="610" y2="288" class="msg"/>
<text x="618" y="255" text-anchor="start" class="c">seen again</text>
<line x1="540" y1="300" x2="392" y2="205" class="msg"/>
<text x="500" y="245" text-anchor="start" class="c">confirmed</text>
<line x1="430" y1="310" x2="487" y2="310" class="msg"/>
</g>
</svg>
<figcaption>Version 1.0 computes New, Resolved and unchanged by comparing scans; this model is the design for version 1.1.</figcaption>
</figure>

States are rounded rectangles; **transitions** are arrows labelled with the triggering event, an optional guard in brackets, and an optional action after a slash: `event [guard] / action`. A filled circle is the initial state; a circled dot is a final state.

This diagram shows how findings should behave across repeated scans. Version 1.0 implements part of it, the comparison between two scans (`netwarden diff`) that classifies findings as new, resolved or unchanged. The full lifecycle with accepted risks and false positives is the design for version 1.1. Drawing it first exposed a question the team had not considered: when an accepted risk's review date passes, who is notified? Models are often most valuable for the questions they raise.

## Component and deployment diagrams

<figure class="diagram">
<svg viewBox="0 0 720 320" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Component diagram. The engine component provides the Assessment interface, which cli requires, and requires the Check, Scanner and KnowledgeBase interfaces, provided by the checks, scanner and knowledge components. The reporting component provides Reporter and the store component provides ScanRepository; cli requires both." xmlns="http://www.w3.org/2000/svg">
<style>
.s4k{ font-family:var(--sans),sans-serif; }
.s4k .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4k .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4k .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4k .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4k .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4k .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4k .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4k .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4k .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4k .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4k .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4k .s{ fill:var(--text-dim); font-size:13px; }
.s4k .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4k .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .c{ fill:var(--text-faint); font-size:12.5px; }
.s4k .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4k .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4k .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4k .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4k-a); }
.s4k .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4k-a); marker-start:url(#s4k-s); }
.s4k .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4k-g); }
.s4k .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-a); }
.s4k .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4k .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4k .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4k .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4k .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4k .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4k-tri); }
.s4k .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-tri); }
.s4k .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4k-open); }
.s4k .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-open); }
.s4k .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4k-dia); }
.s4k .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4k-odia); }
.s4k .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4k-dia); marker-end:url(#s4k-open); }
.s4k .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4k-solid); }
.s4k .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4k-open); }
.s4k .fill{ fill:var(--text); stroke:none; }
.s4k .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4k .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4k .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4k .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4k .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4k .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4k .ks-blue{ fill:#185FA5; font-size:13px; }
.s4k .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4k .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4k .kb-blue, :root[data-theme="dark"] .s4k .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4k .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4k .kh-blue{ fill:#85B7EB; }
.s4k .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4k-blue); }
.s4k .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-blue); }
.s4k .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4k .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4k .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4k .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4k .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4k .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4k .kb-teal, :root[data-theme="dark"] .s4k .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4k .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4k .kh-teal{ fill:#5DCAA5; }
.s4k .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4k-teal); }
.s4k .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-teal); }
.s4k .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4k .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4k .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4k .ks-amber{ fill:#854F0B; font-size:13px; }
.s4k .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4k .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4k .kb-amber, :root[data-theme="dark"] .s4k .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4k .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4k .kh-amber{ fill:#EF9F27; }
.s4k .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4k-amber); }
.s4k .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-amber); }
.s4k .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s4k .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4k .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4k .ks-purple{ fill:#534AB7; font-size:13px; }
.s4k .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4k .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4k .kb-purple, :root[data-theme="dark"] .s4k .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4k .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4k .kh-purple{ fill:#AFA9EC; }
.s4k .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4k-purple); }
.s4k .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-purple); }
.s4k .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s4k .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s4k .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s4k .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s4k .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s4k .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4k .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s4k .kb-gray, :root[data-theme="dark"] .s4k .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s4k .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s4k .kh-gray{ fill:#B4B2A9; }
.s4k .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s4k-gray); }
.s4k .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4k-gray); }
.s4k .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4k-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4k-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4k-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4k-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4k-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4k-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4k-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4k-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4k-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4k-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4k-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s4k-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s4k-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s4k">
<rect x="20" y="120" width="120" height="50" rx="3" class="k-gray"/>
<text x="80.0" y="140.5" text-anchor="middle" class="ks-gray">«component»</text>
<text x="80.0" y="158.5" text-anchor="middle" class="kb-gray">cli</text>
<rect x="118" y="126" width="14" height="10" rx="1" class="k-gray"/>
<rect x="115" y="128" width="6" height="2.5" rx="0" class="k-gray"/>
<rect x="115" y="132" width="6" height="2.5" rx="0" class="k-gray"/>
<rect x="240" y="120" width="130" height="50" rx="3" class="k-teal"/>
<text x="305.0" y="140.5" text-anchor="middle" class="ks-teal">«component»</text>
<text x="305.0" y="158.5" text-anchor="middle" class="kb-teal">engine</text>
<rect x="348" y="126" width="14" height="10" rx="1" class="k-teal"/>
<rect x="345" y="128" width="6" height="2.5" rx="0" class="k-teal"/>
<rect x="345" y="132" width="6" height="2.5" rx="0" class="k-teal"/>
<rect x="560" y="30" width="140" height="50" rx="3" class="k-purple"/>
<text x="630.0" y="50.5" text-anchor="middle" class="ks-purple">«component»</text>
<text x="630.0" y="68.5" text-anchor="middle" class="kb-purple">checks</text>
<rect x="678" y="36" width="14" height="10" rx="1" class="k-purple"/>
<rect x="675" y="38" width="6" height="2.5" rx="0" class="k-purple"/>
<rect x="675" y="42" width="6" height="2.5" rx="0" class="k-purple"/>
<rect x="560" y="120" width="140" height="50" rx="3" class="k-blue"/>
<text x="630.0" y="140.5" text-anchor="middle" class="ks-blue">«component»</text>
<text x="630.0" y="158.5" text-anchor="middle" class="kb-blue">scanner</text>
<rect x="678" y="126" width="14" height="10" rx="1" class="k-blue"/>
<rect x="675" y="128" width="6" height="2.5" rx="0" class="k-blue"/>
<rect x="675" y="132" width="6" height="2.5" rx="0" class="k-blue"/>
<rect x="560" y="210" width="140" height="50" rx="3" class="k-teal"/>
<text x="630.0" y="230.5" text-anchor="middle" class="ks-teal">«component»</text>
<text x="630.0" y="248.5" text-anchor="middle" class="kb-teal">knowledge</text>
<rect x="678" y="216" width="14" height="10" rx="1" class="k-teal"/>
<rect x="675" y="218" width="6" height="2.5" rx="0" class="k-teal"/>
<rect x="675" y="222" width="6" height="2.5" rx="0" class="k-teal"/>
<rect x="120" y="260" width="130" height="50" rx="3" class="k-amber"/>
<text x="185.0" y="280.5" text-anchor="middle" class="ks-amber">«component»</text>
<text x="185.0" y="298.5" text-anchor="middle" class="kb-amber">reporting</text>
<rect x="228" y="266" width="14" height="10" rx="1" class="k-amber"/>
<rect x="225" y="268" width="6" height="2.5" rx="0" class="k-amber"/>
<rect x="225" y="272" width="6" height="2.5" rx="0" class="k-amber"/>
<rect x="330" y="260" width="130" height="50" rx="3" class="k-amber"/>
<text x="395.0" y="280.5" text-anchor="middle" class="ks-amber">«component»</text>
<text x="395.0" y="298.5" text-anchor="middle" class="kb-amber">store</text>
<rect x="438" y="266" width="14" height="10" rx="1" class="k-amber"/>
<rect x="435" y="268" width="6" height="2.5" rx="0" class="k-amber"/>
<rect x="435" y="272" width="6" height="2.5" rx="0" class="k-amber"/>
<line x1="217" y1="145" x2="240" y2="145" class="u"/>
<circle cx="210" cy="145" r="7" class="act"/>
<path d="M204 135 A 10 10 0 0 0 204 155" class="u"/>
<line x1="140" y1="145" x2="194" y2="145" class="u"/>
<text x="210" y="176" text-anchor="middle" class="m">Assessment</text>
<line x1="527" y1="55" x2="560" y2="55" class="u"/>
<circle cx="520" cy="55" r="7" class="act"/>
<path d="M514 45 A 10 10 0 0 0 514 65" class="u"/>
<text x="530" y="39" text-anchor="middle" class="m">Check</text>
<path d="M504 55 L420 55 L420 145 L372 145" class="u"/>
<line x1="527" y1="145" x2="560" y2="145" class="u"/>
<circle cx="520" cy="145" r="7" class="act"/>
<path d="M514 135 A 10 10 0 0 0 514 155" class="u"/>
<text x="530" y="129" text-anchor="middle" class="m">Scanner</text>
<path d="M504 145 L372 145" class="u"/>
<line x1="527" y1="235" x2="560" y2="235" class="u"/>
<circle cx="520" cy="235" r="7" class="act"/>
<path d="M514 225 A 10 10 0 0 0 514 245" class="u"/>
<text x="530" y="219" text-anchor="middle" class="m">KnowledgeBase</text>
<path d="M504 235 L420 235 L420 145 L372 145" class="u"/>
<line x1="185" y1="229" x2="185" y2="260" class="u"/>
<circle cx="185" cy="222" r="7" class="act"/>
<path d="M175 216 A 10 10 0 0 1 195 216" class="u"/>
<text x="201" y="238" text-anchor="start" class="m">Reporter</text>
<line x1="395" y1="229" x2="395" y2="260" class="u"/>
<circle cx="395" cy="222" r="7" class="act"/>
<path d="M385 216 A 10 10 0 0 1 405 216" class="u"/>
<text x="379" y="238" text-anchor="end" class="m">ScanRepository</text>
<path d="M80 172 L80 200 L395 200 L395 206" class="u"/>
<line x1="185" y1="200" x2="185" y2="206" class="u"/>
</g>
</svg>
<figcaption>Balls (lollipops) are provided interfaces, sockets are required ones. A component can be replaced by any other that keeps its interfaces.</figcaption>
</figure>

A **component diagram** shows replaceable parts and the interfaces between them. A ball (lollipop) is an interface a component **provides**; a socket is one it **requires**. Any component that provides the same interface can be plugged in. For NetWarden, a future "live feed" component could replace the bundled knowledge base, as decided in ADR-0002.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Deployment diagram. An administrator workstation node runs a Python 3.13 execution environment containing the netwarden package artifact, the scope file and the netwarden.db history. It connects over TCP to target hosts in the lab network node: a web server, a file server and a database server. A CI runner node builds the container image artifact." xmlns="http://www.w3.org/2000/svg">
<style>
.s4l{ font-family:var(--sans),sans-serif; }
.s4l .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4l .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4l .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4l .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4l .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4l .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4l .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4l .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4l .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4l .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4l .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4l .s{ fill:var(--text-dim); font-size:13px; }
.s4l .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4l .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4l .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4l .c{ fill:var(--text-faint); font-size:12.5px; }
.s4l .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4l .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4l .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4l .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4l-a); }
.s4l .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4l-a); marker-start:url(#s4l-s); }
.s4l .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4l-g); }
.s4l .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-a); }
.s4l .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4l .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4l .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4l .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4l .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4l .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4l-tri); }
.s4l .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-tri); }
.s4l .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4l-open); }
.s4l .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-open); }
.s4l .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4l-dia); }
.s4l .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4l-odia); }
.s4l .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4l-dia); marker-end:url(#s4l-open); }
.s4l .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4l-solid); }
.s4l .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4l-open); }
.s4l .fill{ fill:var(--text); stroke:none; }
.s4l .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4l .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4l .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4l .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4l .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4l .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4l .ks-blue{ fill:#185FA5; font-size:13px; }
.s4l .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4l .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4l .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4l .kb-blue, :root[data-theme="dark"] .s4l .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4l .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4l .kh-blue{ fill:#85B7EB; }
.s4l .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4l-blue); }
.s4l .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-blue); }
.s4l .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4l .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4l .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4l .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4l .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4l .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4l .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4l .kb-teal, :root[data-theme="dark"] .s4l .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4l .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4l .kh-teal{ fill:#5DCAA5; }
.s4l .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4l-teal); }
.s4l .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-teal); }
.s4l .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4l .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4l .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4l .ks-purple{ fill:#534AB7; font-size:13px; }
.s4l .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4l .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4l .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4l .kb-purple, :root[data-theme="dark"] .s4l .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4l .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4l .kh-purple{ fill:#AFA9EC; }
.s4l .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4l-purple); }
.s4l .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-purple); }
.s4l .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s4l .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s4l .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s4l .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s4l .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s4l .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4l .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s4l .kb-gray, :root[data-theme="dark"] .s4l .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s4l .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s4l .kh-gray{ fill:#B4B2A9; }
.s4l .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s4l-gray); }
.s4l .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4l-gray); }
.s4l .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4l-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4l-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4l-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4l-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4l-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4l-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4l-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4l-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4l-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4l-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4l-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s4l-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s4l">
<path d="M20 40 L30 30 L330 30 L330 250 L320 260 L320 40 Z" class="k-gray" style="fill-opacity:0.6"/>
<line x1="320" y1="40" x2="330" y2="30" class="ln-gray"/>
<rect x="20" y="40" width="300" height="220" rx="0" class="k-gray"/>
<text x="170.0" y="60" text-anchor="middle" class="kb-gray">admin workstation</text>
<text x="170.0" y="76" text-anchor="middle" class="ks-gray">«device» Linux</text>
<rect x="40" y="90" width="260" height="150" rx="0" class="k-teal"/>
<text x="170" y="110" text-anchor="middle" class="ks-teal">«execution environment» Python 3.13</text>
<rect x="50" y="122" width="240" height="30" rx="2" class="pnl"/>
<text x="170.0" y="141.5" text-anchor="middle" class="m">«artifact» netwarden-1.0.0.whl</text>
<rect x="50" y="160" width="240" height="30" rx="2" class="pnl"/>
<text x="170.0" y="179.5" text-anchor="middle" class="m">«artifact» scope.txt</text>
<rect x="50" y="198" width="240" height="30" rx="2" class="pnl"/>
<text x="170.0" y="217.5" text-anchor="middle" class="m">«artifact» netwarden.db</text>
<path d="M430 40 L440 30 L710 30 L710 180 L700 190 L700 40 Z" class="k-blue" style="fill-opacity:0.6"/>
<line x1="700" y1="40" x2="710" y2="30" class="ln-blue"/>
<rect x="430" y="40" width="270" height="150" rx="0" class="k-blue"/>
<text x="565.0" y="60" text-anchor="middle" class="kb-blue">lab network</text>
<text x="565.0" y="76" text-anchor="middle" class="ks-blue">192.168.56.0/24</text>
<rect x="445" y="100" width="78" height="70" rx="0" class="k-blue"/>
<text x="484.0" y="130.5" text-anchor="middle" class="kb-blue">web</text>
<text x="484.0" y="148.5" text-anchor="middle" class="ks-blue">server</text>
<rect x="530" y="100" width="78" height="70" rx="0" class="k-blue"/>
<text x="569.0" y="130.5" text-anchor="middle" class="kb-blue">file</text>
<text x="569.0" y="148.5" text-anchor="middle" class="ks-blue">server</text>
<rect x="615" y="100" width="78" height="70" rx="0" class="k-blue"/>
<text x="654.0" y="130.5" text-anchor="middle" class="kb-blue">db</text>
<text x="654.0" y="148.5" text-anchor="middle" class="ks-blue">server</text>
<line x1="322" y1="120" x2="428" y2="120" class="u"/>
<text x="375" y="112" text-anchor="middle" class="c">TCP</text>
<text x="375" y="136" text-anchor="middle" class="c">connect</text>
<path d="M430 220 L440 210 L710 210 L710 270 L700 280 L700 220 Z" class="k-purple" style="fill-opacity:0.6"/>
<line x1="700" y1="220" x2="710" y2="210" class="ln-purple"/>
<rect x="430" y="220" width="270" height="60" rx="0" class="k-purple"/>
<text x="565.0" y="240" text-anchor="middle" class="kb-purple">CI runner</text>
<text x="565.0" y="256" text-anchor="middle" class="ks-purple">builds netwarden image</text>
</g>
</svg>
<figcaption>Deployment diagrams show where software runs and how nodes communicate, which matters for security and operations.</figcaption>
</figure>

A **deployment diagram** shows physical **nodes** (devices and execution environments) and the **artifacts** deployed on them. For a security tool, this view matters: it shows that the history database, a list of every weakness found, sits on the administrator's workstation and must be protected (Chapter 12).

## The C4 model

UML is precise but can feel heavy for describing architecture to a mixed audience. Simon Brown's **C4 model** uses four levels of zoom with simple boxes and labelled arrows: **Context**, **Containers**, **Components** and **Code**.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="C4 system context diagram. People: the network administrator runs assessments and reads reports; the security manager reviews reports and trends. NetWarden, the software system, scans the target hosts on the lab network over TCP and is run by the CI pipeline on a schedule. A vulnerability feed such as NVD or OSV is a planned future data source." xmlns="http://www.w3.org/2000/svg">
<style>
.s4m{ font-family:var(--sans),sans-serif; }
.s4m .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4m .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4m .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4m .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4m .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4m .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4m .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4m .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4m .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4m .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4m .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4m .s{ fill:var(--text-dim); font-size:13px; }
.s4m .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4m .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4m .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4m .c{ fill:var(--text-faint); font-size:12.5px; }
.s4m .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4m .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4m .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4m .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4m-a); }
.s4m .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4m-a); marker-start:url(#s4m-s); }
.s4m .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4m-g); }
.s4m .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4m-a); }
.s4m .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4m .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4m .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4m .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4m .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4m .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4m-tri); }
.s4m .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4m-tri); }
.s4m .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4m-open); }
.s4m .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4m-open); }
.s4m .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4m-dia); }
.s4m .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4m-odia); }
.s4m .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4m-dia); marker-end:url(#s4m-open); }
.s4m .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4m-solid); }
.s4m .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4m-open); }
.s4m .fill{ fill:var(--text); stroke:none; }
.s4m .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4m .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4m .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4m .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4m .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4m .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4m .ks-blue{ fill:#185FA5; font-size:13px; }
.s4m .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4m .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4m .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4m .kb-blue, :root[data-theme="dark"] .s4m .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4m .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4m .kh-blue{ fill:#85B7EB; }
.s4m .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4m-blue); }
.s4m .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4m-blue); }
.s4m .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4m .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4m .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4m .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4m .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4m .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4m .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4m .kb-teal, :root[data-theme="dark"] .s4m .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4m .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4m .kh-teal{ fill:#5DCAA5; }
.s4m .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4m-teal); }
.s4m .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4m-teal); }
.s4m .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4m .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s4m .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s4m .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s4m .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s4m .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4m .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s4m .kb-gray, :root[data-theme="dark"] .s4m .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s4m .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s4m .kh-gray{ fill:#B4B2A9; }
.s4m .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s4m-gray); }
.s4m .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4m-gray); }
.s4m .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4m-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4m-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4m-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4m-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4m-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4m-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4m-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4m-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4m-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4m-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4m-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s4m">
<circle cx="110" cy="24" r="14" class="k-blue"/>
<rect x="20" y="36" width="180" height="56" rx="14" class="k-blue"/>
<text x="110.0" y="59.5" text-anchor="middle" class="kb-blue">administrator</text>
<text x="110.0" y="77.5" text-anchor="middle" class="ks-blue">runs assessments</text>
<circle cx="110" cy="194" r="14" class="k-blue"/>
<rect x="20" y="206" width="180" height="56" rx="14" class="k-blue"/>
<text x="110.0" y="229.5" text-anchor="middle" class="kb-blue">security manager</text>
<text x="110.0" y="247.5" text-anchor="middle" class="ks-blue">reviews reports</text>
<rect x="270" y="110" width="180" height="80" rx="7" class="k-teal"/>
<text x="360.0" y="136.5" text-anchor="middle" class="kb-teal">NetWarden</text>
<text x="360.0" y="154.5" text-anchor="middle" class="ks-teal">[software system]</text>
<text x="360.0" y="172.5" text-anchor="middle" class="ks-teal">assesses services</text>
<rect x="530" y="20" width="170" height="70" rx="7" class="k-gray"/>
<text x="615.0" y="50.5" text-anchor="middle" class="kb-gray">target hosts</text>
<text x="615.0" y="68.5" text-anchor="middle" class="ks-gray">[external system]</text>
<rect x="530" y="120" width="170" height="70" rx="7" class="k-gray"/>
<text x="615.0" y="150.5" text-anchor="middle" class="kb-gray">CI pipeline</text>
<text x="615.0" y="168.5" text-anchor="middle" class="ks-gray">[external system]</text>
<rect x="530" y="220" width="170" height="70" rx="7" class="k-gray"/>
<text x="615.0" y="250.5" text-anchor="middle" class="kb-gray">vulnerability feed</text>
<text x="615.0" y="268.5" text-anchor="middle" class="ks-gray">[future: NVD, OSV]</text>
<line x1="200" y1="62" x2="268" y2="124" class="assoc"/>
<text x="216" y="112" text-anchor="middle" class="c">uses</text>
<line x1="200" y1="232" x2="268" y2="176" class="assoc"/>
<text x="206" y="252" text-anchor="start" class="c">reads reports</text>
<line x1="452" y1="130" x2="528" y2="60" class="assoc"/>
<text x="470" y="80" text-anchor="end" class="c">scans [TCP]</text>
<line x1="528" y1="155" x2="452" y2="150" class="assoc"/>
<text x="490" y="142" text-anchor="middle" class="c">runs</text>
<line x1="452" y1="176" x2="528" y2="250" class="dep"/>
<text x="480" y="232" text-anchor="middle" class="c">reads</text>
</g>
</svg>
<figcaption>C4 level 1: the system as one box, with the people and systems around it. Anyone can read it.</figcaption>
</figure>

The **system context** diagram shows the system as a single box among its users and neighbouring systems. It is the diagram to show a manager or a new team member first.

<figure class="diagram">
<svg viewBox="0 0 720 310" style="width:100%;height:auto;max-width:720px" role="img" aria-label="C4 container diagram for NetWarden. Inside the system boundary: the command-line application, written in Python, reads the knowledge base JSON file, writes scan history to a SQLite database, and writes report files in Markdown, JSON or HTML. The administrator uses the command-line application, which scans target hosts over TCP." xmlns="http://www.w3.org/2000/svg">
<style>
.s4n{ font-family:var(--sans),sans-serif; }
.s4n .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s4n .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s4n .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s4n .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s4n .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s4n .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s4n .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s4n .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s4n .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s4n .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s4n .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s4n .s{ fill:var(--text-dim); font-size:13px; }
.s4n .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s4n .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s4n .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s4n .c{ fill:var(--text-faint); font-size:12.5px; }
.s4n .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s4n .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s4n .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s4n .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4n-a); }
.s4n .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s4n-a); marker-start:url(#s4n-s); }
.s4n .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s4n-g); }
.s4n .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-a); }
.s4n .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s4n .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s4n .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s4n .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s4n .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s4n .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4n-tri); }
.s4n .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-tri); }
.s4n .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4n-open); }
.s4n .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-open); }
.s4n .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4n-dia); }
.s4n .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4n-odia); }
.s4n .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s4n-dia); marker-end:url(#s4n-open); }
.s4n .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s4n-solid); }
.s4n .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s4n-open); }
.s4n .fill{ fill:var(--text); stroke:none; }
.s4n .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s4n .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s4n .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s4n .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s4n .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s4n .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s4n .ks-blue{ fill:#185FA5; font-size:13px; }
.s4n .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s4n .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4n .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s4n .kb-blue, :root[data-theme="dark"] .s4n .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s4n .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s4n .kh-blue{ fill:#85B7EB; }
.s4n .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s4n-blue); }
.s4n .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-blue); }
.s4n .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s4n .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s4n .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s4n .ks-teal{ fill:#0F6E56; font-size:13px; }
.s4n .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s4n .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4n .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s4n .kb-teal, :root[data-theme="dark"] .s4n .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s4n .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s4n .kh-teal{ fill:#5DCAA5; }
.s4n .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s4n-teal); }
.s4n .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-teal); }
.s4n .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s4n .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s4n .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s4n .ks-amber{ fill:#854F0B; font-size:13px; }
.s4n .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s4n .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4n .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s4n .kb-amber, :root[data-theme="dark"] .s4n .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s4n .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s4n .kh-amber{ fill:#EF9F27; }
.s4n .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s4n-amber); }
.s4n .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-amber); }
.s4n .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s4n .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s4n .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s4n .ks-purple{ fill:#534AB7; font-size:13px; }
.s4n .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s4n .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s4n .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s4n .kb-purple, :root[data-theme="dark"] .s4n .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s4n .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s4n .kh-purple{ fill:#AFA9EC; }
.s4n .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s4n-purple); }
.s4n .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s4n-purple); }
.s4n .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s4n-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s4n-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s4n-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s4n-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s4n-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s4n-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s4n-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s4n-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s4n-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s4n-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s4n-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s4n-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s4n">
<rect x="170" y="20" width="530" height="270" rx="8" class="zone"/>
<text x="185" y="42" text-anchor="start" class="b">NetWarden [software system]</text>
<rect x="20" y="130" width="130" height="60" rx="14" class="k-blue"/>
<text x="85.0" y="155.5" text-anchor="middle" class="kb-blue">administrator</text>
<text x="85.0" y="173.5" text-anchor="middle" class="ks-blue">[person]</text>
<rect x="250" y="120" width="190" height="80" rx="7" class="k-teal"/>
<text x="345.0" y="146.5" text-anchor="middle" class="kb-teal">command-line app</text>
<text x="345.0" y="164.5" text-anchor="middle" class="ks-teal">[Python 3.13]</text>
<text x="345.0" y="182.5" text-anchor="middle" class="ks-teal">scan, report, diff</text>
<rect x="500" y="50" width="180" height="64" rx="7" class="k-purple"/>
<text x="590.0" y="77.5" text-anchor="middle" class="kb-purple">knowledge base</text>
<text x="590.0" y="95.5" text-anchor="middle" class="ks-purple">[JSON file]</text>
<rect x="500" y="130" width="180" height="64" rx="7" class="k-purple"/>
<text x="590.0" y="157.5" text-anchor="middle" class="kb-purple">scan history</text>
<text x="590.0" y="175.5" text-anchor="middle" class="ks-purple">[SQLite database]</text>
<rect x="500" y="210" width="180" height="64" rx="7" class="k-amber"/>
<text x="590.0" y="237.5" text-anchor="middle" class="kb-amber">reports</text>
<text x="590.0" y="255.5" text-anchor="middle" class="ks-amber">[MD, JSON, HTML files]</text>
<line x1="152" y1="160" x2="248" y2="160" class="assoc"/>
<text x="200" y="152" text-anchor="middle" class="c">runs</text>
<line x1="442" y1="140" x2="498" y2="86" class="assoc"/>
<text x="430" y="100" text-anchor="end" class="c">reads</text>
<line x1="442" y1="160" x2="498" y2="162" class="assoc"/>
<text x="470" y="150" text-anchor="middle" class="c">writes</text>
<line x1="442" y1="180" x2="498" y2="236" class="assoc"/>
<text x="450" y="226" text-anchor="end" class="c">writes</text>
<line x1="345" y1="202" x2="345" y2="290" class="assoc"/>
<text x="352" y="270" text-anchor="start" class="c">scans target hosts [TCP]</text>
</g>
</svg>
<figcaption>C4 level 2: the deployable or storable pieces and how they talk. Level 3 would show the components inside the app.</figcaption>
</figure>

The **container** diagram zooms in. A C4 "container" is anything that runs or stores data separately: an application, a database, a file store. (It is not the same as a Docker container, though one often maps onto the other.) Level 3 shows the components inside one container, much like the component diagram above, and level 4 is code, for which a UML class diagram is used.

C4's rules are few: every box has a name, a type in brackets, and a short description; every arrow has a label saying what flows; every diagram has a title and a key. Following them makes diagrams that can be understood without the author present.

## Diagrams as code

Diagrams drawn by hand drift out of date. **Diagrams as code** tools generate them from text that lives in the repository and is reviewed like code:

```text
@startuml
interface Check {
  +id: str
  +run(host, service): list[Finding]
}
class HttpHeadersCheck
Check <|.. HttpHeadersCheck
@enduml
```

That is **PlantUML** syntax; **Mermaid** is a similar language that GitHub renders directly in Markdown files, and **Structurizr** supports C4. Some tools also reverse-engineer class diagrams from code, such as `pyreverse` from the Pylint project:

```bash
pip install pylint
pyreverse -o png -p netwarden src/netwarden
```

## Good modelling habits

- Draw a diagram to answer a **specific question**, and leave out everything that does not help answer it.
- Prefer **several small diagrams** to one diagram of everything.
- Give every diagram a **title, a key** where colours or styles carry meaning, and a date or version.
- Keep long-lived diagrams **in the repository**, next to the code, ideally as code.
- Remember the audience: C4 context for everyone; detailed UML for the developers who need it.

## Summary

- Models are simplified views used to **sketch**, **specify**, or (rarely) **execute**.
- **UML 2.5** has 14 diagram types: **structure** (class, object, component, package, deployment) and **behaviour** (use case, activity, state machine, sequence and other interactions).
- **Class diagrams** show classes, attributes, operations and relationships: association, aggregation, composition, generalization, realization, dependency, with multiplicities.
- **Sequence diagrams** show collaboration over time, with `alt`, `opt` and `loop` fragments.
- **Activity diagrams** show workflows with decisions and concurrency; **state machines** show behaviour that depends on history.
- **Component** and **deployment** diagrams show replaceable parts and where software runs.
- The **C4 model** describes architecture at four levels of zoom with simple, labelled boxes.
- Keep diagrams small, focused and versioned, ideally as **diagrams as code**.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-4-modelling-with-uml-and-c4).

**1. What is a model, in the chapter's sense?**

- A. A full copy of the code
- B. A simplified representation built to answer particular questions
- C. A prototype
- D. A test suite

**2. Which relationship means the part is created and destroyed with the whole, like a ScanResult and its Findings?**

- A. Association
- B. Aggregation
- C. Composition
- D. Dependency

**3. In UML, which relationship is a class implementing an interface?**

- A. Realization
- B. Generalization
- C. Association
- D. Dependency

**4. What does the multiplicity 1..* mean?**

- A. One or more
- B. Exactly one
- C. Zero or one
- D. Any number, including zero

**5. In a sequence diagram, what does an alt fragment show?**

- A. A loop
- B. An optional step
- C. Alternative paths, chosen by guards
- D. A parallel step

**6. When should you model something as a state machine?**

- A. When it has many attributes
- B. When its response to an event depends on its history
- C. When it is stored in a database
- D. When it is deployed on a server

**7. What is a C4 container?**

- A. Always a Docker container
- B. A UML package
- C. A class with many attributes
- D. Anything that runs or stores data separately: an application, a database, a file store

**8. Why keep diagrams as code in the repository?**

- A. They render faster
- B. They are reviewed and versioned with the code, so they drift out of date less
- C. UML requires it
- D. They replace documentation
