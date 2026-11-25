# Chapter 17: Teams, Ethics and AI-Assisted Development

Software is built by people, for people, and increasingly with the help of AI tools. This last chapter looks at the human side of software engineering: how teams work, the professional and ethical responsibilities of engineers, especially those who build security tools, and how to use AI coding assistants without giving up the discipline the rest of the book has described.

## Teams

### How teams form

<figure class="diagram">
<svg viewBox="0 0 720 240" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Tuckman&#x27;s stages of team development: forming, polite and uncertain; storming, conflict over roles and approaches; norming, agreed ways of working; performing, effective and self-directed; and adjourning, when the team disbands. Team performance dips during storming and rises through norming and performing." xmlns="http://www.w3.org/2000/svg">
<style>
.s17a{ font-family:var(--sans),sans-serif; }
.s17a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s17a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s17a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s17a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s17a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s17a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s17a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s17a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s17a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s17a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s17a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s17a .s{ fill:var(--text-dim); font-size:13px; }
.s17a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s17a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .c{ fill:var(--text-faint); font-size:12.5px; }
.s17a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s17a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s17a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s17a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17a-a); }
.s17a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17a-a); marker-start:url(#s17a-s); }
.s17a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s17a-g); }
.s17a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-a); }
.s17a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s17a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s17a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s17a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s17a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s17a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17a-tri); }
.s17a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-tri); }
.s17a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17a-open); }
.s17a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-open); }
.s17a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17a-dia); }
.s17a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17a-odia); }
.s17a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17a-dia); marker-end:url(#s17a-open); }
.s17a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17a-solid); }
.s17a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s17a-open); }
.s17a .fill{ fill:var(--text); stroke:none; }
.s17a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s17a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s17a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s17a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s17a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s17a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s17a .ks-blue{ fill:#185FA5; font-size:13px; }
.s17a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s17a .kb-blue, :root[data-theme="dark"] .s17a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s17a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s17a .kh-blue{ fill:#85B7EB; }
.s17a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s17a-blue); }
.s17a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-blue); }
.s17a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s17a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s17a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s17a .ks-amber{ fill:#854F0B; font-size:13px; }
.s17a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s17a .kb-amber, :root[data-theme="dark"] .s17a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s17a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s17a .kh-amber{ fill:#EF9F27; }
.s17a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s17a-amber); }
.s17a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-amber); }
.s17a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s17a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s17a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s17a .ks-purple{ fill:#534AB7; font-size:13px; }
.s17a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s17a .kb-purple, :root[data-theme="dark"] .s17a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s17a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s17a .kh-purple{ fill:#AFA9EC; }
.s17a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s17a-purple); }
.s17a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-purple); }
.s17a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s17a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s17a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s17a .ks-green{ fill:#3B6D11; font-size:13px; }
.s17a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s17a .kb-green, :root[data-theme="dark"] .s17a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s17a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s17a .kh-green{ fill:#97C459; }
.s17a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s17a-green); }
.s17a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-green); }
.s17a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s17a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s17a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s17a .ks-red{ fill:#A32D2D; font-size:13px; }
.s17a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s17a .kb-red, :root[data-theme="dark"] .s17a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s17a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s17a .kh-red{ fill:#F09595; }
.s17a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s17a-red); }
.s17a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-red); }
.s17a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s17a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s17a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s17a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s17a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s17a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s17a .kb-gray, :root[data-theme="dark"] .s17a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s17a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s17a .kh-gray{ fill:#B4B2A9; }
.s17a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s17a-gray); }
.s17a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17a-gray); }
.s17a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s17a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s17a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s17a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s17a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s17a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s17a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s17a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s17a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s17a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s17a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s17a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s17a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s17a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s17a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s17a">
<rect x="20" y="130" width="124" height="56" rx="7" class="k-blue"/>
<text x="82.0" y="153.5" text-anchor="middle" class="kb-blue">forming</text>
<text x="82.0" y="171.5" text-anchor="middle" class="ks-blue">polite, unsure</text>
<rect x="160" y="130" width="124" height="56" rx="7" class="k-red"/>
<text x="222.0" y="153.5" text-anchor="middle" class="kb-red">storming</text>
<text x="222.0" y="171.5" text-anchor="middle" class="ks-red">conflict</text>
<rect x="300" y="130" width="124" height="56" rx="7" class="k-amber"/>
<text x="362.0" y="153.5" text-anchor="middle" class="kb-amber">norming</text>
<text x="362.0" y="171.5" text-anchor="middle" class="ks-amber">agreements</text>
<rect x="440" y="130" width="124" height="56" rx="7" class="k-green"/>
<text x="502.0" y="153.5" text-anchor="middle" class="kb-green">performing</text>
<text x="502.0" y="171.5" text-anchor="middle" class="ks-green">flow</text>
<rect x="580" y="130" width="124" height="56" rx="7" class="k-gray"/>
<text x="642.0" y="153.5" text-anchor="middle" class="kb-gray">adjourning</text>
<text x="642.0" y="171.5" text-anchor="middle" class="ks-gray">wrap up</text>
<path d="M82 110 C 150 110, 180 124, 222 120 C 280 112, 330 80, 362 70 C 420 50, 470 40, 502 38 C 560 36, 600 60, 642 90" class="ln-purple"/>
<text x="30" y="30" text-anchor="start" class="kh-purple">performance</text>
<text x="360" y="224" text-anchor="middle" class="c">Bruce Tuckman, 1965; adjourning added in 1977</text>
</g>
</svg>
<figcaption>Storming is normal. Retrospectives and explicit working agreements help a team move through it.</figcaption>
</figure>

Bruce Tuckman's model describes stages most teams pass through. **Storming**, the phase of disagreement about roles and approaches, is uncomfortable but normal; teams that suppress it never reach real agreement. Explicit **working agreements** ("pull requests reviewed within one working day", "core hours 10:00 to 15:00", "we disagree in the meeting, not afterwards") speed the move to norming.

### What makes teams effective

Google's Project Aristotle, a study of 180 of its teams published in 2015, found that **psychological safety**, the shared belief that it is safe to take interpersonal risks such as admitting a mistake or asking a naive question, mattered more than any other factor it measured. Dependability, clear structure and goals, meaning, and impact followed. The same theme appears in the blameless postmortems of Chapter 14 and in effective code review (Chapter 8): teams that are afraid hide problems; teams that feel safe surface them early, when they are cheap to fix.

### Team size and communication

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Communication paths grow with the square of team size: n times n minus one over two. Three people have 3 paths, five have 10, and ten have 45. This is one reason behind Brooks&#x27;s law, that adding people to a late project makes it later." xmlns="http://www.w3.org/2000/svg">
<style>
.s17b{ font-family:var(--sans),sans-serif; }
.s17b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s17b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s17b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s17b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s17b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s17b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s17b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s17b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s17b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s17b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s17b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s17b .s{ fill:var(--text-dim); font-size:13px; }
.s17b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s17b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s17b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s17b .c{ fill:var(--text-faint); font-size:12.5px; }
.s17b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s17b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s17b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s17b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17b-a); }
.s17b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17b-a); marker-start:url(#s17b-s); }
.s17b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s17b-g); }
.s17b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s17b-a); }
.s17b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s17b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s17b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s17b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s17b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s17b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17b-tri); }
.s17b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17b-tri); }
.s17b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17b-open); }
.s17b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17b-open); }
.s17b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17b-dia); }
.s17b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17b-odia); }
.s17b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17b-dia); marker-end:url(#s17b-open); }
.s17b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17b-solid); }
.s17b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s17b-open); }
.s17b .fill{ fill:var(--text); stroke:none; }
.s17b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s17b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s17b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s17b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s17b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s17b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s17b .ks-blue{ fill:#185FA5; font-size:13px; }
.s17b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s17b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s17b .kb-blue, :root[data-theme="dark"] .s17b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s17b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s17b .kh-blue{ fill:#85B7EB; }
.s17b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s17b-blue); }
.s17b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17b-blue); }
.s17b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s17b .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s17b .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s17b .ks-coral{ fill:#993C1D; font-size:13px; }
.s17b .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s17b .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17b .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s17b .kb-coral, :root[data-theme="dark"] .s17b .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s17b .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s17b .kh-coral{ fill:#F0997B; }
.s17b .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s17b-coral); }
.s17b .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17b-coral); }
.s17b .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s17b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s17b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s17b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s17b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s17b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s17b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s17b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s17b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s17b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s17b-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s17b">
<line x1="110" y1="40" x2="171" y2="145" class="ln-coral"/>
<line x1="110" y1="40" x2="49" y2="145" class="ln-coral"/>
<line x1="171" y1="145" x2="49" y2="145" class="ln-coral"/>
<circle cx="110" cy="40" r="9" class="k-blue"/>
<circle cx="171" cy="145" r="9" class="k-blue"/>
<circle cx="49" cy="145" r="9" class="k-blue"/>
<text x="110" y="214" text-anchor="middle" class="kh-coral">3 people: 3 paths</text>
<line x1="360" y1="40" x2="427" y2="88" class="ln-coral"/>
<line x1="360" y1="40" x2="401" y2="167" class="ln-coral"/>
<line x1="360" y1="40" x2="319" y2="167" class="ln-coral"/>
<line x1="360" y1="40" x2="293" y2="88" class="ln-coral"/>
<line x1="427" y1="88" x2="401" y2="167" class="ln-coral"/>
<line x1="427" y1="88" x2="319" y2="167" class="ln-coral"/>
<line x1="427" y1="88" x2="293" y2="88" class="ln-coral"/>
<line x1="401" y1="167" x2="319" y2="167" class="ln-coral"/>
<line x1="401" y1="167" x2="293" y2="88" class="ln-coral"/>
<line x1="319" y1="167" x2="293" y2="88" class="ln-coral"/>
<circle cx="360" cy="40" r="9" class="k-blue"/>
<circle cx="427" cy="88" r="9" class="k-blue"/>
<circle cx="401" cy="167" r="9" class="k-blue"/>
<circle cx="319" cy="167" r="9" class="k-blue"/>
<circle cx="293" cy="88" r="9" class="k-blue"/>
<text x="360" y="214" text-anchor="middle" class="kh-coral">5 people: 10 paths</text>
<line x1="610" y1="40" x2="651" y2="53" class="ln-coral"/>
<line x1="610" y1="40" x2="677" y2="88" class="ln-coral"/>
<line x1="610" y1="40" x2="677" y2="132" class="ln-coral"/>
<line x1="610" y1="40" x2="651" y2="167" class="ln-coral"/>
<line x1="610" y1="40" x2="610" y2="180" class="ln-coral"/>
<line x1="610" y1="40" x2="569" y2="167" class="ln-coral"/>
<line x1="610" y1="40" x2="543" y2="132" class="ln-coral"/>
<line x1="610" y1="40" x2="543" y2="88" class="ln-coral"/>
<line x1="610" y1="40" x2="569" y2="53" class="ln-coral"/>
<line x1="651" y1="53" x2="677" y2="88" class="ln-coral"/>
<line x1="651" y1="53" x2="677" y2="132" class="ln-coral"/>
<line x1="651" y1="53" x2="651" y2="167" class="ln-coral"/>
<line x1="651" y1="53" x2="610" y2="180" class="ln-coral"/>
<line x1="651" y1="53" x2="569" y2="167" class="ln-coral"/>
<line x1="651" y1="53" x2="543" y2="132" class="ln-coral"/>
<line x1="651" y1="53" x2="543" y2="88" class="ln-coral"/>
<line x1="651" y1="53" x2="569" y2="53" class="ln-coral"/>
<line x1="677" y1="88" x2="677" y2="132" class="ln-coral"/>
<line x1="677" y1="88" x2="651" y2="167" class="ln-coral"/>
<line x1="677" y1="88" x2="610" y2="180" class="ln-coral"/>
<line x1="677" y1="88" x2="569" y2="167" class="ln-coral"/>
<line x1="677" y1="88" x2="543" y2="132" class="ln-coral"/>
<line x1="677" y1="88" x2="543" y2="88" class="ln-coral"/>
<line x1="677" y1="88" x2="569" y2="53" class="ln-coral"/>
<line x1="677" y1="132" x2="651" y2="167" class="ln-coral"/>
<line x1="677" y1="132" x2="610" y2="180" class="ln-coral"/>
<line x1="677" y1="132" x2="569" y2="167" class="ln-coral"/>
<line x1="677" y1="132" x2="543" y2="132" class="ln-coral"/>
<line x1="677" y1="132" x2="543" y2="88" class="ln-coral"/>
<line x1="677" y1="132" x2="569" y2="53" class="ln-coral"/>
<line x1="651" y1="167" x2="610" y2="180" class="ln-coral"/>
<line x1="651" y1="167" x2="569" y2="167" class="ln-coral"/>
<line x1="651" y1="167" x2="543" y2="132" class="ln-coral"/>
<line x1="651" y1="167" x2="543" y2="88" class="ln-coral"/>
<line x1="651" y1="167" x2="569" y2="53" class="ln-coral"/>
<line x1="610" y1="180" x2="569" y2="167" class="ln-coral"/>
<line x1="610" y1="180" x2="543" y2="132" class="ln-coral"/>
<line x1="610" y1="180" x2="543" y2="88" class="ln-coral"/>
<line x1="610" y1="180" x2="569" y2="53" class="ln-coral"/>
<line x1="569" y1="167" x2="543" y2="132" class="ln-coral"/>
<line x1="569" y1="167" x2="543" y2="88" class="ln-coral"/>
<line x1="569" y1="167" x2="569" y2="53" class="ln-coral"/>
<line x1="543" y1="132" x2="543" y2="88" class="ln-coral"/>
<line x1="543" y1="132" x2="569" y2="53" class="ln-coral"/>
<line x1="543" y1="88" x2="569" y2="53" class="ln-coral"/>
<circle cx="610" cy="40" r="9" class="k-blue"/>
<circle cx="651" cy="53" r="9" class="k-blue"/>
<circle cx="677" cy="88" r="9" class="k-blue"/>
<circle cx="677" cy="132" r="9" class="k-blue"/>
<circle cx="651" cy="167" r="9" class="k-blue"/>
<circle cx="610" cy="180" r="9" class="k-blue"/>
<circle cx="569" cy="167" r="9" class="k-blue"/>
<circle cx="543" cy="132" r="9" class="k-blue"/>
<circle cx="543" cy="88" r="9" class="k-blue"/>
<circle cx="569" cy="53" r="9" class="k-blue"/>
<text x="610" y="214" text-anchor="middle" class="kh-coral">10 people: 45 paths</text>
</g>
</svg>
<figcaption>Small teams communicate cheaply. Large efforts split into small, loosely coupled teams, which is Conway's law in reverse.</figcaption>
</figure>

Communication overhead grows quickly with team size. Amazon's "two-pizza team" guideline, Scrum's recommendation of ten or fewer people, and Brooks's law (Chapter 1) all point the same way: keep teams small, and split large efforts into several small teams with clear interfaces.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Conway&#x27;s law: organisations design systems that mirror their communication structure. Three separate teams for scanning, analysis and reporting tend to produce three components with interfaces where the teams meet. The inverse Conway manoeuvre shapes teams to match the architecture you want." xmlns="http://www.w3.org/2000/svg">
<style>
.s17c{ font-family:var(--sans),sans-serif; }
.s17c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s17c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s17c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s17c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s17c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s17c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s17c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s17c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s17c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s17c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s17c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s17c .s{ fill:var(--text-dim); font-size:13px; }
.s17c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s17c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s17c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s17c .c{ fill:var(--text-faint); font-size:12.5px; }
.s17c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s17c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s17c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s17c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17c-a); }
.s17c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17c-a); marker-start:url(#s17c-s); }
.s17c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s17c-g); }
.s17c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s17c-a); }
.s17c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s17c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s17c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s17c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s17c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s17c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17c-tri); }
.s17c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17c-tri); }
.s17c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17c-open); }
.s17c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17c-open); }
.s17c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17c-dia); }
.s17c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17c-odia); }
.s17c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17c-dia); marker-end:url(#s17c-open); }
.s17c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17c-solid); }
.s17c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s17c-open); }
.s17c .fill{ fill:var(--text); stroke:none; }
.s17c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s17c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s17c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s17c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s17c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s17c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s17c .ks-blue{ fill:#185FA5; font-size:13px; }
.s17c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s17c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s17c .kb-blue, :root[data-theme="dark"] .s17c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s17c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s17c .kh-blue{ fill:#85B7EB; }
.s17c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s17c-blue); }
.s17c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17c-blue); }
.s17c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s17c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s17c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s17c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s17c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s17c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s17c .kb-teal, :root[data-theme="dark"] .s17c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s17c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s17c .kh-teal{ fill:#5DCAA5; }
.s17c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s17c-teal); }
.s17c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17c-teal); }
.s17c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
</style>
<defs><marker id="s17c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s17c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s17c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s17c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s17c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s17c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s17c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s17c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s17c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s17c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker></defs>
<g class="s17c">
<text x="180" y="20" text-anchor="middle" class="kh-blue">organisation</text>
<rect x="20" y="40" width="100" height="44" rx="4" class="k-blue"/>
<text x="70.0" y="66.5" text-anchor="middle" class="ks-blue">scan team</text>
<rect x="130" y="40" width="100" height="44" rx="4" class="k-blue"/>
<text x="180.0" y="66.5" text-anchor="middle" class="ks-blue">analysis team</text>
<line x1="120" y1="62" x2="128" y2="62" class="ar2"/>
<rect x="240" y="40" width="100" height="44" rx="4" class="k-blue"/>
<text x="290.0" y="66.5" text-anchor="middle" class="ks-blue">report team</text>
<line x1="230" y1="62" x2="238" y2="62" class="ar2"/>
<text x="540" y="20" text-anchor="middle" class="kh-teal">system</text>
<rect x="380" y="40" width="100" height="44" rx="4" class="k-teal"/>
<text x="430.0" y="66.5" text-anchor="middle" class="ks-teal">scanner</text>
<rect x="490" y="40" width="100" height="44" rx="4" class="k-teal"/>
<text x="540.0" y="66.5" text-anchor="middle" class="ks-teal">checks</text>
<line x1="480" y1="62" x2="488" y2="62" class="ar2"/>
<rect x="600" y="40" width="100" height="44" rx="4" class="k-teal"/>
<text x="650.0" y="66.5" text-anchor="middle" class="ks-teal">report</text>
<line x1="590" y1="62" x2="598" y2="62" class="ar2"/>
<path d="M350 62 L370 62" class="ar"/>
<text x="360" y="140" text-anchor="middle" class="c">"any organization that designs a system will produce a design whose structure</text>
<text x="360" y="160" text-anchor="middle" class="c">is a copy of the organization's communication structure" (Melvin Conway, 1968)</text>
<text x="360" y="210" text-anchor="middle" class="kh-teal">inverse Conway manoeuvre: shape the teams to get the architecture you want</text>
</g>
</svg>
<figcaption>Architecture and organisation are two views of the same decisions.</figcaption>
</figure>

**Conway's law** connects team structure and software structure. If the organisation has separate teams for scanning, analysis and reporting, the system will have interfaces where those teams meet, whether or not that is the best design. Modern organisations use this deliberately: they shape **stream-aligned teams** around the architecture they want (the "inverse Conway manoeuvre"), a central idea of the *Team Topologies* approach.

### Roles

| Role | Focus | In NetWarden's team |
|---|---|---|
| Product owner or manager | What to build and why; value | Security team lead |
| Developers | Building, testing, operating | Three students |
| Scrum master or delivery lead | How the team works; removing obstacles | A senior developer, part-time |
| Architect | Cross-cutting design decisions | Shared; ADRs reviewed by all |
| Tester or QA engineer | Test strategy, exploratory testing | Shared; every developer writes tests |
| Site reliability or operations engineer | Running the system | The developers themselves (DevOps) |
| Security champion | Security practices in the team | One developer, trained in threat modelling |
| UX designer | Usability of interfaces and reports | Consulted for the HTML report |

In small teams, people hold several roles. What matters is that each responsibility has an owner.

### Distributed and hybrid teams

Many teams now work across locations and time zones. What works: written communication by default (design documents, ADRs, pull request descriptions), a small set of overlapping core hours, recorded demos, and tooling that makes work visible (boards, CI status). Much of the practice in this book, small changes, automated checks, documentation in the repository, also makes distributed work easier.

## Professional ethics

Software engineers make decisions that affect people who never see the code. The **ACM/IEEE-CS Software Engineering Code of Ethics and Professional Practice** (1999) sets out eight principles.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The eight principles of the ACM and IEEE Computer Society Software Engineering Code of Ethics: public, act consistently with the public interest; client and employer; product, meet the highest professional standards; judgment, maintain integrity and independence; management, promote an ethical approach; profession, advance its integrity and reputation; colleagues, be fair and supportive; self, keep learning." xmlns="http://www.w3.org/2000/svg">
<style>
.s17d{ font-family:var(--sans),sans-serif; }
.s17d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s17d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s17d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s17d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s17d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s17d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s17d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s17d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s17d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s17d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s17d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s17d .s{ fill:var(--text-dim); font-size:13px; }
.s17d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s17d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .c{ fill:var(--text-faint); font-size:12.5px; }
.s17d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s17d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s17d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s17d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17d-a); }
.s17d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17d-a); marker-start:url(#s17d-s); }
.s17d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s17d-g); }
.s17d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-a); }
.s17d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s17d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s17d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s17d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s17d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s17d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17d-tri); }
.s17d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-tri); }
.s17d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17d-open); }
.s17d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-open); }
.s17d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17d-dia); }
.s17d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17d-odia); }
.s17d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17d-dia); marker-end:url(#s17d-open); }
.s17d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17d-solid); }
.s17d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s17d-open); }
.s17d .fill{ fill:var(--text); stroke:none; }
.s17d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s17d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s17d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s17d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s17d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s17d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s17d .ks-blue{ fill:#185FA5; font-size:13px; }
.s17d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s17d .kb-blue, :root[data-theme="dark"] .s17d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s17d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s17d .kh-blue{ fill:#85B7EB; }
.s17d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s17d-blue); }
.s17d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-blue); }
.s17d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s17d .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s17d .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s17d .ks-teal{ fill:#0F6E56; font-size:13px; }
.s17d .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s17d .kb-teal, :root[data-theme="dark"] .s17d .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s17d .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s17d .kh-teal{ fill:#5DCAA5; }
.s17d .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s17d-teal); }
.s17d .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-teal); }
.s17d .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s17d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s17d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s17d .ks-amber{ fill:#854F0B; font-size:13px; }
.s17d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s17d .kb-amber, :root[data-theme="dark"] .s17d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s17d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s17d .kh-amber{ fill:#EF9F27; }
.s17d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s17d-amber); }
.s17d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-amber); }
.s17d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s17d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s17d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s17d .ks-purple{ fill:#534AB7; font-size:13px; }
.s17d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s17d .kb-purple, :root[data-theme="dark"] .s17d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s17d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s17d .kh-purple{ fill:#AFA9EC; }
.s17d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s17d-purple); }
.s17d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-purple); }
.s17d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s17d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s17d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s17d .ks-green{ fill:#3B6D11; font-size:13px; }
.s17d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s17d .kb-green, :root[data-theme="dark"] .s17d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s17d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s17d .kh-green{ fill:#97C459; }
.s17d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s17d-green); }
.s17d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-green); }
.s17d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s17d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s17d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s17d .ks-red{ fill:#A32D2D; font-size:13px; }
.s17d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s17d .kb-red, :root[data-theme="dark"] .s17d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s17d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s17d .kh-red{ fill:#F09595; }
.s17d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s17d-red); }
.s17d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-red); }
.s17d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s17d .k-pink{ fill:#FBEAF0; stroke:#D4537E; stroke-width:1.6; }
.s17d .kb-pink{ fill:#72243E; font-size:13px; font-weight:700; }
.s17d .ks-pink{ fill:#993556; font-size:13px; }
.s17d .km-pink{ fill:#72243E; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-pink{ fill:#993556; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-pink{ fill:#72243E; stroke:#ED93B1; }
:root[data-theme="dark"] .s17d .kb-pink, :root[data-theme="dark"] .s17d .km-pink{ fill:#FBEAF0; }
:root[data-theme="dark"] .s17d .ks-pink{ fill:#F4C0D1; }
:root[data-theme="dark"] .s17d .kh-pink{ fill:#ED93B1; }
.s17d .ar-pink{ stroke:#D4537E; stroke-width:2; fill:none; marker-end:url(#s17d-pink); }
.s17d .ad-pink{ stroke:#D4537E; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-pink); }
.s17d .ln-pink{ stroke:#D4537E; stroke-width:2; fill:none; }
.s17d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s17d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s17d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s17d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s17d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s17d .kb-gray, :root[data-theme="dark"] .s17d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s17d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s17d .kh-gray{ fill:#B4B2A9; }
.s17d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s17d-gray); }
.s17d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17d-gray); }
.s17d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s17d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s17d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s17d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s17d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s17d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s17d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s17d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s17d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s17d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s17d-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s17d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s17d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s17d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s17d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s17d-pink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D4537E"/></marker><marker id="s17d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s17d">
<rect x="20" y="20" width="162" height="100" rx="7" class="k-red"/>
<text x="101.0" y="65.5" text-anchor="middle" class="kb-red">1 public</text>
<text x="101.0" y="83.5" text-anchor="middle" class="ks-red">public interest first</text>
<rect x="192" y="20" width="162" height="100" rx="7" class="k-amber"/>
<text x="273.0" y="65.5" text-anchor="middle" class="kb-amber">2 client, employer</text>
<text x="273.0" y="83.5" text-anchor="middle" class="ks-amber">consistent with public</text>
<rect x="364" y="20" width="162" height="100" rx="7" class="k-blue"/>
<text x="445.0" y="65.5" text-anchor="middle" class="kb-blue">3 product</text>
<text x="445.0" y="83.5" text-anchor="middle" class="ks-blue">professional standards</text>
<rect x="536" y="20" width="162" height="100" rx="7" class="k-purple"/>
<text x="617.0" y="65.5" text-anchor="middle" class="kb-purple">4 judgment</text>
<text x="617.0" y="83.5" text-anchor="middle" class="ks-purple">integrity, independence</text>
<rect x="20" y="140" width="162" height="100" rx="7" class="k-teal"/>
<text x="101.0" y="185.5" text-anchor="middle" class="kb-teal">5 management</text>
<text x="101.0" y="203.5" text-anchor="middle" class="ks-teal">ethical management</text>
<rect x="192" y="140" width="162" height="100" rx="7" class="k-green"/>
<text x="273.0" y="185.5" text-anchor="middle" class="kb-green">6 profession</text>
<text x="273.0" y="203.5" text-anchor="middle" class="ks-green">integrity, reputation</text>
<rect x="364" y="140" width="162" height="100" rx="7" class="k-pink"/>
<text x="445.0" y="185.5" text-anchor="middle" class="kb-pink">7 colleagues</text>
<text x="445.0" y="203.5" text-anchor="middle" class="ks-pink">fair and supportive</text>
<rect x="536" y="140" width="162" height="100" rx="7" class="k-gray"/>
<text x="617.0" y="185.5" text-anchor="middle" class="kb-gray">8 self</text>
<text x="617.0" y="203.5" text-anchor="middle" class="ks-gray">lifelong learning</text>
</g>
</svg>
<figcaption>Principle 1 comes first for a reason: when interests conflict, the public interest wins.</figcaption>
</figure>

Typical ethical questions in software work include:

- Shipping with a known defect that could harm users, under deadline pressure.
- Collecting more personal data than a feature needs.
- Building systems whose outputs are unfair to groups of people, for example through biased training data.
- Misrepresenting the state of a project or the results of tests to a client or manager.
- Being asked to build features intended to deceive users or evade regulation.

The code gives a clear priority: the public interest comes first, then the client and employer. In Canada, engineering is a regulated profession, and the title "engineer" carries legal duties in provinces that license software engineers; similar arrangements exist elsewhere.

### Privacy and data protection

NetWarden's results are personal data in some jurisdictions (IP addresses can identify people) and sensitive security data everywhere. Laws such as Canada's **PIPEDA**, the EU's **GDPR** and many others require a lawful purpose for collecting data, collecting no more than necessary (**data minimisation**), protecting it, and keeping it no longer than needed. Privacy, like security, is best designed in: **privacy by design**.

### Building security tools responsibly

Security tools are **dual-use**: the same scanner that helps a defender find weaknesses could help an attacker. NetWarden's design reflects that responsibility:

- It refuses targets outside an explicit scope (NW-SR-1) and refuses huge ranges (NW-SR-2).
- It never exploits, logs in to, or changes a target (NW-SR-3).
- Its practice targets are fake services on the user's own machine.
- Its documentation repeats that scanning requires authorisation.

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Rules of engagement before any security assessment: written authorisation from the asset owner; an agreed scope of addresses and services, and what is excluded; a time window; emergency contacts on both sides; data handling rules for results; and a stop condition. NetWarden&#x27;s scope file encodes the second item; the other items are human agreements." xmlns="http://www.w3.org/2000/svg">
<style>
.s17e{ font-family:var(--sans),sans-serif; }
.s17e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s17e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s17e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s17e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s17e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s17e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s17e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s17e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s17e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s17e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s17e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s17e .s{ fill:var(--text-dim); font-size:13px; }
.s17e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s17e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .c{ fill:var(--text-faint); font-size:12.5px; }
.s17e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s17e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s17e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s17e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17e-a); }
.s17e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17e-a); marker-start:url(#s17e-s); }
.s17e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s17e-g); }
.s17e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-a); }
.s17e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s17e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s17e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s17e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s17e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s17e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17e-tri); }
.s17e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-tri); }
.s17e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17e-open); }
.s17e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-open); }
.s17e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17e-dia); }
.s17e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17e-odia); }
.s17e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17e-dia); marker-end:url(#s17e-open); }
.s17e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17e-solid); }
.s17e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s17e-open); }
.s17e .fill{ fill:var(--text); stroke:none; }
.s17e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s17e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s17e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s17e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s17e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s17e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s17e .ks-blue{ fill:#185FA5; font-size:13px; }
.s17e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s17e .kb-blue, :root[data-theme="dark"] .s17e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s17e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s17e .kh-blue{ fill:#85B7EB; }
.s17e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s17e-blue); }
.s17e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-blue); }
.s17e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s17e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s17e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s17e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s17e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s17e .kb-teal, :root[data-theme="dark"] .s17e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s17e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s17e .kh-teal{ fill:#5DCAA5; }
.s17e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s17e-teal); }
.s17e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-teal); }
.s17e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s17e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s17e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s17e .ks-amber{ fill:#854F0B; font-size:13px; }
.s17e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s17e .kb-amber, :root[data-theme="dark"] .s17e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s17e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s17e .kh-amber{ fill:#EF9F27; }
.s17e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s17e-amber); }
.s17e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-amber); }
.s17e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s17e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s17e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s17e .ks-purple{ fill:#534AB7; font-size:13px; }
.s17e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s17e .kb-purple, :root[data-theme="dark"] .s17e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s17e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s17e .kh-purple{ fill:#AFA9EC; }
.s17e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s17e-purple); }
.s17e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-purple); }
.s17e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s17e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s17e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s17e .ks-red{ fill:#A32D2D; font-size:13px; }
.s17e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s17e .kb-red, :root[data-theme="dark"] .s17e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s17e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s17e .kh-red{ fill:#F09595; }
.s17e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s17e-red); }
.s17e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-red); }
.s17e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s17e .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s17e .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s17e .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s17e .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s17e .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17e .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s17e .kb-gray, :root[data-theme="dark"] .s17e .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s17e .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s17e .kh-gray{ fill:#B4B2A9; }
.s17e .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s17e-gray); }
.s17e .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17e-gray); }
.s17e .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s17e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s17e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s17e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s17e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s17e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s17e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s17e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s17e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s17e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s17e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s17e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s17e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s17e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s17e-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s17e">
<rect x="20" y="20" width="218" height="88" rx="7" class="k-red"/>
<text x="129.0" y="59.5" text-anchor="middle" class="kb-red">written authorisation</text>
<text x="129.0" y="77.5" text-anchor="middle" class="ks-red">from the owner, signed</text>
<rect x="250" y="20" width="218" height="88" rx="7" class="k-teal"/>
<text x="359.0" y="59.5" text-anchor="middle" class="kb-teal">scope</text>
<text x="359.0" y="77.5" text-anchor="middle" class="ks-teal">networks in, exclusions out</text>
<rect x="480" y="20" width="218" height="88" rx="7" class="k-blue"/>
<text x="589.0" y="59.5" text-anchor="middle" class="kb-blue">time window</text>
<text x="589.0" y="77.5" text-anchor="middle" class="ks-blue">when scans may run</text>
<rect x="20" y="124" width="218" height="88" rx="7" class="k-purple"/>
<text x="129.0" y="163.5" text-anchor="middle" class="kb-purple">contacts</text>
<text x="129.0" y="181.5" text-anchor="middle" class="ks-purple">who to call if something breaks</text>
<rect x="250" y="124" width="218" height="88" rx="7" class="k-amber"/>
<text x="359.0" y="163.5" text-anchor="middle" class="kb-amber">data handling</text>
<text x="359.0" y="181.5" text-anchor="middle" class="ks-amber">where results live, who sees them</text>
<rect x="480" y="124" width="218" height="88" rx="7" class="k-gray"/>
<text x="589.0" y="163.5" text-anchor="middle" class="kb-gray">stop condition</text>
<text x="589.0" y="181.5" text-anchor="middle" class="ks-gray">when to halt immediately</text>
<text x="360" y="262" text-anchor="middle" class="c">NetWarden enforces only the scope; the rest must be agreed by people, before the first packet</text>
</g>
</svg>
<figcaption>Unauthorised scanning can be a crime, for example under section 342.1 of Canada's Criminal Code. Authorisation comes first.</figcaption>
</figure>

Scanning or probing systems without permission can be a criminal offence. In Canada, unauthorised use of a computer is an offence under section 342.1 of the Criminal Code; the United States has the Computer Fraud and Abuse Act and the United Kingdom the Computer Misuse Act, and most countries have equivalents. Professional penetration testers and security assessors therefore agree **rules of engagement** in writing before any testing begins. A tool can enforce a scope; only people can grant authorisation.

### Open source and licences

NetWarden is released under the **MIT licence**, which allows anyone to use, modify and redistribute it with attribution. **Copyleft** licences such as the GPL require derived works to be released under the same licence. Before adding a dependency or copying code, check that its licence is compatible with yours; tools that generate an SBOM (Chapter 12) can also list licences.

## AI-assisted development

Since about 2021, AI coding assistants have become common tools: completing lines and functions in the editor, answering questions in chat, explaining unfamiliar code, writing tests, and increasingly acting as **agents** that edit files, run commands and propose whole pull requests. Used well, they speed up routine work and help with unfamiliar libraries. Used carelessly, they produce plausible-looking code that is wrong.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Working with an AI coding assistant. The developer gives context and intent; the assistant proposes code, tests or explanations; the developer reviews, runs the tests and static analysis, and decides. Risks along the way: invented APIs or packages, subtle bugs, insecure patterns, licence questions, and leaking secrets or confidential code in prompts. The developer remains accountable for everything that is merged." xmlns="http://www.w3.org/2000/svg">
<style>
.s17f{ font-family:var(--sans),sans-serif; }
.s17f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s17f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s17f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s17f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s17f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s17f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s17f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s17f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s17f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s17f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s17f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s17f .s{ fill:var(--text-dim); font-size:13px; }
.s17f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s17f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .c{ fill:var(--text-faint); font-size:12.5px; }
.s17f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s17f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s17f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s17f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17f-a); }
.s17f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s17f-a); marker-start:url(#s17f-s); }
.s17f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s17f-g); }
.s17f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-a); }
.s17f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s17f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s17f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s17f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s17f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s17f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17f-tri); }
.s17f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-tri); }
.s17f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17f-open); }
.s17f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-open); }
.s17f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17f-dia); }
.s17f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17f-odia); }
.s17f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s17f-dia); marker-end:url(#s17f-open); }
.s17f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s17f-solid); }
.s17f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s17f-open); }
.s17f .fill{ fill:var(--text); stroke:none; }
.s17f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s17f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s17f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s17f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s17f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s17f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s17f .ks-blue{ fill:#185FA5; font-size:13px; }
.s17f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s17f .kb-blue, :root[data-theme="dark"] .s17f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s17f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s17f .kh-blue{ fill:#85B7EB; }
.s17f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s17f-blue); }
.s17f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-blue); }
.s17f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s17f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s17f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s17f .ks-amber{ fill:#854F0B; font-size:13px; }
.s17f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s17f .kb-amber, :root[data-theme="dark"] .s17f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s17f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s17f .kh-amber{ fill:#EF9F27; }
.s17f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s17f-amber); }
.s17f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-amber); }
.s17f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s17f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s17f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s17f .ks-purple{ fill:#534AB7; font-size:13px; }
.s17f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s17f .kb-purple, :root[data-theme="dark"] .s17f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s17f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s17f .kh-purple{ fill:#AFA9EC; }
.s17f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s17f-purple); }
.s17f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-purple); }
.s17f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s17f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s17f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s17f .ks-green{ fill:#3B6D11; font-size:13px; }
.s17f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s17f .kb-green, :root[data-theme="dark"] .s17f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s17f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s17f .kh-green{ fill:#97C459; }
.s17f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s17f-green); }
.s17f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-green); }
.s17f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s17f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s17f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s17f .ks-red{ fill:#A32D2D; font-size:13px; }
.s17f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s17f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s17f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s17f .kb-red, :root[data-theme="dark"] .s17f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s17f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s17f .kh-red{ fill:#F09595; }
.s17f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s17f-red); }
.s17f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s17f-red); }
.s17f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s17f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s17f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s17f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s17f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s17f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s17f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s17f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s17f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s17f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s17f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s17f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s17f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s17f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s17f">
<rect x="20" y="100" width="140" height="70" rx="7" class="k-blue"/>
<text x="90.0" y="130.5" text-anchor="middle" class="kb-blue">developer</text>
<text x="90.0" y="148.5" text-anchor="middle" class="ks-blue">context, intent</text>
<rect x="240" y="100" width="150" height="70" rx="7" class="k-purple"/>
<text x="315.0" y="130.5" text-anchor="middle" class="kb-purple">AI assistant</text>
<text x="315.0" y="148.5" text-anchor="middle" class="ks-purple">proposes</text>
<rect x="470" y="100" width="230" height="70" rx="7" class="k-amber"/>
<text x="585.0" y="130.5" text-anchor="middle" class="kb-amber">verify</text>
<text x="585.0" y="148.5" text-anchor="middle" class="ks-amber">read, test, lint, review</text>
<line x1="162" y1="125" x2="238" y2="125" class="ar"/>
<line x1="392" y1="135" x2="468" y2="135" class="ar"/>
<path d="M585 172 C 585 230, 90 230, 90 172" class="ad"/>
<text x="340" y="246" text-anchor="middle" class="c">accept, edit or reject: the human decides and is accountable</text>
<rect x="20" y="20" width="160" height="36" rx="4" class="k-red"/>
<text x="100.0" y="42.5" text-anchor="middle" class="ks-red">invented APIs, packages</text>
<rect x="192" y="20" width="160" height="36" rx="4" class="k-red"/>
<text x="272.0" y="42.5" text-anchor="middle" class="ks-red">subtle bugs</text>
<rect x="364" y="20" width="160" height="36" rx="4" class="k-red"/>
<text x="444.0" y="42.5" text-anchor="middle" class="ks-red">insecure patterns</text>
<rect x="536" y="20" width="160" height="36" rx="4" class="k-red"/>
<text x="616.0" y="42.5" text-anchor="middle" class="ks-red">secrets in prompts</text>
<text x="360" y="280" text-anchor="middle" class="kh-green">NetWarden's guardrails apply unchanged: tests, mypy, ruff S rules, review, CI</text>
</g>
</svg>
<figcaption>AI tools change how code is produced, not who is responsible for it. The engineering practices in this book are the safety net.</figcaption>
</figure>

### Risks

| Risk | Example | Defence |
|---|---|---|
| **Confident errors** | Code that calls a function or option that does not exist | Run it; tests; type checker |
| **Invented packages** | A suggested dependency name that does not exist, which an attacker could later register | Check every new dependency exists and is reputable before installing |
| **Subtle bugs** | Version comparison by string, an off-by-one in a range | Boundary tests (Chapter 11) |
| **Insecure patterns** | `shell=True`, SQL built with string formatting, missing output escaping | Security lint rules, review, threat model |
| **Data leakage** | Pasting secrets, customer data or confidential code into a tool | Organisational policy; never paste secrets |
| **Licence and provenance** | Generated code closely matching licensed code | Tool settings and policy; review |
| **Skill erosion** | Accepting code you do not understand | Read and explain every change before committing |

### Practices

- **You are accountable** for every line you commit, whoever or whatever wrote it. "The AI wrote it" is not an answer in a code review or a postmortem.
- **Give context**: the relevant code, the requirement, the constraints ("standard library only", "Python 3.11"). Better context gives better suggestions.
- **Verify with the same tools as human code**: tests, type checking, linting, review and CI. NetWarden's guardrails do not care who wrote the code.
- **Use AI where checking is cheap**: test cases, boilerplate, explanations, refactoring suggestions with good test coverage. Be most careful where checking is hard: security-sensitive logic, concurrency, numerical code.
- **Keep changes small**, as with any other change, so they can be reviewed properly.
- **Follow your organisation's policy** on which tools may see which code.

As an exercise, ask an AI assistant to implement US-11 (backport-aware detection) for NetWarden. Then review its answer as you would a teammate's pull request: Does it use only the standard library? Does it keep the `KnowledgeSource` interface? Are the data sources it mentions real? Do the existing 46 tests still pass, and what new tests does it need?

## The engineer you become

The practices in this book are not a checklist to complete once. They are habits: writing requirements that can be tested, drawing the model before the code, keeping the design changeable, testing at every level, automating everything repeatable, measuring honestly, managing risk openly, and caring about the people your software affects. Tools will change, as they always have. The habits, and the professional responsibility behind them, are what make a programmer a software engineer.

## Summary

- Teams develop through **forming, storming, norming and performing**; **psychological safety** is the strongest predictor of team effectiveness.
- Keep teams **small**; communication paths grow as n(n-1)/2. **Conway's law** links team structure to system structure.
- The **ACM/IEEE-CS Code of Ethics** puts the **public interest** first; privacy and data protection are design concerns.
- Security tools are **dual-use**: build in limits, and assess systems only with **written authorisation** and agreed **rules of engagement**.
- Respect **licences**; know what your dependencies allow.
- **AI assistants** speed up routine work but make confident mistakes; verify their output with the same tests, analysis and review as any other code. The engineer remains accountable.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-17-teams-ethics-and-ai-assisted-development).

**1. Which are Tuckman's stages of team development?**

- A. Forming, storming, norming, performing
- B. Plan, do, check, act
- C. Hire, train, review, promote
- D. Start, sprint, release, retire

**2. What did research find to be the strongest predictor of team effectiveness?**

- A. Team size
- B. Seniority
- C. Psychological safety
- D. Office layout

**3. How many communication paths does a team of 6 have?**

- A. 6
- B. 12
- C. 15
- D. 36

**4. What does Conway's law say?**

- A. Teams grow until they fail
- B. Every team needs a manager
- C. Code quality falls with team size
- D. A system's structure tends to mirror the communication structure of the organisation that builds it

**5. What does the ACM/IEEE-CS Software Engineering Code of Ethics put first?**

- A. The employer
- B. The public interest
- C. The client
- D. The profession

**6. What makes NetWarden a dual-use tool?**

- A. It runs on two platforms
- B. It has two interfaces
- C. It is free and paid
- D. The same capability can defend or attack, so it builds in limits and requires authorisation

**7. Why must you check your dependencies' licences?**

- A. They set what you may do with the code, such as distribution and attribution conditions
- B. Licences slow builds
- C. Only commercial code has licences
- D. Licences expire

**8. Who is accountable for code an AI assistant wrote?**

- A. The AI vendor
- B. Nobody
- C. The engineer who accepts it, who must verify it with tests, analysis and review
- D. The code reviewer only
