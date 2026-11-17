# Chapter 12: Quality Assurance and Secure Development

Testing finds problems in a product that already exists. **Quality assurance** (QA) is the broader effort to build quality in: to prevent defects through good process, catch them early through reviews and analysis, and learn from those that escape. For software that people depend on, **security** is part of quality, and it too must be designed in rather than tested in at the end. This chapter covers both, with NetWarden, itself a security tool, as the example.

## Quality assurance and quality control

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Quality assurance, quality control and testing. Quality assurance is process-oriented and preventive: standards, reviews, definitions of done, training, audits. Quality control is product-oriented and detective: inspections, testing, static analysis of the actual work products. Testing is one quality control activity." xmlns="http://www.w3.org/2000/svg">
<style>
.s12a{ font-family:var(--sans),sans-serif; }
.s12a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12a .s{ fill:var(--text-dim); font-size:13px; }
.s12a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12a .c{ fill:var(--text-faint); font-size:12.5px; }
.s12a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12a-a); }
.s12a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12a-a); marker-start:url(#s12a-s); }
.s12a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12a-g); }
.s12a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12a-a); }
.s12a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12a-tri); }
.s12a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12a-tri); }
.s12a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12a-open); }
.s12a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12a-open); }
.s12a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12a-dia); }
.s12a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12a-odia); }
.s12a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12a-dia); marker-end:url(#s12a-open); }
.s12a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12a-solid); }
.s12a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12a-open); }
.s12a .fill{ fill:var(--text); stroke:none; }
.s12a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12a .ks-blue{ fill:#185FA5; font-size:13px; }
.s12a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12a .kb-blue, :root[data-theme="dark"] .s12a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12a .kh-blue{ fill:#85B7EB; }
.s12a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12a-blue); }
.s12a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12a-blue); }
.s12a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s12a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s12a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s12a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s12a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s12a .kb-teal, :root[data-theme="dark"] .s12a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s12a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s12a .kh-teal{ fill:#5DCAA5; }
.s12a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s12a-teal); }
.s12a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12a-teal); }
.s12a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s12a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s12a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s12a .ks-amber{ fill:#854F0B; font-size:13px; }
.s12a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s12a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s12a .kb-amber, :root[data-theme="dark"] .s12a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s12a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s12a .kh-amber{ fill:#EF9F27; }
.s12a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s12a-amber); }
.s12a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12a-amber); }
.s12a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s12a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker></defs>
<g class="s12a">
<rect x="20" y="20" width="680" height="190" rx="10" class="k-blue"/>
<text x="40" y="44" text-anchor="start" class="kh-blue">quality assurance: process, prevent</text>
<text x="40" y="64" text-anchor="start" class="c">standards, reviews of process, definition of done, audits, training</text>
<rect x="60" y="84" width="600" height="110" rx="10" class="k-teal"/>
<text x="80" y="108" text-anchor="start" class="kh-teal">quality control: product, detect</text>
<text x="80" y="128" text-anchor="start" class="c">inspections, static analysis, metrics</text>
<rect x="100" y="142" width="220" height="40" rx="7" class="k-amber"/>
<text x="210.0" y="166.5" text-anchor="middle" class="kb-amber">testing</text>
<rect x="340" y="142" width="300" height="40" rx="7" class="pnl"/>
<text x="490.0" y="166.5" text-anchor="middle" class="s">static analysis: ruff, mypy, bandit</text>
</g>
</svg>
<figcaption>Testing alone finds problems late. Quality assurance aims to stop them being created.</figcaption>
</figure>

| | Quality assurance | Quality control |
|---|---|---|
| Focus | Process | Product |
| Aim | Prevent defects | Detect defects |
| Examples | Coding standards, definition of done, training, process audits, retrospectives | Reviews, inspections, static analysis, testing |
| Who | Everyone, supported by QA specialists | Everyone, supported by testers |

Organisations formalise QA with standards such as **ISO 9001** (quality management systems in general) and maturity models such as **CMMI**, which rate how defined, measured and continuously improved a development process is. Agile teams achieve much of the same through small practices done consistently: the definition of done, reviews, automated checks, and retrospectives.

## Reviews and inspections

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Fagan inspection: planning, overview, individual preparation with a checklist, an inspection meeting led by a moderator that logs defects but does not fix them, rework by the author, and follow-up to verify the fixes and collect data." xmlns="http://www.w3.org/2000/svg">
<style>
.s12b{ font-family:var(--sans),sans-serif; }
.s12b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12b .s{ fill:var(--text-dim); font-size:13px; }
.s12b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .c{ fill:var(--text-faint); font-size:12.5px; }
.s12b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12b-a); }
.s12b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12b-a); marker-start:url(#s12b-s); }
.s12b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12b-g); }
.s12b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-a); }
.s12b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12b-tri); }
.s12b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-tri); }
.s12b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12b-open); }
.s12b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-open); }
.s12b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12b-dia); }
.s12b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12b-odia); }
.s12b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12b-dia); marker-end:url(#s12b-open); }
.s12b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12b-solid); }
.s12b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12b-open); }
.s12b .fill{ fill:var(--text); stroke:none; }
.s12b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12b .ks-blue{ fill:#185FA5; font-size:13px; }
.s12b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12b .kb-blue, :root[data-theme="dark"] .s12b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12b .kh-blue{ fill:#85B7EB; }
.s12b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12b-blue); }
.s12b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-blue); }
.s12b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s12b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s12b .ks-amber{ fill:#854F0B; font-size:13px; }
.s12b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s12b .kb-amber, :root[data-theme="dark"] .s12b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s12b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s12b .kh-amber{ fill:#EF9F27; }
.s12b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s12b-amber); }
.s12b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-amber); }
.s12b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s12b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s12b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s12b .ks-purple{ fill:#534AB7; font-size:13px; }
.s12b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s12b .kb-purple, :root[data-theme="dark"] .s12b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s12b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s12b .kh-purple{ fill:#AFA9EC; }
.s12b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s12b-purple); }
.s12b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-purple); }
.s12b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s12b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s12b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s12b .ks-green{ fill:#3B6D11; font-size:13px; }
.s12b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s12b .kb-green, :root[data-theme="dark"] .s12b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s12b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s12b .kh-green{ fill:#97C459; }
.s12b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s12b-green); }
.s12b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-green); }
.s12b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s12b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s12b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s12b .ks-red{ fill:#A32D2D; font-size:13px; }
.s12b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s12b .kb-red, :root[data-theme="dark"] .s12b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s12b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s12b .kh-red{ fill:#F09595; }
.s12b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s12b-red); }
.s12b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-red); }
.s12b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s12b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s12b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s12b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s12b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s12b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s12b .kb-gray, :root[data-theme="dark"] .s12b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s12b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s12b .kh-gray{ fill:#B4B2A9; }
.s12b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s12b-gray); }
.s12b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12b-gray); }
.s12b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s12b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s12b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s12b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s12b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s12b">
<rect x="20" y="60" width="104" height="64" rx="7" class="k-gray"/>
<text x="72.0" y="87.5" text-anchor="middle" class="kb-gray">planning</text>
<text x="72.0" y="105.5" text-anchor="middle" class="ks-gray">moderator</text>
<rect x="136" y="60" width="104" height="64" rx="7" class="k-blue"/>
<text x="188.0" y="87.5" text-anchor="middle" class="kb-blue">overview</text>
<text x="188.0" y="105.5" text-anchor="middle" class="ks-blue">explain</text>
<line x1="124" y1="92" x2="134" y2="92" class="ar"/>
<rect x="252" y="60" width="104" height="64" rx="7" class="k-purple"/>
<text x="304.0" y="87.5" text-anchor="middle" class="kb-purple">preparation</text>
<text x="304.0" y="105.5" text-anchor="middle" class="ks-purple">checklist</text>
<line x1="240" y1="92" x2="250" y2="92" class="ar"/>
<rect x="368" y="60" width="104" height="64" rx="7" class="k-red"/>
<text x="420.0" y="87.5" text-anchor="middle" class="kb-red">meeting</text>
<text x="420.0" y="105.5" text-anchor="middle" class="ks-red">log defects</text>
<line x1="356" y1="92" x2="366" y2="92" class="ar"/>
<rect x="484" y="60" width="104" height="64" rx="7" class="k-amber"/>
<text x="536.0" y="87.5" text-anchor="middle" class="kb-amber">rework</text>
<text x="536.0" y="105.5" text-anchor="middle" class="ks-amber">author fixes</text>
<line x1="472" y1="92" x2="482" y2="92" class="ar"/>
<rect x="600" y="60" width="104" height="64" rx="7" class="k-green"/>
<text x="652.0" y="87.5" text-anchor="middle" class="kb-green">follow-up</text>
<text x="652.0" y="105.5" text-anchor="middle" class="ks-green">verify</text>
<line x1="588" y1="92" x2="598" y2="92" class="ar"/>
<text x="360" y="170" text-anchor="middle" class="c">formal, slow and very effective; modern pull-request review is its lightweight descendant</text>
</g>
</svg>
<figcaption>Michael Fagan, IBM, 1976. Inspections remain common in safety-critical work.</figcaption>
</figure>

Reviews are the oldest quality technique and still one of the most cost-effective, because they find defects in requirements, designs and code **before** they become failures, and they find kinds of defects that tests do not: unclear names, missing requirements, security weaknesses, duplicated logic. Their formality ranges widely:

| Type | Formality | Typical use |
|---|---|---|
| Pair programming | Continuous, informal | Complex or critical code |
| Pull-request review | Asynchronous, tool-supported | Every change (Chapter 8) |
| Walkthrough | Author leads the group through the work | Designs, onboarding |
| Technical review | Peers evaluate against standards | Architecture, ADRs |
| Inspection | Formal roles, checklists, metrics | Safety-critical code, requirements baselines |

**Checklists** make reviews consistent. A NetWarden review checklist includes: is every new target-handling path routed through `Scope`? Is all network data escaped before it reaches HTML? Does every new finding include evidence and remediation? Is there a test for the new behaviour?

## Static analysis

**Static analysis** examines code without running it. NetWarden's pipeline runs three kinds:

| Tool | Finds | Example |
|---|---|---|
| **ruff** (lint, with bugbear rules) | Likely bugs, unused code, bad patterns | Mutable default arguments, unused imports |
| **ruff `S` rules** (bandit, security) | Insecure code patterns | `shell=True`, `pickle.loads`, hard-coded passwords, binding to all interfaces |
| **mypy** (strict) | Type errors | Comparing `None` with a `Severity` |

Larger organisations add deeper **SAST** (static application security testing) tools such as CodeQL or Semgrep, which trace untrusted data through the program. Static analysis produces false positives, so tune the rules and require a short justification comment, such as `# noqa: S104  binding to all interfaces is intended here`, for each suppression.

## Metrics

Metrics turn quality into numbers that can be tracked, but every metric can be gamed or misread. **Goodhart's law**: when a measure becomes a target, it ceases to be a good measure. Victor Basili's **goal, question, metric** (GQM) approach starts from what you want to know.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Goal, question, metric for NetWarden. Goal: improve the reliability of NetWarden&#x27;s findings. Questions: how many reported findings are false positives? How quickly are defects fixed? Metrics: false positive rate from manual verification of a sample; defects found after release per release; mean time from defect report to fix." xmlns="http://www.w3.org/2000/svg">
<style>
.s12c{ font-family:var(--sans),sans-serif; }
.s12c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12c .s{ fill:var(--text-dim); font-size:13px; }
.s12c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12c .c{ fill:var(--text-faint); font-size:12.5px; }
.s12c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12c-a); }
.s12c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12c-a); marker-start:url(#s12c-s); }
.s12c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12c-g); }
.s12c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12c-a); }
.s12c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12c-tri); }
.s12c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12c-tri); }
.s12c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12c-open); }
.s12c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12c-open); }
.s12c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12c-dia); }
.s12c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12c-odia); }
.s12c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12c-dia); marker-end:url(#s12c-open); }
.s12c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12c-solid); }
.s12c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12c-open); }
.s12c .fill{ fill:var(--text); stroke:none; }
.s12c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12c .ks-blue{ fill:#185FA5; font-size:13px; }
.s12c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12c .kb-blue, :root[data-theme="dark"] .s12c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12c .kh-blue{ fill:#85B7EB; }
.s12c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12c-blue); }
.s12c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12c-blue); }
.s12c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s12c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s12c .ks-purple{ fill:#534AB7; font-size:13px; }
.s12c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s12c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s12c .kb-purple, :root[data-theme="dark"] .s12c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s12c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s12c .kh-purple{ fill:#AFA9EC; }
.s12c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s12c-purple); }
.s12c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12c-purple); }
.s12c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s12c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s12c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s12c .ks-green{ fill:#3B6D11; font-size:13px; }
.s12c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s12c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s12c .kb-green, :root[data-theme="dark"] .s12c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s12c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s12c .kh-green{ fill:#97C459; }
.s12c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s12c-green); }
.s12c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12c-green); }
.s12c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s12c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s12c">
<rect x="170" y="16" width="380" height="50" rx="7" class="k-purple"/>
<text x="360.0" y="36.5" text-anchor="middle" class="kb-purple">goal: trustworthy findings</text>
<text x="360.0" y="54.5" text-anchor="middle" class="ks-purple">improve reliability, from the administrators' view</text>
<rect x="30" y="110" width="210" height="50" rx="5" class="k-blue"/>
<text x="135.0" y="139.5" text-anchor="middle" class="ks-blue">Q1: how many are false?</text>
<line x1="360" y1="68" x2="135" y2="108" class="u"/>
<rect x="30" y="210" width="210" height="56" rx="5" class="k-green"/>
<text x="135.0" y="233.5" text-anchor="middle" class="kb-green">false positive rate</text>
<text x="135.0" y="251.5" text-anchor="middle" class="ks-green">sampled, verified by hand</text>
<line x1="135" y1="162" x2="135" y2="208" class="u"/>
<rect x="260" y="110" width="210" height="50" rx="5" class="k-blue"/>
<text x="365.0" y="139.5" text-anchor="middle" class="ks-blue">Q2: how many bugs escape?</text>
<line x1="360" y1="68" x2="365" y2="108" class="u"/>
<rect x="260" y="210" width="210" height="56" rx="5" class="k-green"/>
<text x="365.0" y="233.5" text-anchor="middle" class="kb-green">defects after release</text>
<text x="365.0" y="251.5" text-anchor="middle" class="ks-green">per release</text>
<line x1="365" y1="162" x2="365" y2="208" class="u"/>
<rect x="490" y="110" width="210" height="50" rx="5" class="k-blue"/>
<text x="595.0" y="139.5" text-anchor="middle" class="ks-blue">Q3: how fast are fixes?</text>
<line x1="360" y1="68" x2="595" y2="108" class="u"/>
<rect x="490" y="210" width="210" height="56" rx="5" class="k-green"/>
<text x="595.0" y="233.5" text-anchor="middle" class="kb-green">mean time to fix</text>
<text x="595.0" y="251.5" text-anchor="middle" class="ks-green">report to merged fix</text>
<line x1="595" y1="162" x2="595" y2="208" class="u"/>
</g>
</svg>
<figcaption>Start from a goal, ask questions that tell you whether you are reaching it, and only then choose metrics (Basili, GQM).</figcaption>
</figure>

Common product metrics, with NetWarden's values:

| Metric | What it indicates | NetWarden |
|---|---|---|
| Lines of code | Size, roughly | about 900 in `src/` (568 statements) |
| Cyclomatic complexity | Testing effort, comprehension difficulty | Average 3.1 (grade A in radon); highest 9 |
| Test coverage | Untested code | 95% statements |
| Static analysis findings | Rule violations | 0 (CI enforces) |
| Defect density | Defects per thousand lines | Tracked per release |
| Dependencies with known vulnerabilities | Supply-chain risk | 0 (`pip-audit`) |

```bash
pip install radon
radon cc -s -a src/netwarden     # cyclomatic complexity, average A (3.1)
radon mi src/netwarden           # maintainability index
```

Process metrics, such as lead time, deployment frequency, change failure rate and time to restore, are covered in Chapter 14.

## Managing defects

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The lifecycle of a defect report: new, triaged with a severity and priority, assigned, in progress, fixed with a regression test, verified and closed. A verified failure reopens it. Triage may also close it as duplicate, won&#x27;t fix, or cannot reproduce." xmlns="http://www.w3.org/2000/svg">
<style>
.s12d{ font-family:var(--sans),sans-serif; }
.s12d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12d .s{ fill:var(--text-dim); font-size:13px; }
.s12d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .c{ fill:var(--text-faint); font-size:12.5px; }
.s12d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12d-a); }
.s12d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12d-a); marker-start:url(#s12d-s); }
.s12d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12d-g); }
.s12d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-a); }
.s12d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12d-tri); }
.s12d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-tri); }
.s12d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12d-open); }
.s12d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-open); }
.s12d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12d-dia); }
.s12d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12d-odia); }
.s12d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12d-dia); marker-end:url(#s12d-open); }
.s12d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12d-solid); }
.s12d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12d-open); }
.s12d .fill{ fill:var(--text); stroke:none; }
.s12d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12d .ks-blue{ fill:#185FA5; font-size:13px; }
.s12d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12d .kb-blue, :root[data-theme="dark"] .s12d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12d .kh-blue{ fill:#85B7EB; }
.s12d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12d-blue); }
.s12d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-blue); }
.s12d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12d .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s12d .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s12d .ks-teal{ fill:#0F6E56; font-size:13px; }
.s12d .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12d .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s12d .kb-teal, :root[data-theme="dark"] .s12d .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s12d .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s12d .kh-teal{ fill:#5DCAA5; }
.s12d .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s12d-teal); }
.s12d .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-teal); }
.s12d .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s12d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s12d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s12d .ks-amber{ fill:#854F0B; font-size:13px; }
.s12d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s12d .kb-amber, :root[data-theme="dark"] .s12d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s12d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s12d .kh-amber{ fill:#EF9F27; }
.s12d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s12d-amber); }
.s12d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-amber); }
.s12d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s12d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s12d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s12d .ks-purple{ fill:#534AB7; font-size:13px; }
.s12d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s12d .kb-purple, :root[data-theme="dark"] .s12d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s12d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s12d .kh-purple{ fill:#AFA9EC; }
.s12d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s12d-purple); }
.s12d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-purple); }
.s12d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s12d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s12d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s12d .ks-green{ fill:#3B6D11; font-size:13px; }
.s12d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s12d .kb-green, :root[data-theme="dark"] .s12d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s12d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s12d .kh-green{ fill:#97C459; }
.s12d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s12d-green); }
.s12d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-green); }
.s12d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s12d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s12d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s12d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s12d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s12d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s12d .kb-gray, :root[data-theme="dark"] .s12d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s12d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s12d .kh-gray{ fill:#B4B2A9; }
.s12d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s12d-gray); }
.s12d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12d-gray); }
.s12d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12d-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s12d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s12d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s12d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s12d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s12d">
<circle cx="30" cy="60" r="9" class="fill"/>
<rect x="60" y="40" width="98" height="40" rx="16" class="k-gray"/>
<text x="109.0" y="64.5" text-anchor="middle" class="kb-gray">new</text>
<rect x="175" y="40" width="98" height="40" rx="16" class="k-purple"/>
<text x="224.0" y="64.5" text-anchor="middle" class="kb-purple">triaged</text>
<rect x="290" y="40" width="98" height="40" rx="16" class="k-blue"/>
<text x="339.0" y="64.5" text-anchor="middle" class="kb-blue">assigned</text>
<rect x="405" y="40" width="98" height="40" rx="16" class="k-amber"/>
<text x="454.0" y="64.5" text-anchor="middle" class="kb-amber">in progress</text>
<rect x="520" y="40" width="98" height="40" rx="16" class="k-teal"/>
<text x="569.0" y="64.5" text-anchor="middle" class="kb-teal">fixed</text>
<rect x="620" y="40" width="80" height="40" rx="16" class="k-green"/>
<text x="660.0" y="64.5" text-anchor="middle" class="kb-green">verified</text>
<line x1="158" y1="60" x2="173" y2="60" class="msg"/>
<line x1="273" y1="60" x2="288" y2="60" class="msg"/>
<line x1="388" y1="60" x2="403" y2="60" class="msg"/>
<line x1="503" y1="60" x2="518" y2="60" class="msg"/>
<line x1="618" y1="60" x2="618" y2="60" class="msg"/>
<line x1="39" y1="60" x2="58" y2="60" class="msg"/>
<rect x="570" y="160" width="130" height="40" rx="16" class="k-gray"/>
<text x="635.0" y="184.5" text-anchor="middle" class="kb-gray">closed</text>
<line x1="660" y1="82" x2="640" y2="158" class="msg"/>
<circle cx="635" cy="260" r="11" class="act"/>
<circle cx="635" cy="260" r="6.5" class="fill"/>
<line x1="635" y1="202" x2="635" y2="248" class="msg"/>
<path d="M540 82 C 540 130, 460 130, 455 84" class="msg"/>
<text x="500" y="140" text-anchor="middle" class="c">fails verification: reopened</text>
<rect x="90" y="160" width="320" height="40" rx="16" class="k-gray"/>
<text x="250.0" y="184.5" text-anchor="middle" class="kb-gray">duplicate / won't fix / can't reproduce</text>
<line x1="224" y1="82" x2="250" y2="158" class="msg"/>
<path d="M250 202 C 250 250, 560 260, 623 260" class="msg"/>
<text x="360" y="290" text-anchor="middle" class="c">severity: impact on users (critical ... low); priority: order of fixing; they are different</text>
</g>
</svg>
<figcaption>Every bug fix comes with a test that reproduces the bug, so it cannot silently come back (a regression test).</figcaption>
</figure>

A good defect report contains: a short summary, steps to reproduce, expected and actual results, environment (version, operating system, Python version), evidence (logs, output), and **severity** (impact) as opposed to **priority** (order of fixing). A cosmetic typo in the report title may have low severity and high priority before a demo; a crash on IPv6 targets may have high severity and low priority if nobody scans IPv6 yet.

Two habits turn defects into improvements:

- **Every fix gets a regression test** that fails before the fix and passes after it.
- **Root cause analysis** for significant defects: ask "why?" until you reach a process cause that can be changed (the "five whys"). Why did NetWarden report OpenSSH 10.0 as vulnerable in a prototype? Versions were compared as strings. Why was that not caught? No boundary tests for version ranges. Why? No test design technique was applied to the knowledge base. Action: boundary value tests for every range, added to the review checklist.

## Secure development

### Security across the lifecycle

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Security activities across the lifecycle. Requirements: security requirements and abuse cases. Design: threat modelling. Implementation: secure coding standards, static analysis and code review. Testing: security tests, dependency scanning, fuzzing. Release: software bill of materials and signed artifacts. Operations: monitoring, patching and incident response." xmlns="http://www.w3.org/2000/svg">
<style>
.s12e{ font-family:var(--sans),sans-serif; }
.s12e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12e .s{ fill:var(--text-dim); font-size:13px; }
.s12e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .c{ fill:var(--text-faint); font-size:12.5px; }
.s12e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12e-a); }
.s12e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12e-a); marker-start:url(#s12e-s); }
.s12e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12e-g); }
.s12e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-a); }
.s12e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12e-tri); }
.s12e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-tri); }
.s12e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12e-open); }
.s12e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-open); }
.s12e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12e-dia); }
.s12e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12e-odia); }
.s12e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12e-dia); marker-end:url(#s12e-open); }
.s12e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12e-solid); }
.s12e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12e-open); }
.s12e .fill{ fill:var(--text); stroke:none; }
.s12e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12e .ks-blue{ fill:#185FA5; font-size:13px; }
.s12e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12e .kb-blue, :root[data-theme="dark"] .s12e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12e .kh-blue{ fill:#85B7EB; }
.s12e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12e-blue); }
.s12e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-blue); }
.s12e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s12e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s12e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s12e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s12e .kb-teal, :root[data-theme="dark"] .s12e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s12e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s12e .kh-teal{ fill:#5DCAA5; }
.s12e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s12e-teal); }
.s12e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-teal); }
.s12e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s12e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s12e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s12e .ks-amber{ fill:#854F0B; font-size:13px; }
.s12e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s12e .kb-amber, :root[data-theme="dark"] .s12e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s12e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s12e .kh-amber{ fill:#EF9F27; }
.s12e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s12e-amber); }
.s12e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-amber); }
.s12e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s12e .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s12e .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s12e .ks-coral{ fill:#993C1D; font-size:13px; }
.s12e .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s12e .kb-coral, :root[data-theme="dark"] .s12e .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s12e .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s12e .kh-coral{ fill:#F0997B; }
.s12e .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s12e-coral); }
.s12e .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-coral); }
.s12e .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s12e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s12e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s12e .ks-purple{ fill:#534AB7; font-size:13px; }
.s12e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s12e .kb-purple, :root[data-theme="dark"] .s12e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s12e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s12e .kh-purple{ fill:#AFA9EC; }
.s12e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s12e-purple); }
.s12e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-purple); }
.s12e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s12e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s12e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s12e .ks-green{ fill:#3B6D11; font-size:13px; }
.s12e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s12e .kb-green, :root[data-theme="dark"] .s12e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s12e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s12e .kh-green{ fill:#97C459; }
.s12e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s12e-green); }
.s12e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-green); }
.s12e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s12e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s12e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s12e .ks-red{ fill:#A32D2D; font-size:13px; }
.s12e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s12e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s12e .kb-red, :root[data-theme="dark"] .s12e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s12e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s12e .kh-red{ fill:#F09595; }
.s12e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s12e-red); }
.s12e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12e-red); }
.s12e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s12e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s12e-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s12e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s12e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s12e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s12e">
<rect x="20" y="20" width="104" height="40" rx="7" class="k-blue"/>
<text x="72.0" y="44.5" text-anchor="middle" class="kb-blue">requirements</text>
<rect x="20" y="74" width="104" height="38" rx="4" class="pnl"/>
<text x="72.0" y="97.5" text-anchor="middle" class="c">security reqs</text>
<rect x="20" y="120" width="104" height="38" rx="4" class="pnl"/>
<text x="72.0" y="143.5" text-anchor="middle" class="c">abuse cases</text>
<rect x="136" y="20" width="104" height="40" rx="7" class="k-purple"/>
<text x="188.0" y="44.5" text-anchor="middle" class="kb-purple">design</text>
<rect x="136" y="74" width="104" height="38" rx="4" class="pnl"/>
<text x="188.0" y="97.5" text-anchor="middle" class="c">threat model</text>
<rect x="136" y="120" width="104" height="38" rx="4" class="pnl"/>
<text x="188.0" y="143.5" text-anchor="middle" class="c">secure defaults</text>
<rect x="252" y="20" width="104" height="40" rx="7" class="k-teal"/>
<text x="304.0" y="44.5" text-anchor="middle" class="kb-teal">code</text>
<rect x="252" y="74" width="104" height="38" rx="4" class="pnl"/>
<text x="304.0" y="97.5" text-anchor="middle" class="c">SAST (ruff S)</text>
<rect x="252" y="120" width="104" height="38" rx="4" class="pnl"/>
<text x="304.0" y="143.5" text-anchor="middle" class="c">review</text>
<rect x="368" y="20" width="104" height="40" rx="7" class="k-amber"/>
<text x="420.0" y="44.5" text-anchor="middle" class="kb-amber">test</text>
<rect x="368" y="74" width="104" height="38" rx="4" class="pnl"/>
<text x="420.0" y="97.5" text-anchor="middle" class="c">security tests</text>
<rect x="368" y="120" width="104" height="38" rx="4" class="pnl"/>
<text x="420.0" y="143.5" text-anchor="middle" class="c">pip-audit, fuzz</text>
<rect x="484" y="20" width="104" height="40" rx="7" class="k-coral"/>
<text x="536.0" y="44.5" text-anchor="middle" class="kb-coral">release</text>
<rect x="484" y="74" width="104" height="38" rx="4" class="pnl"/>
<text x="536.0" y="97.5" text-anchor="middle" class="c">SBOM</text>
<rect x="484" y="120" width="104" height="38" rx="4" class="pnl"/>
<text x="536.0" y="143.5" text-anchor="middle" class="c">signed builds</text>
<rect x="600" y="20" width="104" height="40" rx="7" class="k-green"/>
<text x="652.0" y="44.5" text-anchor="middle" class="kb-green">operate</text>
<rect x="600" y="74" width="104" height="38" rx="4" class="pnl"/>
<text x="652.0" y="97.5" text-anchor="middle" class="c">monitor, patch</text>
<rect x="600" y="120" width="104" height="38" rx="4" class="pnl"/>
<text x="652.0" y="143.5" text-anchor="middle" class="c">incidents</text>
<path d="M30 190 L690 190" class="ar"/>
<text x="360" y="222" text-anchor="middle" class="kh-red">"shift left": the earlier a security flaw is found, the cheaper it is (Chapter 1)</text>
<text x="360" y="252" text-anchor="middle" class="c">frameworks: Microsoft SDL, OWASP SAMM, NIST SSDF (SP 800-218)</text>
</g>
</svg>
<figcaption>Security is not a phase at the end. Each activity has a security counterpart.</figcaption>
</figure>

A **secure software development lifecycle** (SSDLC) adds a security activity to every phase. Well-known frameworks include Microsoft's Security Development Lifecycle (SDL), the OWASP Software Assurance Maturity Model (SAMM), and NIST's **Secure Software Development Framework** (SSDF, SP 800-218), which US government suppliers are expected to follow.

### Security requirements and abuse cases

Use cases describe what users want to do; **abuse cases** describe what an attacker or a careless user might do, and turn into requirements:

| Abuse case | Requirement |
|---|---|
| A user mistypes a subnet and scans another organisation | NW-SR-1: refuse targets outside the scope, before any packet |
| A user scans a /8 by accident, flooding the network | NW-SR-2: refuse more than 1024 hosts; NW-NFR-3: concurrency limit |
| A malicious host sends a banner containing `<script>` | NW-SR-4: escape all network data in HTML reports |
| Someone uses NetWarden as an attack tool | NW-SR-3: no exploitation, login attempts or changes to targets |

### Threat modelling

**Threat modelling** asks, during design: what are we building, what can go wrong, what are we going to do about it, and did we do a good job? (Adam Shostack's four questions). A common method draws a **data flow diagram** with **trust boundaries** and walks each element through Microsoft's **STRIDE** categories.

<figure class="diagram">
<svg viewBox="0 0 720 340" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Data flow diagram of NetWarden for threat modelling. The administrator gives commands to the NetWarden process. NetWarden reads the scope file and the knowledge base, writes the history database and report files, and exchanges TCP traffic with target hosts across a trust boundary. Data from targets, such as banners, is untrusted. STRIDE threats are marked: spoofing and elevation from banners, tampering with the scope file, information disclosure from reports and the database, denial of service against the network." xmlns="http://www.w3.org/2000/svg">
<style>
.s12f{ font-family:var(--sans),sans-serif; }
.s12f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12f .s{ fill:var(--text-dim); font-size:13px; }
.s12f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .c{ fill:var(--text-faint); font-size:12.5px; }
.s12f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12f-a); }
.s12f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12f-a); marker-start:url(#s12f-s); }
.s12f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12f-g); }
.s12f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-a); }
.s12f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12f-tri); }
.s12f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-tri); }
.s12f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12f-open); }
.s12f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-open); }
.s12f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12f-dia); }
.s12f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12f-odia); }
.s12f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12f-dia); marker-end:url(#s12f-open); }
.s12f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12f-solid); }
.s12f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12f-open); }
.s12f .fill{ fill:var(--text); stroke:none; }
.s12f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12f .ks-blue{ fill:#185FA5; font-size:13px; }
.s12f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12f .kb-blue, :root[data-theme="dark"] .s12f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12f .kh-blue{ fill:#85B7EB; }
.s12f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12f-blue); }
.s12f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-blue); }
.s12f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s12f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s12f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s12f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s12f .kb-teal, :root[data-theme="dark"] .s12f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s12f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s12f .kh-teal{ fill:#5DCAA5; }
.s12f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s12f-teal); }
.s12f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-teal); }
.s12f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s12f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s12f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s12f .ks-amber{ fill:#854F0B; font-size:13px; }
.s12f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s12f .kb-amber, :root[data-theme="dark"] .s12f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s12f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s12f .kh-amber{ fill:#EF9F27; }
.s12f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s12f-amber); }
.s12f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-amber); }
.s12f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s12f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s12f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s12f .ks-purple{ fill:#534AB7; font-size:13px; }
.s12f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s12f .kb-purple, :root[data-theme="dark"] .s12f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s12f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s12f .kh-purple{ fill:#AFA9EC; }
.s12f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s12f-purple); }
.s12f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-purple); }
.s12f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s12f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s12f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s12f .ks-red{ fill:#A32D2D; font-size:13px; }
.s12f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s12f .kb-red, :root[data-theme="dark"] .s12f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s12f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s12f .kh-red{ fill:#F09595; }
.s12f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s12f-red); }
.s12f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-red); }
.s12f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s12f .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s12f .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s12f .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s12f .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s12f .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12f .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s12f .kb-gray, :root[data-theme="dark"] .s12f .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s12f .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s12f .kh-gray{ fill:#B4B2A9; }
.s12f .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s12f-gray); }
.s12f .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12f-gray); }
.s12f .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s12f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s12f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s12f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s12f-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s12f">
<rect x="20" y="140" width="130" height="50" rx="0" class="k-blue"/>
<text x="85.0" y="169.5" text-anchor="middle" class="kb-blue">administrator</text>
<circle cx="320" cy="165" r="60" class="k-teal"/>
<text x="320" y="162" text-anchor="middle" class="kb-teal">NetWarden</text>
<text x="320" y="180" text-anchor="middle" class="ks-teal">process</text>
<line x1="220" y1="20" x2="350" y2="20" class="ln-purple"/>
<line x1="220" y1="50" x2="350" y2="50" class="ln-purple"/>
<text x="285" y="40" text-anchor="middle" class="m">scope.txt</text>
<line x1="380" y1="20" x2="510" y2="20" class="ln-purple"/>
<line x1="380" y1="50" x2="510" y2="50" class="ln-purple"/>
<text x="445" y="40" text-anchor="middle" class="m">vulns.json</text>
<line x1="220" y1="290" x2="350" y2="290" class="ln-purple"/>
<line x1="220" y1="320" x2="350" y2="320" class="ln-purple"/>
<text x="285" y="310" text-anchor="middle" class="m">netwarden.db</text>
<line x1="380" y1="290" x2="510" y2="290" class="ln-purple"/>
<line x1="380" y1="320" x2="510" y2="320" class="ln-purple"/>
<text x="445" y="310" text-anchor="middle" class="m">reports</text>
<line x1="152" y1="165" x2="258" y2="165" class="ar"/>
<text x="205" y="156" text-anchor="middle" class="c">commands</text>
<line x1="285" y1="52" x2="300" y2="108" class="ar"/>
<line x1="445" y1="52" x2="345" y2="110" class="ar"/>
<line x1="300" y1="222" x2="285" y2="288" class="ar"/>
<line x1="345" y1="220" x2="445" y2="288" class="ar"/>
<rect x="500" y="60" width="200" height="210" rx="8" class="k-red" style="fill-opacity:0.25;stroke-dasharray:6 4"/>
<text x="600" y="82" text-anchor="middle" class="kh-red">untrusted: target network</text>
<rect x="540" y="140" width="120" height="50" rx="0" class="k-gray"/>
<text x="600.0" y="169.5" text-anchor="middle" class="kb-gray">target hosts</text>
<line x1="382" y1="158" x2="538" y2="158" class="ar"/>
<line x1="538" y1="174" x2="382" y2="174" class="ar-red"/>
<text x="460" y="150" text-anchor="middle" class="c">probes</text>
<text x="460" y="192" text-anchor="middle" class="kh-red">banners</text>
<rect x="138" y="18" width="44" height="22" rx="10" class="k-amber"/>
<text x="160.0" y="33.5" text-anchor="middle" class="kb-amber">T</text>
<rect x="238" y="126" width="44" height="22" rx="10" class="k-amber"/>
<text x="260.0" y="141.5" text-anchor="middle" class="kb-amber">S, E</text>
<rect x="128" y="298" width="44" height="22" rx="10" class="k-amber"/>
<text x="150.0" y="313.5" text-anchor="middle" class="kb-amber">I</text>
<rect x="518" y="298" width="44" height="22" rx="10" class="k-amber"/>
<text x="540.0" y="313.5" text-anchor="middle" class="kb-amber">I</text>
<rect x="578" y="248" width="44" height="22" rx="10" class="k-amber"/>
<text x="600.0" y="263.5" text-anchor="middle" class="kb-amber">D</text>
</g>
</svg>
<figcaption>Threat modelling asks, for each element and flow: how could this be spoofed, tampered with, repudiated, disclosed, denied or abused?</figcaption>
</figure>

| STRIDE | Property violated | NetWarden threat | Mitigation |
|---|---|---|---|
| **S**poofing | Authenticity | A host fakes a banner to hide or invent findings | Report evidence; document the limitation |
| **T**ampering | Integrity | The scope file is edited to add unauthorised networks | Keep it in version control and review changes |
| **R**epudiation | Non-repudiation | An operator denies running a scan | History records time and targets |
| **I**nformation disclosure | Confidentiality | Reports and the database reveal weaknesses | Restrict permissions; never commit them |
| **D**enial of service | Availability | A large scan disrupts fragile devices | Limits on hosts, concurrency and timeouts |
| **E**levation of privilege | Authorisation | Script in a banner runs in a browser viewing the report | HTML escaping, tested |

NetWarden's full threat model is `docs/threat-model.md`. The most interesting point is the **trust boundary**: everything that comes from the network is attacker-controlled. The banner a "web server" sends is data chosen by whoever runs that server, and the HTML report must treat it that way:

```python
def test_html_report_escapes_banners():
    result = ScanResult(["10.0.0.9"], findings=[Finding("10.0.0.9", 80, "X", "<script>alert(1)</script>",
                                                        Severity.LOW, "e", "r")])
    html = get_reporter("html").render(result)
    assert "<script>" not in html and "&lt;script&gt;" in html
```

### Secure coding

The **OWASP Top 10** lists the most critical web application security risks, and the **CWE Top 25** the most dangerous software weaknesses. Most share a few root causes, which give the core secure coding rules:

- **Treat all input as untrusted**: validate it (allowlists over blocklists) at trust boundaries; NetWarden validates targets with `ipaddress` and ports with `parse_ports`.
- **Encode output for its context**: HTML-escape for HTML, parameterise SQL. `store.py` uses `?` placeholders, never string formatting, so a finding title containing `'; DROP TABLE scans; --` is harmless.
- **Never build shell commands from input**; NetWarden calls no external programs at all.
- **Keep secrets out of code** and logs (Chapter 8).
- **Fail securely**: errors deny rather than allow; the scope check raises rather than skipping.
- **Least privilege**: no root needed for a connect scan; the container runs as an unprivileged user.

### The software supply chain

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The software supply chain. NetWarden&#x27;s runtime has no third-party dependencies, but its development tools do: pytest, ruff, mypy and pytest-cov, which pull in their own transitive dependencies, plus the Python base image and GitHub Actions. Defences: pin versions, scan with pip-audit, generate an SBOM, update with Dependabot, and review new dependencies." xmlns="http://www.w3.org/2000/svg">
<style>
.s12g{ font-family:var(--sans),sans-serif; }
.s12g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s12g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s12g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s12g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s12g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s12g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s12g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s12g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s12g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s12g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s12g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s12g .s{ fill:var(--text-dim); font-size:13px; }
.s12g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s12g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s12g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s12g .c{ fill:var(--text-faint); font-size:12.5px; }
.s12g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s12g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s12g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s12g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12g-a); }
.s12g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s12g-a); marker-start:url(#s12g-s); }
.s12g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s12g-g); }
.s12g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-a); }
.s12g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s12g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s12g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s12g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s12g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s12g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12g-tri); }
.s12g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-tri); }
.s12g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12g-open); }
.s12g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-open); }
.s12g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12g-dia); }
.s12g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12g-odia); }
.s12g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s12g-dia); marker-end:url(#s12g-open); }
.s12g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s12g-solid); }
.s12g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s12g-open); }
.s12g .fill{ fill:var(--text); stroke:none; }
.s12g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s12g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s12g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s12g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s12g .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s12g .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s12g .ks-blue{ fill:#185FA5; font-size:13px; }
.s12g .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s12g .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12g .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s12g .kb-blue, :root[data-theme="dark"] .s12g .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s12g .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s12g .kh-blue{ fill:#85B7EB; }
.s12g .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s12g-blue); }
.s12g .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-blue); }
.s12g .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s12g .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s12g .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s12g .ks-teal{ fill:#0F6E56; font-size:13px; }
.s12g .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s12g .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12g .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s12g .kb-teal, :root[data-theme="dark"] .s12g .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s12g .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s12g .kh-teal{ fill:#5DCAA5; }
.s12g .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s12g-teal); }
.s12g .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-teal); }
.s12g .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s12g .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s12g .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s12g .ks-green{ fill:#3B6D11; font-size:13px; }
.s12g .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s12g .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12g .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s12g .kb-green, :root[data-theme="dark"] .s12g .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s12g .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s12g .kh-green{ fill:#97C459; }
.s12g .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s12g-green); }
.s12g .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-green); }
.s12g .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s12g .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s12g .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s12g .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s12g .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s12g .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s12g .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s12g .kb-gray, :root[data-theme="dark"] .s12g .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s12g .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s12g .kh-gray{ fill:#B4B2A9; }
.s12g .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s12g-gray); }
.s12g .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s12g-gray); }
.s12g .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s12g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s12g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s12g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s12g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s12g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s12g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s12g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s12g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s12g-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s12g-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s12g-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s12g-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s12g">
<rect x="20" y="90" width="150" height="60" rx="7" class="k-teal"/>
<text x="95.0" y="115.5" text-anchor="middle" class="kb-teal">netwarden</text>
<text x="95.0" y="133.5" text-anchor="middle" class="ks-teal">runtime: stdlib only</text>
<rect x="240" y="20" width="120" height="36" rx="4" class="k-blue"/>
<text x="300.0" y="42.5" text-anchor="middle" class="km-blue">pytest</text>
<line x1="172" y1="120" x2="238" y2="38" class="dep"/>
<rect x="240" y="70" width="120" height="36" rx="4" class="k-blue"/>
<text x="300.0" y="92.5" text-anchor="middle" class="km-blue">ruff</text>
<line x1="172" y1="120" x2="238" y2="88" class="dep"/>
<rect x="240" y="120" width="120" height="36" rx="4" class="k-blue"/>
<text x="300.0" y="142.5" text-anchor="middle" class="km-blue">mypy</text>
<line x1="172" y1="120" x2="238" y2="138" class="dep"/>
<rect x="240" y="170" width="120" height="36" rx="4" class="k-blue"/>
<text x="300.0" y="192.5" text-anchor="middle" class="km-blue">pytest-cov</text>
<line x1="172" y1="120" x2="238" y2="188" class="dep"/>
<circle cx="420" cy="40" r="10" class="k-gray"/>
<circle cx="450" cy="40" r="10" class="k-gray"/>
<circle cx="480" cy="40" r="10" class="k-gray"/>
<circle cx="420" cy="180" r="10" class="k-gray"/>
<circle cx="450" cy="180" r="10" class="k-gray"/>
<circle cx="480" cy="180" r="10" class="k-gray"/>
<line x1="362" y1="38" x2="410" y2="40" class="ln"/>
<line x1="362" y1="88" x2="410" y2="40" class="ln"/>
<line x1="362" y1="138" x2="410" y2="180" class="ln"/>
<line x1="362" y1="188" x2="410" y2="180" class="ln"/>
<text x="450" y="110" text-anchor="middle" class="c">transitive</text>
<rect x="520" y="20" width="180" height="210" rx="7" class="k-green"/>
<text x="610.0" y="51.5" text-anchor="middle" class="kb-green">defences</text>
<text x="610.0" y="77.5" text-anchor="middle" class="ks-green">pin versions</text>
<text x="610.0" y="103.5" text-anchor="middle" class="ks-green">pip-audit: known CVEs</text>
<text x="610.0" y="129.5" text-anchor="middle" class="ks-green">SBOM (CycloneDX, SPDX)</text>
<text x="610.0" y="155.5" text-anchor="middle" class="ks-green">Dependabot updates</text>
<text x="610.0" y="181.5" text-anchor="middle" class="ks-green">review new deps</text>
<text x="610.0" y="207.5" text-anchor="middle" class="ks-green">base image updates</text>
</g>
</svg>
<figcaption>Most code you ship was written by someone else. Know what it is and keep it patched.</figcaption>
</figure>

Modern software is mostly other people's code. Attacks on the supply chain, such as malicious packages with names similar to popular ones, compromised maintainer accounts, or poisoned build systems, have grown sharply. Defences:

- Minimise dependencies; NetWarden's runtime has **none** (ADR-0001).
- **Pin versions** and update deliberately (Dependabot, Chapter 13).
- Scan for known vulnerabilities: `pip-audit` reports none for NetWarden's development dependencies.
- Generate a **software bill of materials** (SBOM) in the CycloneDX or SPDX format, so users know what is inside.
- Protect the build: the **SLSA** framework describes levels of build integrity, from a scripted build to signed, verifiable provenance.

### Responsible disclosure

A security tool's project should say how to report vulnerabilities in it. A `SECURITY.md` file gives a private contact, the supported versions, and a disclosure timeline. Users who find a vulnerability in someone else's product should report it privately to the vendor and allow time for a fix before publishing, following coordinated vulnerability disclosure practice.

## Hands on

1. Add `test_html_report_escapes_banners` (above) to `tests/test_units.py` and run it.
2. Run `ruff check --select S src` and read each rule's documentation. Why are there no findings?
3. Run `pip-audit` in your virtual environment.
4. Extend the threat model: what new threats appear if NetWarden gets a web dashboard? Use STRIDE on the new data flows.

## Summary

- **QA** prevents defects through process; **QC** detects them in products; testing is one QC activity.
- **Reviews and inspections** find defects early, including kinds tests miss; use **checklists**.
- **Static analysis** (lint, types, security rules) runs on every commit.
- Choose **metrics** with **goal, question, metric**, and beware Goodhart's law.
- Every defect fix gets a **regression test**; significant defects get **root cause analysis**.
- Build security into every phase: **abuse cases**, **threat modelling** with **STRIDE**, **secure coding**, dependency scanning and **SBOMs**.
- Everything from the network, or from any user, is **untrusted** until validated or encoded.
