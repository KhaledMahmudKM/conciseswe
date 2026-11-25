# Chapter 15: Maintenance and Evolution

Release 1.0 is not the end of a software project; for successful software it is the beginning. Users find new uses, platforms change, dependencies release new versions, vulnerabilities are disclosed, and the business changes its mind. **Software maintenance** is everything done to software after delivery. It is usually the largest part of a system's lifetime cost, and the reason so many of the practices in this book exist.

## Why software must change

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The lifecycle cost iceberg: initial development is the visible part above the waterline; below it, years of maintenance and evolution: corrective fixes, adaptation to new platforms, new features, dependency and security updates, operations and support, which together usually cost more than the first release." xmlns="http://www.w3.org/2000/svg">
<style>
.s15b{ font-family:var(--sans),sans-serif; }
.s15b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s15b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s15b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s15b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s15b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s15b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s15b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s15b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s15b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s15b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s15b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s15b .s{ fill:var(--text-dim); font-size:13px; }
.s15b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s15b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s15b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s15b .c{ fill:var(--text-faint); font-size:12.5px; }
.s15b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s15b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s15b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s15b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15b-a); }
.s15b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15b-a); marker-start:url(#s15b-s); }
.s15b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s15b-g); }
.s15b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s15b-a); }
.s15b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s15b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s15b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s15b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s15b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s15b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15b-tri); }
.s15b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15b-tri); }
.s15b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15b-open); }
.s15b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15b-open); }
.s15b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15b-dia); }
.s15b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15b-odia); }
.s15b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15b-dia); marker-end:url(#s15b-open); }
.s15b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15b-solid); }
.s15b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s15b-open); }
.s15b .fill{ fill:var(--text); stroke:none; }
.s15b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s15b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s15b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s15b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s15b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s15b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s15b .ks-blue{ fill:#185FA5; font-size:13px; }
.s15b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s15b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s15b .kb-blue, :root[data-theme="dark"] .s15b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s15b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s15b .kh-blue{ fill:#85B7EB; }
.s15b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s15b-blue); }
.s15b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15b-blue); }
.s15b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s15b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s15b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s15b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s15b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s15b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s15b .kb-teal, :root[data-theme="dark"] .s15b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s15b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s15b .kh-teal{ fill:#5DCAA5; }
.s15b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s15b-teal); }
.s15b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15b-teal); }
.s15b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s15b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s15b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s15b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s15b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s15b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s15b .kb-gray, :root[data-theme="dark"] .s15b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s15b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s15b .kh-gray{ fill:#B4B2A9; }
.s15b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s15b-gray); }
.s15b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15b-gray); }
.s15b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s15b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s15b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s15b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s15b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s15b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s15b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s15b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s15b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s15b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s15b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s15b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s15b">
<path d="M300 30 L420 30 L470 110 L250 110 Z" class="k-blue"/>
<text x="360" y="80" text-anchor="middle" class="kb-blue">development</text>
<line x1="40" y1="112" x2="680" y2="112" class="ln-teal"/>
<text x="690" y="108" text-anchor="end" class="kh-teal">waterline</text>
<path d="M250 114 L470 114 L600 270 L120 270 Z" class="k-gray"/>
<text x="360" y="140" text-anchor="middle" class="kb-gray">bug fixes</text>
<text x="360" y="165" text-anchor="middle" class="kb-gray">new platforms and versions</text>
<text x="360" y="190" text-anchor="middle" class="kb-gray">new features</text>
<text x="360" y="215" text-anchor="middle" class="kb-gray">security and dependency updates</text>
<text x="360" y="240" text-anchor="middle" class="kb-gray">operations and support</text>
</g>
</svg>
<figcaption>Successful software is never finished. Design for the decades of change, not just the first release.</figcaption>
</figure>

Surveys over several decades have consistently found that maintenance and evolution consume more effort than initial development, often much more. The exact share varies with the system and the study, but the lesson is stable: a design decision that makes change cheaper pays for itself many times over.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A selection of Lehman&#x27;s laws of software evolution: continuing change, a system must keep adapting or become less useful; increasing complexity, complexity grows unless work is done to reduce it; continuing growth, functionality must grow to keep users satisfied; declining quality, quality appears to decline unless the system is actively maintained; and feedback system, evolution is a multi-loop feedback process." xmlns="http://www.w3.org/2000/svg">
<style>
.s15d{ font-family:var(--sans),sans-serif; }
.s15d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s15d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s15d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s15d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s15d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s15d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s15d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s15d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s15d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s15d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s15d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s15d .s{ fill:var(--text-dim); font-size:13px; }
.s15d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s15d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s15d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s15d .c{ fill:var(--text-faint); font-size:12.5px; }
.s15d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s15d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s15d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s15d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15d-a); }
.s15d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15d-a); marker-start:url(#s15d-s); }
.s15d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s15d-g); }
.s15d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s15d-a); }
.s15d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s15d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s15d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s15d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s15d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s15d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15d-tri); }
.s15d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15d-tri); }
.s15d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15d-open); }
.s15d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15d-open); }
.s15d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15d-dia); }
.s15d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15d-odia); }
.s15d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15d-dia); marker-end:url(#s15d-open); }
.s15d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15d-solid); }
.s15d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s15d-open); }
.s15d .fill{ fill:var(--text); stroke:none; }
.s15d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s15d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s15d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s15d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s15d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s15d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s15d .ks-purple{ fill:#534AB7; font-size:13px; }
.s15d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s15d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s15d .kb-purple, :root[data-theme="dark"] .s15d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s15d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s15d .kh-purple{ fill:#AFA9EC; }
.s15d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s15d-purple); }
.s15d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15d-purple); }
.s15d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s15d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s15d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s15d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s15d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s15d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s15d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s15d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s15d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s15d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s15d">
<rect x="20" y="14" width="220" height="44" rx="4" class="k-purple"/>
<text x="130.0" y="40.5" text-anchor="middle" class="kb-purple">continuing change</text>
<text x="256" y="41" text-anchor="start" class="s">adapt, or become progressively less useful</text>
<rect x="20" y="70" width="220" height="44" rx="4" class="k-purple"/>
<text x="130.0" y="96.5" text-anchor="middle" class="kb-purple">increasing complexity</text>
<text x="256" y="97" text-anchor="start" class="s">grows unless work is done to reduce it</text>
<rect x="20" y="126" width="220" height="44" rx="4" class="k-purple"/>
<text x="130.0" y="152.5" text-anchor="middle" class="kb-purple">continuing growth</text>
<text x="256" y="153" text-anchor="start" class="s">functionality must grow to satisfy users</text>
<rect x="20" y="182" width="220" height="44" rx="4" class="k-purple"/>
<text x="130.0" y="208.5" text-anchor="middle" class="kb-purple">declining quality</text>
<text x="256" y="209" text-anchor="start" class="s">unless actively maintained and adapted</text>
<rect x="20" y="238" width="220" height="44" rx="4" class="k-purple"/>
<text x="130.0" y="264.5" text-anchor="middle" class="kb-purple">feedback system</text>
<text x="256" y="265" text-anchor="start" class="s">evolution is driven by feedback loops</text>
</g>
</svg>
<figcaption>Meir Lehman studied large systems such as IBM's OS/360 from the 1970s. His laws describe systems used in the real world.</figcaption>
</figure>

Meir Lehman, studying IBM's OS/360 and other large systems from the 1970s onwards, formulated **laws of software evolution** for systems used in the real world. The first two are the most quoted: such systems must continually change or become less useful, and as they change their complexity increases unless work is done to reduce it. Refactoring (Chapter 10) is that work.

## Kinds of maintenance

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Types of maintenance from ISO/IEC/IEEE 14764 with NetWarden examples: corrective, fixing defects, such as the ProFTPD version bug; adaptive, keeping up with a changing environment, such as a new Python version or a changed banner format; perfective, improving functionality or performance, such as a CSV report; preventive, reducing future problems, such as refactoring or updating dependencies. Lientz and Swanson&#x27;s classic survey found most effort went to non-corrective work." xmlns="http://www.w3.org/2000/svg">
<style>
.s15a{ font-family:var(--sans),sans-serif; }
.s15a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s15a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s15a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s15a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s15a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s15a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s15a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s15a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s15a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s15a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s15a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s15a .s{ fill:var(--text-dim); font-size:13px; }
.s15a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s15a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s15a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s15a .c{ fill:var(--text-faint); font-size:12.5px; }
.s15a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s15a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s15a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s15a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15a-a); }
.s15a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15a-a); marker-start:url(#s15a-s); }
.s15a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s15a-g); }
.s15a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-a); }
.s15a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s15a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s15a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s15a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s15a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s15a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15a-tri); }
.s15a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-tri); }
.s15a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15a-open); }
.s15a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-open); }
.s15a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15a-dia); }
.s15a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15a-odia); }
.s15a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15a-dia); marker-end:url(#s15a-open); }
.s15a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15a-solid); }
.s15a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s15a-open); }
.s15a .fill{ fill:var(--text); stroke:none; }
.s15a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s15a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s15a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s15a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s15a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s15a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s15a .ks-blue{ fill:#185FA5; font-size:13px; }
.s15a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s15a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s15a .kb-blue, :root[data-theme="dark"] .s15a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s15a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s15a .kh-blue{ fill:#85B7EB; }
.s15a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s15a-blue); }
.s15a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-blue); }
.s15a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s15a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s15a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s15a .ks-amber{ fill:#854F0B; font-size:13px; }
.s15a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s15a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s15a .kb-amber, :root[data-theme="dark"] .s15a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s15a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s15a .kh-amber{ fill:#EF9F27; }
.s15a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s15a-amber); }
.s15a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-amber); }
.s15a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s15a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s15a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s15a .ks-green{ fill:#3B6D11; font-size:13px; }
.s15a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s15a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s15a .kb-green, :root[data-theme="dark"] .s15a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s15a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s15a .kh-green{ fill:#97C459; }
.s15a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s15a-green); }
.s15a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-green); }
.s15a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s15a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s15a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s15a .ks-red{ fill:#A32D2D; font-size:13px; }
.s15a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s15a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s15a .kb-red, :root[data-theme="dark"] .s15a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s15a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s15a .kh-red{ fill:#F09595; }
.s15a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s15a-red); }
.s15a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15a-red); }
.s15a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s15a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s15a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s15a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s15a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s15a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s15a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s15a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s15a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s15a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s15a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s15a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s15a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s15a">
<rect x="20" y="16" width="330" height="84" rx="7" class="k-red"/>
<text x="185.0" y="40.5" text-anchor="middle" class="kb-red">corrective</text>
<text x="185.0" y="62.5" text-anchor="middle" class="ks-red">fix defects</text>
<text x="185.0" y="84.5" text-anchor="middle" class="km-red">ProFTPD 1.3.5a compared wrongly</text>
<rect x="370" y="16" width="330" height="84" rx="7" class="k-amber"/>
<text x="535.0" y="40.5" text-anchor="middle" class="kb-amber">adaptive</text>
<text x="535.0" y="62.5" text-anchor="middle" class="ks-amber">keep up with the environment</text>
<text x="535.0" y="84.5" text-anchor="middle" class="km-amber">add Python 3.14; new banner formats</text>
<rect x="20" y="116" width="330" height="84" rx="7" class="k-blue"/>
<text x="185.0" y="140.5" text-anchor="middle" class="kb-blue">perfective</text>
<text x="185.0" y="162.5" text-anchor="middle" class="ks-blue">improve or extend</text>
<text x="185.0" y="184.5" text-anchor="middle" class="km-blue">CSV report; faster scans</text>
<rect x="370" y="116" width="330" height="84" rx="7" class="k-green"/>
<text x="535.0" y="140.5" text-anchor="middle" class="kb-green">preventive</text>
<text x="535.0" y="162.5" text-anchor="middle" class="ks-green">prevent future problems</text>
<text x="535.0" y="184.5" text-anchor="middle" class="km-green">refactor; update dependencies</text>
<text x="360" y="240" text-anchor="middle" class="c">Lientz and Swanson (1980): roughly half of maintenance effort was perfective; only about a fifth corrective</text>
</g>
</svg>
<figcaption>Most "maintenance" is not fixing bugs. It is changing working software because the world around it changed.</figcaption>
</figure>

The four classic categories, used by the ISO/IEC/IEEE 14764 maintenance standard, are:

| Type | Purpose | NetWarden example |
|---|---|---|
| **Corrective** | Fix defects found after release | ProFTPD `1.3.5a` was compared as equal to `1.3.5`; fixed in 0.2.0 |
| **Adaptive** | Keep working in a changed environment | Support Python 3.14; new banner formats; a new OpenSSH release |
| **Perfective** | Improve or add functionality, performance, usability | A CSV report; faster scans; IPv6 targets |
| **Preventive** | Reduce the risk of future problems | Refactoring; dependency updates; more tests |

Lientz and Swanson's classic 1980 survey of data processing departments found that roughly half of maintenance effort was perfective and only about a fifth corrective. "Maintenance" is mostly **evolution**, not repair.

## A maintenance story: banners and backports

The real world quickly finds the edges of any design. NetWarden 1.0 decides whether OpenSSH is vulnerable to regreSSHion (CVE-2024-6387) by comparing the version in its banner with the affected range, 8.5p1 up to but not including 9.8p1.

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A real maintenance problem behind backlog item US-11. Ubuntu fixed regreSSHion in its OpenSSH 8.9p1 package by backporting the patch, so the banner of the fixed package, OpenSSH_8.9p1 Ubuntu-3ubuntu0.10, still reports version 8.9p1. NetWarden compares only the upstream version, so it reports CVE-2024-6387 on a patched server: a false positive. The fix needs distribution-specific data, such as Ubuntu&#x27;s security notices or OSV ecosystem records." xmlns="http://www.w3.org/2000/svg">
<style>
.s15c{ font-family:var(--sans),sans-serif; }
.s15c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s15c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s15c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s15c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s15c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s15c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s15c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s15c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s15c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s15c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s15c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s15c .s{ fill:var(--text-dim); font-size:13px; }
.s15c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s15c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s15c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s15c .c{ fill:var(--text-faint); font-size:12.5px; }
.s15c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s15c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s15c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s15c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15c-a); }
.s15c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15c-a); marker-start:url(#s15c-s); }
.s15c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s15c-g); }
.s15c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-a); }
.s15c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s15c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s15c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s15c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s15c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s15c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15c-tri); }
.s15c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-tri); }
.s15c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15c-open); }
.s15c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-open); }
.s15c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15c-dia); }
.s15c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15c-odia); }
.s15c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15c-dia); marker-end:url(#s15c-open); }
.s15c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15c-solid); }
.s15c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s15c-open); }
.s15c .fill{ fill:var(--text); stroke:none; }
.s15c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s15c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s15c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s15c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s15c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s15c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s15c .ks-blue{ fill:#185FA5; font-size:13px; }
.s15c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s15c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s15c .kb-blue, :root[data-theme="dark"] .s15c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s15c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s15c .kh-blue{ fill:#85B7EB; }
.s15c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s15c-blue); }
.s15c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-blue); }
.s15c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s15c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s15c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s15c .ks-amber{ fill:#854F0B; font-size:13px; }
.s15c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s15c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s15c .kb-amber, :root[data-theme="dark"] .s15c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s15c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s15c .kh-amber{ fill:#EF9F27; }
.s15c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s15c-amber); }
.s15c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-amber); }
.s15c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s15c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s15c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s15c .ks-green{ fill:#3B6D11; font-size:13px; }
.s15c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s15c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s15c .kb-green, :root[data-theme="dark"] .s15c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s15c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s15c .kh-green{ fill:#97C459; }
.s15c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s15c-green); }
.s15c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-green); }
.s15c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s15c .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s15c .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s15c .ks-red{ fill:#A32D2D; font-size:13px; }
.s15c .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s15c .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15c .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s15c .kb-red, :root[data-theme="dark"] .s15c .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s15c .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s15c .kh-red{ fill:#F09595; }
.s15c .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s15c-red); }
.s15c .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15c-red); }
.s15c .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s15c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s15c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s15c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s15c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s15c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s15c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s15c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s15c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s15c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s15c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s15c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s15c-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s15c">
<rect x="20" y="20" width="300" height="60" rx="7" class="k-red"/>
<text x="170.0" y="45.5" text-anchor="middle" class="km-red">SSH-2.0-OpenSSH_8.9p1</text>
<text x="170.0" y="63.5" text-anchor="middle" class="km-red">Ubuntu-3ubuntu0.6</text>
<rect x="20" y="110" width="300" height="60" rx="7" class="k-green"/>
<text x="170.0" y="135.5" text-anchor="middle" class="km-green">SSH-2.0-OpenSSH_8.9p1</text>
<text x="170.0" y="153.5" text-anchor="middle" class="km-green">Ubuntu-3ubuntu0.10</text>
<text x="170" y="98" text-anchor="middle" class="kh-red">vulnerable package</text>
<text x="170" y="188" text-anchor="middle" class="kh-green">patched package (backport)</text>
<rect x="380" y="50" width="140" height="90" rx="7" class="k-amber"/>
<text x="450.0" y="81.5" text-anchor="middle" class="kb-amber">NetWarden 1.0</text>
<text x="450.0" y="99.5" text-anchor="middle" class="ks-amber">sees 8.9p1</text>
<text x="450.0" y="117.5" text-anchor="middle" class="ks-amber">in 8.5p1..9.8p1</text>
<line x1="322" y1="50" x2="378" y2="80" class="ar"/>
<line x1="322" y1="140" x2="378" y2="110" class="ar"/>
<rect x="560" y="20" width="140" height="50" rx="7" class="k-green"/>
<text x="630.0" y="49.5" text-anchor="middle" class="kb-green">CVE: correct</text>
<rect x="560" y="110" width="140" height="60" rx="7" class="k-red"/>
<text x="630.0" y="135.5" text-anchor="middle" class="kb-red">CVE reported:</text>
<text x="630.0" y="153.5" text-anchor="middle" class="ks-red">false positive</text>
<line x1="522" y1="80" x2="558" y2="45" class="ar"/>
<line x1="522" y1="110" x2="558" y2="138" class="ar"/>
<rect x="20" y="210" width="680" height="54" rx="7" class="k-blue"/>
<text x="360.0" y="231.5" text-anchor="middle" class="ks-blue">US-11: use distribution security data (Ubuntu notices, Debian tracker, OSV ecosystems) to map</text>
<text x="360.0" y="251.5" text-anchor="middle" class="ks-blue">package revisions to fixed versions</text>
</g>
</svg>
<figcaption>Requirements written today meet the real world tomorrow. Maintenance is where software learns.</figcaption>
</figure>

Linux distributions, however, rarely jump to new upstream versions. They **backport** security fixes into the version they ship. Ubuntu 22.04's fixed OpenSSH package still announces itself as `OpenSSH_8.9p1`; only the package revision suffix (`Ubuntu-3ubuntu0.10` rather than an earlier `0.6`) shows that the fix is present. NetWarden therefore reports the vulnerability on a patched server: a **false positive**.

This is not a coding bug; the code does what the requirements said. It is a **requirements gap** discovered in operation, which is very common. The response follows the process of the earlier chapters:

1. A **defect report** with evidence (the banner, the package version, the vendor notice).
2. Triage: a known **limitation**, documented in the README and the risk register (R2), with a new backlog item, **US-11**.
3. A **design** response: knowledge of distribution package revisions, from sources such as Ubuntu's security notices, the Debian security tracker, or OSV's ecosystem records, behind the same `KnowledgeSource` interface (the adapter in Chapter 6).
4. **Tests first**: banners for vulnerable and patched packages, with the expected results.

Evolution is where the investment in interfaces, tests and documentation is repaid.

## Legacy code

Michael Feathers defines **legacy code** simply as code without tests. Whatever its age, such code is risky to change, because nothing tells you when you break it. Feathers's approach in *Working Effectively with Legacy Code* (2004):

1. Identify the change point.
2. Find **test points**, places where behaviour can be observed.
3. Break dependencies to get the code into a test harness, using **seams**: places where behaviour can be changed without editing the code, such as a constructor parameter or an overridable method.
4. Write **characterisation tests** that record what the code does now, right or wrong.
5. Make the change, refactor, and keep the tests.

Reading unfamiliar code is a skill in itself: run it, read the tests first, follow one scenario through with a debugger, draw the sequence diagram (Chapter 4), and check the history with `git log` and `git blame` (Chapter 8) to learn why it is the way it is.

## Re-engineering without a rewrite

When a large part of a system must be replaced, the tempting option is a complete rewrite. Rewrites are risky: the old system keeps changing while the new one is built, hidden behaviour is forgotten, and nothing is delivered for a long time. The **strangler fig** pattern replaces a system piece by piece instead.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The strangler fig pattern applied to NetWarden&#x27;s knowledge base. Step 1: all lookups go to the bundled JSON. Step 2: a routing facade sends OpenSSH lookups to the new OSV adapter and the rest to the JSON. Step 3: all products use OSV, and the old JSON code is removed. The system keeps working at every step." xmlns="http://www.w3.org/2000/svg">
<style>
.s15e{ font-family:var(--sans),sans-serif; }
.s15e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s15e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s15e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s15e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s15e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s15e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s15e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s15e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s15e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s15e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s15e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s15e .s{ fill:var(--text-dim); font-size:13px; }
.s15e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s15e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s15e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s15e .c{ fill:var(--text-faint); font-size:12.5px; }
.s15e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s15e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s15e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s15e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15e-a); }
.s15e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15e-a); marker-start:url(#s15e-s); }
.s15e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s15e-g); }
.s15e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s15e-a); }
.s15e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s15e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s15e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s15e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s15e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s15e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15e-tri); }
.s15e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15e-tri); }
.s15e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15e-open); }
.s15e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15e-open); }
.s15e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15e-dia); }
.s15e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15e-odia); }
.s15e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15e-dia); marker-end:url(#s15e-open); }
.s15e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15e-solid); }
.s15e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s15e-open); }
.s15e .fill{ fill:var(--text); stroke:none; }
.s15e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s15e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s15e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s15e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s15e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s15e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s15e .ks-amber{ fill:#854F0B; font-size:13px; }
.s15e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s15e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s15e .kb-amber, :root[data-theme="dark"] .s15e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s15e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s15e .kh-amber{ fill:#EF9F27; }
.s15e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s15e-amber); }
.s15e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15e-amber); }
.s15e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s15e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s15e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s15e .ks-green{ fill:#3B6D11; font-size:13px; }
.s15e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s15e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s15e .kb-green, :root[data-theme="dark"] .s15e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s15e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s15e .kh-green{ fill:#97C459; }
.s15e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s15e-green); }
.s15e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15e-green); }
.s15e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s15e .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s15e .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s15e .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s15e .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s15e .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15e .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s15e .kb-gray, :root[data-theme="dark"] .s15e .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s15e .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s15e .kh-gray{ fill:#B4B2A9; }
.s15e .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s15e-gray); }
.s15e .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15e-gray); }
.s15e .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s15e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s15e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s15e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s15e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s15e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s15e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s15e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s15e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s15e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s15e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s15e-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s15e">
<text x="125" y="24" text-anchor="middle" class="b">1. today</text>
<rect x="20" y="40" width="210" height="40" rx="4" class="k-gray"/>
<text x="125.0" y="64.5" text-anchor="middle" class="km-gray">lookup(product, version)</text>
<rect x="20" y="110" width="210.0" height="60" rx="4" class="k-amber"/>
<text x="125.0" y="144.5" text-anchor="middle" class="kb-amber">bundled JSON</text>
<line x1="125" y1="82" x2="125.0" y2="108" class="ar"/>
<text x="360" y="24" text-anchor="middle" class="b">2. migrating</text>
<rect x="255" y="40" width="210" height="40" rx="4" class="k-gray"/>
<text x="360.0" y="64.5" text-anchor="middle" class="km-gray">lookup(product, version)</text>
<rect x="255" y="110" width="105.0" height="60" rx="4" class="k-amber"/>
<text x="307.5" y="144.5" text-anchor="middle" class="kb-amber">JSON</text>
<line x1="360" y1="82" x2="307.5" y2="108" class="ar"/>
<rect x="360.0" y="110" width="105.0" height="60" rx="4" class="k-green"/>
<text x="412.5" y="144.5" text-anchor="middle" class="kb-green">OSV</text>
<line x1="360" y1="82" x2="412.5" y2="108" class="ar"/>
<text x="595" y="24" text-anchor="middle" class="b">3. done</text>
<rect x="490" y="40" width="210" height="40" rx="4" class="k-gray"/>
<text x="595.0" y="64.5" text-anchor="middle" class="km-gray">lookup(product, version)</text>
<rect x="490" y="110" width="210.0" height="60" rx="4" class="k-green"/>
<text x="595.0" y="144.5" text-anchor="middle" class="kb-green">OSV adapter</text>
<line x1="595" y1="82" x2="595.0" y2="108" class="ar"/>
<text x="360" y="214" text-anchor="middle" class="c">new code grows around the old, taking over one route at a time, until the old can be cut away</text>
<text x="360" y="240" text-anchor="middle" class="c">each step is released and tested; no big-bang rewrite</text>
</g>
</svg>
<figcaption>Named by Martin Fowler after vines that grow around a tree and eventually replace it.</figcaption>
</figure>

A routing layer (here, a facade in front of `lookup`) sends some requests to new code and the rest to old code. Over many small releases, the new code takes over, and finally the old code is deleted. Each step is tested and released, and can be stopped or reversed.

Other re-engineering activities include **reverse engineering** (recovering designs and models from code, for example with `pyreverse`), **restructuring** (refactoring at scale), and **data migration**.

## Changing interfaces without breaking users

<figure class="diagram">
<svg viewBox="0 0 720 220" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Deprecating a feature without breaking users: in version 1.4 add the replacement and keep the old option working; in 1.5 the old option prints a deprecation warning naming the replacement and the removal version; in 2.0, a major version, remove it, and document the change in the changelog and upgrade notes." xmlns="http://www.w3.org/2000/svg">
<style>
.s15f{ font-family:var(--sans),sans-serif; }
.s15f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s15f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s15f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s15f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s15f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s15f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s15f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s15f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s15f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s15f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s15f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s15f .s{ fill:var(--text-dim); font-size:13px; }
.s15f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s15f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s15f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s15f .c{ fill:var(--text-faint); font-size:12.5px; }
.s15f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s15f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s15f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s15f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15f-a); }
.s15f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s15f-a); marker-start:url(#s15f-s); }
.s15f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s15f-g); }
.s15f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s15f-a); }
.s15f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s15f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s15f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s15f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s15f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s15f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15f-tri); }
.s15f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15f-tri); }
.s15f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15f-open); }
.s15f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s15f-open); }
.s15f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15f-dia); }
.s15f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15f-odia); }
.s15f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s15f-dia); marker-end:url(#s15f-open); }
.s15f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s15f-solid); }
.s15f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s15f-open); }
.s15f .fill{ fill:var(--text); stroke:none; }
.s15f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s15f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s15f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s15f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s15f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s15f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s15f .ks-blue{ fill:#185FA5; font-size:13px; }
.s15f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s15f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s15f .kb-blue, :root[data-theme="dark"] .s15f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s15f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s15f .kh-blue{ fill:#85B7EB; }
.s15f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s15f-blue); }
.s15f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15f-blue); }
.s15f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s15f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s15f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s15f .ks-amber{ fill:#854F0B; font-size:13px; }
.s15f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s15f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s15f .kb-amber, :root[data-theme="dark"] .s15f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s15f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s15f .kh-amber{ fill:#EF9F27; }
.s15f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s15f-amber); }
.s15f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15f-amber); }
.s15f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s15f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s15f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s15f .ks-red{ fill:#A32D2D; font-size:13px; }
.s15f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s15f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s15f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s15f .kb-red, :root[data-theme="dark"] .s15f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s15f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s15f .kh-red{ fill:#F09595; }
.s15f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s15f-red); }
.s15f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s15f-red); }
.s15f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s15f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s15f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s15f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s15f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s15f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s15f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s15f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s15f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s15f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s15f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s15f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s15f">
<rect x="20" y="40" width="210" height="90" rx="7" class="k-blue"/>
<text x="125.0" y="65.5" text-anchor="middle" class="kb-blue">1.4</text>
<text x="125.0" y="89.5" text-anchor="middle" class="ks-blue">add --format md</text>
<text x="125.0" y="113.5" text-anchor="middle" class="km-blue">keep --markdown</text>
<rect x="255" y="40" width="210" height="90" rx="7" class="k-amber"/>
<text x="360.0" y="65.5" text-anchor="middle" class="kb-amber">1.5</text>
<text x="360.0" y="89.5" text-anchor="middle" class="ks-amber">--markdown warns:</text>
<text x="360.0" y="113.5" text-anchor="middle" class="km-amber">removed in 2.0</text>
<line x1="233" y1="85" x2="253" y2="85" class="ar"/>
<rect x="490" y="40" width="210" height="90" rx="7" class="k-red"/>
<text x="595.0" y="65.5" text-anchor="middle" class="kb-red">2.0</text>
<text x="595.0" y="89.5" text-anchor="middle" class="ks-red">remove --markdown</text>
<text x="595.0" y="113.5" text-anchor="middle" class="km-red">CHANGELOG, upgrade notes</text>
<line x1="468" y1="85" x2="488" y2="85" class="ar"/>
<text x="360" y="180" text-anchor="middle" class="c">removal only in a MAJOR version (semantic versioning, Chapter 13)</text>
</g>
</svg>
<figcaption>Give users time and information. Surprise removals destroy trust faster than bugs do.</figcaption>
</figure>

Users build on whatever a system exposes: command-line options, file formats, exit codes, JSON fields. Changing them breaks their scripts and pipelines. The safe path is **deprecation**: add the replacement, warn about the old way for at least one release, and remove it only in a major version, announced in the changelog. Python's `warnings.warn(..., DeprecationWarning)` is the standard mechanism inside Python code.

## Keeping up with dependencies and platforms

Every dependency and platform has its own lifecycle:

- **Python** versions receive bug fixes for about two years and security fixes for five; each release has a published end-of-life date. Python 3.11, NetWarden's minimum, reaches end of life in October 2027, after which NetWarden 2.0 should require at least 3.12.
- **Base images** (`python:3.13-slim`) receive operating system security fixes; rebuild images regularly, not only when the code changes.
- **Development tools** release often; Dependabot pull requests (Chapter 13) keep updates small and tested.

Small, regular updates are cheap. Skipping them for years leads to "upgrade cliffs", where everything must change at once.

## Documentation for maintainers

The future maintainer, often you, needs to know **why**, not just what. The documents that matter most in maintenance are the ones NetWarden keeps beside the code: the README (how to build, test and run), architecture notes and C4 diagrams, ADRs (why decisions were made), the requirements with trace links, the changelog, and contributing guidelines. Documentation that lives in the repository is reviewed with the code and is much less likely to rot.

## End of life

Eventually software is retired. A responsible retirement announces a timeline, provides migration help, keeps security fixes going for a stated period, archives the code and data, and removes the system from production so it does not become an unmaintained, vulnerable leftover, the kind of forgotten server that tools like NetWarden exist to find.

## Summary

- **Maintenance** is all work after delivery and usually costs more than initial development.
- **Lehman's laws**: real-world software must keep changing, and its complexity grows unless actively reduced.
- Maintenance is **corrective, adaptive, perfective or preventive**; most of it is evolution, not repair.
- Operation reveals **requirements gaps**, such as backported fixes; handle them through the normal process.
- **Legacy code** is code without tests: add **characterisation tests** at **seams** before changing it.
- Replace large parts incrementally with the **strangler fig** pattern, not a big-bang rewrite.
- **Deprecate** before removing; keep **dependencies and platforms** current in small steps.
- Keep maintainer documentation, especially **ADRs** and the **changelog**, next to the code.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-15-maintenance-and-evolution).

**1. What does maintenance usually cost compared with initial development?**

- A. More
- B. Much less
- C. About the same
- D. Nothing, if the code is good

**2. What do Lehman's laws say about real-world software?**

- A. It can be finished
- B. It never needs updates
- C. It must keep changing, and its complexity grows unless actively reduced
- D. It gets simpler with age

**3. Updating NetWarden to work with a new Python version is which kind of maintenance?**

- A. Corrective
- B. Perfective
- C. Preventive
- D. Adaptive

**4. Michael Feathers defines legacy code as what?**

- A. Old code
- B. Code without tests
- C. Code in an old language
- D. Code written by someone else

**5. Before changing legacy code, what should you add first?**

- A. Comments
- B. New features
- C. Characterisation tests at seams, recording what the code does today
- D. A rewrite plan

**6. What is the strangler fig pattern?**

- A. Replacing a system incrementally, routing more and more to the new parts until the old one can go
- B. A big-bang rewrite
- C. A testing technique
- D. A branching strategy

**7. How should you remove a feature others depend on?**

- A. Deprecate it first, with a warning and a timeline, then remove it
- B. Delete it in the next release
- C. Rename it
- D. Hide it from the documentation

**8. The Ubuntu OpenSSH false alarm, where a patched version still matched an old CVE, is an example of what?**

- A. A typo
- B. A hardware fault
- C. A requirements gap revealed in operation, handled through the normal process
- D. A network outage
