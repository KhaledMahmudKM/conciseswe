# Chapter 6: Design Patterns

A **design pattern** is a named, reusable solution to a problem that recurs in a particular context. The idea comes from the architect Christopher Alexander, who catalogued patterns for buildings and towns. In 1994, Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, the "Gang of Four" (GoF), published *Design Patterns: Elements of Reusable Object-Oriented Software*, describing 23 patterns for object-oriented code. Patterns give developers a shared vocabulary: "make the checks strategies" says in four words what would otherwise take a paragraph.

This chapter covers the patterns that appear in NetWarden, how they look in Python, and when not to use them.

## Anatomy of a pattern

Each pattern description has the same parts:

| Part | Meaning |
|---|---|
| **Name** | A short handle for discussion |
| **Problem** | The situation and the forces that make it hard |
| **Solution** | The roles of classes and objects and how they collaborate, usually as a class diagram |
| **Consequences** | What you gain and what it costs |

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The 23 Gang of Four patterns in three groups. Creational: abstract factory, builder, factory method, prototype, singleton. Structural: adapter, bridge, composite, decorator, facade, flyweight, proxy. Behavioural: chain of responsibility, command, interpreter, iterator, mediator, memento, observer, state, strategy, template method, visitor. Patterns used or discussed with NetWarden are highlighted." xmlns="http://www.w3.org/2000/svg">
<style>
.s6a{ font-family:var(--sans),sans-serif; }
.s6a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6a .s{ fill:var(--text-dim); font-size:13px; }
.s6a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6a .c{ fill:var(--text-faint); font-size:12.5px; }
.s6a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6a-a); }
.s6a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6a-a); marker-start:url(#s6a-s); }
.s6a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6a-g); }
.s6a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6a-a); }
.s6a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6a-tri); }
.s6a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6a-tri); }
.s6a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6a-open); }
.s6a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6a-open); }
.s6a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6a-dia); }
.s6a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6a-odia); }
.s6a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6a-dia); marker-end:url(#s6a-open); }
.s6a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6a-solid); }
.s6a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6a-open); }
.s6a .fill{ fill:var(--text); stroke:none; }
.s6a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6a .ks-blue{ fill:#185FA5; font-size:13px; }
.s6a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6a .kb-blue, :root[data-theme="dark"] .s6a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6a .kh-blue{ fill:#85B7EB; }
.s6a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6a-blue); }
.s6a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6a-blue); }
.s6a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6a .kb-teal, :root[data-theme="dark"] .s6a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6a .kh-teal{ fill:#5DCAA5; }
.s6a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6a-teal); }
.s6a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6a-teal); }
.s6a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6a .ks-purple{ fill:#534AB7; font-size:13px; }
.s6a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6a .kb-purple, :root[data-theme="dark"] .s6a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6a .kh-purple{ fill:#AFA9EC; }
.s6a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6a-purple); }
.s6a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6a-purple); }
.s6a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s6a">
<rect x="20" y="10" width="218" height="46" rx="7" class="k-blue"/>
<text x="129.0" y="28.5" text-anchor="middle" class="kb-blue">creational</text>
<text x="129.0" y="46.5" text-anchor="middle" class="ks-blue">how objects are made</text>
<rect x="20" y="64" width="218" height="24" rx="4" class="pnl"/>
<text x="129.0" y="80.5" text-anchor="middle" class="c">abstract factory</text>
<rect x="20" y="94" width="218" height="24" rx="4" class="pnl"/>
<text x="129.0" y="110.5" text-anchor="middle" class="c">builder</text>
<rect x="20" y="124" width="218" height="24" rx="4" class="k-blue"/>
<text x="129.0" y="140.5" text-anchor="middle" class="ks-blue">factory method</text>
<rect x="20" y="154" width="218" height="24" rx="4" class="pnl"/>
<text x="129.0" y="170.5" text-anchor="middle" class="c">prototype</text>
<rect x="20" y="184" width="218" height="24" rx="4" class="pnl"/>
<text x="129.0" y="200.5" text-anchor="middle" class="c">singleton</text>
<rect x="252" y="10" width="218" height="46" rx="7" class="k-teal"/>
<text x="361.0" y="28.5" text-anchor="middle" class="kb-teal">structural</text>
<text x="361.0" y="46.5" text-anchor="middle" class="ks-teal">how objects are composed</text>
<rect x="252" y="64" width="218" height="24" rx="4" class="k-teal"/>
<text x="361.0" y="80.5" text-anchor="middle" class="ks-teal">adapter</text>
<rect x="252" y="94" width="218" height="24" rx="4" class="pnl"/>
<text x="361.0" y="110.5" text-anchor="middle" class="c">bridge</text>
<rect x="252" y="124" width="218" height="24" rx="4" class="pnl"/>
<text x="361.0" y="140.5" text-anchor="middle" class="c">composite</text>
<rect x="252" y="154" width="218" height="24" rx="4" class="k-teal"/>
<text x="361.0" y="170.5" text-anchor="middle" class="ks-teal">decorator</text>
<rect x="252" y="184" width="218" height="24" rx="4" class="k-teal"/>
<text x="361.0" y="200.5" text-anchor="middle" class="ks-teal">facade</text>
<rect x="252" y="214" width="218" height="24" rx="4" class="pnl"/>
<text x="361.0" y="230.5" text-anchor="middle" class="c">flyweight</text>
<rect x="252" y="244" width="218" height="24" rx="4" class="pnl"/>
<text x="361.0" y="260.5" text-anchor="middle" class="c">proxy</text>
<rect x="484" y="10" width="218" height="46" rx="7" class="k-purple"/>
<text x="593.0" y="28.5" text-anchor="middle" class="kb-purple">behavioural</text>
<text x="593.0" y="46.5" text-anchor="middle" class="ks-purple">how objects interact</text>
<rect x="484" y="64" width="109" height="24" rx="4" class="pnl"/>
<text x="538.5" y="80.5" text-anchor="middle" class="c">chain of resp.</text>
<rect x="594" y="64" width="109" height="24" rx="4" class="pnl"/>
<text x="648.5" y="80.5" text-anchor="middle" class="c">command</text>
<rect x="484" y="94" width="109" height="24" rx="4" class="pnl"/>
<text x="538.5" y="110.5" text-anchor="middle" class="c">interpreter</text>
<rect x="594" y="94" width="109" height="24" rx="4" class="k-purple"/>
<text x="648.5" y="110.5" text-anchor="middle" class="ks-purple">iterator</text>
<rect x="484" y="124" width="109" height="24" rx="4" class="pnl"/>
<text x="538.5" y="140.5" text-anchor="middle" class="c">mediator</text>
<rect x="594" y="124" width="109" height="24" rx="4" class="pnl"/>
<text x="648.5" y="140.5" text-anchor="middle" class="c">memento</text>
<rect x="484" y="154" width="109" height="24" rx="4" class="k-purple"/>
<text x="538.5" y="170.5" text-anchor="middle" class="ks-purple">observer</text>
<rect x="594" y="154" width="109" height="24" rx="4" class="pnl"/>
<text x="648.5" y="170.5" text-anchor="middle" class="c">state</text>
<rect x="484" y="184" width="109" height="24" rx="4" class="k-purple"/>
<text x="538.5" y="200.5" text-anchor="middle" class="ks-purple">strategy</text>
<rect x="594" y="184" width="109" height="24" rx="4" class="k-purple"/>
<text x="648.5" y="200.5" text-anchor="middle" class="ks-purple">template method</text>
<rect x="484" y="214" width="109" height="24" rx="4" class="pnl"/>
<text x="538.5" y="230.5" text-anchor="middle" class="c">visitor</text>
</g>
</svg>
<figcaption>Coloured: patterns that appear in NetWarden or are discussed in this chapter.</figcaption>
</figure>

The GoF grouped their patterns by purpose: **creational** patterns deal with creating objects, **structural** patterns with composing them, and **behavioural** patterns with how they interact and share responsibility.

## Strategy

**Problem:** an algorithm varies, and you do not want the code that uses it to be full of conditionals that choose between versions.

**Solution:** define a family of algorithms behind a common interface, and give the client a reference to one (or several).

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The strategy pattern. Generic form: a Context holds a reference to a Strategy interface and calls execute; ConcreteStrategyA and ConcreteStrategyB implement it. In NetWarden: Assessment is the context, Check is the strategy, and each check class is a concrete strategy; the reporters form a second strategy family selected by format." xmlns="http://www.w3.org/2000/svg">
<style>
.s6b{ font-family:var(--sans),sans-serif; }
.s6b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6b .s{ fill:var(--text-dim); font-size:13px; }
.s6b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6b .c{ fill:var(--text-faint); font-size:12.5px; }
.s6b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6b-a); }
.s6b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6b-a); marker-start:url(#s6b-s); }
.s6b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6b-g); }
.s6b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-a); }
.s6b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6b-tri); }
.s6b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-tri); }
.s6b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6b-open); }
.s6b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-open); }
.s6b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6b-dia); }
.s6b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6b-odia); }
.s6b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6b-dia); marker-end:url(#s6b-open); }
.s6b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6b-solid); }
.s6b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6b-open); }
.s6b .fill{ fill:var(--text); stroke:none; }
.s6b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6b .ks-blue{ fill:#185FA5; font-size:13px; }
.s6b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6b .kb-blue, :root[data-theme="dark"] .s6b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6b .kh-blue{ fill:#85B7EB; }
.s6b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6b-blue); }
.s6b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-blue); }
.s6b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6b .kb-teal, :root[data-theme="dark"] .s6b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6b .kh-teal{ fill:#5DCAA5; }
.s6b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6b-teal); }
.s6b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-teal); }
.s6b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6b .ks-purple{ fill:#534AB7; font-size:13px; }
.s6b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6b .kb-purple, :root[data-theme="dark"] .s6b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6b .kh-purple{ fill:#AFA9EC; }
.s6b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6b-purple); }
.s6b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-purple); }
.s6b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s6b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s6b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s6b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s6b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s6b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s6b .kb-gray, :root[data-theme="dark"] .s6b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s6b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s6b .kh-gray{ fill:#B4B2A9; }
.s6b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s6b-gray); }
.s6b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6b-gray); }
.s6b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s6b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s6b">
<text x="170" y="18" text-anchor="middle" class="kh-gray">pattern</text>
<rect x="20" y="30" width="120" height="86" rx="3" class="k-gray"/>
<text x="80.0" y="50" text-anchor="middle" class="kb-gray">Context</text>
<line x1="20" y1="60" x2="140" y2="60" class="ln-gray"/>
<text x="28" y="78" text-anchor="start" class="km-gray">- strategy</text>
<line x1="20" y1="88" x2="140" y2="88" class="ln-gray"/>
<text x="28" y="106" text-anchor="start" class="km-gray">+ do()</text>
<rect x="190" y="30" width="140" height="86" rx="3" class="k-gray"/>
<text x="260.0" y="50" text-anchor="middle" class="ks-gray">«interface»</text>
<text x="260.0" y="68" text-anchor="middle" class="kb-gray">Strategy</text>
<line x1="190" y1="78" x2="330" y2="78" class="ln-gray"/>
<line x1="190" y1="88" x2="330" y2="88" class="ln-gray"/>
<text x="198" y="106" text-anchor="start" class="km-gray">+ execute()</text>
<line x1="142" y1="70" x2="188" y2="70" class="assoc"/>
<rect x="170" y="170" width="80" height="36" rx="3" class="k-gray"/>
<text x="210.0" y="192.5" text-anchor="middle" class="ks-gray">ConcreteA</text>
<rect x="270" y="170" width="80" height="36" rx="3" class="k-gray"/>
<text x="310.0" y="192.5" text-anchor="middle" class="ks-gray">ConcreteB</text>
<line x1="210" y1="168" x2="245" y2="118" class="real"/>
<line x1="310" y1="168" x2="275" y2="118" class="real"/>
<text x="540" y="18" text-anchor="middle" class="kh-teal">NetWarden</text>
<rect x="390" y="30" width="130" height="86" rx="3" class="k-teal"/>
<text x="455.0" y="50" text-anchor="middle" class="kb-teal">Assessment</text>
<line x1="390" y1="60" x2="520" y2="60" class="ln-teal"/>
<text x="398" y="78" text-anchor="start" class="km-teal">- checks</text>
<line x1="390" y1="88" x2="520" y2="88" class="ln-teal"/>
<text x="398" y="106" text-anchor="start" class="km-teal">+ run()</text>
<rect x="560" y="30" width="140" height="86" rx="3" class="k-purple"/>
<text x="630.0" y="50" text-anchor="middle" class="ks-purple">«interface»</text>
<text x="630.0" y="68" text-anchor="middle" class="kb-purple">Check</text>
<line x1="560" y1="78" x2="700" y2="78" class="ln-purple"/>
<line x1="560" y1="88" x2="700" y2="88" class="ln-purple"/>
<text x="568" y="106" text-anchor="start" class="km-purple">+ run(host, svc)</text>
<line x1="522" y1="70" x2="558" y2="70" class="assoc"/>
<text x="548" y="62" text-anchor="middle" class="c">*</text>
<rect x="400" y="170" width="94" height="36" rx="3" class="k-blue"/>
<text x="447.0" y="192.5" text-anchor="middle" class="ks-blue">Cleartext</text>
<line x1="447" y1="168" x2="630" y2="118" class="real"/>
<rect x="502" y="170" width="94" height="36" rx="3" class="k-blue"/>
<text x="549.0" y="192.5" text-anchor="middle" class="ks-blue">ExposedDb</text>
<line x1="549" y1="168" x2="630" y2="118" class="real"/>
<rect x="604" y="170" width="94" height="36" rx="3" class="k-blue"/>
<text x="651.0" y="192.5" text-anchor="middle" class="ks-blue">KnownVuln</text>
<line x1="651" y1="168" x2="630" y2="118" class="real"/>
<text x="360" y="250" text-anchor="middle" class="c">vary an algorithm independently of the code that uses it; swap or add strategies without touching the context</text>
</g>
</svg>
<figcaption>Strategy turns "which algorithm?" from an if/elif chain into a choice of object.</figcaption>
</figure>

NetWarden's checks are strategies. Without the pattern, the engine would contain a growing `if service.name == "telnet": ... elif service.port == 3306: ...` chain. With it, the engine runs whatever checks it was given:

```python
for service in host.services:
    for check in self.checks:
        for finding in check.run(host, service):
            result.findings.append(finding)
```

In Python, a strategy does not even need a class: any function with the right signature works. A class is useful when the strategy has configuration or state, like `KnownVulnerabilityCheck`, which holds a knowledge base.

**Consequences:** new behaviour without changing the context (open/closed principle); each strategy is small and testable on its own. The cost is more classes, and the client must choose which strategies to use, here in `default_checks()`.

## Observer

**Problem:** several parts of a program need to react when something happens, but the part where it happens should not depend on all of them.

**Solution:** the **subject** keeps a list of **observers** and notifies them; observers subscribe and unsubscribe themselves.

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The observer pattern in NetWarden. The EventBus keeps a list of handlers per event type. The cli subscribes progress printers; tests subscribe a spy. When Assessment publishes FindingRaised, the bus calls every subscribed handler in turn. Assessment does not know who is listening." xmlns="http://www.w3.org/2000/svg">
<style>
.s6c{ font-family:var(--sans),sans-serif; }
.s6c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6c .s{ fill:var(--text-dim); font-size:13px; }
.s6c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .c{ fill:var(--text-faint); font-size:12.5px; }
.s6c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6c-a); }
.s6c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6c-a); marker-start:url(#s6c-s); }
.s6c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6c-g); }
.s6c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-a); }
.s6c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6c-tri); }
.s6c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-tri); }
.s6c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6c-open); }
.s6c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-open); }
.s6c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6c-dia); }
.s6c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6c-odia); }
.s6c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6c-dia); marker-end:url(#s6c-open); }
.s6c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6c-solid); }
.s6c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6c-open); }
.s6c .fill{ fill:var(--text); stroke:none; }
.s6c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6c .ks-blue{ fill:#185FA5; font-size:13px; }
.s6c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6c .kb-blue, :root[data-theme="dark"] .s6c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6c .kh-blue{ fill:#85B7EB; }
.s6c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6c-blue); }
.s6c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-blue); }
.s6c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6c .kb-teal, :root[data-theme="dark"] .s6c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6c .kh-teal{ fill:#5DCAA5; }
.s6c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6c-teal); }
.s6c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-teal); }
.s6c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s6c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s6c .ks-amber{ fill:#854F0B; font-size:13px; }
.s6c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s6c .kb-amber, :root[data-theme="dark"] .s6c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s6c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s6c .kh-amber{ fill:#EF9F27; }
.s6c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s6c-amber); }
.s6c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-amber); }
.s6c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s6c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6c .ks-purple{ fill:#534AB7; font-size:13px; }
.s6c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6c .kb-purple, :root[data-theme="dark"] .s6c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6c .kh-purple{ fill:#AFA9EC; }
.s6c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6c-purple); }
.s6c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-purple); }
.s6c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s6c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s6c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s6c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s6c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s6c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s6c .kb-gray, :root[data-theme="dark"] .s6c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s6c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s6c .kh-gray{ fill:#B4B2A9; }
.s6c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s6c-gray); }
.s6c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6c-gray); }
.s6c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s6c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s6c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s6c">
<rect x="20" y="30" width="220" height="104" rx="3" class="k-amber"/>
<text x="130.0" y="50" text-anchor="middle" class="kb-amber">EventBus</text>
<line x1="20" y1="60" x2="240" y2="60" class="ln-amber"/>
<text x="28" y="78" text-anchor="start" class="km-amber">- handlers: dict</text>
<line x1="20" y1="88" x2="240" y2="88" class="ln-amber"/>
<text x="28" y="106" text-anchor="start" class="km-amber">+ subscribe(type, handler)</text>
<text x="28" y="124" text-anchor="start" class="km-amber">+ publish(event)</text>
<rect x="20" y="200" width="200" height="44" rx="7" class="k-teal"/>
<text x="120.0" y="217.5" text-anchor="middle" class="kb-teal">Assessment</text>
<text x="120.0" y="235.5" text-anchor="middle" class="ks-teal">publishes events</text>
<line x1="120" y1="198" x2="120" y2="140" class="dep"/>
<text x="128" y="176" text-anchor="start" class="c">publish(FindingRaised)</text>
<rect x="460" y="20" width="240" height="64" rx="7" class="k-gray"/>
<text x="580.0" y="47.5" text-anchor="middle" class="kb-gray">progress printer (cli)</text>
<text x="580.0" y="65.5" text-anchor="middle" class="ks-gray">prints to stderr</text>
<line x1="242" y1="90" x2="458" y2="52" class="ad-amber"/>
<rect x="460" y="106" width="240" height="64" rx="7" class="k-purple"/>
<text x="580.0" y="133.5" text-anchor="middle" class="kb-purple">test spy (Mock)</text>
<text x="580.0" y="151.5" text-anchor="middle" class="ks-purple">records calls</text>
<line x1="242" y1="90" x2="458" y2="138" class="ad-amber"/>
<rect x="460" y="192" width="240" height="64" rx="7" class="k-blue"/>
<text x="580.0" y="219.5" text-anchor="middle" class="kb-blue">future: web dashboard</text>
<text x="580.0" y="237.5" text-anchor="middle" class="ks-blue">pushes to browsers</text>
<line x1="242" y1="90" x2="458" y2="224" class="ad-amber"/>
<text x="330" y="40" text-anchor="middle" class="kh-amber">notify</text>
</g>
</svg>
<figcaption>Subjects announce; observers decide what to do. Adding an observer never changes the subject.</figcaption>
</figure>

```python
class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[type, list[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(self, event_type: type[E], handler: Callable[[E], None]) -> None:
        self._handlers[event_type].append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._handlers[type(event)]:
            handler(event)
```

The engine publishes `ScanStarted`, `HostFound`, `FindingRaised` and `ScanFinished`. The command-line interface subscribes functions that print progress to standard error, keeping standard output clean for the report. A test subscribes a `Mock` and checks which events arrived. A future web dashboard could subscribe and push findings to browsers as they are found, without any change to the engine. GUI frameworks, JavaScript event listeners, and message brokers (Chapter 7) are all observers at different scales.

**Consequences:** loose coupling between the source of events and their consumers. The cost is that control flow becomes harder to follow, because nothing in the publisher says who will run.

## Factory

**Problem:** code needs an object but should not hard-code which class to create.

<figure class="diagram">
<svg viewBox="0 0 720 240" style="width:100%;height:auto;max-width:720px" role="img" aria-label="A simple factory in NetWarden. The cli asks get_reporter for the format named on the command line: md, json or html. The factory looks the name up in a registry and returns a MarkdownReporter, JsonReporter or HtmlReporter; an unknown name raises ValueError. The cli only sees the Reporter interface." xmlns="http://www.w3.org/2000/svg">
<style>
.s6d{ font-family:var(--sans),sans-serif; }
.s6d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6d .s{ fill:var(--text-dim); font-size:13px; }
.s6d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6d .c{ fill:var(--text-faint); font-size:12.5px; }
.s6d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6d-a); }
.s6d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6d-a); marker-start:url(#s6d-s); }
.s6d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6d-g); }
.s6d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-a); }
.s6d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6d-tri); }
.s6d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-tri); }
.s6d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6d-open); }
.s6d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-open); }
.s6d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6d-dia); }
.s6d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6d-odia); }
.s6d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6d-dia); marker-end:url(#s6d-open); }
.s6d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6d-solid); }
.s6d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6d-open); }
.s6d .fill{ fill:var(--text); stroke:none; }
.s6d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6d .ks-blue{ fill:#185FA5; font-size:13px; }
.s6d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6d .kb-blue, :root[data-theme="dark"] .s6d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6d .kh-blue{ fill:#85B7EB; }
.s6d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6d-blue); }
.s6d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-blue); }
.s6d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s6d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s6d .ks-amber{ fill:#854F0B; font-size:13px; }
.s6d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s6d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s6d .kb-amber, :root[data-theme="dark"] .s6d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s6d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s6d .kh-amber{ fill:#EF9F27; }
.s6d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s6d-amber); }
.s6d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-amber); }
.s6d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s6d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s6d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s6d .ks-red{ fill:#A32D2D; font-size:13px; }
.s6d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s6d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s6d .kb-red, :root[data-theme="dark"] .s6d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s6d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s6d .kh-red{ fill:#F09595; }
.s6d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s6d-red); }
.s6d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-red); }
.s6d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s6d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s6d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s6d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s6d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s6d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s6d .kb-gray, :root[data-theme="dark"] .s6d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s6d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s6d .kh-gray{ fill:#B4B2A9; }
.s6d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s6d-gray); }
.s6d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6d-gray); }
.s6d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s6d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s6d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s6d">
<rect x="20" y="90" width="120" height="50" rx="7" class="k-gray"/>
<text x="80.0" y="110.5" text-anchor="middle" class="kb-gray">cli</text>
<text x="80.0" y="128.5" text-anchor="middle" class="km-gray">--format html</text>
<rect x="200" y="80" width="180" height="70" rx="7" class="k-amber"/>
<text x="290.0" y="110.5" text-anchor="middle" class="km-amber">get_reporter(fmt)</text>
<text x="290.0" y="128.5" text-anchor="middle" class="ks-amber">REPORTERS registry</text>
<line x1="142" y1="115" x2="198" y2="115" class="ar"/>
<rect x="470" y="20" width="180" height="44" rx="3" class="k-blue"/>
<text x="560.0" y="46.5" text-anchor="middle" class="kb-blue">MarkdownReporter</text>
<line x1="382" y1="115" x2="468" y2="42" class="ad"/>
<rect x="470" y="80" width="180" height="44" rx="3" class="k-blue"/>
<text x="560.0" y="106.5" text-anchor="middle" class="kb-blue">JsonReporter</text>
<line x1="382" y1="115" x2="468" y2="102" class="ad"/>
<rect x="470" y="140" width="180" height="44" rx="3" class="k-blue"/>
<text x="560.0" y="166.5" text-anchor="middle" class="kb-blue">HtmlReporter</text>
<line x1="382" y1="115" x2="468" y2="162" class="ad"/>
<rect x="470" y="200" width="180" height="34" rx="3" class="k-red"/>
<text x="560.0" y="221.5" text-anchor="middle" class="km-red">ValueError</text>
<line x1="382" y1="130" x2="468" y2="214" class="ad-red"/>
<text x="200" y="186" text-anchor="start" class="c">creation logic in one place</text>
</g>
</svg>
<figcaption>Callers ask for what they need by name; the factory decides which class to create.</figcaption>
</figure>

```python
REPORTERS: dict[str, type[Reporter]] = {"md": MarkdownReporter, "json": JsonReporter, "html": HtmlReporter}

def get_reporter(fmt: str) -> Reporter:
    try:
        return REPORTERS[fmt]()
    except KeyError:
        raise ValueError(f"Unknown report format {fmt!r}; choose from {', '.join(REPORTERS)}") from None
```

This is a **simple factory**, a function that chooses a class. The GoF **factory method** is a related pattern in which a subclass overrides a creation method. In Python, classes are objects, so a dictionary from names to classes is often all a factory needs. The same dictionary also feeds `argparse`, which lists the valid choices in `--help`: one source of truth (DRY).

## Adapter

**Problem:** you want to use a class whose interface does not match what your code expects.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The adapter pattern, planned for user story US-10. The Check code expects a KnowledgeSource with a lookup method. The OSV vulnerability service has a different, HTTP and JSON interface. An OsvAdapter implements lookup by calling the OSV API and converting its records into Vulnerability objects." xmlns="http://www.w3.org/2000/svg">
<style>
.s6e{ font-family:var(--sans),sans-serif; }
.s6e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6e .s{ fill:var(--text-dim); font-size:13px; }
.s6e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .c{ fill:var(--text-faint); font-size:12.5px; }
.s6e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6e-a); }
.s6e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6e-a); marker-start:url(#s6e-s); }
.s6e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6e-g); }
.s6e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-a); }
.s6e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6e-tri); }
.s6e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-tri); }
.s6e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6e-open); }
.s6e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-open); }
.s6e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6e-dia); }
.s6e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6e-odia); }
.s6e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6e-dia); marker-end:url(#s6e-open); }
.s6e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6e-solid); }
.s6e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6e-open); }
.s6e .fill{ fill:var(--text); stroke:none; }
.s6e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6e .ks-blue{ fill:#185FA5; font-size:13px; }
.s6e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6e .kb-blue, :root[data-theme="dark"] .s6e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6e .kh-blue{ fill:#85B7EB; }
.s6e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6e-blue); }
.s6e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-blue); }
.s6e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6e .kb-teal, :root[data-theme="dark"] .s6e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6e .kh-teal{ fill:#5DCAA5; }
.s6e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6e-teal); }
.s6e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-teal); }
.s6e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6e .ks-purple{ fill:#534AB7; font-size:13px; }
.s6e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6e .kb-purple, :root[data-theme="dark"] .s6e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6e .kh-purple{ fill:#AFA9EC; }
.s6e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6e-purple); }
.s6e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-purple); }
.s6e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s6e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s6e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s6e .ks-green{ fill:#3B6D11; font-size:13px; }
.s6e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s6e .kb-green, :root[data-theme="dark"] .s6e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s6e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s6e .kh-green{ fill:#97C459; }
.s6e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s6e-green); }
.s6e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-green); }
.s6e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s6e .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s6e .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s6e .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s6e .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s6e .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6e .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s6e .kb-gray, :root[data-theme="dark"] .s6e .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s6e .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s6e .kh-gray{ fill:#B4B2A9; }
.s6e .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s6e-gray); }
.s6e .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6e-gray); }
.s6e .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s6e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s6e-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s6e">
<rect x="20" y="40" width="170" height="86" rx="3" class="k-blue"/>
<text x="105.0" y="60" text-anchor="middle" class="kb-blue">KnownVulnCheck</text>
<line x1="20" y1="70" x2="190" y2="70" class="ln-blue"/>
<text x="28" y="88" text-anchor="start" class="km-blue">- kb</text>
<line x1="20" y1="98" x2="190" y2="98" class="ln-blue"/>
<text x="28" y="116" text-anchor="start" class="km-blue">+ run()</text>
<rect x="250" y="30" width="190" height="86" rx="3" class="k-purple"/>
<text x="345.0" y="50" text-anchor="middle" class="ks-purple">«interface»</text>
<text x="345.0" y="68" text-anchor="middle" class="kb-purple">KnowledgeSource</text>
<line x1="250" y1="78" x2="440" y2="78" class="ln-purple"/>
<line x1="250" y1="88" x2="440" y2="88" class="ln-purple"/>
<text x="258" y="106" text-anchor="start" class="km-purple">+ lookup(prod, ver)</text>
<line x1="192" y1="80" x2="248" y2="80" class="assoc"/>
<rect x="250" y="170" width="190" height="50" rx="3" class="k-green"/>
<text x="345.0" y="190.5" text-anchor="middle" class="kb-green">OsvAdapter</text>
<text x="345.0" y="208.5" text-anchor="middle" class="ks-green">lookup() calls OSV</text>
<line x1="345" y1="168" x2="345" y2="118" class="real"/>
<rect x="510" y="165" width="190" height="60" rx="7" class="k-gray"/>
<text x="605.0" y="190.5" text-anchor="middle" class="kb-gray">OSV API</text>
<text x="605.0" y="208.5" text-anchor="middle" class="km-gray">POST /v1/query  (JSON)</text>
<line x1="442" y1="195" x2="508" y2="195" class="ar"/>
<text x="475" y="188" text-anchor="middle" class="c">adapts</text>
<rect x="510" y="40" width="190" height="50" rx="3" class="k-teal"/>
<text x="605.0" y="60.5" text-anchor="middle" class="kb-teal">bundled JSON</text>
<text x="605.0" y="78.5" text-anchor="middle" class="ks-teal">KnowledgeBase today</text>
<path d="M508 64 L442 64" class="real"/>
</g>
</svg>
<figcaption>An adapter converts one interface into the one the client expects, so neither side has to change.</figcaption>
</figure>

NetWarden's backlog has US-10, "load an up-to-date vulnerability feed". The OSV.dev service exposes vulnerabilities through an HTTP API with its own JSON format. An **adapter** implements NetWarden's `lookup(product, version)` by calling the API and converting the results into `Vulnerability` objects. The checks never learn that the data came from the internet. ADR-0002 anticipated this: the bundled knowledge base was hidden behind an interface precisely so that an adapter could replace it later.

## Decorator

**Problem:** you want to add responsibilities to individual objects, such as logging, timing, caching or retries, without changing their classes or creating a subclass for every combination.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The decorator pattern. A TimedCheck wraps any Check, implements the same interface, and adds behaviour: it measures how long the wrapped check&#x27;s run takes and records it. Decorators can be stacked, for example a CachingCheck around a TimedCheck around a KnownVulnerabilityCheck." xmlns="http://www.w3.org/2000/svg">
<style>
.s6f{ font-family:var(--sans),sans-serif; }
.s6f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6f .s{ fill:var(--text-dim); font-size:13px; }
.s6f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6f .c{ fill:var(--text-faint); font-size:12.5px; }
.s6f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6f-a); }
.s6f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6f-a); marker-start:url(#s6f-s); }
.s6f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6f-g); }
.s6f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6f-a); }
.s6f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6f-tri); }
.s6f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6f-tri); }
.s6f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6f-open); }
.s6f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6f-open); }
.s6f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6f-dia); }
.s6f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6f-odia); }
.s6f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6f-dia); marker-end:url(#s6f-open); }
.s6f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6f-solid); }
.s6f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6f-open); }
.s6f .fill{ fill:var(--text); stroke:none; }
.s6f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6f .ks-blue{ fill:#185FA5; font-size:13px; }
.s6f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6f .kb-blue, :root[data-theme="dark"] .s6f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6f .kh-blue{ fill:#85B7EB; }
.s6f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6f-blue); }
.s6f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6f-blue); }
.s6f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s6f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s6f .ks-amber{ fill:#854F0B; font-size:13px; }
.s6f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s6f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s6f .kb-amber, :root[data-theme="dark"] .s6f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s6f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s6f .kh-amber{ fill:#EF9F27; }
.s6f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s6f-amber); }
.s6f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6f-amber); }
.s6f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s6f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6f .ks-purple{ fill:#534AB7; font-size:13px; }
.s6f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6f .kb-purple, :root[data-theme="dark"] .s6f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6f .kh-purple{ fill:#AFA9EC; }
.s6f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6f-purple); }
.s6f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6f-purple); }
.s6f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s6f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s6f">
<rect x="250" y="16" width="200" height="86" rx="3" class="k-purple"/>
<text x="350.0" y="36" text-anchor="middle" class="ks-purple">«interface»</text>
<text x="350.0" y="54" text-anchor="middle" class="kb-purple">Check</text>
<line x1="250" y1="64" x2="450" y2="64" class="ln-purple"/>
<line x1="250" y1="74" x2="450" y2="74" class="ln-purple"/>
<text x="258" y="92" text-anchor="start" class="km-purple">+ run(host, svc)</text>
<rect x="60" y="170" width="200" height="54" rx="3" class="k-blue"/>
<text x="160.0" y="192.5" text-anchor="middle" class="kb-blue">KnownVulnerability</text>
<text x="160.0" y="210.5" text-anchor="middle" class="kb-blue">Check</text>
<rect x="440" y="170" width="220" height="54" rx="3" class="k-amber"/>
<text x="550.0" y="192.5" text-anchor="middle" class="kb-amber">TimedCheck</text>
<text x="550.0" y="210.5" text-anchor="middle" class="km-amber">- inner: Check</text>
<line x1="160" y1="168" x2="330" y2="118" class="real"/>
<line x1="550" y1="168" x2="370" y2="118" class="real"/>
<path d="M560 168 C 560 130, 520 110, 452 90" class="assoc"/>
<text x="560" y="130" text-anchor="start" class="c">wraps</text>
<text x="360" y="248" text-anchor="middle" class="m">start = now(); result = inner.run(...); record(now() - start); return result</text>
</g>
</svg>
<figcaption>Same interface in, same interface out, plus one extra responsibility, added without editing the original class.</figcaption>
</figure>

```python
class TimedCheck:
    """Decorator: same interface as the check it wraps, plus timing."""
    def __init__(self, inner: Check, timings: dict[str, float]):
        self.inner, self.timings, self.id = inner, timings, inner.id

    def run(self, host: Host, service: Service) -> list[Finding]:
        start = time.perf_counter()
        try:
            return self.inner.run(host, service)
        finally:
            self.timings[self.id] = self.timings.get(self.id, 0.0) + time.perf_counter() - start
```

Wrapping every check is one line: `checks = [TimedCheck(c, timings) for c in default_checks(kb)]`. Python's `@decorator` syntax for functions is the same idea applied to functions: `functools.lru_cache` decorates a function with caching.

## Facade

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Assessment as a facade. Clients call one method, run, instead of coordinating Scope, TcpScanner, Fingerprinter, the checks and the EventBus themselves. The subsystem classes remain available for tests and advanced uses." xmlns="http://www.w3.org/2000/svg">
<style>
.s6h{ font-family:var(--sans),sans-serif; }
.s6h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6h .s{ fill:var(--text-dim); font-size:13px; }
.s6h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .c{ fill:var(--text-faint); font-size:12.5px; }
.s6h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6h-a); }
.s6h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6h-a); marker-start:url(#s6h-s); }
.s6h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6h-g); }
.s6h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-a); }
.s6h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6h-tri); }
.s6h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-tri); }
.s6h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6h-open); }
.s6h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-open); }
.s6h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6h-dia); }
.s6h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6h-odia); }
.s6h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6h-dia); marker-end:url(#s6h-open); }
.s6h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6h-solid); }
.s6h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6h-open); }
.s6h .fill{ fill:var(--text); stroke:none; }
.s6h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6h .ks-blue{ fill:#185FA5; font-size:13px; }
.s6h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6h .kb-blue, :root[data-theme="dark"] .s6h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6h .kh-blue{ fill:#85B7EB; }
.s6h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6h-blue); }
.s6h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-blue); }
.s6h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6h .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6h .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6h .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6h .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6h .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6h .kb-teal, :root[data-theme="dark"] .s6h .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6h .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6h .kh-teal{ fill:#5DCAA5; }
.s6h .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6h-teal); }
.s6h .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-teal); }
.s6h .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6h .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s6h .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s6h .ks-amber{ fill:#854F0B; font-size:13px; }
.s6h .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6h .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s6h .kb-amber, :root[data-theme="dark"] .s6h .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s6h .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s6h .kh-amber{ fill:#EF9F27; }
.s6h .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s6h-amber); }
.s6h .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-amber); }
.s6h .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s6h .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6h .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6h .ks-purple{ fill:#534AB7; font-size:13px; }
.s6h .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6h .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6h .kb-purple, :root[data-theme="dark"] .s6h .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6h .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6h .kh-purple{ fill:#AFA9EC; }
.s6h .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6h-purple); }
.s6h .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-purple); }
.s6h .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s6h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s6h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s6h .ks-red{ fill:#A32D2D; font-size:13px; }
.s6h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s6h .kb-red, :root[data-theme="dark"] .s6h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s6h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s6h .kh-red{ fill:#F09595; }
.s6h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s6h-red); }
.s6h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-red); }
.s6h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s6h .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s6h .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s6h .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s6h .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s6h .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6h .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s6h .kb-gray, :root[data-theme="dark"] .s6h .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s6h .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s6h .kh-gray{ fill:#B4B2A9; }
.s6h .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s6h-gray); }
.s6h .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6h-gray); }
.s6h .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6h-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6h-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s6h-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s6h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s6h-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s6h">
<rect x="20" y="100" width="140" height="50" rx="7" class="k-gray"/>
<text x="90.0" y="129.5" text-anchor="middle" class="kb-gray">cli, CI script</text>
<rect x="220" y="90" width="180" height="70" rx="7" class="k-teal"/>
<text x="310.0" y="120.5" text-anchor="middle" class="kb-teal">Assessment</text>
<text x="310.0" y="138.5" text-anchor="middle" class="km-teal">run(targets, ports)</text>
<line x1="162" y1="125" x2="218" y2="125" class="ar"/>
<rect x="440" y="10" width="260" height="240" rx="8" class="zone"/>
<text x="570" y="30" text-anchor="middle" class="c">subsystem</text>
<rect x="470" y="40" width="200" height="34" rx="4" class="k-red"/>
<text x="570.0" y="61.5" text-anchor="middle" class="kb-red">Scope</text>
<line x1="402" y1="125" x2="468" y2="57" class="u"/>
<rect x="470" y="82" width="200" height="34" rx="4" class="k-blue"/>
<text x="570.0" y="103.5" text-anchor="middle" class="kb-blue">TcpScanner</text>
<line x1="402" y1="125" x2="468" y2="99" class="u"/>
<rect x="470" y="124" width="200" height="34" rx="4" class="k-purple"/>
<text x="570.0" y="145.5" text-anchor="middle" class="kb-purple">Fingerprinter</text>
<line x1="402" y1="125" x2="468" y2="141" class="u"/>
<rect x="470" y="166" width="200" height="34" rx="4" class="k-amber"/>
<text x="570.0" y="187.5" text-anchor="middle" class="kb-amber">checks</text>
<line x1="402" y1="125" x2="468" y2="183" class="u"/>
<rect x="470" y="208" width="200" height="34" rx="4" class="k-gray"/>
<text x="570.0" y="229.5" text-anchor="middle" class="kb-gray">EventBus</text>
<line x1="402" y1="125" x2="468" y2="225" class="u"/>
</g>
</svg>
<figcaption>A facade gives a simple entry point to a complex subsystem.</figcaption>
</figure>

A **facade** provides one simple interface to a complicated subsystem. `Assessment.run()` is NetWarden's facade: the command-line code, a CI script, or a future web service can run a complete assessment with one call. The facade does not hide the subsystem; tests still use `Scope` or `Fingerprinter` directly.

## Repository

The **repository** pattern comes from Martin Fowler's *Patterns of Enterprise Application Architecture* (2002) and Eric Evans's *Domain-Driven Design* (2003), rather than from the GoF.

<figure class="diagram">
<svg viewBox="0 0 720 240" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The repository pattern. The cli and the diff function work with ScanResult objects through ScanRepository methods: save, get and history. Only the repository knows about SQL and the SQLite file; a PostgreSQL repository could replace it without changing callers." xmlns="http://www.w3.org/2000/svg">
<style>
.s6g{ font-family:var(--sans),sans-serif; }
.s6g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6g .s{ fill:var(--text-dim); font-size:13px; }
.s6g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6g .c{ fill:var(--text-faint); font-size:12.5px; }
.s6g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6g-a); }
.s6g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6g-a); marker-start:url(#s6g-s); }
.s6g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6g-g); }
.s6g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6g-a); }
.s6g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6g-tri); }
.s6g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6g-tri); }
.s6g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6g-open); }
.s6g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6g-open); }
.s6g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6g-dia); }
.s6g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6g-odia); }
.s6g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6g-dia); marker-end:url(#s6g-open); }
.s6g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6g-solid); }
.s6g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6g-open); }
.s6g .fill{ fill:var(--text); stroke:none; }
.s6g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6g .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6g .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6g .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6g .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6g .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6g .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6g .kb-teal, :root[data-theme="dark"] .s6g .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6g .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6g .kh-teal{ fill:#5DCAA5; }
.s6g .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6g-teal); }
.s6g .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6g-teal); }
.s6g .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6g .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s6g .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s6g .ks-amber{ fill:#854F0B; font-size:13px; }
.s6g .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s6g .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6g .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s6g .kb-amber, :root[data-theme="dark"] .s6g .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s6g .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s6g .kh-amber{ fill:#EF9F27; }
.s6g .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s6g-amber); }
.s6g .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6g-amber); }
.s6g .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s6g .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6g .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6g .ks-purple{ fill:#534AB7; font-size:13px; }
.s6g .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6g .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6g .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6g .kb-purple, :root[data-theme="dark"] .s6g .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6g .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6g .kh-purple{ fill:#AFA9EC; }
.s6g .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6g-purple); }
.s6g .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6g-purple); }
.s6g .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6g-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6g-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s6g-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s6g">
<rect x="20" y="80" width="160" height="60" rx="7" class="k-teal"/>
<text x="100.0" y="105.5" text-anchor="middle" class="kb-teal">cli, diff()</text>
<text x="100.0" y="123.5" text-anchor="middle" class="ks-teal">domain objects</text>
<rect x="250" y="40" width="200" height="122" rx="3" class="k-amber"/>
<text x="350.0" y="60" text-anchor="middle" class="kb-amber">ScanRepository</text>
<line x1="250" y1="70" x2="450" y2="70" class="ln-amber"/>
<text x="258" y="88" text-anchor="start" class="km-amber">- db: Connection</text>
<line x1="250" y1="98" x2="450" y2="98" class="ln-amber"/>
<text x="258" y="116" text-anchor="start" class="km-amber">+ save(result): int</text>
<text x="258" y="134" text-anchor="start" class="km-amber">+ get(id): ScanResult</text>
<text x="258" y="152" text-anchor="start" class="km-amber">+ history()</text>
<line x1="182" y1="110" x2="248" y2="110" class="assoc"/>
<rect x="520" y="60" width="180" height="50" rx="7" class="k-purple"/>
<text x="610.0" y="80.5" text-anchor="middle" class="kb-purple">netwarden.db</text>
<text x="610.0" y="98.5" text-anchor="middle" class="ks-purple">SQLite</text>
<rect x="520" y="150" width="180" height="50" rx="7" class="pnl"/>
<text x="610.0" y="170.5" text-anchor="middle" class="b">PostgreSQL</text>
<text x="610.0" y="188.5" text-anchor="middle" class="c">future option</text>
<line x1="452" y1="90" x2="518" y2="85" class="ar"/>
<line x1="452" y1="120" x2="518" y2="175" class="ad"/>
<text x="360" y="226" text-anchor="middle" class="c">SQL lives in one file: store.py</text>
</g>
</svg>
<figcaption>A repository looks like an in-memory collection of domain objects and hides how they are stored.</figcaption>
</figure>

A repository makes stored objects look like a collection: `save`, `get`, `history`. All SQL lives in `store.py`, so the rest of NetWarden deals only with `ScanResult` and `Finding` objects. ADR-0003 records the consequence: if NetWarden becomes a shared service, a PostgreSQL repository can replace the SQLite one without changing its callers.

## Dependency injection

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Dependency injection. In production, the composition root in cli.py creates the real Scope, TcpScanner, Fingerprinter, checks and EventBus and passes them to Assessment. In tests, the same Assessment receives a FakeScanner and a spy instead. Assessment&#x27;s code is identical in both cases." xmlns="http://www.w3.org/2000/svg">
<style>
.s6i{ font-family:var(--sans),sans-serif; }
.s6i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6i .s{ fill:var(--text-dim); font-size:13px; }
.s6i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6i .c{ fill:var(--text-faint); font-size:12.5px; }
.s6i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6i-a); }
.s6i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6i-a); marker-start:url(#s6i-s); }
.s6i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6i-g); }
.s6i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6i-a); }
.s6i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6i-tri); }
.s6i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6i-tri); }
.s6i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6i-open); }
.s6i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6i-open); }
.s6i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6i-dia); }
.s6i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6i-odia); }
.s6i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6i-dia); marker-end:url(#s6i-open); }
.s6i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6i-solid); }
.s6i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6i-open); }
.s6i .fill{ fill:var(--text); stroke:none; }
.s6i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6i .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s6i .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s6i .ks-blue{ fill:#185FA5; font-size:13px; }
.s6i .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s6i .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6i .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s6i .kb-blue, :root[data-theme="dark"] .s6i .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s6i .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s6i .kh-blue{ fill:#85B7EB; }
.s6i .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s6i-blue); }
.s6i .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6i-blue); }
.s6i .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s6i .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s6i .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s6i .ks-teal{ fill:#0F6E56; font-size:13px; }
.s6i .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s6i .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6i .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s6i .kb-teal, :root[data-theme="dark"] .s6i .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s6i .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s6i .kh-teal{ fill:#5DCAA5; }
.s6i .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s6i-teal); }
.s6i .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6i-teal); }
.s6i .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s6i .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s6i .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s6i .ks-purple{ fill:#534AB7; font-size:13px; }
.s6i .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s6i .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6i .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s6i .kb-purple, :root[data-theme="dark"] .s6i .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s6i .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s6i .kh-purple{ fill:#AFA9EC; }
.s6i .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s6i-purple); }
.s6i .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6i-purple); }
.s6i .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6i-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s6i-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s6i-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker></defs>
<g class="s6i">
<text x="180" y="18" text-anchor="middle" class="kh-teal">production: cli.py builds the graph</text>
<rect x="110" y="30" width="140" height="40" rx="7" class="k-teal"/>
<text x="180.0" y="54.5" text-anchor="middle" class="kb-teal">Assessment</text>
<rect x="16" y="120" width="84" height="34" rx="3" class="k-blue"/>
<text x="58.0" y="141.5" text-anchor="middle" class="ks-blue">Scope</text>
<line x1="60" y1="118" x2="180" y2="72" class="ar"/>
<rect x="102" y="120" width="84" height="34" rx="3" class="k-blue"/>
<text x="144.0" y="141.5" text-anchor="middle" class="ks-blue">TcpScanner</text>
<line x1="145" y1="118" x2="180" y2="72" class="ar"/>
<rect x="188" y="120" width="84" height="34" rx="3" class="k-blue"/>
<text x="230.0" y="141.5" text-anchor="middle" class="ks-blue">checks</text>
<line x1="230" y1="118" x2="180" y2="72" class="ar"/>
<rect x="274" y="120" width="84" height="34" rx="3" class="k-blue"/>
<text x="316.0" y="141.5" text-anchor="middle" class="ks-blue">EventBus</text>
<line x1="315" y1="118" x2="180" y2="72" class="ar"/>
<text x="540" y="18" text-anchor="middle" class="kh-purple">tests: inject doubles</text>
<rect x="470" y="30" width="140" height="40" rx="7" class="k-teal"/>
<text x="540.0" y="54.5" text-anchor="middle" class="kb-teal">Assessment</text>
<rect x="364" y="120" width="88" height="34" rx="3" class="k-blue"/>
<text x="408.0" y="141.5" text-anchor="middle" class="ks-blue">Scope</text>
<line x1="408" y1="118" x2="540" y2="72" class="ar"/>
<rect x="453" y="120" width="88" height="34" rx="3" class="k-purple"/>
<text x="497.0" y="141.5" text-anchor="middle" class="ks-purple">FakeScanner</text>
<line x1="497" y1="118" x2="540" y2="72" class="ar"/>
<rect x="542" y="120" width="88" height="34" rx="3" class="k-blue"/>
<text x="586.0" y="141.5" text-anchor="middle" class="ks-blue">2 checks</text>
<line x1="586" y1="118" x2="540" y2="72" class="ar"/>
<rect x="631" y="120" width="88" height="34" rx="3" class="k-purple"/>
<text x="675.0" y="141.5" text-anchor="middle" class="ks-purple">spy bus</text>
<line x1="675" y1="118" x2="540" y2="72" class="ar"/>
<rect x="20" y="190" width="680" height="60" rx="7" class="pnl"/>
<text x="360.0" y="214.5" text-anchor="middle" class="m">Assessment(scope, scanner, fingerprinter, checks, bus)</text>
<text x="360.0" y="234.5" text-anchor="middle" class="c">the class asks for what it needs; it never constructs its own collaborators</text>
</g>
</svg>
<figcaption>Dependencies are passed in, not created inside. That single habit is what makes the engine testable.</figcaption>
</figure>

**Dependency injection** is less a pattern than a habit: objects receive their collaborators instead of creating them. The place where concrete objects are created and wired together is the **composition root**; in NetWarden it is `cmd_scan` in `cli.py`:

```python
scope = Scope.from_file(args.scope)
bus = EventBus()
progress(bus)
kb = KnowledgeBase.load()
assessment = Assessment(scope, TcpScanner(timeout=args.timeout), Fingerprinter(), default_checks(kb), bus)
```

Large frameworks provide DI containers that build such graphs automatically. For a program of NetWarden's size, plain constructor arguments are clearer.

## Other patterns you will meet

| Pattern | Idea | Where you have seen it |
|---|---|---|
| **Iterator** | Traverse a collection without exposing its structure | Every Python `for` loop; generators |
| **Template method** | A base class fixes the steps; subclasses fill some in | `unittest.TestCase` calls your `setUp`, test, `tearDown` |
| **Command** | Wrap a request as an object | `argparse` subcommands; undo stacks in editors |
| **Composite** | Treat a group of objects like one | File systems; UI widget trees |
| **Proxy** | A stand-in that controls access to another object | Lazy loading; `unittest.mock` objects |
| **Singleton** | Exactly one instance, globally accessible | Python modules are effectively singletons; prefer injection |

## Anti-patterns and pattern misuse

<figure class="diagram">
<svg viewBox="0 0 720 240" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Common anti-patterns: the god object that knows and does everything; spaghetti code with tangled control flow; copy and paste programming; the golden hammer, using one familiar tool for every problem; magic numbers and strings; and premature optimisation." xmlns="http://www.w3.org/2000/svg">
<style>
.s6j{ font-family:var(--sans),sans-serif; }
.s6j .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s6j .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s6j .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s6j .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s6j .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s6j .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s6j .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s6j .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s6j .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s6j .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s6j .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s6j .s{ fill:var(--text-dim); font-size:13px; }
.s6j .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s6j .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s6j .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s6j .c{ fill:var(--text-faint); font-size:12.5px; }
.s6j .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s6j .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s6j .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s6j .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6j-a); }
.s6j .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s6j-a); marker-start:url(#s6j-s); }
.s6j .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s6j-g); }
.s6j .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s6j-a); }
.s6j .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s6j .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s6j .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s6j .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s6j .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s6j .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6j-tri); }
.s6j .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6j-tri); }
.s6j .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6j-open); }
.s6j .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s6j-open); }
.s6j .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6j-dia); }
.s6j .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6j-odia); }
.s6j .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s6j-dia); marker-end:url(#s6j-open); }
.s6j .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s6j-solid); }
.s6j .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s6j-open); }
.s6j .fill{ fill:var(--text); stroke:none; }
.s6j .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s6j .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s6j .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s6j .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s6j .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s6j .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s6j .ks-red{ fill:#A32D2D; font-size:13px; }
.s6j .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s6j .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s6j .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s6j .kb-red, :root[data-theme="dark"] .s6j .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s6j .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s6j .kh-red{ fill:#F09595; }
.s6j .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s6j-red); }
.s6j .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s6j-red); }
.s6j .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s6j-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s6j-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s6j-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s6j-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s6j-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s6j-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s6j-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s6j-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s6j-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s6j">
<rect x="20" y="20" width="218" height="84" rx="7" class="k-red"/>
<text x="129.0" y="57.5" text-anchor="middle" class="kb-red">god object</text>
<text x="129.0" y="75.5" text-anchor="middle" class="ks-red">one class does everything</text>
<rect x="250" y="20" width="218" height="84" rx="7" class="k-red"/>
<text x="359.0" y="57.5" text-anchor="middle" class="kb-red">spaghetti code</text>
<text x="359.0" y="75.5" text-anchor="middle" class="ks-red">tangled control flow</text>
<rect x="480" y="20" width="218" height="84" rx="7" class="k-red"/>
<text x="589.0" y="57.5" text-anchor="middle" class="kb-red">copy and paste</text>
<text x="589.0" y="75.5" text-anchor="middle" class="ks-red">fix a bug five times</text>
<rect x="20" y="124" width="218" height="84" rx="7" class="k-red"/>
<text x="129.0" y="161.5" text-anchor="middle" class="kb-red">golden hammer</text>
<text x="129.0" y="179.5" text-anchor="middle" class="ks-red">one tool for every job</text>
<rect x="250" y="124" width="218" height="84" rx="7" class="k-red"/>
<text x="359.0" y="161.5" text-anchor="middle" class="kb-red">magic numbers</text>
<text x="359.0" y="179.5" text-anchor="middle" class="ks-red">if port == 3306 ... why?</text>
<rect x="480" y="124" width="218" height="84" rx="7" class="k-red"/>
<text x="589.0" y="161.5" text-anchor="middle" class="kb-red">premature optimisation</text>
<text x="589.0" y="179.5" text-anchor="middle" class="ks-red">fast, wrong, unreadable</text>
</g>
</svg>
<figcaption>Anti-patterns are common solutions that look reasonable and cause more problems than they solve.</figcaption>
</figure>

Patterns are not goals. Applying them where the problem does not exist adds indirection without benefit; some call this "patternitis". Before introducing a pattern, name the force that makes it necessary: "we expect many checks" justified strategy in NetWarden; nothing justifies an abstract factory for its three reporters. Peter Norvig observed in 1996 that many GoF patterns are invisible or much simpler in dynamic languages, because functions and classes are first-class objects. Use the vocabulary freely, and the machinery sparingly.

## Hands on

1. Add `TimedCheck` to NetWarden, wrap the default checks in `cmd_scan`, and print the timings after a demo scan. Which check is slowest? Did you change any existing class?
2. Write a `CsvReporter` and register it in `REPORTERS`. Which files did you change, and did `--help` update itself?
3. Find the strategy, observer, factory, facade and repository in the code. For each, name the force that justified it.

## Summary

- A **pattern** is a named solution to a recurring problem in a context, with known consequences.
- The **Gang of Four** catalogued 23: **creational**, **structural**, **behavioural**.
- NetWarden uses **strategy** (checks, reporters), **observer** (event bus), **factory** (reporters), **facade** (Assessment), **repository** (scan history) and **dependency injection** (composition root in `cli.py`); **adapter** and **decorator** are its planned extensions.
- In Python, functions and classes are objects, so many patterns are lighter than in Java or C++.
- Use patterns to resolve real forces, not for their own sake; recognise **anti-patterns** such as the god object.
