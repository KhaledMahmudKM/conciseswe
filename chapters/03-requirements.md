# Chapter 3: Requirements Engineering

A **requirement** is a statement of something a system must do, or a quality it must have, to meet a stakeholder's need. **Requirements engineering** is the work of discovering, documenting, checking and managing those statements. Studies of failed projects have repeatedly found requirements problems near the top of the list: missing requirements, misunderstood requirements, and requirements that changed without anyone tracking the consequences. This chapter shows how to do better, using NetWarden's own requirements as the example.

## The process

<figure class="diagram">
<svg viewBox="0 0 720 262" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The requirements engineering process: elicitation discovers needs from stakeholders; analysis resolves conflicts, prioritises and models; specification writes the requirements down; validation checks that they are right. The activities repeat, and requirements management controls changes and traceability throughout." xmlns="http://www.w3.org/2000/svg">
<style>
.s3a{ font-family:var(--sans),sans-serif; }
.s3a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3a .s{ fill:var(--text-dim); font-size:13px; }
.s3a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .c{ fill:var(--text-faint); font-size:12.5px; }
.s3a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3a-a); }
.s3a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3a-a); marker-start:url(#s3a-s); }
.s3a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3a-g); }
.s3a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-a); }
.s3a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3a-tri); }
.s3a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-tri); }
.s3a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3a-open); }
.s3a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-open); }
.s3a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3a-dia); }
.s3a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3a-odia); }
.s3a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3a-dia); marker-end:url(#s3a-open); }
.s3a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3a-solid); }
.s3a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3a-open); }
.s3a .fill{ fill:var(--text); stroke:none; }
.s3a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s3a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s3a .ks-blue{ fill:#185FA5; font-size:13px; }
.s3a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s3a .kb-blue, :root[data-theme="dark"] .s3a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s3a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s3a .kh-blue{ fill:#85B7EB; }
.s3a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s3a-blue); }
.s3a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-blue); }
.s3a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s3a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s3a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s3a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s3a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s3a .kb-teal, :root[data-theme="dark"] .s3a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s3a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s3a .kh-teal{ fill:#5DCAA5; }
.s3a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s3a-teal); }
.s3a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-teal); }
.s3a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s3a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s3a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s3a .ks-amber{ fill:#854F0B; font-size:13px; }
.s3a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s3a .kb-amber, :root[data-theme="dark"] .s3a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s3a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s3a .kh-amber{ fill:#EF9F27; }
.s3a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s3a-amber); }
.s3a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-amber); }
.s3a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s3a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s3a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s3a .ks-purple{ fill:#534AB7; font-size:13px; }
.s3a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s3a .kb-purple, :root[data-theme="dark"] .s3a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s3a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s3a .kh-purple{ fill:#AFA9EC; }
.s3a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s3a-purple); }
.s3a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-purple); }
.s3a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s3a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s3a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s3a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s3a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s3a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s3a .kb-gray, :root[data-theme="dark"] .s3a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s3a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s3a .kh-gray{ fill:#B4B2A9; }
.s3a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s3a-gray); }
.s3a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3a-gray); }
.s3a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s3a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s3a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s3a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s3a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s3a">
<rect x="20" y="50" width="155" height="60" rx="7" class="k-blue"/>
<text x="97.5" y="75.5" text-anchor="middle" class="kb-blue">elicitation</text>
<text x="97.5" y="93.5" text-anchor="middle" class="ks-blue">talk, observe, read</text>
<rect x="195" y="50" width="155" height="60" rx="7" class="k-purple"/>
<text x="272.5" y="75.5" text-anchor="middle" class="kb-purple">analysis</text>
<text x="272.5" y="93.5" text-anchor="middle" class="ks-purple">conflicts, priorities</text>
<line x1="177" y1="80" x2="193" y2="80" class="ar"/>
<rect x="370" y="50" width="155" height="60" rx="7" class="k-teal"/>
<text x="447.5" y="75.5" text-anchor="middle" class="kb-teal">specification</text>
<text x="447.5" y="93.5" text-anchor="middle" class="ks-teal">write it down</text>
<line x1="352" y1="80" x2="368" y2="80" class="ar"/>
<rect x="545" y="50" width="155" height="60" rx="7" class="k-amber"/>
<text x="622.5" y="75.5" text-anchor="middle" class="kb-amber">validation</text>
<text x="622.5" y="93.5" text-anchor="middle" class="ks-amber">is it right?</text>
<line x1="527" y1="80" x2="543" y2="80" class="ar"/>
<path d="M600 112 C 600 160, 98 160, 98 114" class="ad"/>
<text x="350" y="176" text-anchor="middle" class="c">iterate: each pass uncovers new questions</text>
<rect x="20" y="196" width="680" height="50" rx="7" class="k-gray"/>
<text x="360.0" y="225.5" text-anchor="middle" class="kb-gray">requirements management: baselines, change control, traceability, status</text>
<text x="20" y="30" text-anchor="start" class="kh-blue">stakeholders' needs</text>
<text x="700" y="30" text-anchor="end" class="kh-amber">agreed requirements</text>
</g>
</svg>
<figcaption>Requirements are discovered and negotiated, not simply collected.</figcaption>
</figure>

| Activity | Goal | Typical outputs |
|---|---|---|
| **Elicitation** | Discover needs, goals, constraints and context | Interview notes, workshop results, observations |
| **Analysis** | Resolve conflicts, find gaps, prioritise, model | Prioritised list, models, open questions |
| **Specification** | Write requirements clearly and checkably | Specification document, backlog, use cases |
| **Validation** | Check that these are the **right** requirements | Review records, prototype feedback, acceptance tests |
| **Management** | Control change, keep traceability | Baselines, change requests, trace links |

The activities overlap and repeat. In an agile project they happen continuously, a few stories at a time; in a plan-driven project there is a large up-front effort and a formal baseline. Either way, the work is the same.

## Stakeholders

A **stakeholder** is anyone who affects or is affected by the system. Users are the obvious ones, but managers who pay, operators who run it, regulators, and people who are affected without ever using it all count. For NetWarden, the owners of the machines being scanned are stakeholders: a careless scan could disrupt their service.

<figure class="diagram">
<svg viewBox="0 0 720 330" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A stakeholder power and interest grid for NetWarden. High power, high interest: security manager and network administrators, managed closely. High power, low interest: the IT director and the legal and compliance office, kept satisfied. Low power, high interest: asset owners, students and the instructor, kept informed. Low power, low interest: end users of the scanned systems, monitored." xmlns="http://www.w3.org/2000/svg">
<style>
.s3b{ font-family:var(--sans),sans-serif; }
.s3b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3b .s{ fill:var(--text-dim); font-size:13px; }
.s3b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3b .c{ fill:var(--text-faint); font-size:12.5px; }
.s3b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3b-a); }
.s3b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3b-a); marker-start:url(#s3b-s); }
.s3b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3b-g); }
.s3b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-a); }
.s3b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3b-tri); }
.s3b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-tri); }
.s3b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3b-open); }
.s3b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-open); }
.s3b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3b-dia); }
.s3b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3b-odia); }
.s3b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3b-dia); marker-end:url(#s3b-open); }
.s3b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3b-solid); }
.s3b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3b-open); }
.s3b .fill{ fill:var(--text); stroke:none; }
.s3b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s3b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s3b .ks-blue{ fill:#185FA5; font-size:13px; }
.s3b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s3b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s3b .kb-blue, :root[data-theme="dark"] .s3b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s3b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s3b .kh-blue{ fill:#85B7EB; }
.s3b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s3b-blue); }
.s3b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-blue); }
.s3b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s3b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s3b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s3b .ks-amber{ fill:#854F0B; font-size:13px; }
.s3b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s3b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s3b .kb-amber, :root[data-theme="dark"] .s3b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s3b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s3b .kh-amber{ fill:#EF9F27; }
.s3b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s3b-amber); }
.s3b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-amber); }
.s3b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s3b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s3b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s3b .ks-red{ fill:#A32D2D; font-size:13px; }
.s3b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s3b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s3b .kb-red, :root[data-theme="dark"] .s3b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s3b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s3b .kh-red{ fill:#F09595; }
.s3b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s3b-red); }
.s3b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-red); }
.s3b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s3b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s3b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s3b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s3b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s3b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s3b .kb-gray, :root[data-theme="dark"] .s3b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s3b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s3b .kh-gray{ fill:#B4B2A9; }
.s3b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s3b-gray); }
.s3b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3b-gray); }
.s3b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s3b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s3b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s3b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s3b">
<line x1="60" y1="300" x2="700" y2="300" class="ar"/>
<line x1="60" y1="300" x2="60" y2="20" class="ar"/>
<text x="380" y="324" text-anchor="middle" class="c">interest</text>
<text x="48" y="160" text-anchor="end" class="c">power</text>
<line x1="380" y1="30" x2="380" y2="296" class="gd"/>
<line x1="64" y1="160" x2="696" y2="160" class="gd"/>
<text x="220" y="50" text-anchor="middle" class="kh-amber">keep satisfied</text>
<rect x="110" y="64" width="220" height="38" rx="7" class="k-amber"/>
<text x="220.0" y="87.5" text-anchor="middle" class="kb-amber">IT director</text>
<rect x="110" y="110" width="220" height="38" rx="7" class="k-amber"/>
<text x="220.0" y="133.5" text-anchor="middle" class="kb-amber">legal and compliance</text>
<text x="540" y="50" text-anchor="middle" class="kh-red">manage closely</text>
<rect x="430" y="64" width="220" height="38" rx="7" class="k-red"/>
<text x="540.0" y="87.5" text-anchor="middle" class="kb-red">security manager</text>
<rect x="430" y="110" width="220" height="38" rx="7" class="k-red"/>
<text x="540.0" y="133.5" text-anchor="middle" class="kb-red">network administrators</text>
<text x="220" y="190" text-anchor="middle" class="kh-gray">monitor</text>
<rect x="110" y="204" width="220" height="38" rx="7" class="k-gray"/>
<text x="220.0" y="227.5" text-anchor="middle" class="kb-gray">users of scanned systems</text>
<text x="540" y="190" text-anchor="middle" class="kh-blue">keep informed</text>
<rect x="430" y="204" width="220" height="38" rx="7" class="k-blue"/>
<text x="540.0" y="227.5" text-anchor="middle" class="kb-blue">asset owners</text>
<rect x="430" y="250" width="220" height="38" rx="7" class="k-blue"/>
<text x="540.0" y="273.5" text-anchor="middle" class="kb-blue">students, instructor</text>
</g>
</svg>
<figcaption>Different stakeholders need different amounts of attention. Missing one is a classic source of failed projects.</figcaption>
</figure>

A **power and interest grid** decides how much attention each group needs. Stakeholders with high power and high interest are managed closely; those with low power but high interest are kept informed; and so on. Stakeholders who are missed at the start tend to appear later with requirements that are expensive to add.

## Kinds and levels of requirements

<figure class="diagram">
<svg viewBox="0 0 720 310" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Levels of requirements with NetWarden examples. Business requirement: reduce the number of known-vulnerable services in the lab network. User requirement: as an administrator I want known vulnerabilities flagged with severity. System requirements split into functional, such as NW-FR-4, report CVE, CVSS and severity, and non-functional, such as NW-NFR-1, a /24 network in under 60 seconds." xmlns="http://www.w3.org/2000/svg">
<style>
.s3c{ font-family:var(--sans),sans-serif; }
.s3c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3c .s{ fill:var(--text-dim); font-size:13px; }
.s3c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3c .c{ fill:var(--text-faint); font-size:12.5px; }
.s3c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3c-a); }
.s3c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3c-a); marker-start:url(#s3c-s); }
.s3c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3c-g); }
.s3c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3c-a); }
.s3c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3c-tri); }
.s3c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3c-tri); }
.s3c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3c-open); }
.s3c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3c-open); }
.s3c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3c-dia); }
.s3c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3c-odia); }
.s3c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3c-dia); marker-end:url(#s3c-open); }
.s3c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3c-solid); }
.s3c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3c-open); }
.s3c .fill{ fill:var(--text); stroke:none; }
.s3c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s3c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s3c .ks-blue{ fill:#185FA5; font-size:13px; }
.s3c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s3c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s3c .kb-blue, :root[data-theme="dark"] .s3c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s3c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s3c .kh-blue{ fill:#85B7EB; }
.s3c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s3c-blue); }
.s3c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3c-blue); }
.s3c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s3c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s3c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s3c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s3c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s3c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s3c .kb-teal, :root[data-theme="dark"] .s3c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s3c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s3c .kh-teal{ fill:#5DCAA5; }
.s3c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s3c-teal); }
.s3c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3c-teal); }
.s3c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s3c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s3c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s3c .ks-purple{ fill:#534AB7; font-size:13px; }
.s3c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s3c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s3c .kb-purple, :root[data-theme="dark"] .s3c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s3c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s3c .kh-purple{ fill:#AFA9EC; }
.s3c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s3c-purple); }
.s3c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3c-purple); }
.s3c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s3c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s3c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s3c">
<rect x="100" y="16" width="520" height="58" rx="7" class="k-purple"/>
<text x="360.0" y="40.5" text-anchor="middle" class="kb-purple">business requirements: why</text>
<text x="360.0" y="58.5" text-anchor="middle" class="ks-purple">reduce known-vulnerable services in the lab by 80% this year</text>
<rect x="60" y="86" width="600" height="58" rx="7" class="k-blue"/>
<text x="360.0" y="110.5" text-anchor="middle" class="kb-blue">user requirements: what users need</text>
<text x="360.0" y="128.5" text-anchor="middle" class="ks-blue">US-4: as an administrator, I want known vulnerabilities flagged</text>
<rect x="20" y="156" width="680" height="116" rx="7" class="k-teal"/>
<text x="360" y="178" text-anchor="middle" class="kb-teal">system requirements: what the software shall do, and how well</text>
<rect x="40" y="192" width="310" height="66" rx="7" class="pnl"/>
<text x="195.0" y="219.5" text-anchor="middle" class="b">functional  NW-FR-4</text>
<text x="195.0" y="239.5" text-anchor="middle" class="c">report CVE ID, CVSS score, severity</text>
<rect x="370" y="192" width="310" height="66" rx="7" class="pnl"/>
<text x="525.0" y="219.5" text-anchor="middle" class="b">non-functional  NW-NFR-1</text>
<text x="525.0" y="239.5" text-anchor="middle" class="c">a /24 on 17 ports in under 60 s</text>
<text x="360" y="296" text-anchor="middle" class="c">each level refines the one above; each lower requirement should trace to a higher one</text>
</g>
</svg>
<figcaption>Business goals justify user needs; user needs justify what the system shall do.</figcaption>
</figure>

Requirements exist at several **levels**. **Business requirements** state why the organisation wants the system. **User requirements** state what users need to accomplish, often as user stories or use cases. **System requirements** state precisely what the software shall do and how well.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Functional requirements say what the system does; non-functional requirements say how well, and constrain how it is built. Non-functional categories include performance, security, reliability, usability, maintainability, portability, and constraints such as law, standards and budget." xmlns="http://www.w3.org/2000/svg">
<style>
.s3d{ font-family:var(--sans),sans-serif; }
.s3d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3d .s{ fill:var(--text-dim); font-size:13px; }
.s3d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3d .c{ fill:var(--text-faint); font-size:12.5px; }
.s3d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3d-a); }
.s3d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3d-a); marker-start:url(#s3d-s); }
.s3d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3d-g); }
.s3d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3d-a); }
.s3d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3d-tri); }
.s3d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3d-tri); }
.s3d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3d-open); }
.s3d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3d-open); }
.s3d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3d-dia); }
.s3d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3d-odia); }
.s3d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3d-dia); marker-end:url(#s3d-open); }
.s3d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3d-solid); }
.s3d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3d-open); }
.s3d .fill{ fill:var(--text); stroke:none; }
.s3d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s3d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s3d .ks-blue{ fill:#185FA5; font-size:13px; }
.s3d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s3d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s3d .kb-blue, :root[data-theme="dark"] .s3d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s3d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s3d .kh-blue{ fill:#85B7EB; }
.s3d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s3d-blue); }
.s3d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3d-blue); }
.s3d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s3d .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s3d .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s3d .ks-coral{ fill:#993C1D; font-size:13px; }
.s3d .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s3d .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3d .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s3d .kb-coral, :root[data-theme="dark"] .s3d .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s3d .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s3d .kh-coral{ fill:#F0997B; }
.s3d .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s3d-coral); }
.s3d .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3d-coral); }
.s3d .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s3d-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s3d">
<rect x="20" y="20" width="250" height="200" rx="7" class="k-blue"/>
<text x="145.0" y="58.5" text-anchor="middle" class="kb-blue">functional</text>
<text x="145.0" y="80.5" text-anchor="middle" class="ks-blue">what it does</text>
<text x="145.0" y="102.5" text-anchor="middle" class="ks-blue"></text>
<text x="145.0" y="124.5" text-anchor="middle" class="ks-blue">accept CIDR targets</text>
<text x="145.0" y="146.5" text-anchor="middle" class="ks-blue">detect open ports</text>
<text x="145.0" y="168.5" text-anchor="middle" class="ks-blue">report CVEs</text>
<text x="145.0" y="190.5" text-anchor="middle" class="ks-blue">compare scans</text>
<rect x="290" y="20" width="200" height="58" rx="7" class="k-coral"/>
<text x="390.0" y="44.5" text-anchor="middle" class="kb-coral">performance</text>
<text x="390.0" y="62.5" text-anchor="middle" class="ks-coral">60 s per /24</text>
<rect x="500" y="20" width="200" height="58" rx="7" class="k-coral"/>
<text x="600.0" y="44.5" text-anchor="middle" class="kb-coral">security</text>
<text x="600.0" y="62.5" text-anchor="middle" class="ks-coral">scope enforced</text>
<rect x="290" y="88" width="200" height="58" rx="7" class="k-coral"/>
<text x="390.0" y="112.5" text-anchor="middle" class="kb-coral">reliability</text>
<text x="390.0" y="130.5" text-anchor="middle" class="ks-coral">no crash on bad banners</text>
<rect x="500" y="88" width="200" height="58" rx="7" class="k-coral"/>
<text x="600.0" y="112.5" text-anchor="middle" class="kb-coral">usability</text>
<text x="600.0" y="130.5" text-anchor="middle" class="ks-coral">demo in 5 minutes</text>
<rect x="290" y="156" width="200" height="58" rx="7" class="k-coral"/>
<text x="390.0" y="180.5" text-anchor="middle" class="kb-coral">maintainability</text>
<text x="390.0" y="198.5" text-anchor="middle" class="ks-coral">90% coverage</text>
<rect x="500" y="156" width="200" height="58" rx="7" class="k-coral"/>
<text x="600.0" y="180.5" text-anchor="middle" class="kb-coral">portability</text>
<text x="600.0" y="198.5" text-anchor="middle" class="ks-coral">3 operating systems</text>
<text x="500" y="236" text-anchor="middle" class="kh-coral">non-functional: how well, and under which constraints</text>
</g>
</svg>
<figcaption>Non-functional requirements are often the hardest to change later: they shape the whole architecture.</figcaption>
</figure>

System requirements are either **functional** (behaviour: inputs, outputs, rules) or **non-functional** (qualities and constraints). Non-functional requirements are easy to forget and hard to retrofit. "It must be secure" or "it must be fast" are not requirements; they are wishes. A good non-functional requirement is **measurable**:

| Vague | Measurable (NetWarden) |
|---|---|
| The scan should be fast | NW-NFR-1: a /24 network on the 17 default ports shall complete in under 60 s on a LAN |
| The tool should be safe | NW-SR-1: the system shall refuse any target outside the authorised scope, before sending any packet |
| It should be easy to use | NW-NFR-5: a first-time user can run the demo scan following the README in under 5 minutes |
| The code should be maintainable | NW-NFR-4: adding a check requires one new class and no engine changes; coverage at least 90% |

## Elicitation

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Elicitation techniques: interviews, workshops, observation of people at work, questionnaires, prototypes and mock-ups, and analysis of existing documents and systems, each with what it is good at." xmlns="http://www.w3.org/2000/svg">
<style>
.s3e{ font-family:var(--sans),sans-serif; }
.s3e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3e .s{ fill:var(--text-dim); font-size:13px; }
.s3e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .c{ fill:var(--text-faint); font-size:12.5px; }
.s3e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3e-a); }
.s3e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3e-a); marker-start:url(#s3e-s); }
.s3e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3e-g); }
.s3e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-a); }
.s3e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3e-tri); }
.s3e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-tri); }
.s3e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3e-open); }
.s3e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-open); }
.s3e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3e-dia); }
.s3e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3e-odia); }
.s3e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3e-dia); marker-end:url(#s3e-open); }
.s3e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3e-solid); }
.s3e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3e-open); }
.s3e .fill{ fill:var(--text); stroke:none; }
.s3e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s3e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s3e .ks-blue{ fill:#185FA5; font-size:13px; }
.s3e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s3e .kb-blue, :root[data-theme="dark"] .s3e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s3e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s3e .kh-blue{ fill:#85B7EB; }
.s3e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s3e-blue); }
.s3e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-blue); }
.s3e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s3e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s3e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s3e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s3e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s3e .kb-teal, :root[data-theme="dark"] .s3e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s3e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s3e .kh-teal{ fill:#5DCAA5; }
.s3e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s3e-teal); }
.s3e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-teal); }
.s3e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s3e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s3e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s3e .ks-amber{ fill:#854F0B; font-size:13px; }
.s3e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s3e .kb-amber, :root[data-theme="dark"] .s3e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s3e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s3e .kh-amber{ fill:#EF9F27; }
.s3e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s3e-amber); }
.s3e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-amber); }
.s3e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s3e .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s3e .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s3e .ks-coral{ fill:#993C1D; font-size:13px; }
.s3e .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3e .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s3e .kb-coral, :root[data-theme="dark"] .s3e .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s3e .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s3e .kh-coral{ fill:#F0997B; }
.s3e .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s3e-coral); }
.s3e .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-coral); }
.s3e .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s3e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s3e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s3e .ks-purple{ fill:#534AB7; font-size:13px; }
.s3e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s3e .kb-purple, :root[data-theme="dark"] .s3e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s3e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s3e .kh-purple{ fill:#AFA9EC; }
.s3e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s3e-purple); }
.s3e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-purple); }
.s3e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s3e .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s3e .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s3e .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s3e .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s3e .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3e .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s3e .kb-gray, :root[data-theme="dark"] .s3e .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s3e .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s3e .kh-gray{ fill:#B4B2A9; }
.s3e .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s3e-gray); }
.s3e .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3e-gray); }
.s3e .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s3e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s3e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s3e-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s3e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s3e-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s3e">
<rect x="20" y="20" width="218" height="80" rx="7" class="k-blue"/>
<text x="129.0" y="55.5" text-anchor="middle" class="kb-blue">interviews</text>
<text x="129.0" y="73.5" text-anchor="middle" class="ks-blue">depth from individuals</text>
<rect x="250" y="20" width="218" height="80" rx="7" class="k-purple"/>
<text x="359.0" y="55.5" text-anchor="middle" class="kb-purple">workshops</text>
<text x="359.0" y="73.5" text-anchor="middle" class="ks-purple">agreement across groups</text>
<rect x="480" y="20" width="218" height="80" rx="7" class="k-teal"/>
<text x="589.0" y="55.5" text-anchor="middle" class="kb-teal">observation</text>
<text x="589.0" y="73.5" text-anchor="middle" class="ks-teal">what people really do</text>
<rect x="20" y="120" width="218" height="80" rx="7" class="k-amber"/>
<text x="129.0" y="155.5" text-anchor="middle" class="kb-amber">questionnaires</text>
<text x="129.0" y="173.5" text-anchor="middle" class="ks-amber">breadth, many users</text>
<rect x="250" y="120" width="218" height="80" rx="7" class="k-coral"/>
<text x="359.0" y="155.5" text-anchor="middle" class="kb-coral">prototypes</text>
<text x="359.0" y="173.5" text-anchor="middle" class="ks-coral">reactions to something real</text>
<rect x="480" y="120" width="218" height="80" rx="7" class="k-gray"/>
<text x="589.0" y="155.5" text-anchor="middle" class="kb-gray">documents, systems</text>
<text x="589.0" y="173.5" text-anchor="middle" class="ks-gray">rules, current behaviour</text>
</g>
</svg>
<figcaption>Use several techniques: people cannot always say what they need, and they rarely mention what seems obvious to them.</figcaption>
</figure>

People are not good at listing their requirements on demand. They forget things that seem obvious, describe solutions instead of problems ("add a button that exports to Excel"), and disagree with each other. Good elicitation combines techniques: **interviews** for depth, **workshops** to reach agreement, **observation** to see what people really do, **questionnaires** for breadth, **prototypes** to get reactions to something concrete, and **document analysis** for rules and existing behaviour.

NetWarden's requirements came from interviews with two network administrators and a security manager, observation of how they currently ran ad hoc `nmap` scans and copied results into spreadsheets, and a workshop that produced the scope rule after a story about an intern who once scanned a neighbouring organisation's network by mistyping a subnet. That story became NW-SR-1, the most important requirement in the system.

## Writing requirements

### The "shall" statement

Traditional specifications use one sentence per requirement, with **shall** for mandatory behaviour, and a unique identifier. The international standard **ISO/IEC/IEEE 29148** lists the characteristics of a good individual requirement:

| Characteristic | Test | Bad example | Better |
|---|---|---|---|
| **Unambiguous** | Only one reading | "Scan quickly" | "Complete a /24 in under 60 s" |
| **Verifiable** | A test can prove it | "User friendly" | "Demo runs in under 5 minutes from the README" |
| **Singular** | One requirement per statement | "Scan and report and email results" | Three requirements |
| **Feasible** | Achievable within constraints | "Detect every vulnerability" | "Report vulnerabilities in the knowledge base" |
| **Necessary** | Traces to a need | "Support Gopher" | (delete it) |
| **Appropriate** | Right level of detail: says what, not how | "Use a SQLite table" | "Store scan results between runs" |

NetWarden's specification excerpt, `docs/requirements.md`, follows this format, with a column linking each requirement to the test that verifies it.

### User stories

Agile teams usually express user requirements as **user stories**: *As a* role, *I want* capability, *so that* benefit.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A user story card for NetWarden. Front: as an administrator, I want to define the networks I am allowed to scan, so that I never scan someone else&#x27;s systems by mistake; 3 points. Back: acceptance criteria written as given, when, then scenarios. Below, the INVEST checklist: independent, negotiable, valuable, estimable, small, testable." xmlns="http://www.w3.org/2000/svg">
<style>
.s3f{ font-family:var(--sans),sans-serif; }
.s3f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3f .s{ fill:var(--text-dim); font-size:13px; }
.s3f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3f .c{ fill:var(--text-faint); font-size:12.5px; }
.s3f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3f-a); }
.s3f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3f-a); marker-start:url(#s3f-s); }
.s3f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3f-g); }
.s3f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3f-a); }
.s3f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3f-tri); }
.s3f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3f-tri); }
.s3f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3f-open); }
.s3f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3f-open); }
.s3f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3f-dia); }
.s3f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3f-odia); }
.s3f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3f-dia); marker-end:url(#s3f-open); }
.s3f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3f-solid); }
.s3f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3f-open); }
.s3f .fill{ fill:var(--text); stroke:none; }
.s3f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s3f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s3f .ks-amber{ fill:#854F0B; font-size:13px; }
.s3f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s3f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s3f .kb-amber, :root[data-theme="dark"] .s3f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s3f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s3f .kh-amber{ fill:#EF9F27; }
.s3f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s3f-amber); }
.s3f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3f-amber); }
.s3f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s3f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s3f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s3f .ks-green{ fill:#3B6D11; font-size:13px; }
.s3f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s3f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s3f .kb-green, :root[data-theme="dark"] .s3f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s3f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s3f .kh-green{ fill:#97C459; }
.s3f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s3f-green); }
.s3f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3f-green); }
.s3f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s3f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s3f">
<rect x="20" y="20" width="330" height="190" rx="7" class="k-amber"/>
<text x="185.0" y="59.5" text-anchor="middle" class="kb-amber">US-1  (3 points)</text>
<text x="185.0" y="79.5" text-anchor="middle" class="ks-amber"></text>
<text x="185.0" y="99.5" text-anchor="middle" class="ks-amber">As an administrator,</text>
<text x="185.0" y="119.5" text-anchor="middle" class="ks-amber">I want to define the networks</text>
<text x="185.0" y="139.5" text-anchor="middle" class="ks-amber">I am allowed to scan,</text>
<text x="185.0" y="159.5" text-anchor="middle" class="ks-amber">so that I never scan someone</text>
<text x="185.0" y="179.5" text-anchor="middle" class="ks-amber">else's systems by mistake.</text>
<rect x="370" y="20" width="330" height="190" rx="7" class="pnl"/>
<text x="535.0" y="59.5" text-anchor="middle" class="b">acceptance criteria</text>
<text x="535.0" y="79.5" text-anchor="middle" class="c"></text>
<text x="535.0" y="99.5" text-anchor="middle" class="m">Given scope 192.168.56.0/24</text>
<text x="535.0" y="119.5" text-anchor="middle" class="m">When I scan 10.0.0.5</text>
<text x="535.0" y="139.5" text-anchor="middle" class="m">Then no connection is made</text>
<text x="535.0" y="159.5" text-anchor="middle" class="m">And the error names the target</text>
<text x="535.0" y="179.5" text-anchor="middle" class="m">And the exit status is 2</text>
<text x="185" y="12" text-anchor="middle" class="c">front: who, what, why</text>
<text x="535" y="12" text-anchor="middle" class="c">back: how we will know it is done</text>
<rect x="20" y="230" width="105" height="56" rx="7" class="k-green"/>
<text x="72.5" y="253.5" text-anchor="middle" class="kb-green">I</text>
<text x="72.5" y="271.5" text-anchor="middle" class="ks-green">independent</text>
<rect x="135" y="230" width="105" height="56" rx="7" class="k-green"/>
<text x="187.5" y="253.5" text-anchor="middle" class="kb-green">N</text>
<text x="187.5" y="271.5" text-anchor="middle" class="ks-green">negotiable</text>
<rect x="250" y="230" width="105" height="56" rx="7" class="k-green"/>
<text x="302.5" y="253.5" text-anchor="middle" class="kb-green">V</text>
<text x="302.5" y="271.5" text-anchor="middle" class="ks-green">valuable</text>
<rect x="365" y="230" width="105" height="56" rx="7" class="k-green"/>
<text x="417.5" y="253.5" text-anchor="middle" class="kb-green">E</text>
<text x="417.5" y="271.5" text-anchor="middle" class="ks-green">estimable</text>
<rect x="480" y="230" width="105" height="56" rx="7" class="k-green"/>
<text x="532.5" y="253.5" text-anchor="middle" class="kb-green">S</text>
<text x="532.5" y="271.5" text-anchor="middle" class="ks-green">small</text>
<rect x="595" y="230" width="105" height="56" rx="7" class="k-green"/>
<text x="647.5" y="253.5" text-anchor="middle" class="kb-green">T</text>
<text x="647.5" y="271.5" text-anchor="middle" class="ks-green">testable</text>
</g>
</svg>
<figcaption>A story is a promise of a conversation; the acceptance criteria record what the conversation agreed.</figcaption>
</figure>

A story is deliberately short; it is a placeholder for a conversation. The **acceptance criteria** record what the conversation decided and become tests. Writing them in the **Given, When, Then** style of behaviour-driven development (BDD) makes them readable by stakeholders and executable by tools such as `behave` or `pytest-bdd`.

Bill Wake's **INVEST** criteria describe a good story: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, and **T**estable. A story too large for one sprint is an **epic** and must be split, for example by workflow step, by data type, or by happy path first and error handling later.

### Use cases

A **use case** describes how an actor uses the system to reach a goal, including what can go wrong. Ivar Jacobson introduced use cases in the late 1980s, and they became part of UML.

<figure class="diagram">
<svg viewBox="0 0 720 420" style="width:100%;height:auto;max-width:720px" role="img" aria-label="UML use case diagram for NetWarden. Inside the system boundary: run assessment, which includes check scope and discover services, and is extended by fail pipeline on findings; manage scope; start practice targets; view report; compare scans. Actors: administrator (run assessment, manage scope, start practice targets, view report), security manager (view report, compare scans), CI pipeline (run assessment). Target host is a secondary actor of discover services." xmlns="http://www.w3.org/2000/svg">
<style>
.s3h{ font-family:var(--sans),sans-serif; }
.s3h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3h .s{ fill:var(--text-dim); font-size:13px; }
.s3h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3h .c{ fill:var(--text-faint); font-size:12.5px; }
.s3h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3h-a); }
.s3h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3h-a); marker-start:url(#s3h-s); }
.s3h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3h-g); }
.s3h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3h-a); }
.s3h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3h-tri); }
.s3h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3h-tri); }
.s3h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3h-open); }
.s3h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3h-open); }
.s3h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3h-dia); }
.s3h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3h-odia); }
.s3h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3h-dia); marker-end:url(#s3h-open); }
.s3h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3h-solid); }
.s3h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3h-open); }
.s3h .fill{ fill:var(--text); stroke:none; }
.s3h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3h .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s3h .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s3h .ks-teal{ fill:#0F6E56; font-size:13px; }
.s3h .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s3h .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3h .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s3h .kb-teal, :root[data-theme="dark"] .s3h .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s3h .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s3h .kh-teal{ fill:#5DCAA5; }
.s3h .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s3h-teal); }
.s3h .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3h-teal); }
.s3h .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3h-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker></defs>
<g class="s3h">
<rect x="170" y="16" width="420" height="390" rx="6" class="pnl"/>
<text x="380" y="38" text-anchor="middle" class="b">NetWarden</text>
<circle cx="70" cy="49" r="9" class="act"/>
<line x1="70" y1="58" x2="70" y2="84" class="stick"/>
<line x1="56" y1="68" x2="84" y2="68" class="stick"/>
<line x1="70" y1="84" x2="58" y2="102" class="stick"/>
<line x1="70" y1="84" x2="82" y2="102" class="stick"/>
<text x="70" y="120" text-anchor="middle" class="b">administrator</text>
<circle cx="70" cy="299" r="9" class="act"/>
<line x1="70" y1="308" x2="70" y2="334" class="stick"/>
<line x1="56" y1="318" x2="84" y2="318" class="stick"/>
<line x1="70" y1="334" x2="58" y2="352" class="stick"/>
<line x1="70" y1="334" x2="82" y2="352" class="stick"/>
<text x="70" y="370" text-anchor="middle" class="b">security manager</text>
<circle cx="660" cy="39" r="9" class="act"/>
<line x1="660" y1="48" x2="660" y2="74" class="stick"/>
<line x1="646" y1="58" x2="674" y2="58" class="stick"/>
<line x1="660" y1="74" x2="648" y2="92" class="stick"/>
<line x1="660" y1="74" x2="672" y2="92" class="stick"/>
<text x="660" y="110" text-anchor="middle" class="b">CI pipeline</text>
<circle cx="660" cy="259" r="9" class="act"/>
<line x1="660" y1="268" x2="660" y2="294" class="stick"/>
<line x1="646" y1="278" x2="674" y2="278" class="stick"/>
<line x1="660" y1="294" x2="648" y2="312" class="stick"/>
<line x1="660" y1="294" x2="672" y2="312" class="stick"/>
<text x="660" y="330" text-anchor="middle" class="b">target host</text>
<ellipse cx="290" cy="80" rx="80" ry="24" class="k-teal"/>
<text x="290" y="84.5" text-anchor="middle" class="kb-teal">run assessment</text>
<ellipse cx="290" cy="155" rx="80" ry="24" class="k-teal"/>
<text x="290" y="159.5" text-anchor="middle" class="kb-teal">manage scope</text>
<ellipse cx="290" cy="225" rx="80" ry="24" class="k-teal"/>
<text x="290" y="221.0" text-anchor="middle" class="kb-teal">start practice</text>
<text x="290" y="238.0" text-anchor="middle" class="kb-teal">targets</text>
<ellipse cx="290" cy="295" rx="80" ry="24" class="k-teal"/>
<text x="290" y="299.5" text-anchor="middle" class="kb-teal">view report</text>
<ellipse cx="290" cy="365" rx="80" ry="24" class="k-teal"/>
<text x="290" y="369.5" text-anchor="middle" class="kb-teal">compare scans</text>
<ellipse cx="500" cy="160" rx="70" ry="24" class="k-teal"/>
<text x="500" y="156.0" text-anchor="middle" class="kb-teal">fail pipeline</text>
<text x="500" y="173.0" text-anchor="middle" class="kb-teal">on findings</text>
<ellipse cx="500" cy="240" rx="70" ry="24" class="k-teal"/>
<text x="500" y="244.5" text-anchor="middle" class="kb-teal">check scope</text>
<ellipse cx="500" cy="320" rx="70" ry="24" class="k-teal"/>
<text x="500" y="316.0" text-anchor="middle" class="kb-teal">discover</text>
<text x="500" y="333.0" text-anchor="middle" class="kb-teal">services</text>
<line x1="100" y1="78" x2="210" y2="80" class="u"/>
<line x1="100" y1="78" x2="210" y2="155" class="u"/>
<line x1="100" y1="78" x2="210" y2="225" class="u"/>
<line x1="100" y1="78" x2="210" y2="295" class="u"/>
<line x1="100" y1="328" x2="210" y2="295" class="u"/>
<line x1="100" y1="328" x2="210" y2="365" class="u"/>
<line x1="632" y1="66" x2="370" y2="80" class="u"/>
<line x1="632" y1="290" x2="570" y2="316" class="u"/>
<line x1="368" y1="86" x2="430" y2="238" class="dep"/>
<text x="500" y="204" text-anchor="middle" class="c">«include»</text>
<line x1="362" y1="96" x2="432" y2="316" class="dep"/>
<text x="500" y="284" text-anchor="middle" class="c">«include»</text>
<line x1="448" y1="144" x2="362" y2="94" class="dep"/>
<text x="440" y="112" text-anchor="start" class="c">«extend»</text>
</g>
</svg>
<figcaption>Actors outside the boundary, goals inside. Include: always part of; extend: optionally adds to.</figcaption>
</figure>

The diagram gives an overview; the real content is the **use case specification**:

| Field | Run assessment (UC-1) |
|---|---|
| Primary actor | Administrator (or CI pipeline) |
| Goal | Know which services on authorised targets are exposed or vulnerable |
| Preconditions | A scope file exists; the administrator is authorised to assess the targets |
| Main success scenario | 1. Administrator gives targets, scope file and ports. 2. System checks every target against the scope. 3. System discovers open services. 4. System identifies products and versions. 5. System runs the checks. 6. System saves the results and shows the report. |
| Extensions | 2a. A target is outside the scope: system shows an error, sends no traffic, exits with status 2. 3a. No host responds: system reports zero hosts. 6a. Findings at or above the threshold: system exits with status 1. |
| Postconditions | The scan is stored in the history; a report exists |

Use cases are good at capturing **alternative flows**, which user stories tend to leave to the conversation. Many teams use both: stories for planning, use cases for the parts of the system with complex behaviour.

## Prioritisation

There is never time for everything. The **MoSCoW** method sorts requirements into **M**ust have, **S**hould have, **C**ould have and **W**on't have this time.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="MoSCoW prioritisation of NetWarden&#x27;s backlog for release 1.0. Must have: scope, discovery, fingerprinting, known vulnerabilities, remediation, reports. Should have: history and diff, exit codes. Could have: demo targets, HTML styling. Won&#x27;t have this time: live vulnerability feed, backport detection, graphical interface." xmlns="http://www.w3.org/2000/svg">
<style>
.s3g{ font-family:var(--sans),sans-serif; }
.s3g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3g .s{ fill:var(--text-dim); font-size:13px; }
.s3g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3g .c{ fill:var(--text-faint); font-size:12.5px; }
.s3g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3g-a); }
.s3g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3g-a); marker-start:url(#s3g-s); }
.s3g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3g-g); }
.s3g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-a); }
.s3g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3g-tri); }
.s3g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-tri); }
.s3g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3g-open); }
.s3g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-open); }
.s3g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3g-dia); }
.s3g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3g-odia); }
.s3g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3g-dia); marker-end:url(#s3g-open); }
.s3g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3g-solid); }
.s3g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3g-open); }
.s3g .fill{ fill:var(--text); stroke:none; }
.s3g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3g .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s3g .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s3g .ks-blue{ fill:#185FA5; font-size:13px; }
.s3g .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s3g .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3g .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s3g .kb-blue, :root[data-theme="dark"] .s3g .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s3g .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s3g .kh-blue{ fill:#85B7EB; }
.s3g .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s3g-blue); }
.s3g .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-blue); }
.s3g .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s3g .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s3g .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s3g .ks-amber{ fill:#854F0B; font-size:13px; }
.s3g .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s3g .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3g .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s3g .kb-amber, :root[data-theme="dark"] .s3g .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s3g .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s3g .kh-amber{ fill:#EF9F27; }
.s3g .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s3g-amber); }
.s3g .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-amber); }
.s3g .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s3g .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s3g .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s3g .ks-red{ fill:#A32D2D; font-size:13px; }
.s3g .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s3g .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3g .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s3g .kb-red, :root[data-theme="dark"] .s3g .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s3g .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s3g .kh-red{ fill:#F09595; }
.s3g .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s3g-red); }
.s3g .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-red); }
.s3g .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s3g .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s3g .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s3g .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s3g .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s3g .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3g .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s3g .kb-gray, :root[data-theme="dark"] .s3g .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s3g .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s3g .kh-gray{ fill:#B4B2A9; }
.s3g .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s3g-gray); }
.s3g .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3g-gray); }
.s3g .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3g-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s3g-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s3g-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s3g-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s3g">
<rect x="20" y="16" width="160" height="36" rx="7" class="k-red"/>
<text x="100.0" y="38.5" text-anchor="middle" class="kb-red">Must</text>
<rect x="20" y="60" width="160" height="32" rx="5" class="pnl"/>
<text x="100.0" y="80.5" text-anchor="middle" class="s">US-1 scope</text>
<rect x="20" y="98" width="160" height="32" rx="5" class="pnl"/>
<text x="100.0" y="118.5" text-anchor="middle" class="s">US-2 discovery</text>
<rect x="20" y="136" width="160" height="32" rx="5" class="pnl"/>
<text x="100.0" y="156.5" text-anchor="middle" class="s">US-3 fingerprint</text>
<rect x="20" y="174" width="160" height="32" rx="5" class="pnl"/>
<text x="100.0" y="194.5" text-anchor="middle" class="s">US-4 CVEs</text>
<rect x="20" y="212" width="160" height="32" rx="5" class="pnl"/>
<text x="100.0" y="232.5" text-anchor="middle" class="s">US-5 fixes</text>
<rect x="192" y="16" width="160" height="36" rx="7" class="k-amber"/>
<text x="272.0" y="38.5" text-anchor="middle" class="kb-amber">Should</text>
<rect x="192" y="60" width="160" height="32" rx="5" class="pnl"/>
<text x="272.0" y="80.5" text-anchor="middle" class="s">US-6 HTML</text>
<rect x="192" y="98" width="160" height="32" rx="5" class="pnl"/>
<text x="272.0" y="118.5" text-anchor="middle" class="s">US-7 diff</text>
<rect x="192" y="136" width="160" height="32" rx="5" class="pnl"/>
<text x="272.0" y="156.5" text-anchor="middle" class="s">US-8 exit codes</text>
<rect x="364" y="16" width="160" height="36" rx="7" class="k-blue"/>
<text x="444.0" y="38.5" text-anchor="middle" class="kb-blue">Could</text>
<rect x="364" y="60" width="160" height="32" rx="5" class="pnl"/>
<text x="444.0" y="80.5" text-anchor="middle" class="s">US-9 demo</text>
<rect x="364" y="98" width="160" height="32" rx="5" class="pnl"/>
<text x="444.0" y="118.5" text-anchor="middle" class="s">colour report</text>
<rect x="536" y="16" width="160" height="36" rx="7" class="k-gray"/>
<text x="616.0" y="38.5" text-anchor="middle" class="kb-gray">Won't (now)</text>
<rect x="536" y="60" width="160" height="32" rx="5" class="pnl"/>
<text x="616.0" y="80.5" text-anchor="middle" class="s">US-10 live feed</text>
<rect x="536" y="98" width="160" height="32" rx="5" class="pnl"/>
<text x="616.0" y="118.5" text-anchor="middle" class="s">US-11 backports</text>
<rect x="536" y="136" width="160" height="32" rx="5" class="pnl"/>
<text x="616.0" y="156.5" text-anchor="middle" class="s">GUI</text>
</g>
</svg>
<figcaption>Must haves alone should make a usable release. If everything is a must, nothing is prioritised.</figcaption>
</figure>

Other techniques include ranking by value and cost, the **Kano model** (basic expectations, performance attributes, and delighters), and simply ordering the backlog, which is what Scrum requires of the product owner.

## Validation

Validation asks: **are these the right requirements?** It differs from **verification** (does the software meet its requirements?), a distinction Boehm summarised as "building the right product" versus "building the product right". Validation techniques include:

- **Reviews and inspections** of the specification with stakeholders, using a checklist like the table above.
- **Prototypes**: NetWarden's first prototype printed raw banners; administrators immediately asked for the product and version to be parsed out, which became NW-FR-3.
- **Writing acceptance tests early**: a requirement for which nobody can write a test is not finished.
- **Model checking**: drawing the use cases and state diagrams (Chapter 4) often reveals missing cases.

## Managing change and traceability

Requirements change, and that is normal. What matters is that change is **visible and deliberate**. A **baseline** is an agreed version of the requirements; later changes go through **change control**, which records who asked, why, the estimated impact, and the decision.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Traceability for one requirement: the business goal, user story US-1, system requirement NW-SR-1, the design element Scope.expand, the test test_scope_refuses_targets_outside_it, and the commit that implemented it are linked in both directions, so a change at any point shows what else is affected." xmlns="http://www.w3.org/2000/svg">
<style>
.s3i{ font-family:var(--sans),sans-serif; }
.s3i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s3i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s3i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s3i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s3i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s3i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s3i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s3i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s3i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s3i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s3i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s3i .s{ fill:var(--text-dim); font-size:13px; }
.s3i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s3i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .c{ fill:var(--text-faint); font-size:12.5px; }
.s3i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s3i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s3i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s3i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3i-a); }
.s3i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s3i-a); marker-start:url(#s3i-s); }
.s3i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s3i-g); }
.s3i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-a); }
.s3i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s3i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s3i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s3i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s3i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s3i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3i-tri); }
.s3i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-tri); }
.s3i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3i-open); }
.s3i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-open); }
.s3i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3i-dia); }
.s3i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3i-odia); }
.s3i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s3i-dia); marker-end:url(#s3i-open); }
.s3i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s3i-solid); }
.s3i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s3i-open); }
.s3i .fill{ fill:var(--text); stroke:none; }
.s3i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s3i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s3i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s3i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s3i .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s3i .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s3i .ks-teal{ fill:#0F6E56; font-size:13px; }
.s3i .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3i .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s3i .kb-teal, :root[data-theme="dark"] .s3i .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s3i .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s3i .kh-teal{ fill:#5DCAA5; }
.s3i .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s3i-teal); }
.s3i .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-teal); }
.s3i .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s3i .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s3i .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s3i .ks-amber{ fill:#854F0B; font-size:13px; }
.s3i .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3i .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s3i .kb-amber, :root[data-theme="dark"] .s3i .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s3i .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s3i .kh-amber{ fill:#EF9F27; }
.s3i .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s3i-amber); }
.s3i .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-amber); }
.s3i .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s3i .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s3i .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s3i .ks-purple{ fill:#534AB7; font-size:13px; }
.s3i .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3i .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s3i .kb-purple, :root[data-theme="dark"] .s3i .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s3i .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s3i .kh-purple{ fill:#AFA9EC; }
.s3i .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s3i-purple); }
.s3i .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-purple); }
.s3i .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s3i .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s3i .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s3i .ks-green{ fill:#3B6D11; font-size:13px; }
.s3i .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3i .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s3i .kb-green, :root[data-theme="dark"] .s3i .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s3i .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s3i .kh-green{ fill:#97C459; }
.s3i .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s3i-green); }
.s3i .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-green); }
.s3i .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s3i .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s3i .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s3i .ks-red{ fill:#A32D2D; font-size:13px; }
.s3i .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3i .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s3i .kb-red, :root[data-theme="dark"] .s3i .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s3i .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s3i .kh-red{ fill:#F09595; }
.s3i .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s3i-red); }
.s3i .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-red); }
.s3i .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s3i .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s3i .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s3i .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s3i .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s3i .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s3i .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s3i .kb-gray, :root[data-theme="dark"] .s3i .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s3i .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s3i .kh-gray{ fill:#B4B2A9; }
.s3i .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s3i-gray); }
.s3i .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s3i-gray); }
.s3i .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s3i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s3i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s3i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s3i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s3i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s3i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s3i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s3i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s3i-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s3i-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s3i-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s3i-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s3i-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s3i-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s3i">
<rect x="12" y="50" width="96" height="64" rx="7" class="k-purple"/>
<text x="60.0" y="77.5" text-anchor="middle" class="kb-purple">goal</text>
<text x="60.0" y="95.5" text-anchor="middle" class="ks-purple">safe use</text>
<rect x="132" y="50" width="96" height="64" rx="7" class="k-amber"/>
<text x="180.0" y="77.5" text-anchor="middle" class="kb-amber">US-1</text>
<text x="180.0" y="95.5" text-anchor="middle" class="ks-amber">story</text>
<line x1="110" y1="82" x2="130" y2="82" class="ar2"/>
<rect x="252" y="50" width="96" height="64" rx="7" class="k-red"/>
<text x="300.0" y="77.5" text-anchor="middle" class="kb-red">NW-SR-1</text>
<text x="300.0" y="95.5" text-anchor="middle" class="ks-red">requirement</text>
<line x1="230" y1="82" x2="250" y2="82" class="ar2"/>
<rect x="372" y="50" width="96" height="64" rx="7" class="k-teal"/>
<text x="420.0" y="77.5" text-anchor="middle" class="kb-teal">Scope</text>
<text x="420.0" y="95.5" text-anchor="middle" class="ks-teal">expand()</text>
<line x1="350" y1="82" x2="370" y2="82" class="ar2"/>
<rect x="492" y="50" width="96" height="64" rx="7" class="k-green"/>
<text x="540.0" y="77.5" text-anchor="middle" class="kb-green">test_scope_</text>
<text x="540.0" y="95.5" text-anchor="middle" class="ks-green">refuses_...</text>
<line x1="470" y1="82" x2="490" y2="82" class="ar2"/>
<rect x="612" y="50" width="96" height="64" rx="7" class="k-gray"/>
<text x="660.0" y="77.5" text-anchor="middle" class="kb-gray">3f2a9c1</text>
<text x="660.0" y="95.5" text-anchor="middle" class="ks-gray">commit</text>
<line x1="590" y1="82" x2="610" y2="82" class="ar2"/>
<text x="360" y="30" text-anchor="middle" class="kh-teal">forward: is every requirement implemented and tested?</text>
<text x="360" y="150" text-anchor="middle" class="kh-purple">backward: why does this code exist? what breaks if the requirement changes?</text>
<rect x="20" y="180" width="680" height="50" rx="7" class="pnl"/>
<text x="360.0" y="209.5" text-anchor="middle" class="s">NetWarden: IDs in requirements.md, test names, code comments and commit messages</text>
</g>
</svg>
<figcaption>Traceability is cheap to maintain with consistent IDs, and invaluable during change and audits.</figcaption>
</figure>

**Traceability** links each requirement backwards to its source and forwards to the design, code and tests that realise it. When the scope rule changes, the trace shows exactly which code and tests must change. With consistent identifiers, a team can maintain traceability using nothing more than conventions: NetWarden's requirements table has a "Verified by" column naming tests, code comments mention requirement IDs, and commit messages mention story IDs.

## Summary

- Requirements engineering covers **elicitation, analysis, specification, validation and management**.
- Identify all **stakeholders**, including people affected by the system who never use it.
- Distinguish **business, user and system** requirements, and **functional** from **non-functional** ones.
- Good requirements are **unambiguous, verifiable, singular, feasible, necessary** and say **what**, not how. Make non-functional requirements **measurable**.
- **User stories** with **acceptance criteria** suit agile planning; **use cases** capture alternative flows.
- Prioritise with **MoSCoW** or an ordered backlog.
- **Validate** that requirements are right; **trace** them to design, code and tests; control **change**.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-3-requirements-engineering).

**1. Which requirements engineering activity checks that these are the right requirements?**

- A. Validation
- B. Elicitation
- C. Specification
- D. Management

**2. For NetWarden, who is a stakeholder who never uses the system?**

- A. The administrator
- B. The developers
- C. The owners of the machines being scanned
- D. The CI pipeline

**3. Which of these is a well-written non-functional requirement?**

- A. The scan should be fast
- B. The tool should be safe
- C. The code should be maintainable
- D. A /24 network on the 17 default ports shall complete in under 60 s on a LAN

**4. The requirement 'Use a SQLite table' is poor. Which characteristic does it break?**

- A. Verifiable
- B. Appropriate: it says how, not what
- C. Singular
- D. Feasible

**5. What is the role of acceptance criteria in a user story?**

- A. They estimate the story
- B. They name the user role
- C. They record what the conversation decided, and become tests
- D. They assign the story to a sprint

**6. What does INVEST stand for?**

- A. Independent, Negotiable, Valuable, Estimable, Small, Testable
- B. Iterative, New, Verified, Estimated, Simple, Tracked
- C. Important, Necessary, Valid, Exact, Short, Timed
- D. Initial, Normal, Variable, Extended, Stable, Typed

**7. What are use cases better at than user stories?**

- A. Capturing alternative flows, such as what happens when a target is out of scope
- B. Estimating effort
- C. Prioritising
- D. Describing the user interface

**8. What does traceability give you when the scope rule changes?**

- A. A new baseline automatically
- B. A MoSCoW priority
- C. Links showing exactly which design, code and tests realise that requirement
- D. An approval from the product owner
