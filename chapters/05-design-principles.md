# Chapter 5: Design Principles

Requirements say what to build; **design** decides how to structure it. A design is good if the software does what it should **and** stays easy to understand, test and change. This chapter collects the principles that experienced engineers use to judge designs. They are not laws; they are heuristics distilled from decades of systems that were, or were not, pleasant to change. Each one is illustrated with a decision in NetWarden.

## Abstraction

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Layers of abstraction behind one command. netwarden scan uses Assessment.run, which uses TcpScanner.scan, which uses asyncio.open_connection, which uses operating system sockets, which use TCP/IP on the network. Each level offers a simple interface and hides the complexity below it." xmlns="http://www.w3.org/2000/svg">
<style>
.s5a{ font-family:var(--sans),sans-serif; }
.s5a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5a .s{ fill:var(--text-dim); font-size:13px; }
.s5a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .c{ fill:var(--text-faint); font-size:12.5px; }
.s5a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5a-a); }
.s5a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5a-a); marker-start:url(#s5a-s); }
.s5a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5a-g); }
.s5a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-a); }
.s5a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5a-tri); }
.s5a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-tri); }
.s5a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5a-open); }
.s5a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-open); }
.s5a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5a-dia); }
.s5a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5a-odia); }
.s5a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5a-dia); marker-end:url(#s5a-open); }
.s5a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5a-solid); }
.s5a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5a-open); }
.s5a .fill{ fill:var(--text); stroke:none; }
.s5a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s5a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s5a .ks-blue{ fill:#185FA5; font-size:13px; }
.s5a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s5a .kb-blue, :root[data-theme="dark"] .s5a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s5a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s5a .kh-blue{ fill:#85B7EB; }
.s5a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s5a-blue); }
.s5a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-blue); }
.s5a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s5a .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s5a .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s5a .ks-teal{ fill:#0F6E56; font-size:13px; }
.s5a .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5a .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s5a .kb-teal, :root[data-theme="dark"] .s5a .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s5a .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s5a .kh-teal{ fill:#5DCAA5; }
.s5a .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s5a-teal); }
.s5a .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-teal); }
.s5a .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s5a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s5a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s5a .ks-amber{ fill:#854F0B; font-size:13px; }
.s5a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s5a .kb-amber, :root[data-theme="dark"] .s5a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s5a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s5a .kh-amber{ fill:#EF9F27; }
.s5a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s5a-amber); }
.s5a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-amber); }
.s5a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s5a .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s5a .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s5a .ks-coral{ fill:#993C1D; font-size:13px; }
.s5a .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5a .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s5a .kb-coral, :root[data-theme="dark"] .s5a .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s5a .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s5a .kh-coral{ fill:#F0997B; }
.s5a .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s5a-coral); }
.s5a .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-coral); }
.s5a .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s5a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s5a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s5a .ks-purple{ fill:#534AB7; font-size:13px; }
.s5a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s5a .kb-purple, :root[data-theme="dark"] .s5a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s5a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s5a .kh-purple{ fill:#AFA9EC; }
.s5a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s5a-purple); }
.s5a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-purple); }
.s5a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s5a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s5a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s5a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s5a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s5a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s5a .kb-gray, :root[data-theme="dark"] .s5a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s5a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s5a .kh-gray{ fill:#B4B2A9; }
.s5a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s5a-gray); }
.s5a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5a-gray); }
.s5a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s5a-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s5a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s5a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s5a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s5a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s5a">
<rect x="20" y="14" width="420" height="38" rx="5" class="k-coral"/>
<text x="230.0" y="37.5" text-anchor="middle" class="km-coral">netwarden scan 192.168.56.0/24</text>
<text x="470" y="38" text-anchor="start" class="s">what the user sees</text>
<rect x="34" y="60" width="392" height="38" rx="5" class="k-teal"/>
<text x="230.0" y="83.5" text-anchor="middle" class="km-teal">Assessment.run(targets, ports)</text>
<text x="470" y="84" text-anchor="start" class="s">the application</text>
<rect x="48" y="106" width="364" height="38" rx="5" class="k-blue"/>
<text x="230.0" y="129.5" text-anchor="middle" class="km-blue">TcpScanner.scan(addresses, ports)</text>
<text x="470" y="130" text-anchor="start" class="s">discovery</text>
<rect x="62" y="152" width="336" height="38" rx="5" class="k-purple"/>
<text x="230.0" y="175.5" text-anchor="middle" class="km-purple">asyncio.open_connection(host, port)</text>
<text x="470" y="176" text-anchor="start" class="s">Python standard library</text>
<rect x="76" y="198" width="308" height="38" rx="5" class="k-gray"/>
<text x="230.0" y="221.5" text-anchor="middle" class="km-gray">socket(), connect()</text>
<text x="470" y="222" text-anchor="start" class="s">operating system</text>
<rect x="90" y="244" width="280" height="38" rx="5" class="k-amber"/>
<text x="230.0" y="267.5" text-anchor="middle" class="km-amber">SYN, SYN-ACK, ACK</text>
<text x="470" y="268" text-anchor="start" class="s">TCP/IP on the wire</text>
<path d="M690 30 L690 270" class="ar"/>
<text x="680" y="150" text-anchor="end" class="c">more detail</text>
</g>
</svg>
<figcaption>Abstraction lets you think at one level at a time. Each interface is a promise about what the level below will do.</figcaption>
</figure>

**Abstraction** means working with the essential properties of something and ignoring the rest. When `Assessment` calls `scanner.scan(addresses, ports)`, it does not care about sockets, timeouts or TCP handshakes; it cares that it gets back a list of hosts with open services. Good abstractions have a clear purpose, a small interface, and a name that says what they do, not how.

Abstractions are layered. Each layer is built from the one below and offers something simpler to the one above. When a layer **leaks**, callers must know about the details it was meant to hide; Joel Spolsky's "law of leaky abstractions" observes that all non-trivial abstractions leak to some degree. A TCP connect scan, for example, is visible in the target's logs: the abstraction "find open ports" leaks a side effect that the README must mention.

## Modularity: coupling and cohesion

A **module** is any unit of design with an interface and a hidden implementation: a function, a class, a Python module, a package, a service. Two measures, introduced by Larry Constantine in the late 1960s, judge how well a system is divided into modules.

**Coupling** measures how much modules depend on each other.

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Coupling between modules. Tightly coupled: every module reaches into many others, so a change ripples everywhere. Loosely coupled: modules talk through a few narrow interfaces, so a change stays local." xmlns="http://www.w3.org/2000/svg">
<style>
.s5b{ font-family:var(--sans),sans-serif; }
.s5b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5b .s{ fill:var(--text-dim); font-size:13px; }
.s5b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5b .c{ fill:var(--text-faint); font-size:12.5px; }
.s5b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5b-a); }
.s5b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5b-a); marker-start:url(#s5b-s); }
.s5b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5b-g); }
.s5b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5b-a); }
.s5b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5b-tri); }
.s5b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5b-tri); }
.s5b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5b-open); }
.s5b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5b-open); }
.s5b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5b-dia); }
.s5b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5b-odia); }
.s5b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5b-dia); marker-end:url(#s5b-open); }
.s5b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5b-solid); }
.s5b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5b-open); }
.s5b .fill{ fill:var(--text); stroke:none; }
.s5b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5b .ks-green{ fill:#3B6D11; font-size:13px; }
.s5b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5b .kb-green, :root[data-theme="dark"] .s5b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5b .kh-green{ fill:#97C459; }
.s5b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5b-green); }
.s5b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5b-green); }
.s5b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5b .ks-red{ fill:#A32D2D; font-size:13px; }
.s5b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5b .kb-red, :root[data-theme="dark"] .s5b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5b .kh-red{ fill:#F09595; }
.s5b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5b-red); }
.s5b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5b-red); }
.s5b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s5b">
<line x1="180.0" y1="50.0" x2="257.9422863405995" y2="90.0" class="ln-red"/>
<line x1="180.0" y1="50.0" x2="257.9422863405995" y2="170.0" class="ln-red"/>
<line x1="180.0" y1="50.0" x2="180.0" y2="210.0" class="ln-red"/>
<line x1="180.0" y1="50.0" x2="102.05771365940053" y2="170.00000000000003" class="ln-red"/>
<line x1="180.0" y1="50.0" x2="102.05771365940052" y2="90.0" class="ln-red"/>
<line x1="257.9422863405995" y1="90.0" x2="257.9422863405995" y2="170.0" class="ln-red"/>
<line x1="257.9422863405995" y1="90.0" x2="180.0" y2="210.0" class="ln-red"/>
<line x1="257.9422863405995" y1="90.0" x2="102.05771365940053" y2="170.00000000000003" class="ln-red"/>
<line x1="257.9422863405995" y1="90.0" x2="102.05771365940052" y2="90.0" class="ln-red"/>
<line x1="257.9422863405995" y1="170.0" x2="180.0" y2="210.0" class="ln-red"/>
<line x1="257.9422863405995" y1="170.0" x2="102.05771365940053" y2="170.00000000000003" class="ln-red"/>
<line x1="257.9422863405995" y1="170.0" x2="102.05771365940052" y2="90.0" class="ln-red"/>
<line x1="180.0" y1="210.0" x2="102.05771365940053" y2="170.00000000000003" class="ln-red"/>
<line x1="180.0" y1="210.0" x2="102.05771365940052" y2="90.0" class="ln-red"/>
<line x1="102.05771365940053" y1="170.00000000000003" x2="102.05771365940052" y2="90.0" class="ln-red"/>
<circle cx="180" cy="50" r="18" class="k-red"/>
<circle cx="258" cy="90" r="18" class="k-red"/>
<circle cx="258" cy="170" r="18" class="k-red"/>
<circle cx="180" cy="210" r="18" class="k-red"/>
<circle cx="102" cy="170" r="18" class="k-red"/>
<circle cx="102" cy="90" r="18" class="k-red"/>
<text x="180" y="252" text-anchor="middle" class="kh-red">tight: 15 dependencies</text>
<line x1="540.0" y1="50.0" x2="617.9422863405995" y2="90.0" class="ln-green"/>
<line x1="617.9422863405995" y1="90.0" x2="617.9422863405995" y2="170.0" class="ln-green"/>
<line x1="540.0" y1="50.0" x2="540.0" y2="210.0" class="ln-green"/>
<line x1="540.0" y1="210.0" x2="462.0577136594005" y2="170.00000000000003" class="ln-green"/>
<line x1="462.0577136594005" y1="170.00000000000003" x2="462.0577136594005" y2="90.0" class="ln-green"/>
<circle cx="540" cy="50" r="18" class="k-green"/>
<circle cx="618" cy="90" r="18" class="k-green"/>
<circle cx="618" cy="170" r="18" class="k-green"/>
<circle cx="540" cy="210" r="18" class="k-green"/>
<circle cx="462" cy="170" r="18" class="k-green"/>
<circle cx="462" cy="90" r="18" class="k-green"/>
<text x="540" y="252" text-anchor="middle" class="kh-green">loose: 5 narrow interfaces</text>
</g>
</svg>
<figcaption>Count the lines. Every line is something that can break when the other end changes.</figcaption>
</figure>

**Cohesion** measures how strongly the parts inside one module belong together.

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Cohesion inside modules. Low cohesion: a utils module mixes port parsing, HTML escaping, CVSS conversion, SQL and colour codes. High cohesion: each module groups things that change for the same reason: scanner, report, models, store." xmlns="http://www.w3.org/2000/svg">
<style>
.s5c{ font-family:var(--sans),sans-serif; }
.s5c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5c .s{ fill:var(--text-dim); font-size:13px; }
.s5c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5c .c{ fill:var(--text-faint); font-size:12.5px; }
.s5c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5c-a); }
.s5c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5c-a); marker-start:url(#s5c-s); }
.s5c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5c-g); }
.s5c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5c-a); }
.s5c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5c-tri); }
.s5c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5c-tri); }
.s5c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5c-open); }
.s5c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5c-open); }
.s5c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5c-dia); }
.s5c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5c-odia); }
.s5c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5c-dia); marker-end:url(#s5c-open); }
.s5c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5c-solid); }
.s5c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5c-open); }
.s5c .fill{ fill:var(--text); stroke:none; }
.s5c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5c .ks-green{ fill:#3B6D11; font-size:13px; }
.s5c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5c .kb-green, :root[data-theme="dark"] .s5c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5c .kh-green{ fill:#97C459; }
.s5c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5c-green); }
.s5c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5c-green); }
.s5c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5c .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5c .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5c .ks-red{ fill:#A32D2D; font-size:13px; }
.s5c .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5c .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5c .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5c .kb-red, :root[data-theme="dark"] .s5c .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5c .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5c .kh-red{ fill:#F09595; }
.s5c .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5c-red); }
.s5c .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5c-red); }
.s5c .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5c-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s5c">
<rect x="20" y="20" width="260" height="220" rx="7" class="k-red"/>
<text x="150.0" y="62.5" text-anchor="middle" class="kb-red">utils.py  (low cohesion)</text>
<text x="150.0" y="86.5" text-anchor="middle" class="ks-red"></text>
<text x="150.0" y="110.5" text-anchor="middle" class="km-red">parse_ports()</text>
<text x="150.0" y="134.5" text-anchor="middle" class="km-red">escape_html()</text>
<text x="150.0" y="158.5" text-anchor="middle" class="km-red">cvss_to_severity()</text>
<text x="150.0" y="182.5" text-anchor="middle" class="km-red">save_sql()</text>
<text x="150.0" y="206.5" text-anchor="middle" class="km-red">colour_for()</text>
<rect x="340" y="20" width="175" height="100" rx="7" class="k-green"/>
<text x="427.5" y="65.5" text-anchor="middle" class="kb-green">scanner.py</text>
<text x="427.5" y="83.5" text-anchor="middle" class="ks-green">parse_ports, TcpScanner</text>
<rect x="525" y="20" width="175" height="100" rx="7" class="k-green"/>
<text x="612.5" y="65.5" text-anchor="middle" class="kb-green">report.py</text>
<text x="612.5" y="83.5" text-anchor="middle" class="ks-green">escaping, colours, formats</text>
<rect x="340" y="135" width="175" height="100" rx="7" class="k-green"/>
<text x="427.5" y="180.5" text-anchor="middle" class="kb-green">models.py</text>
<text x="427.5" y="198.5" text-anchor="middle" class="ks-green">Severity.from_cvss</text>
<rect x="525" y="135" width="175" height="100" rx="7" class="k-green"/>
<text x="612.5" y="180.5" text-anchor="middle" class="kb-green">store.py</text>
<text x="612.5" y="198.5" text-anchor="middle" class="ks-green">SQL, history, diff</text>
<line x1="286" y1="130" x2="330" y2="130" class="ar"/>
</g>
</svg>
<figcaption>A module named utils, helpers or misc is usually a sign of low cohesion.</figcaption>
</figure>

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The two-by-two of coupling and cohesion. High cohesion and low coupling is the goal: well-defined modules. Low cohesion and low coupling: modules that do little. High cohesion and high coupling: good modules tangled together. Low cohesion and high coupling: a big ball of mud." xmlns="http://www.w3.org/2000/svg">
<style>
.s5d{ font-family:var(--sans),sans-serif; }
.s5d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5d .s{ fill:var(--text-dim); font-size:13px; }
.s5d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5d .c{ fill:var(--text-faint); font-size:12.5px; }
.s5d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5d-a); }
.s5d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5d-a); marker-start:url(#s5d-s); }
.s5d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5d-g); }
.s5d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5d-a); }
.s5d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5d-tri); }
.s5d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5d-tri); }
.s5d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5d-open); }
.s5d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5d-open); }
.s5d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5d-dia); }
.s5d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5d-odia); }
.s5d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5d-dia); marker-end:url(#s5d-open); }
.s5d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5d-solid); }
.s5d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5d-open); }
.s5d .fill{ fill:var(--text); stroke:none; }
.s5d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s5d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s5d .ks-amber{ fill:#854F0B; font-size:13px; }
.s5d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s5d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s5d .kb-amber, :root[data-theme="dark"] .s5d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s5d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s5d .kh-amber{ fill:#EF9F27; }
.s5d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s5d-amber); }
.s5d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5d-amber); }
.s5d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s5d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5d .ks-green{ fill:#3B6D11; font-size:13px; }
.s5d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5d .kb-green, :root[data-theme="dark"] .s5d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5d .kh-green{ fill:#97C459; }
.s5d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5d-green); }
.s5d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5d-green); }
.s5d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5d .ks-red{ fill:#A32D2D; font-size:13px; }
.s5d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5d .kb-red, :root[data-theme="dark"] .s5d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5d .kh-red{ fill:#F09595; }
.s5d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5d-red); }
.s5d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5d-red); }
.s5d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s5d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s5d">
<line x1="80" y1="260" x2="680" y2="260" class="ar"/>
<line x1="80" y1="260" x2="80" y2="20" class="ar"/>
<text x="380" y="284" text-anchor="middle" class="c">coupling: low to high</text>
<text x="70" y="140" text-anchor="end" class="c">cohesion</text>
<rect x="90" y="30" width="280" height="100" rx="7" class="k-green"/>
<text x="230.0" y="84.5" text-anchor="middle" class="kb-green">goal: clear modules</text>
<rect x="390" y="30" width="280" height="100" rx="7" class="k-amber"/>
<text x="530.0" y="84.5" text-anchor="middle" class="kb-amber">good parts, tangled</text>
<rect x="90" y="148" width="280" height="100" rx="7" class="k-amber"/>
<text x="230.0" y="202.5" text-anchor="middle" class="kb-amber">scattered, pointless</text>
<rect x="390" y="148" width="280" height="100" rx="7" class="k-red"/>
<text x="530.0" y="202.5" text-anchor="middle" class="kb-red">big ball of mud</text>
</g>
</svg>
<figcaption>Aim for the top-left: each module does one thing well and depends on others as little as possible.</figcaption>
</figure>

The goal is **high cohesion and low coupling**. High cohesion makes a module easy to understand and name; low coupling means a change in one module rarely forces changes elsewhere. NetWarden's modules each have one theme: `scope.py` is about authorisation, `scanner.py` about network discovery, `report.py` about presentation. The only module that knows about all the others is `cli.py`, where everything is wired together.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Types of coupling from worst to best: content coupling (reaching into another module&#x27;s internals), common coupling (shared global data), control coupling (passing flags that change behaviour), stamp coupling (passing whole structures when parts are needed), and data coupling (passing only the data needed). Types of cohesion from worst to best: coincidental, logical, temporal, procedural, communicational, sequential, functional." xmlns="http://www.w3.org/2000/svg">
<style>
.s5k{ font-family:var(--sans),sans-serif; }
.s5k .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5k .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5k .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5k .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5k .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5k .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5k .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5k .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5k .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5k .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5k .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5k .s{ fill:var(--text-dim); font-size:13px; }
.s5k .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5k .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5k .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5k .c{ fill:var(--text-faint); font-size:12.5px; }
.s5k .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5k .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5k .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5k .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5k-a); }
.s5k .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5k-a); marker-start:url(#s5k-s); }
.s5k .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5k-g); }
.s5k .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5k-a); }
.s5k .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5k .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5k .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5k .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5k .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5k .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5k-tri); }
.s5k .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5k-tri); }
.s5k .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5k-open); }
.s5k .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5k-open); }
.s5k .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5k-dia); }
.s5k .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5k-odia); }
.s5k .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5k-dia); marker-end:url(#s5k-open); }
.s5k .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5k-solid); }
.s5k .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5k-open); }
.s5k .fill{ fill:var(--text); stroke:none; }
.s5k .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5k .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5k .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5k .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5k .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s5k .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s5k .ks-amber{ fill:#854F0B; font-size:13px; }
.s5k .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s5k .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5k .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s5k .kb-amber, :root[data-theme="dark"] .s5k .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s5k .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s5k .kh-amber{ fill:#EF9F27; }
.s5k .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s5k-amber); }
.s5k .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5k-amber); }
.s5k .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s5k .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5k .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5k .ks-green{ fill:#3B6D11; font-size:13px; }
.s5k .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5k .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5k .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5k .kb-green, :root[data-theme="dark"] .s5k .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5k .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5k .kh-green{ fill:#97C459; }
.s5k .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5k-green); }
.s5k .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5k-green); }
.s5k .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5k .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5k .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5k .ks-red{ fill:#A32D2D; font-size:13px; }
.s5k .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5k .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5k .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5k .kb-red, :root[data-theme="dark"] .s5k .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5k .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5k .kh-red{ fill:#F09595; }
.s5k .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5k-red); }
.s5k .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5k-red); }
.s5k .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5k-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5k-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5k-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5k-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5k-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5k-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5k-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5k-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5k-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s5k-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5k-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s5k">
<text x="20" y="24" text-anchor="start" class="b">coupling</text>
<rect x="110" y="10" width="110" height="30" rx="4" class="k-red"/>
<text x="165.0" y="29.5" text-anchor="middle" class="ks-red">content</text>
<rect x="228" y="10" width="110" height="30" rx="4" class="k-red"/>
<text x="283.0" y="29.5" text-anchor="middle" class="ks-red">common</text>
<rect x="346" y="10" width="110" height="30" rx="4" class="k-amber"/>
<text x="401.0" y="29.5" text-anchor="middle" class="ks-amber">control</text>
<rect x="464" y="10" width="110" height="30" rx="4" class="k-amber"/>
<text x="519.0" y="29.5" text-anchor="middle" class="ks-amber">stamp</text>
<rect x="582" y="10" width="110" height="30" rx="4" class="k-green"/>
<text x="637.0" y="29.5" text-anchor="middle" class="ks-green">data</text>
<text x="20" y="124" text-anchor="start" class="b">cohesion</text>
<rect x="110" y="110" width="80" height="30" rx="4" class="k-red"/>
<text x="150.0" y="129.5" text-anchor="middle" class="ks-red">coincidental</text>
<rect x="194" y="110" width="80" height="30" rx="4" class="k-red"/>
<text x="234.0" y="129.5" text-anchor="middle" class="ks-red">logical</text>
<rect x="278" y="110" width="80" height="30" rx="4" class="k-amber"/>
<text x="318.0" y="129.5" text-anchor="middle" class="ks-amber">temporal</text>
<rect x="362" y="110" width="80" height="30" rx="4" class="k-amber"/>
<text x="402.0" y="129.5" text-anchor="middle" class="ks-amber">procedural</text>
<rect x="446" y="110" width="80" height="30" rx="4" class="k-amber"/>
<text x="486.0" y="129.5" text-anchor="middle" class="ks-amber">communic.</text>
<rect x="530" y="110" width="80" height="30" rx="4" class="k-green"/>
<text x="570.0" y="129.5" text-anchor="middle" class="ks-green">sequential</text>
<rect x="614" y="110" width="80" height="30" rx="4" class="k-green"/>
<text x="654.0" y="129.5" text-anchor="middle" class="ks-green">functional</text>
<path d="M110 70 L700 70" class="ar"/>
<text x="405" y="62" text-anchor="middle" class="c">worse to better</text>
<path d="M110 170 L700 170" class="ar"/>
<text x="405" y="162" text-anchor="middle" class="c">worse to better</text>
<text x="360" y="220" text-anchor="middle" class="kh-green">NetWarden aims for data coupling and functional cohesion</text>
</g>
</svg>
<figcaption>Classic scales from structured design (Stevens, Myers and Constantine, 1974). The names matter less than the direction.</figcaption>
</figure>

## Information hiding

David Parnas's 1972 paper *On the Criteria to Be Used in Decomposing Systems into Modules* argued that modules should be chosen to **hide design decisions likely to change**, not to follow the steps of a flowchart.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Information hiding in NetWarden&#x27;s Scope class. Visible to callers: the constructor, from_file, allows and expand. Hidden: how networks are stored, the _hosts helper that expands CIDR blocks, and the MAX_HOSTS rule. Callers depend only on the visible interface, so the hidden parts can change freely." xmlns="http://www.w3.org/2000/svg">
<style>
.s5e{ font-family:var(--sans),sans-serif; }
.s5e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5e .s{ fill:var(--text-dim); font-size:13px; }
.s5e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5e .c{ fill:var(--text-faint); font-size:12.5px; }
.s5e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5e-a); }
.s5e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5e-a); marker-start:url(#s5e-s); }
.s5e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5e-g); }
.s5e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5e-a); }
.s5e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5e-tri); }
.s5e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5e-tri); }
.s5e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5e-open); }
.s5e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5e-open); }
.s5e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5e-dia); }
.s5e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5e-odia); }
.s5e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5e-dia); marker-end:url(#s5e-open); }
.s5e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5e-solid); }
.s5e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5e-open); }
.s5e .fill{ fill:var(--text); stroke:none; }
.s5e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s5e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s5e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s5e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s5e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s5e .kb-teal, :root[data-theme="dark"] .s5e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s5e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s5e .kh-teal{ fill:#5DCAA5; }
.s5e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s5e-teal); }
.s5e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5e-teal); }
.s5e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s5e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5e .ks-red{ fill:#A32D2D; font-size:13px; }
.s5e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5e .kb-red, :root[data-theme="dark"] .s5e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5e .kh-red{ fill:#F09595; }
.s5e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5e-red); }
.s5e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5e-red); }
.s5e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s5e .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s5e .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s5e .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s5e .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s5e .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5e .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s5e .kb-gray, :root[data-theme="dark"] .s5e .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s5e .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s5e .kh-gray{ fill:#B4B2A9; }
.s5e .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s5e-gray); }
.s5e .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5e-gray); }
.s5e .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s5e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s5e-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s5e">
<rect x="140" y="20" width="440" height="210" rx="10" class="k-red"/>
<text x="360" y="44" text-anchor="middle" class="kb-red">Scope</text>
<rect x="160" y="58" width="195" height="34" rx="5" class="pnl"/>
<text x="257.5" y="79.5" text-anchor="middle" class="m">Scope(networks)</text>
<rect x="365" y="58" width="195" height="34" rx="5" class="pnl"/>
<text x="462.5" y="79.5" text-anchor="middle" class="m">Scope.from_file(path)</text>
<rect x="160" y="102" width="195" height="34" rx="5" class="pnl"/>
<text x="257.5" y="123.5" text-anchor="middle" class="m">allows(address)</text>
<rect x="365" y="102" width="195" height="34" rx="5" class="pnl"/>
<text x="462.5" y="123.5" text-anchor="middle" class="m">expand(targets)</text>
<rect x="170" y="150" width="380" height="66" rx="6" class="k-gray"/>
<text x="360" y="170" text-anchor="middle" class="kh-gray">hidden: may change without notice</text>
<text x="360" y="194" text-anchor="middle" class="m">networks list  |  _hosts()  |  MAX_HOSTS</text>
<rect x="20" y="60" width="90" height="60" rx="7" class="k-teal"/>
<text x="65.0" y="94.5" text-anchor="middle" class="kb-teal">engine</text>
<line x1="112" y1="90" x2="158" y2="90" class="ar"/>
<rect x="610" y="60" width="90" height="60" rx="7" class="k-gray"/>
<text x="655.0" y="94.5" text-anchor="middle" class="kb-gray">cli</text>
<line x1="608" y1="90" x2="562" y2="90" class="ar"/>
</g>
</svg>
<figcaption>Parnas (1972): hide each design decision that is likely to change behind an interface.</figcaption>
</figure>

`Scope` hides how networks are stored and how CIDR blocks are expanded. If NetWarden later supports hostname targets or IPv6 ranges with exclusions, only `Scope` changes. Python has no enforced privacy, so the convention is a leading underscore (`_hosts`) for "internal, do not depend on this".

## SOLID

Robert C. Martin collected five object-oriented design principles whose initials spell **SOLID**.

### S: Single responsibility

*A module should have one, and only one, reason to change.* "Reason to change" means a person or group who might request a change.

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The single responsibility principle. Before: one Scanner god class scans, parses banners, checks vulnerabilities, formats reports and saves to a database, so it has five reasons to change. After: TcpScanner, Fingerprinter, the checks, the reporters and ScanRepository each have one reason to change." xmlns="http://www.w3.org/2000/svg">
<style>
.s5f{ font-family:var(--sans),sans-serif; }
.s5f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5f .s{ fill:var(--text-dim); font-size:13px; }
.s5f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5f .c{ fill:var(--text-faint); font-size:12.5px; }
.s5f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5f-a); }
.s5f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5f-a); marker-start:url(#s5f-s); }
.s5f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5f-g); }
.s5f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5f-a); }
.s5f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5f-tri); }
.s5f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5f-tri); }
.s5f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5f-open); }
.s5f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5f-open); }
.s5f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5f-dia); }
.s5f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5f-odia); }
.s5f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5f-dia); marker-end:url(#s5f-open); }
.s5f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5f-solid); }
.s5f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5f-open); }
.s5f .fill{ fill:var(--text); stroke:none; }
.s5f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5f .ks-green{ fill:#3B6D11; font-size:13px; }
.s5f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5f .kb-green, :root[data-theme="dark"] .s5f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5f .kh-green{ fill:#97C459; }
.s5f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5f-green); }
.s5f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5f-green); }
.s5f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5f .ks-red{ fill:#A32D2D; font-size:13px; }
.s5f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5f .kb-red, :root[data-theme="dark"] .s5f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5f .kh-red{ fill:#F09595; }
.s5f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5f-red); }
.s5f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5f-red); }
.s5f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s5f">
<rect x="20" y="30" width="230" height="176" rx="3" class="k-red"/>
<text x="135.0" y="50" text-anchor="middle" class="kb-red">Scanner</text>
<line x1="20" y1="60" x2="250" y2="60" class="ln-red"/>
<text x="28" y="78" text-anchor="start" class="km-red">- db</text>
<text x="28" y="96" text-anchor="start" class="km-red">- html_template</text>
<line x1="20" y1="106" x2="250" y2="106" class="ln-red"/>
<text x="28" y="124" text-anchor="start" class="km-red">+ scan()</text>
<text x="28" y="142" text-anchor="start" class="km-red">+ parse_banner()</text>
<text x="28" y="160" text-anchor="start" class="km-red">+ check_cves()</text>
<text x="28" y="178" text-anchor="start" class="km-red">+ to_html()</text>
<text x="28" y="196" text-anchor="start" class="km-red">+ save()</text>
<text x="135" y="270" text-anchor="middle" class="kh-red">five reasons to change</text>
<line x1="262" y1="120" x2="318" y2="120" class="ar"/>
<rect x="330" y="18" width="200" height="42" rx="4" class="k-green"/>
<text x="430.0" y="43.5" text-anchor="middle" class="kb-green">TcpScanner</text>
<text x="546" y="44" text-anchor="start" class="c">when: network</text>
<rect x="330" y="68" width="200" height="42" rx="4" class="k-green"/>
<text x="430.0" y="93.5" text-anchor="middle" class="kb-green">Fingerprinter</text>
<text x="546" y="94" text-anchor="start" class="c">when: banner formats</text>
<rect x="330" y="118" width="200" height="42" rx="4" class="k-green"/>
<text x="430.0" y="143.5" text-anchor="middle" class="kb-green">Check classes</text>
<text x="546" y="144" text-anchor="start" class="c">when: security rules</text>
<rect x="330" y="168" width="200" height="42" rx="4" class="k-green"/>
<text x="430.0" y="193.5" text-anchor="middle" class="kb-green">Reporter classes</text>
<text x="546" y="194" text-anchor="start" class="c">when: report layout</text>
<rect x="330" y="218" width="200" height="42" rx="4" class="k-green"/>
<text x="430.0" y="243.5" text-anchor="middle" class="kb-green">ScanRepository</text>
<text x="546" y="244" text-anchor="start" class="c">when: storage</text>
</g>
</svg>
<figcaption>A class should have one reason to change. Ask: who would request a change to this code?</figcaption>
</figure>

An early NetWarden prototype had a single `Scanner` class that scanned, parsed banners, checked CVEs, produced HTML and wrote to SQLite. Every change, a new banner format, a new report column, a schema change, touched the same class and risked breaking the others. The current design separates them.

### O: Open/closed

*Software entities should be open for extension but closed for modification.* (Bertrand Meyer, 1988.)

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The open/closed principle. The engine is closed for modification: its code does not change. The system is open for extension: a new SmbSigningCheck class realises the Check interface and is added to the list of checks." xmlns="http://www.w3.org/2000/svg">
<style>
.s5g{ font-family:var(--sans),sans-serif; }
.s5g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5g .s{ fill:var(--text-dim); font-size:13px; }
.s5g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5g .c{ fill:var(--text-faint); font-size:12.5px; }
.s5g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5g-a); }
.s5g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5g-a); marker-start:url(#s5g-s); }
.s5g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5g-g); }
.s5g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-a); }
.s5g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5g-tri); }
.s5g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-tri); }
.s5g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5g-open); }
.s5g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-open); }
.s5g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5g-dia); }
.s5g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5g-odia); }
.s5g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5g-dia); marker-end:url(#s5g-open); }
.s5g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5g-solid); }
.s5g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5g-open); }
.s5g .fill{ fill:var(--text); stroke:none; }
.s5g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5g .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s5g .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s5g .ks-blue{ fill:#185FA5; font-size:13px; }
.s5g .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s5g .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5g .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s5g .kb-blue, :root[data-theme="dark"] .s5g .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s5g .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s5g .kh-blue{ fill:#85B7EB; }
.s5g .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s5g-blue); }
.s5g .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-blue); }
.s5g .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s5g .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s5g .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s5g .ks-teal{ fill:#0F6E56; font-size:13px; }
.s5g .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s5g .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5g .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s5g .kb-teal, :root[data-theme="dark"] .s5g .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s5g .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s5g .kh-teal{ fill:#5DCAA5; }
.s5g .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s5g-teal); }
.s5g .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-teal); }
.s5g .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s5g .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s5g .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s5g .ks-purple{ fill:#534AB7; font-size:13px; }
.s5g .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s5g .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5g .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s5g .kb-purple, :root[data-theme="dark"] .s5g .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s5g .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s5g .kh-purple{ fill:#AFA9EC; }
.s5g .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s5g-purple); }
.s5g .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-purple); }
.s5g .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s5g .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5g .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5g .ks-green{ fill:#3B6D11; font-size:13px; }
.s5g .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5g .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5g .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5g .kb-green, :root[data-theme="dark"] .s5g .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5g .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5g .kh-green{ fill:#97C459; }
.s5g .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5g-green); }
.s5g .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5g-green); }
.s5g .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5g-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s5g-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s5g-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s5g-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s5g">
<rect x="20" y="40" width="190" height="86" rx="3" class="k-teal"/>
<text x="115.0" y="60" text-anchor="middle" class="kb-teal">Assessment</text>
<line x1="20" y1="70" x2="210" y2="70" class="ln-teal"/>
<text x="28" y="88" text-anchor="start" class="km-teal">- checks: list[Check]</text>
<line x1="20" y1="98" x2="210" y2="98" class="ln-teal"/>
<text x="28" y="116" text-anchor="start" class="km-teal">+ run()</text>
<rect x="270" y="30" width="180" height="86" rx="3" class="k-purple"/>
<text x="360.0" y="50" text-anchor="middle" class="ks-purple">«interface»</text>
<text x="360.0" y="68" text-anchor="middle" class="kb-purple">Check</text>
<line x1="270" y1="78" x2="450" y2="78" class="ln-purple"/>
<line x1="270" y1="88" x2="450" y2="88" class="ln-purple"/>
<text x="278" y="106" text-anchor="start" class="km-purple">+ run(host, service)</text>
<line x1="212" y1="80" x2="268" y2="80" class="assoc"/>
<rect x="500" y="20" width="200" height="40" rx="3" class="k-blue"/>
<text x="600.0" y="44.5" text-anchor="middle" class="kb-blue">CleartextProtocolCheck</text>
<line x1="498" y1="40" x2="452" y2="75" class="real"/>
<rect x="500" y="70" width="200" height="40" rx="3" class="k-blue"/>
<text x="600.0" y="94.5" text-anchor="middle" class="kb-blue">HttpHeadersCheck</text>
<line x1="498" y1="90" x2="452" y2="75" class="real"/>
<rect x="500" y="140" width="200" height="44" rx="3" class="k-green"/>
<text x="600.0" y="166.5" text-anchor="middle" class="kb-green">SmbSigningCheck  (new)</text>
<line x1="498" y1="160" x2="452" y2="90" class="real"/>
<text x="115" y="160" text-anchor="middle" class="kh-teal">closed: unchanged</text>
<text x="600" y="210" text-anchor="middle" class="kh-green">open: add a class</text>
</g>
</svg>
<figcaption>New behaviour is added by writing new code, not by editing code that already works and is tested.</figcaption>
</figure>

To add an SMB signing check, a developer writes one class and adds it to `default_checks()`. The engine, its tests, and the other checks are untouched. This is requirement NW-NFR-4, achieved by design.

```python
class SmbSigningCheck:
    """Hypothetical new check: no other file changes except the list below."""
    id = "NW-SMB-SIGNING"

    def run(self, host: Host, service: Service) -> list[Finding]:
        ...

def default_checks(kb: KnowledgeBase) -> list[Check]:
    return [KnownVulnerabilityCheck(kb), CleartextProtocolCheck(), ExposedDatabaseCheck(),
            HttpHeadersCheck(), VersionDisclosureCheck(), SmbSigningCheck()]
```

### L: Liskov substitution

*Objects of a subtype must be usable wherever the base type is expected, without surprising the caller.* (Barbara Liskov, 1987.)

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The Liskov substitution principle. The cli calls render on any Reporter and writes the string to a file. MarkdownReporter, JsonReporter and HtmlReporter all return text, so they can be substituted. A PdfReporter that returns bytes or raises NotImplementedError breaks the contract: the caller would need special cases." xmlns="http://www.w3.org/2000/svg">
<style>
.s5h{ font-family:var(--sans),sans-serif; }
.s5h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5h .s{ fill:var(--text-dim); font-size:13px; }
.s5h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5h .c{ fill:var(--text-faint); font-size:12.5px; }
.s5h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5h-a); }
.s5h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5h-a); marker-start:url(#s5h-s); }
.s5h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5h-g); }
.s5h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5h-a); }
.s5h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5h-tri); }
.s5h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5h-tri); }
.s5h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5h-open); }
.s5h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5h-open); }
.s5h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5h-dia); }
.s5h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5h-odia); }
.s5h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5h-dia); marker-end:url(#s5h-open); }
.s5h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5h-solid); }
.s5h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5h-open); }
.s5h .fill{ fill:var(--text); stroke:none; }
.s5h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5h .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s5h .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s5h .ks-purple{ fill:#534AB7; font-size:13px; }
.s5h .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s5h .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5h .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s5h .kb-purple, :root[data-theme="dark"] .s5h .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s5h .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s5h .kh-purple{ fill:#AFA9EC; }
.s5h .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s5h-purple); }
.s5h .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5h-purple); }
.s5h .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s5h .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5h .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5h .ks-green{ fill:#3B6D11; font-size:13px; }
.s5h .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5h .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5h .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5h .kb-green, :root[data-theme="dark"] .s5h .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5h .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5h .kh-green{ fill:#97C459; }
.s5h .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5h-green); }
.s5h .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5h-green); }
.s5h .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5h .ks-red{ fill:#A32D2D; font-size:13px; }
.s5h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5h .kb-red, :root[data-theme="dark"] .s5h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5h .kh-red{ fill:#F09595; }
.s5h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5h-red); }
.s5h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5h-red); }
.s5h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5h-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s5h-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s5h">
<rect x="250" y="16" width="220" height="104" rx="3" class="k-purple"/>
<text x="360.0" y="36" text-anchor="middle" class="ks-purple">«protocol»</text>
<text x="360.0" y="54" text-anchor="middle" class="kb-purple">Reporter</text>
<line x1="250" y1="64" x2="470" y2="64" class="ln-purple"/>
<text x="258" y="82" text-anchor="start" class="km-purple">+ extension: str</text>
<line x1="250" y1="92" x2="470" y2="92" class="ln-purple"/>
<text x="258" y="110" text-anchor="start" class="km-purple">+ render(result): str</text>
<rect x="20" y="170" width="160" height="50" rx="3" class="k-green"/>
<text x="100.0" y="190.5" text-anchor="middle" class="kb-green">MarkdownReporter</text>
<text x="100.0" y="208.5" text-anchor="middle" class="ks-green">returns str</text>
<line x1="100" y1="168" x2="360" y2="120" class="real"/>
<rect x="195" y="170" width="160" height="50" rx="3" class="k-green"/>
<text x="275.0" y="190.5" text-anchor="middle" class="kb-green">JsonReporter</text>
<text x="275.0" y="208.5" text-anchor="middle" class="ks-green">returns str</text>
<line x1="275" y1="168" x2="360" y2="120" class="real"/>
<rect x="370" y="170" width="160" height="50" rx="3" class="k-green"/>
<text x="450.0" y="190.5" text-anchor="middle" class="kb-green">HtmlReporter</text>
<text x="450.0" y="208.5" text-anchor="middle" class="ks-green">returns str</text>
<line x1="450" y1="168" x2="360" y2="120" class="real"/>
<rect x="545" y="170" width="160" height="50" rx="3" class="k-red"/>
<text x="625.0" y="190.5" text-anchor="middle" class="kb-red">PdfReporter</text>
<text x="625.0" y="208.5" text-anchor="middle" class="ks-red">returns bytes!</text>
<line x1="625" y1="168" x2="360" y2="120" class="real"/>
<text x="360" y="246" text-anchor="middle" class="c">if a subtype surprises callers, it is not a true subtype</text>
</g>
</svg>
<figcaption>Subtypes must honour the base type's contract: same inputs accepted, same kind of outputs, no new exceptions.</figcaption>
</figure>

Substitutability is about **behaviour**, not just method names. The command-line code writes whatever `render()` returns into a text file. A reporter that returned bytes, or raised `NotImplementedError` for some inputs, would type-check by name but break callers. In design-by-contract terms, a subtype may not strengthen preconditions or weaken postconditions.

### I: Interface segregation

*Clients should not be forced to depend on methods they do not use.*

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The interface segregation principle. A fat ScanStore interface forces the report writer to depend on save, delete and migrate, which it never uses. Split into ScanReader, with get and history, and ScanWriter, with save; each client depends only on what it needs." xmlns="http://www.w3.org/2000/svg">
<style>
.s5i{ font-family:var(--sans),sans-serif; }
.s5i .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5i .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5i .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5i .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5i .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5i .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5i .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5i .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5i .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5i .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5i .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5i .s{ fill:var(--text-dim); font-size:13px; }
.s5i .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5i .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5i .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5i .c{ fill:var(--text-faint); font-size:12.5px; }
.s5i .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5i .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5i .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5i .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5i-a); }
.s5i .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5i-a); marker-start:url(#s5i-s); }
.s5i .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5i-g); }
.s5i .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5i-a); }
.s5i .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5i .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5i .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5i .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5i .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5i .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5i-tri); }
.s5i .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5i-tri); }
.s5i .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5i-open); }
.s5i .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5i-open); }
.s5i .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5i-dia); }
.s5i .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5i-odia); }
.s5i .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5i-dia); marker-end:url(#s5i-open); }
.s5i .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5i-solid); }
.s5i .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5i-open); }
.s5i .fill{ fill:var(--text); stroke:none; }
.s5i .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5i .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5i .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5i .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5i .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5i .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5i .ks-green{ fill:#3B6D11; font-size:13px; }
.s5i .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5i .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5i .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5i .kb-green, :root[data-theme="dark"] .s5i .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5i .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5i .kh-green{ fill:#97C459; }
.s5i .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5i-green); }
.s5i .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5i-green); }
.s5i .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5i .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5i .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5i .ks-red{ fill:#A32D2D; font-size:13px; }
.s5i .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5i .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5i .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5i .kb-red, :root[data-theme="dark"] .s5i .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5i .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5i .kh-red{ fill:#F09595; }
.s5i .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5i-red); }
.s5i .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5i-red); }
.s5i .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s5i .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s5i .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s5i .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s5i .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s5i .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5i .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s5i .kb-gray, :root[data-theme="dark"] .s5i .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s5i .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s5i .kh-gray{ fill:#B4B2A9; }
.s5i .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s5i-gray); }
.s5i .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5i-gray); }
.s5i .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5i-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5i-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5i-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5i-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5i-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5i-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5i-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5i-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5i-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5i-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s5i-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s5i">
<rect x="20" y="30" width="200" height="158" rx="3" class="k-red"/>
<text x="120.0" y="50" text-anchor="middle" class="ks-red">«interface»</text>
<text x="120.0" y="68" text-anchor="middle" class="kb-red">ScanStore</text>
<line x1="20" y1="78" x2="220" y2="78" class="ln-red"/>
<line x1="20" y1="88" x2="220" y2="88" class="ln-red"/>
<text x="28" y="106" text-anchor="start" class="km-red">+ save()</text>
<text x="28" y="124" text-anchor="start" class="km-red">+ get()</text>
<text x="28" y="142" text-anchor="start" class="km-red">+ history()</text>
<text x="28" y="160" text-anchor="start" class="km-red">+ delete()</text>
<text x="28" y="178" text-anchor="start" class="km-red">+ migrate()</text>
<text x="120" y="230" text-anchor="middle" class="kh-red">fat: everyone depends on all</text>
<line x1="240" y1="110" x2="290" y2="110" class="ar"/>
<rect x="320" y="30" width="170" height="104" rx="3" class="k-green"/>
<text x="405.0" y="50" text-anchor="middle" class="ks-green">«interface»</text>
<text x="405.0" y="68" text-anchor="middle" class="kb-green">ScanReader</text>
<line x1="320" y1="78" x2="490" y2="78" class="ln-green"/>
<line x1="320" y1="88" x2="490" y2="88" class="ln-green"/>
<text x="328" y="106" text-anchor="start" class="km-green">+ get()</text>
<text x="328" y="124" text-anchor="start" class="km-green">+ history()</text>
<rect x="320" y="150" width="170" height="86" rx="3" class="k-green"/>
<text x="405.0" y="170" text-anchor="middle" class="ks-green">«interface»</text>
<text x="405.0" y="188" text-anchor="middle" class="kb-green">ScanWriter</text>
<line x1="320" y1="198" x2="490" y2="198" class="ln-green"/>
<line x1="320" y1="208" x2="490" y2="208" class="ln-green"/>
<text x="328" y="226" text-anchor="start" class="km-green">+ save()</text>
<rect x="560" y="50" width="140" height="50" rx="7" class="k-gray"/>
<text x="630.0" y="79.5" text-anchor="middle" class="kb-gray">diff command</text>
<line x1="558" y1="75" x2="492" y2="75" class="dep"/>
<rect x="560" y="160" width="140" height="50" rx="7" class="k-gray"/>
<text x="630.0" y="189.5" text-anchor="middle" class="kb-gray">scan command</text>
<line x1="558" y1="185" x2="492" y2="185" class="dep"/>
</g>
</svg>
<figcaption>Many small, role-specific interfaces are better than one general-purpose one.</figcaption>
</figure>

### D: Dependency inversion

*High-level modules should not depend on low-level modules; both should depend on abstractions.*

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The dependency inversion principle. Without it, the high-level Assessment depends directly on low-level details: TcpScanner, sockets and a JSON file. With it, both depend on abstractions owned by the high level: a Scanner interface and a Check interface. Arrows show source code dependencies; with inversion they point upward towards the abstractions." xmlns="http://www.w3.org/2000/svg">
<style>
.s5j{ font-family:var(--sans),sans-serif; }
.s5j .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s5j .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s5j .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s5j .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s5j .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s5j .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s5j .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s5j .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s5j .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s5j .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s5j .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s5j .s{ fill:var(--text-dim); font-size:13px; }
.s5j .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s5j .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .c{ fill:var(--text-faint); font-size:12.5px; }
.s5j .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s5j .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s5j .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s5j .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5j-a); }
.s5j .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s5j-a); marker-start:url(#s5j-s); }
.s5j .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s5j-g); }
.s5j .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-a); }
.s5j .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s5j .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s5j .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s5j .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s5j .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s5j .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5j-tri); }
.s5j .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-tri); }
.s5j .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5j-open); }
.s5j .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-open); }
.s5j .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5j-dia); }
.s5j .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5j-odia); }
.s5j .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s5j-dia); marker-end:url(#s5j-open); }
.s5j .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s5j-solid); }
.s5j .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s5j-open); }
.s5j .fill{ fill:var(--text); stroke:none; }
.s5j .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s5j .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s5j .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s5j .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s5j .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s5j .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s5j .ks-teal{ fill:#0F6E56; font-size:13px; }
.s5j .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5j .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s5j .kb-teal, :root[data-theme="dark"] .s5j .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s5j .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s5j .kh-teal{ fill:#5DCAA5; }
.s5j .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s5j-teal); }
.s5j .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-teal); }
.s5j .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s5j .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s5j .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s5j .ks-purple{ fill:#534AB7; font-size:13px; }
.s5j .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5j .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s5j .kb-purple, :root[data-theme="dark"] .s5j .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s5j .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s5j .kh-purple{ fill:#AFA9EC; }
.s5j .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s5j-purple); }
.s5j .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-purple); }
.s5j .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s5j .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s5j .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s5j .ks-green{ fill:#3B6D11; font-size:13px; }
.s5j .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5j .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s5j .kb-green, :root[data-theme="dark"] .s5j .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s5j .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s5j .kh-green{ fill:#97C459; }
.s5j .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s5j-green); }
.s5j .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-green); }
.s5j .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s5j .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s5j .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s5j .ks-red{ fill:#A32D2D; font-size:13px; }
.s5j .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5j .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s5j .kb-red, :root[data-theme="dark"] .s5j .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s5j .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s5j .kh-red{ fill:#F09595; }
.s5j .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s5j-red); }
.s5j .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-red); }
.s5j .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s5j .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s5j .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s5j .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s5j .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s5j .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s5j .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s5j .kb-gray, :root[data-theme="dark"] .s5j .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s5j .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s5j .kh-gray{ fill:#B4B2A9; }
.s5j .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s5j-gray); }
.s5j .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s5j-gray); }
.s5j .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s5j-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s5j-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s5j-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s5j-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s5j-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s5j-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s5j-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s5j-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s5j-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s5j-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s5j-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s5j-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s5j-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s5j">
<text x="170" y="20" text-anchor="middle" class="kh-red">without: policy depends on details</text>
<rect x="80" y="36" width="180" height="44" rx="7" class="k-teal"/>
<text x="170.0" y="62.5" text-anchor="middle" class="kb-teal">Assessment</text>
<rect x="20" y="140" width="95" height="40" rx="3" class="k-gray"/>
<text x="67.5" y="164.5" text-anchor="middle" class="km-gray">TcpScanner</text>
<line x1="170" y1="82" x2="67" y2="138" class="dep"/>
<rect x="125" y="140" width="95" height="40" rx="3" class="k-gray"/>
<text x="172.5" y="164.5" text-anchor="middle" class="km-gray">socket</text>
<line x1="170" y1="82" x2="172" y2="138" class="dep"/>
<rect x="230" y="140" width="95" height="40" rx="3" class="k-gray"/>
<text x="277.5" y="164.5" text-anchor="middle" class="km-gray">vulns.json</text>
<line x1="170" y1="82" x2="277" y2="138" class="dep"/>
<text x="540" y="20" text-anchor="middle" class="kh-green">with: both depend on abstractions</text>
<rect x="450" y="36" width="180" height="44" rx="7" class="k-teal"/>
<text x="540.0" y="62.5" text-anchor="middle" class="kb-teal">Assessment</text>
<rect x="380" y="120" width="150" height="40" rx="3" class="k-purple"/>
<text x="455.0" y="144.5" text-anchor="middle" class="ks-purple">«interface» Scanner</text>
<rect x="550" y="120" width="150" height="40" rx="3" class="k-purple"/>
<text x="625.0" y="144.5" text-anchor="middle" class="ks-purple">«interface» Check</text>
<line x1="500" y1="82" x2="470" y2="118" class="dep"/>
<line x1="580" y1="82" x2="610" y2="118" class="dep"/>
<rect x="380" y="230" width="150" height="40" rx="3" class="k-gray"/>
<text x="455.0" y="254.5" text-anchor="middle" class="km-gray">TcpScanner</text>
<line x1="455" y1="228" x2="455" y2="162" class="real"/>
<rect x="550" y="230" width="150" height="40" rx="3" class="k-gray"/>
<text x="625.0" y="254.5" text-anchor="middle" class="km-gray">KnownVuln...Check</text>
<line x1="625" y1="228" x2="625" y2="162" class="real"/>
<text x="540" y="290" text-anchor="middle" class="c">details point up to abstractions</text>
</g>
</svg>
<figcaption>High-level policy should not depend on low-level detail; both should depend on abstractions.</figcaption>
</figure>

`Assessment` is NetWarden's policy: the order of steps and the rules. Sockets, files and databases are details. Because `Assessment` receives its scanner and checks as constructor arguments that satisfy interfaces, tests can pass a `FakeScanner` and run the whole pipeline without a network:

```python
class FakeScanner:
    """A stub: returns canned hosts instead of touching the network."""
    def __init__(self, hosts):
        self.hosts = hosts
        self.calls = []

    async def scan(self, addresses, ports):
        self.calls.append((list(addresses), list(ports)))
        return self.hosts
```

Passing collaborators in, rather than creating them inside, is called **dependency injection** (Chapter 6).

## Other principles

| Principle | Meaning | NetWarden example |
|---|---|---|
| **DRY**, Don't Repeat Yourself | Every piece of knowledge has one authoritative place | The CVSS-to-severity mapping exists only in `Severity.from_cvss` |
| **KISS**, Keep It Simple | Prefer the simplest design that works | Version comparison is a tuple of integers, not a general version-parsing library |
| **YAGNI**, You Aren't Gonna Need It | Do not build features for imagined future needs | No plugin loader from external directories until someone needs one |
| **Law of Demeter** | Talk to immediate collaborators, not strangers' internals | The CLI calls `result.counts()`, not `len([f for f in result.findings if ...])` |
| **Composition over inheritance** | Build behaviour by combining objects | Checks are separate objects in a list, not subclasses of one big `BaseScanner` |
| **Separation of concerns** | Different concerns in different places | Progress printing is an observer; the engine never prints |
| **Principle of least astonishment** | Behave as users and readers expect | Reports go to stdout, progress to stderr, so `> report.md` works |

DRY is about **knowledge**, not text: two pieces of code that look alike but would change for different reasons are not duplication, and merging them creates coupling. Similarly, KISS and YAGNI are in tension with the open/closed principle; the resolution is to make code open for the extensions you **know** are coming. NetWarden knew new checks would come; it did not know about a GUI, so it does not have extension points for one.

## Design for security

For a security tool, some principles from Saltzer and Schroeder's classic 1975 paper are design principles too:

- **Fail-safe defaults**: deny by default. NetWarden scans nothing unless a scope file explicitly allows it.
- **Least privilege**: the container image runs as an unprivileged user; a TCP connect scan needs no root access.
- **Economy of mechanism**: keep security-relevant code small enough to review. `scope.py` is 60 lines.
- **Complete mediation**: check every access. Every target goes through `Scope.expand`, including targets from CIDR expansion.

Chapter 12 returns to these.

## Hands on: measure the design

Tools can estimate some of these properties. Try them on NetWarden:

```bash
pip install radon
radon cc -s -a src/netwarden      # cyclomatic complexity per function, and the average
radon mi src/netwarden            # maintainability index per module
```

Then imagine three changes and count the files each would touch: a new check; a new report format; storing history in PostgreSQL instead of SQLite. In a well-designed system each touches one or two files. Finally, read `cli.py` and find the one place where concrete classes are chosen and connected. Why is it good that this happens in exactly one place?

## Summary

- **Abstraction** hides detail behind simple interfaces, in layers.
- Aim for **high cohesion** inside modules and **low coupling** between them.
- **Information hiding**: put each decision likely to change behind an interface.
- **SOLID**: single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion.
- **DRY, KISS, YAGNI**, Law of Demeter, composition over inheritance, separation of concerns.
- Security design principles: **fail-safe defaults, least privilege, economy of mechanism, complete mediation**.
- Principles are heuristics: apply them to the changes you expect, and avoid speculative generality.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-5-design-principles).

**1. What is the design goal for modules, in terms of coupling and cohesion?**

- A. Low coupling, high cohesion
- B. High coupling, low cohesion
- C. High coupling, high cohesion
- D. Low coupling, low cohesion

**2. According to Parnas, how should a system be divided into modules?**

- A. By the steps of a flowchart
- B. By file size
- C. To hide design decisions likely to change
- D. By team

**3. Which SOLID principle says a module should be open for extension but closed for modification?**

- A. Single responsibility
- B. Open/closed
- C. Liskov substitution
- D. Dependency inversion

**4. A reporter class has render() but returns bytes where callers expect text. Which principle does it break?**

- A. Interface segregation
- B. DRY
- C. KISS
- D. Liskov substitution

**5. What does dependency inversion ask for?**

- A. Low-level modules depend on high-level ones by name
- B. High-level modules depend on abstractions, not on concrete low-level details
- C. No dependencies at all
- D. Inheritance everywhere

**6. The CVSS-to-severity mapping exists only in Severity.from_cvss. Which principle is that?**

- A. YAGNI
- B. Law of Demeter
- C. KISS
- D. DRY

**7. Not building a plugin loader until someone needs one follows which principle?**

- A. YAGNI
- B. DRY
- C. SOLID
- D. Demeter

**8. What is a leaky abstraction?**

- A. One that crashes
- B. One with too many methods
- C. One whose callers must know about the details it was meant to hide
- D. One that is not documented
