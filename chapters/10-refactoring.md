# Chapter 10: Refactoring and Technical Debt

**Refactoring** is changing the internal structure of software to make it easier to understand and cheaper to modify, **without changing its observable behaviour** (Martin Fowler, *Refactoring*, 1999; second edition 2018). It is how clean code stays clean, and how messy code becomes clean, one small safe step at a time. Its counterpart is **technical debt**: the accumulated cost of design shortcuts, which makes every future change slower. This chapter covers both.

## How to refactor

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The refactoring loop: make sure tests pass; make one small behaviour-preserving change; run the tests; if green, commit; if red, undo; repeat. Each step is small enough that a failure points directly at its cause." xmlns="http://www.w3.org/2000/svg">
<style>
.s10a{ font-family:var(--sans),sans-serif; }
.s10a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s10a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s10a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s10a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s10a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s10a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s10a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s10a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s10a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s10a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s10a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s10a .s{ fill:var(--text-dim); font-size:13px; }
.s10a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s10a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .c{ fill:var(--text-faint); font-size:12.5px; }
.s10a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s10a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s10a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s10a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10a-a); }
.s10a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10a-a); marker-start:url(#s10a-s); }
.s10a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s10a-g); }
.s10a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-a); }
.s10a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s10a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s10a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s10a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s10a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s10a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10a-tri); }
.s10a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-tri); }
.s10a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10a-open); }
.s10a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-open); }
.s10a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10a-dia); }
.s10a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10a-odia); }
.s10a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10a-dia); marker-end:url(#s10a-open); }
.s10a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10a-solid); }
.s10a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s10a-open); }
.s10a .fill{ fill:var(--text); stroke:none; }
.s10a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s10a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s10a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s10a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s10a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s10a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s10a .ks-blue{ fill:#185FA5; font-size:13px; }
.s10a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s10a .kb-blue, :root[data-theme="dark"] .s10a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s10a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s10a .kh-blue{ fill:#85B7EB; }
.s10a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s10a-blue); }
.s10a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-blue); }
.s10a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s10a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s10a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s10a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s10a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s10a .kb-teal, :root[data-theme="dark"] .s10a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s10a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s10a .kh-teal{ fill:#5DCAA5; }
.s10a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s10a-teal); }
.s10a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-teal); }
.s10a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s10a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s10a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s10a .ks-amber{ fill:#854F0B; font-size:13px; }
.s10a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s10a .kb-amber, :root[data-theme="dark"] .s10a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s10a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s10a .kh-amber{ fill:#EF9F27; }
.s10a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s10a-amber); }
.s10a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-amber); }
.s10a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s10a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s10a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s10a .ks-green{ fill:#3B6D11; font-size:13px; }
.s10a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s10a .kb-green, :root[data-theme="dark"] .s10a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s10a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s10a .kh-green{ fill:#97C459; }
.s10a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s10a-green); }
.s10a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-green); }
.s10a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s10a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s10a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s10a .ks-red{ fill:#A32D2D; font-size:13px; }
.s10a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s10a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s10a .kb-red, :root[data-theme="dark"] .s10a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s10a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s10a .kh-red{ fill:#F09595; }
.s10a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s10a-red); }
.s10a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10a-red); }
.s10a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s10a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s10a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s10a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s10a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s10a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s10a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s10a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s10a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s10a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s10a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s10a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s10a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s10a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s10a">
<rect x="285" y="13" width="150" height="40" rx="7" class="k-green"/>
<text x="360.0" y="37.5" text-anchor="middle" class="kb-green">tests green</text>
<rect x="460" y="105" width="150" height="40" rx="7" class="k-blue"/>
<text x="535.0" y="129.5" text-anchor="middle" class="kb-blue">one small change</text>
<rect x="285" y="197" width="150" height="40" rx="7" class="k-amber"/>
<text x="360.0" y="221.5" text-anchor="middle" class="kb-amber">run tests</text>
<rect x="110" y="105" width="150" height="40" rx="7" class="k-teal"/>
<text x="185.0" y="129.5" text-anchor="middle" class="kb-teal">commit</text>
<path d="M440 50 C 520 50, 540 80, 540 100" class="ar"/>
<path d="M540 150 C 540 175, 520 200, 440 205" class="ar"/>
<path d="M280 205 C 200 200, 180 175, 180 150" class="ar"/>
<path d="M180 100 C 180 80, 200 50, 280 50" class="ar"/>
<text x="360" y="130" text-anchor="middle" class="kh-red">red? undo, take a smaller step</text>
</g>
</svg>
<figcaption>Refactoring is a sequence of tiny, safe transformations, never a big rewrite with the tests switched off.</figcaption>
</figure>

Refactoring depends on **tests**. Without them, you cannot know that behaviour is unchanged. The process is a loop of tiny steps:

1. Make sure all tests pass.
2. Make one small structural change: rename, extract, move.
3. Run the tests.
4. Green: commit. Red: undo and take a smaller step.

Kent Beck's advice summarises the attitude: "make the change easy (warning: this may be hard), then make the easy change". Refactoring is not a separate project scheduled for "later"; it is part of everyday work, done just before or just after adding a feature. **Rewriting** is different: throwing code away and starting again is a big, risky bet, and is rarely the right choice for code that works.

Modern editors automate the mechanical refactorings, such as rename, extract function or variable, inline, and move, safely across a whole project, especially when the code has type hints.

## Code smells

A **code smell** is a surface symptom that usually indicates a deeper design problem. Kent Beck and Martin Fowler named and catalogued them.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A selection of code smells from Fowler&#x27;s catalogue: long function, large class, long parameter list, duplicated code, feature envy, data clumps, primitive obsession, shotgun surgery, divergent change, switch statements, speculative generality and comments explaining bad code. Each has typical refactorings." xmlns="http://www.w3.org/2000/svg">
<style>
.s10b{ font-family:var(--sans),sans-serif; }
.s10b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s10b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s10b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s10b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s10b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s10b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s10b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s10b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s10b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s10b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s10b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s10b .s{ fill:var(--text-dim); font-size:13px; }
.s10b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s10b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s10b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s10b .c{ fill:var(--text-faint); font-size:12.5px; }
.s10b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s10b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s10b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s10b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10b-a); }
.s10b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10b-a); marker-start:url(#s10b-s); }
.s10b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s10b-g); }
.s10b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s10b-a); }
.s10b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s10b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s10b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s10b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s10b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s10b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10b-tri); }
.s10b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10b-tri); }
.s10b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10b-open); }
.s10b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10b-open); }
.s10b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10b-dia); }
.s10b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10b-odia); }
.s10b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10b-dia); marker-end:url(#s10b-open); }
.s10b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10b-solid); }
.s10b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s10b-open); }
.s10b .fill{ fill:var(--text); stroke:none; }
.s10b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s10b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s10b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s10b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s10b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s10b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s10b .ks-amber{ fill:#854F0B; font-size:13px; }
.s10b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s10b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s10b .kb-amber, :root[data-theme="dark"] .s10b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s10b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s10b .kh-amber{ fill:#EF9F27; }
.s10b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s10b-amber); }
.s10b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10b-amber); }
.s10b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
</style>
<defs><marker id="s10b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s10b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s10b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s10b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s10b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s10b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s10b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s10b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s10b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker></defs>
<g class="s10b">
<rect x="20" y="14" width="218" height="58" rx="7" class="k-amber"/>
<text x="129.0" y="38.5" text-anchor="middle" class="kb-amber">long function</text>
<text x="129.0" y="56.5" text-anchor="middle" class="ks-amber">-&gt; extract function</text>
<rect x="250" y="14" width="218" height="58" rx="7" class="k-amber"/>
<text x="359.0" y="38.5" text-anchor="middle" class="kb-amber">large class</text>
<text x="359.0" y="56.5" text-anchor="middle" class="ks-amber">-&gt; extract class</text>
<rect x="480" y="14" width="218" height="58" rx="7" class="k-amber"/>
<text x="589.0" y="38.5" text-anchor="middle" class="kb-amber">long parameter list</text>
<text x="589.0" y="56.5" text-anchor="middle" class="ks-amber">-&gt; introduce parameter object</text>
<rect x="20" y="82" width="218" height="58" rx="7" class="k-amber"/>
<text x="129.0" y="106.5" text-anchor="middle" class="kb-amber">duplicated code</text>
<text x="129.0" y="124.5" text-anchor="middle" class="ks-amber">-&gt; extract, pull up</text>
<rect x="250" y="82" width="218" height="58" rx="7" class="k-amber"/>
<text x="359.0" y="106.5" text-anchor="middle" class="kb-amber">feature envy</text>
<text x="359.0" y="124.5" text-anchor="middle" class="ks-amber">-&gt; move function</text>
<rect x="480" y="82" width="218" height="58" rx="7" class="k-amber"/>
<text x="589.0" y="106.5" text-anchor="middle" class="kb-amber">data clumps</text>
<text x="589.0" y="124.5" text-anchor="middle" class="ks-amber">-&gt; introduce class</text>
<rect x="20" y="150" width="218" height="58" rx="7" class="k-amber"/>
<text x="129.0" y="174.5" text-anchor="middle" class="kb-amber">primitive obsession</text>
<text x="129.0" y="192.5" text-anchor="middle" class="ks-amber">-&gt; replace with object</text>
<rect x="250" y="150" width="218" height="58" rx="7" class="k-amber"/>
<text x="359.0" y="174.5" text-anchor="middle" class="kb-amber">shotgun surgery</text>
<text x="359.0" y="192.5" text-anchor="middle" class="ks-amber">-&gt; move, combine</text>
<rect x="480" y="150" width="218" height="58" rx="7" class="k-amber"/>
<text x="589.0" y="174.5" text-anchor="middle" class="kb-amber">divergent change</text>
<text x="589.0" y="192.5" text-anchor="middle" class="ks-amber">-&gt; split phase</text>
<rect x="20" y="218" width="218" height="58" rx="7" class="k-amber"/>
<text x="129.0" y="242.5" text-anchor="middle" class="kb-amber">type switches</text>
<text x="129.0" y="260.5" text-anchor="middle" class="ks-amber">-&gt; polymorphism</text>
<rect x="250" y="218" width="218" height="58" rx="7" class="k-amber"/>
<text x="359.0" y="242.5" text-anchor="middle" class="kb-amber">speculative generality</text>
<text x="359.0" y="260.5" text-anchor="middle" class="ks-amber">-&gt; inline, remove</text>
<rect x="480" y="218" width="218" height="58" rx="7" class="k-amber"/>
<text x="589.0" y="242.5" text-anchor="middle" class="kb-amber">explaining comments</text>
<text x="589.0" y="260.5" text-anchor="middle" class="ks-amber">-&gt; rename, extract</text>
</g>
</svg>
<figcaption>A smell is not a bug; it is a hint that the design makes some change harder than it should be.</figcaption>
</figure>

Each smell points to refactorings that remove it. For example, **feature envy**, a function that uses another object's data more than its own, suggests moving the function to that object. NetWarden's `ScanResult.counts()` exists because report code kept reaching into `result.findings` to count severities; the counting moved to the class that owns the data.

## Common refactorings

| Refactoring | Before | After |
|---|---|---|
| **Rename** | `def p(s):` | `def identify(service):` |
| **Extract function** | A block with a comment explaining it | A function named after the comment |
| **Inline** | A trivial function used once | Its body at the call site |
| **Extract variable** | A long expression | A well-named intermediate variable |
| **Introduce parameter object** | `scan(host, port, timeout, retries, banner_len)` | `scan(host, port, options)` |
| **Replace magic number with constant** | `if n > 1024:` | `if n > MAX_HOSTS:` |
| **Move function** | Logic in the class that uses data | Logic in the class that owns data |
| **Replace conditional with polymorphism** | `if`/`elif` on a type code | One class per case with a common interface |
| **Split phase** | One function that parses and computes | A parse step producing data, then a compute step |

### A NetWarden refactoring story

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Replace conditional with polymorphism. Before: one function with an if and elif chain over service names and ports decides which problems to report, and grows with every new rule. After: each rule is a Check class with a run method, and the engine loops over a list of checks." xmlns="http://www.w3.org/2000/svg">
<style>
.s10c{ font-family:var(--sans),sans-serif; }
.s10c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s10c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s10c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s10c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s10c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s10c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s10c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s10c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s10c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s10c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s10c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s10c .s{ fill:var(--text-dim); font-size:13px; }
.s10c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s10c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s10c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s10c .c{ fill:var(--text-faint); font-size:12.5px; }
.s10c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s10c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s10c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s10c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10c-a); }
.s10c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10c-a); marker-start:url(#s10c-s); }
.s10c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s10c-g); }
.s10c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s10c-a); }
.s10c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s10c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s10c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s10c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s10c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s10c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10c-tri); }
.s10c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10c-tri); }
.s10c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10c-open); }
.s10c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10c-open); }
.s10c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10c-dia); }
.s10c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10c-odia); }
.s10c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10c-dia); marker-end:url(#s10c-open); }
.s10c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10c-solid); }
.s10c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s10c-open); }
.s10c .fill{ fill:var(--text); stroke:none; }
.s10c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s10c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s10c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s10c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s10c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s10c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s10c .ks-green{ fill:#3B6D11; font-size:13px; }
.s10c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s10c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s10c .kb-green, :root[data-theme="dark"] .s10c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s10c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s10c .kh-green{ fill:#97C459; }
.s10c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s10c-green); }
.s10c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10c-green); }
.s10c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s10c .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s10c .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s10c .ks-red{ fill:#A32D2D; font-size:13px; }
.s10c .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s10c .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10c .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s10c .kb-red, :root[data-theme="dark"] .s10c .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s10c .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s10c .kh-red{ fill:#F09595; }
.s10c .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s10c-red); }
.s10c .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10c-red); }
.s10c .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s10c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s10c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s10c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s10c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s10c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s10c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s10c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s10c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s10c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s10c-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s10c">
<text x="185" y="20" text-anchor="middle" class="kh-red">before</text>
<rect x="20" y="30" width="330" height="236" rx="6" class="k-red"/>
<text x="32" y="54" text-anchor="start" class="km-red">def find_problems(svc):</text>
<text x="62.0" y="78" text-anchor="start" class="km-red">out = []</text>
<text x="62.0" y="102" text-anchor="start" class="km-red">if svc.name == "telnet":</text>
<text x="92.0" y="126" text-anchor="start" class="km-red">out.append(...)</text>
<text x="62.0" y="150" text-anchor="start" class="km-red">elif svc.port == 3306:</text>
<text x="92.0" y="174" text-anchor="start" class="km-red">out.append(...)</text>
<text x="62.0" y="198" text-anchor="start" class="km-red">elif svc.banner.startswith("HTTP"):</text>
<text x="92.0" y="222" text-anchor="start" class="km-red">...  # grows forever</text>
<text x="62.0" y="246" text-anchor="start" class="km-red">return out</text>
<line x1="360" y1="148" x2="382" y2="148" class="ar"/>
<text x="545" y="20" text-anchor="middle" class="kh-green">after</text>
<rect x="390" y="30" width="310" height="236" rx="6" class="k-green"/>
<text x="402" y="54" text-anchor="start" class="km-green">for check in self.checks:</text>
<text x="432.0" y="78" text-anchor="start" class="km-green">findings += check.run(host, svc)</text>
<text x="402" y="102" text-anchor="start" class="km-green"></text>
<text x="402" y="126" text-anchor="start" class="km-green">class CleartextProtocolCheck:</text>
<text x="432.0" y="150" text-anchor="start" class="km-green">def run(self, host, svc): ...</text>
<text x="402" y="174" text-anchor="start" class="km-green">class ExposedDatabaseCheck:</text>
<text x="432.0" y="198" text-anchor="start" class="km-green">def run(self, host, svc): ...</text>
<text x="402" y="222" text-anchor="start" class="km-green">class HttpHeadersCheck:</text>
<text x="432.0" y="246" text-anchor="start" class="km-green">def run(self, host, svc): ...</text>
</g>
</svg>
<figcaption>This is how NetWarden's strategy-based checks came about: a refactoring of the prototype's growing if/elif chain.</figcaption>
</figure>

NetWarden's first prototype had one function with a growing `if`/`elif` chain deciding which problems to report. Each new rule meant editing the same function and re-testing all of it. The team refactored in small steps:

1. Wrote **characterisation tests** that pinned down the current output for a set of sample services.
2. Extracted each branch into its own function, running tests after each extraction.
3. Gave each function the same signature, `(host, service) -> list[Finding]`.
4. Turned the functions into classes with an `id`, introduced the `Check` protocol, and replaced the chain with a loop over a list.
5. Deleted the old function. All tests still passed; the behaviour had not changed.

The result is the strategy design from Chapter 6. Nobody designed it up front; it **emerged** from refactoring when the need became clear.

### Hands on: a real fix found by the tests

While writing this book, NetWarden's test suite produced `ResourceWarning: unclosed database` messages. The cause: `ScanRepository` opened a SQLite connection that callers sometimes forgot to close. The refactoring, done under green tests, added the context manager protocol and changed the callers:

```python
class ScanRepository:
    ...
    def __enter__(self) -> ScanRepository:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

# before                                          # after
repo = ScanRepository(args.db)                    with ScanRepository(args.db) as repo:
print(repo.save(result))                              print(repo.save(result))
repo.close()   # skipped if save() raises
```

Running `pytest -W error::ResourceWarning` now turns any future leak into a failing test, so the fix cannot silently regress.

## Technical debt

Ward Cunningham coined the **technical debt** metaphor in 1992: shipping code that is not quite right is like borrowing money. It can be a good decision, because you learn sooner and deliver value earlier, but the debt accrues **interest**: every change in that area costs more until the debt is repaid by refactoring.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Martin Fowler&#x27;s technical debt quadrant. Reckless and deliberate: we do not have time for design. Prudent and deliberate: we must ship now and will deal with the consequences, recorded in the backlog. Reckless and inadvertent: what is layering? Prudent and inadvertent: now we know how we should have done it." xmlns="http://www.w3.org/2000/svg">
<style>
.s10d{ font-family:var(--sans),sans-serif; }
.s10d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s10d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s10d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s10d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s10d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s10d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s10d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s10d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s10d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s10d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s10d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s10d .s{ fill:var(--text-dim); font-size:13px; }
.s10d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s10d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s10d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s10d .c{ fill:var(--text-faint); font-size:12.5px; }
.s10d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s10d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s10d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s10d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10d-a); }
.s10d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10d-a); marker-start:url(#s10d-s); }
.s10d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s10d-g); }
.s10d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s10d-a); }
.s10d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s10d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s10d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s10d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s10d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s10d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10d-tri); }
.s10d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10d-tri); }
.s10d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10d-open); }
.s10d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10d-open); }
.s10d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10d-dia); }
.s10d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10d-odia); }
.s10d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10d-dia); marker-end:url(#s10d-open); }
.s10d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10d-solid); }
.s10d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s10d-open); }
.s10d .fill{ fill:var(--text); stroke:none; }
.s10d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s10d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s10d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s10d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s10d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s10d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s10d .ks-amber{ fill:#854F0B; font-size:13px; }
.s10d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s10d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s10d .kb-amber, :root[data-theme="dark"] .s10d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s10d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s10d .kh-amber{ fill:#EF9F27; }
.s10d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s10d-amber); }
.s10d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10d-amber); }
.s10d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s10d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s10d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s10d .ks-green{ fill:#3B6D11; font-size:13px; }
.s10d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s10d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s10d .kb-green, :root[data-theme="dark"] .s10d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s10d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s10d .kh-green{ fill:#97C459; }
.s10d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s10d-green); }
.s10d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10d-green); }
.s10d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s10d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s10d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s10d .ks-red{ fill:#A32D2D; font-size:13px; }
.s10d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s10d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s10d .kb-red, :root[data-theme="dark"] .s10d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s10d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s10d .kh-red{ fill:#F09595; }
.s10d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s10d-red); }
.s10d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10d-red); }
.s10d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s10d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s10d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s10d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s10d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s10d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s10d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s10d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s10d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s10d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s10d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s10d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s10d">
<line x1="360" y1="30" x2="360" y2="280" class="ln"/>
<line x1="40" y1="155" x2="680" y2="155" class="ln"/>
<text x="200" y="22" text-anchor="middle" class="kh-red">reckless</text>
<text x="520" y="22" text-anchor="middle" class="kh-green">prudent</text>
<text x="30" y="95" text-anchor="start" class="c">deliberate</text>
<text x="30" y="225" text-anchor="start" class="c">inadvertent</text>
<rect x="120" y="40" width="220" height="100" rx="7" class="k-red"/>
<text x="230.0" y="94.5" text-anchor="middle" class="kb-red">"no time for design"</text>
<rect x="380" y="40" width="220" height="100" rx="7" class="k-green"/>
<text x="490.0" y="94.5" text-anchor="middle" class="kb-green">"ship now, fix later" (logged)</text>
<rect x="120" y="170" width="220" height="100" rx="7" class="k-red"/>
<text x="230.0" y="224.5" text-anchor="middle" class="kb-red">"what's layering?"</text>
<rect x="380" y="170" width="220" height="100" rx="7" class="k-amber"/>
<text x="490.0" y="224.5" text-anchor="middle" class="kb-amber">"now we know how"</text>
</g>
</svg>
<figcaption>Not all debt is bad: prudent, deliberate debt is a business decision. The dangerous kind is the debt nobody knows about.</figcaption>
</figure>

Martin Fowler's quadrant distinguishes kinds of debt. **Prudent, deliberate** debt is a conscious trade-off: NetWarden 1.0 ships with a small, bundled knowledge base (ADR-0002) and a backlog item, US-10, to replace it. **Reckless** debt comes from ignoring good practice. **Inadvertent** debt is unavoidable: teams learn how a design should have been only after building it.

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Technical debt as interest. Without refactoring, the cost of each new feature rises over time as the code becomes harder to change. With regular refactoring, the cost stays roughly flat. Early on, skipping refactoring looks faster; the lines cross after a few months. Illustrative curves." xmlns="http://www.w3.org/2000/svg">
<style>
.s10e{ font-family:var(--sans),sans-serif; }
.s10e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s10e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s10e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s10e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s10e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s10e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s10e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s10e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s10e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s10e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s10e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s10e .s{ fill:var(--text-dim); font-size:13px; }
.s10e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s10e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s10e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s10e .c{ fill:var(--text-faint); font-size:12.5px; }
.s10e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s10e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s10e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s10e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10e-a); }
.s10e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s10e-a); marker-start:url(#s10e-s); }
.s10e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s10e-g); }
.s10e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s10e-a); }
.s10e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s10e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s10e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s10e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s10e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s10e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10e-tri); }
.s10e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10e-tri); }
.s10e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10e-open); }
.s10e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s10e-open); }
.s10e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10e-dia); }
.s10e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10e-odia); }
.s10e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s10e-dia); marker-end:url(#s10e-open); }
.s10e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s10e-solid); }
.s10e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s10e-open); }
.s10e .fill{ fill:var(--text); stroke:none; }
.s10e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s10e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s10e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s10e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s10e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s10e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s10e .ks-amber{ fill:#854F0B; font-size:13px; }
.s10e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s10e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s10e .kb-amber, :root[data-theme="dark"] .s10e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s10e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s10e .kh-amber{ fill:#EF9F27; }
.s10e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s10e-amber); }
.s10e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10e-amber); }
.s10e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s10e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s10e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s10e .ks-green{ fill:#3B6D11; font-size:13px; }
.s10e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s10e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s10e .kb-green, :root[data-theme="dark"] .s10e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s10e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s10e .kh-green{ fill:#97C459; }
.s10e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s10e-green); }
.s10e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10e-green); }
.s10e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s10e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s10e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s10e .ks-red{ fill:#A32D2D; font-size:13px; }
.s10e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s10e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s10e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s10e .kb-red, :root[data-theme="dark"] .s10e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s10e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s10e .kh-red{ fill:#F09595; }
.s10e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s10e-red); }
.s10e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s10e-red); }
.s10e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s10e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s10e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s10e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s10e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s10e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s10e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s10e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s10e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s10e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s10e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s10e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s10e">
<line x1="60" y1="240" x2="680" y2="240" class="ar"/>
<line x1="60" y1="240" x2="60" y2="20" class="ar"/>
<text x="370" y="268" text-anchor="middle" class="c">time</text>
<text x="70" y="16" text-anchor="start" class="c">cost per feature</text>
<path d="M60 200 C 250 190, 450 140, 660 40" class="ln-red"/>
<text x="640" y="60" text-anchor="end" class="kh-red">no refactoring</text>
<path d="M60 170 C 250 165, 450 162, 660 158" class="ln-green"/>
<text x="640" y="150" text-anchor="end" class="kh-green">continuous refactoring</text>
<circle cx="312" cy="188" r="5" class="k-amber"/>
<text x="312" y="214" text-anchor="middle" class="kh-amber">crossover</text>
</g>
</svg>
<figcaption>Illustrative shape, not measured data. The interest on technical debt is paid in slower, riskier changes.</figcaption>
</figure>

### Managing debt

- **Make it visible**: record debt as backlog items or issues with a label, explaining the cost of leaving it. "We should clean this up" in a chat message is forgotten by Friday.
- **Measure symptoms**: complexity, duplication, change frequency of files, time to implement typical changes, defect rates. Tools such as SonarQube report many of these.
- **Pay continuously**: the **Boy Scout Rule**, "leave the code a little better than you found it", applied on every change; plus a share of each sprint (some teams reserve 10 to 20%) for larger repayments.
- **Prioritise by interest**: debt in code that never changes costs nothing. Debt in the busiest module costs every day. Change frequency multiplied by complexity, sometimes called a **hotspot** analysis, finds where repayment pays off most.
- **Avoid new reckless debt**: definition of done, code review, and automated checks.

### Talking to managers about debt

Technical debt is a business concern, so explain it in business terms: "adding the PostgreSQL backend will take three weeks instead of one because the storage code is tangled with reporting; one week of refactoring now saves two on this feature and more on the next". A product owner can weigh that like any other investment.

## When not to refactor

- When there are **no tests** and you cannot add them first: add characterisation tests, then refactor.
- When the code is about to be **deleted** or replaced.
- In the middle of a **production incident**: fix first, refactor afterwards.
- When the change is cosmetic and the code never changes: the interest is zero.

## Summary

- **Refactoring** improves structure without changing behaviour, in tiny steps protected by **tests**.
- **Code smells** hint at design problems; each has typical refactorings.
- Common refactorings: rename, extract, inline, move, introduce parameter object, replace conditional with polymorphism.
- Good designs often **emerge** from refactoring when the need is clear.
- **Technical debt** accrues **interest**; distinguish prudent from reckless, deliberate from inadvertent.
- Make debt **visible**, prioritise **hotspots**, and repay continuously with the **Boy Scout Rule**.
