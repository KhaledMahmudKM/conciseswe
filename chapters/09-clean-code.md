# Chapter 9: Clean Code

Code is read far more often than it is written: by reviewers, by teammates fixing bugs, and by you, six months later, having forgotten everything. **Clean code**, a term popularised by Robert C. Martin's book of that name, is code that a competent reader can understand quickly and change safely. This chapter covers the habits that make code clean: naming, functions, comments, error handling, types, and the tools that enforce the boring parts automatically. The examples are NetWarden's own code.

## Names

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Naming examples from bad to good. A variable d becomes elapsed_days; lst becomes open_ports; a function proc becomes fingerprint; a boolean flag becomes is_in_scope; the magic number 1024 becomes MAX_HOSTS." xmlns="http://www.w3.org/2000/svg">
<style>
.s9a{ font-family:var(--sans),sans-serif; }
.s9a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s9a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s9a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s9a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s9a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s9a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s9a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s9a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s9a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s9a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s9a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s9a .s{ fill:var(--text-dim); font-size:13px; }
.s9a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s9a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s9a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s9a .c{ fill:var(--text-faint); font-size:12.5px; }
.s9a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s9a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s9a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s9a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9a-a); }
.s9a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9a-a); marker-start:url(#s9a-s); }
.s9a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s9a-g); }
.s9a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s9a-a); }
.s9a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s9a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s9a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s9a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s9a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s9a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9a-tri); }
.s9a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9a-tri); }
.s9a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9a-open); }
.s9a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9a-open); }
.s9a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9a-dia); }
.s9a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9a-odia); }
.s9a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9a-dia); marker-end:url(#s9a-open); }
.s9a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9a-solid); }
.s9a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s9a-open); }
.s9a .fill{ fill:var(--text); stroke:none; }
.s9a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s9a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s9a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s9a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s9a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s9a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s9a .ks-green{ fill:#3B6D11; font-size:13px; }
.s9a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s9a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s9a .kb-green, :root[data-theme="dark"] .s9a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s9a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s9a .kh-green{ fill:#97C459; }
.s9a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s9a-green); }
.s9a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9a-green); }
.s9a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s9a .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s9a .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s9a .ks-red{ fill:#A32D2D; font-size:13px; }
.s9a .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s9a .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9a .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s9a .kb-red, :root[data-theme="dark"] .s9a .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s9a .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s9a .kh-red{ fill:#F09595; }
.s9a .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s9a-red); }
.s9a .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9a-red); }
.s9a .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s9a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s9a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s9a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s9a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s9a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s9a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s9a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s9a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s9a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s9a-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s9a">
<rect x="20" y="16" width="260" height="36" rx="4" class="k-red"/>
<text x="150.0" y="38.5" text-anchor="middle" class="km-red">d</text>
<line x1="290" y1="34" x2="420" y2="34" class="ar"/>
<rect x="430" y="16" width="270" height="36" rx="4" class="k-green"/>
<text x="565.0" y="38.5" text-anchor="middle" class="km-green">elapsed_days</text>
<rect x="20" y="62" width="260" height="36" rx="4" class="k-red"/>
<text x="150.0" y="84.5" text-anchor="middle" class="km-red">lst</text>
<line x1="290" y1="80" x2="420" y2="80" class="ar"/>
<rect x="430" y="62" width="270" height="36" rx="4" class="k-green"/>
<text x="565.0" y="84.5" text-anchor="middle" class="km-green">open_ports</text>
<rect x="20" y="108" width="260" height="36" rx="4" class="k-red"/>
<text x="150.0" y="130.5" text-anchor="middle" class="km-red">def proc(x):</text>
<line x1="290" y1="126" x2="420" y2="126" class="ar"/>
<rect x="430" y="108" width="270" height="36" rx="4" class="k-green"/>
<text x="565.0" y="130.5" text-anchor="middle" class="km-green">def identify(service):</text>
<rect x="20" y="154" width="260" height="36" rx="4" class="k-red"/>
<text x="150.0" y="176.5" text-anchor="middle" class="km-red">flag</text>
<line x1="290" y1="172" x2="420" y2="172" class="ar"/>
<rect x="430" y="154" width="270" height="36" rx="4" class="k-green"/>
<text x="565.0" y="176.5" text-anchor="middle" class="km-green">is_in_scope</text>
<rect x="20" y="200" width="260" height="36" rx="4" class="k-red"/>
<text x="150.0" y="222.5" text-anchor="middle" class="km-red">if n &gt; 1024:</text>
<line x1="290" y1="218" x2="420" y2="218" class="ar"/>
<rect x="430" y="200" width="270" height="36" rx="4" class="k-green"/>
<text x="565.0" y="222.5" text-anchor="middle" class="km-green">if n &gt; MAX_HOSTS:</text>
</g>
</svg>
<figcaption>A good name tells you why it exists, what it does, and how it is used, without a comment.</figcaption>
</figure>

Names are the main way code explains itself. Good names:

- **reveal intent**: `open_ports`, not `lst`; `is_in_scope`, not `flag`;
- use the **vocabulary of the domain**: NetWarden says `Finding`, `Severity`, `Scope`, the words the administrators used in interviews (Chapter 3);
- are **pronounceable and searchable**: `MAX_HOSTS` can be found with a search, `1024` cannot;
- follow **conventions**: in Python, PEP 8's `snake_case` for functions and variables, `CapWords` for classes, `UPPER_CASE` for constants;
- have length proportional to scope: `i` is fine in a three-line loop; a module-level name needs to be descriptive.

Functions are named with verbs (`expand`, `identify`, `render`), classes with nouns (`Assessment`, `ScanRepository`), and booleans read as questions (`allows(address)`, `is_global`).

## Functions

Small functions that do one thing at one level of abstraction are easier to name, test and reuse. Compare NetWarden's engine loop with what it would look like if every detail were inline:

```python
async def run_async(self, targets, ports) -> ScanResult:
    targets, ports = list(targets), list(ports)
    addresses = self.scope.expand(targets)          # raises ScopeError before any packet is sent
    result = ScanResult(targets=targets)
    self.bus.publish(ScanStarted(hosts=len(addresses), ports=len(ports)))
    result.hosts = await self.scanner.scan(addresses, ports)
    for host in result.hosts:
        for service in host.services:
            self.fingerprinter.identify(service)
        ...
```

Each line is a step in the assessment, stated at the same level: expand, scan, identify, check. The details of how to expand a CIDR block or parse an SSH banner live in other functions, each with its own name and tests.

Guidelines:

| Guideline | Why |
|---|---|
| Do one thing | One reason to change; one name that describes it |
| Keep one level of abstraction | Mixing "send packets" with "decide severity" confuses readers |
| Few parameters (0 to 3 is comfortable) | Many parameters often hide a missing concept; group them into an object |
| No surprising side effects | A function named `get_` should not also write to the database |
| Command or query, not both | Either change state or return information (command-query separation) |
| Prefer returning values to mutating arguments | Easier to test and reason about |

Measured complexity helps find candidates for simplification. **Cyclomatic complexity**, introduced by Thomas McCabe in 1976, counts the independent paths through a function; values above about 10 usually deserve attention. Chapter 12 uses it as a quality metric.

## Comments and docstrings

Comments should explain **why**, not repeat **what** the code already says.

```python
# Bad: repeats the code
i += 1  # add one to i

# Good: explains a decision a reader could not guess
MAX_HOSTS = 1024  # NW-SR-2: guard against accidentally scanning huge ranges

# Good: explains a non-obvious external fact
elif service.banner.startswith("\xff"):           # Telnet option negotiation (IAC)
```

Docstrings document the **contract** of public modules, classes and functions: what it does, its parameters and return value, what it raises. They are read by `help()`, by editors, and by documentation generators.

```python
def expand(self, targets: Iterable[str]) -> list[str]:
    """Turn targets (addresses or CIDR blocks) into addresses, all inside the scope."""
```

If you need a long comment to explain what a block of code does, try first to make the code explain itself: extract the block into a function whose name is the comment.

## Error handling

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Error handling across NetWarden&#x27;s layers. Deep in the domain, Scope raises ScopeError and parse_ports raises ValueError. The engine lets them propagate. Only at the boundary, the cli main function, are they caught and turned into a readable message and exit status 2. Network errors during a probe are expected and handled locally: the port is simply closed." xmlns="http://www.w3.org/2000/svg">
<style>
.s9b{ font-family:var(--sans),sans-serif; }
.s9b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s9b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s9b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s9b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s9b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s9b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s9b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s9b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s9b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s9b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s9b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s9b .s{ fill:var(--text-dim); font-size:13px; }
.s9b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s9b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s9b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s9b .c{ fill:var(--text-faint); font-size:12.5px; }
.s9b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s9b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s9b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s9b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9b-a); }
.s9b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9b-a); marker-start:url(#s9b-s); }
.s9b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s9b-g); }
.s9b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-a); }
.s9b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s9b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s9b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s9b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s9b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s9b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9b-tri); }
.s9b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-tri); }
.s9b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9b-open); }
.s9b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-open); }
.s9b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9b-dia); }
.s9b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9b-odia); }
.s9b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9b-dia); marker-end:url(#s9b-open); }
.s9b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9b-solid); }
.s9b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s9b-open); }
.s9b .fill{ fill:var(--text); stroke:none; }
.s9b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s9b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s9b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s9b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s9b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s9b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s9b .ks-blue{ fill:#185FA5; font-size:13px; }
.s9b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s9b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s9b .kb-blue, :root[data-theme="dark"] .s9b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s9b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s9b .kh-blue{ fill:#85B7EB; }
.s9b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s9b-blue); }
.s9b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-blue); }
.s9b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s9b .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s9b .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s9b .ks-teal{ fill:#0F6E56; font-size:13px; }
.s9b .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s9b .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9b .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s9b .kb-teal, :root[data-theme="dark"] .s9b .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s9b .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s9b .kh-teal{ fill:#5DCAA5; }
.s9b .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s9b-teal); }
.s9b .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-teal); }
.s9b .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s9b .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s9b .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s9b .ks-red{ fill:#A32D2D; font-size:13px; }
.s9b .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s9b .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9b .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s9b .kb-red, :root[data-theme="dark"] .s9b .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s9b .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s9b .kh-red{ fill:#F09595; }
.s9b .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s9b-red); }
.s9b .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-red); }
.s9b .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s9b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s9b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s9b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s9b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s9b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s9b .kb-gray, :root[data-theme="dark"] .s9b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s9b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s9b .kh-gray{ fill:#B4B2A9; }
.s9b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s9b-gray); }
.s9b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9b-gray); }
.s9b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s9b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s9b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s9b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s9b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s9b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s9b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s9b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s9b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s9b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s9b-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s9b-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s9b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s9b">
<rect x="30" y="20" width="190" height="48" rx="4" class="k-gray"/>
<text x="125.0" y="48.5" text-anchor="middle" class="km-gray">cli.main()</text>
<text x="236" y="49" text-anchor="start" class="s">catch ScopeError, ValueError, OSError -&gt; message, exit 2</text>
<rect x="30" y="84" width="190" height="48" rx="4" class="k-teal"/>
<text x="125.0" y="112.5" text-anchor="middle" class="km-teal">Assessment.run()</text>
<text x="236" y="113" text-anchor="start" class="s">lets errors propagate; no try/except</text>
<rect x="30" y="148" width="190" height="48" rx="4" class="k-red"/>
<text x="125.0" y="176.5" text-anchor="middle" class="km-red">Scope.expand()</text>
<text x="236" y="177" text-anchor="start" class="s">raise ScopeError("8.8.8.8 is outside ...")</text>
<rect x="30" y="212" width="190" height="48" rx="4" class="k-blue"/>
<text x="125.0" y="240.5" text-anchor="middle" class="km-blue">TcpScanner._probe()</text>
<text x="236" y="241" text-anchor="start" class="s">except (OSError, TimeoutError): port is closed</text>
<path d="M16 150 L16 52" class="ar-red"/>
<text x="360" y="280" text-anchor="middle" class="c">catch where you can do something useful; fail fast and loudly everywhere else</text>
</g>
</svg>
<figcaption>Expected conditions are handled where they occur; unexpected ones travel up to a boundary that can report them.</figcaption>
</figure>

Good error handling separates **expected conditions** from **unexpected failures**:

- A closed port is expected; the scanner handles `OSError` and timeouts locally by reporting the port as closed.
- An out-of-scope target is a user error; the domain raises a specific exception, `ScopeError`, with a message that names the address.
- At the **boundary**, `cli.main()` catches the known exception types and turns them into a clear message and exit status 2. It does not catch everything: an unexpected `TypeError` should crash loudly with a traceback, because it is a bug.

Practices:

- **Raise specific exceptions** with useful messages; define your own types (`ScopeError`) for domain errors.
- **Never silently swallow exceptions** (`except: pass`). If ignoring one is right, say why in a comment.
- **Fail fast**: validate inputs at the boundary (`parse_ports` rejects port 0 immediately) rather than failing mysteriously later.
- **Clean up reliably** with `with` statements and `try/finally`. Chapter 10 shows how NetWarden's tests found unclosed database connections, fixed by making `ScanRepository` a context manager.
- **Use exit codes** consistently for command-line tools: NetWarden documents 0 (fine), 1 (findings at or above the threshold), and 2 (error), so scripts can rely on them.

## Types

<figure class="diagram">
<svg viewBox="0 0 720 220" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Type hints and a static type checker find a class of bugs before the code runs. Example: worst() is declared to return Severity or None, so comparing its result directly with Severity.HIGH is reported by mypy as an unsupported operation on None, before the code ever runs." xmlns="http://www.w3.org/2000/svg">
<style>
.s9d{ font-family:var(--sans),sans-serif; }
.s9d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s9d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s9d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s9d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s9d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s9d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s9d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s9d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s9d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s9d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s9d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s9d .s{ fill:var(--text-dim); font-size:13px; }
.s9d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s9d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s9d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s9d .c{ fill:var(--text-faint); font-size:12.5px; }
.s9d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s9d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s9d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s9d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9d-a); }
.s9d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9d-a); marker-start:url(#s9d-s); }
.s9d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s9d-g); }
.s9d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s9d-a); }
.s9d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s9d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s9d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s9d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s9d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s9d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9d-tri); }
.s9d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9d-tri); }
.s9d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9d-open); }
.s9d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9d-open); }
.s9d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9d-dia); }
.s9d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9d-odia); }
.s9d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9d-dia); marker-end:url(#s9d-open); }
.s9d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9d-solid); }
.s9d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s9d-open); }
.s9d .fill{ fill:var(--text); stroke:none; }
.s9d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s9d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s9d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s9d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s9d .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s9d .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s9d .ks-red{ fill:#A32D2D; font-size:13px; }
.s9d .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s9d .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9d .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s9d .kb-red, :root[data-theme="dark"] .s9d .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s9d .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s9d .kh-red{ fill:#F09595; }
.s9d .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s9d-red); }
.s9d .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9d-red); }
.s9d .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s9d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s9d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s9d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s9d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s9d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s9d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s9d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s9d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s9d-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s9d">
<rect x="20" y="20" width="330" height="120" rx="7" class="pnl"/>
<text x="185.0" y="54.5" text-anchor="middle" class="m">def worst(self) -&gt; Severity | None:</text>
<text x="185.0" y="74.5" text-anchor="middle" class="c"></text>
<text x="185.0" y="94.5" text-anchor="middle" class="m">if result.worst() &gt;= Severity.HIGH:</text>
<text x="185.0" y="114.5" text-anchor="middle" class="m">    ...</text>
<rect x="370" y="20" width="330" height="120" rx="7" class="k-red"/>
<text x="535.0" y="54.5" text-anchor="middle" class="kb-red">mypy:</text>
<text x="535.0" y="74.5" text-anchor="middle" class="km-red">Unsupported operand types for &gt;=</text>
<text x="535.0" y="94.5" text-anchor="middle" class="km-red">("None" and "Severity")</text>
<text x="535.0" y="114.5" text-anchor="middle" class="ks-red">worst() may return None!</text>
<text x="360" y="176" text-anchor="middle" class="m">the fix: worst = result.worst(); if worst is not None and worst &gt;= ...</text>
<text x="360" y="204" text-anchor="middle" class="c">NetWarden runs mypy in strict mode: every function is annotated</text>
</g>
</svg>
<figcaption>Types are documentation that a tool checks. They also make editors' completion and refactoring far more reliable.</figcaption>
</figure>

Python is dynamically typed, but **type hints** (PEP 484) plus a **static type checker** such as mypy catch whole classes of errors before the code runs: misspelled attributes, wrong argument types, forgotten `None` checks. NetWarden runs mypy in **strict** mode, which requires annotations everywhere. Types also make code self-documenting and make editors' completion and automated refactoring far more reliable.

Other ways to make illegal states unrepresentable:

- `Enum` for fixed sets of values (`Severity`) instead of strings;
- `@dataclass(frozen=True)` for values that should not change (`Finding`);
- `Protocol` for interfaces (`Check`, `Reporter`).

## Formatting, linting and the toolchain

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The local quality toolchain, run automatically by a pre-commit hook before each commit and again in CI: a formatter rewrites layout, a linter such as ruff finds bugs and style problems, a type checker such as mypy finds type errors, and pytest runs the tests." xmlns="http://www.w3.org/2000/svg">
<style>
.s9c{ font-family:var(--sans),sans-serif; }
.s9c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s9c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s9c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s9c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s9c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s9c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s9c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s9c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s9c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s9c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s9c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s9c .s{ fill:var(--text-dim); font-size:13px; }
.s9c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s9c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s9c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s9c .c{ fill:var(--text-faint); font-size:12.5px; }
.s9c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s9c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s9c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s9c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9c-a); }
.s9c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s9c-a); marker-start:url(#s9c-s); }
.s9c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s9c-g); }
.s9c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-a); }
.s9c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s9c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s9c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s9c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s9c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s9c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9c-tri); }
.s9c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-tri); }
.s9c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9c-open); }
.s9c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-open); }
.s9c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9c-dia); }
.s9c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9c-odia); }
.s9c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s9c-dia); marker-end:url(#s9c-open); }
.s9c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s9c-solid); }
.s9c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s9c-open); }
.s9c .fill{ fill:var(--text); stroke:none; }
.s9c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s9c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s9c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s9c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s9c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s9c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s9c .ks-amber{ fill:#854F0B; font-size:13px; }
.s9c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s9c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s9c .kb-amber, :root[data-theme="dark"] .s9c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s9c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s9c .kh-amber{ fill:#EF9F27; }
.s9c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s9c-amber); }
.s9c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-amber); }
.s9c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s9c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s9c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s9c .ks-purple{ fill:#534AB7; font-size:13px; }
.s9c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s9c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s9c .kb-purple, :root[data-theme="dark"] .s9c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s9c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s9c .kh-purple{ fill:#AFA9EC; }
.s9c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s9c-purple); }
.s9c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-purple); }
.s9c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s9c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s9c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s9c .ks-green{ fill:#3B6D11; font-size:13px; }
.s9c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s9c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s9c .kb-green, :root[data-theme="dark"] .s9c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s9c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s9c .kh-green{ fill:#97C459; }
.s9c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s9c-green); }
.s9c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-green); }
.s9c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s9c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s9c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s9c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s9c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s9c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s9c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s9c .kb-gray, :root[data-theme="dark"] .s9c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s9c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s9c .kh-gray{ fill:#B4B2A9; }
.s9c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s9c-gray); }
.s9c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s9c-gray); }
.s9c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s9c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s9c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s9c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s9c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s9c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s9c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s9c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s9c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s9c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s9c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s9c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s9c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s9c">
<rect x="20" y="60" width="152" height="64" rx="7" class="k-gray"/>
<text x="96.0" y="87.5" text-anchor="middle" class="kb-gray">format</text>
<text x="96.0" y="105.5" text-anchor="middle" class="km-gray">ruff format</text>
<rect x="196" y="60" width="152" height="64" rx="7" class="k-amber"/>
<text x="272.0" y="87.5" text-anchor="middle" class="kb-amber">lint</text>
<text x="272.0" y="105.5" text-anchor="middle" class="km-amber">ruff check</text>
<line x1="174" y1="92" x2="194" y2="92" class="ar"/>
<rect x="372" y="60" width="152" height="64" rx="7" class="k-purple"/>
<text x="448.0" y="87.5" text-anchor="middle" class="kb-purple">type check</text>
<text x="448.0" y="105.5" text-anchor="middle" class="km-purple">mypy --strict</text>
<line x1="350" y1="92" x2="370" y2="92" class="ar"/>
<rect x="548" y="60" width="152" height="64" rx="7" class="k-green"/>
<text x="624.0" y="87.5" text-anchor="middle" class="kb-green">test</text>
<text x="624.0" y="105.5" text-anchor="middle" class="km-green">pytest --cov</text>
<line x1="526" y1="92" x2="546" y2="92" class="ar"/>
<text x="360" y="34" text-anchor="middle" class="kh-gray">git commit triggers pre-commit hooks</text>
<text x="360" y="160" text-anchor="middle" class="c">the same commands run in CI (Chapter 13): what passes locally passes in the pipeline</text>
<text x="360" y="190" text-anchor="middle" class="c">machines check the boring things, so humans can review the interesting ones</text>
</g>
</svg>
<figcaption>Automate every rule that can be automated. Every rule left to memory will be broken.</figcaption>
</figure>

Arguments about formatting waste review time. Choose a formatter and let it decide. NetWarden configures **ruff** in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 120
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP", "S"]   # pycodestyle, pyflakes, isort, bugbear, pyupgrade, bandit security rules
ignore = ["S101"]                               # assert is fine in tests
```

The `S` rules come from **bandit** and flag security problems such as `subprocess` calls with `shell=True`, hard-coded passwords, or `pickle` on untrusted data.

To run the tools automatically before every commit, use the **pre-commit** framework with a `.pre-commit-config.yaml` file. The same commands run in CI (Chapter 13), so a change that passes locally passes in the pipeline.

## Hands on: clean it up

The following function is legal Python and works. Rewrite it using this chapter's guidelines, then compare with how NetWarden actually does it in `fingerprint.py` and `checks.py`.

```python
def p(s, x=0):
    r = []
    if s[1].startswith("SSH-2.0-OpenSSH_"):
        v = s[1][16:].split(" ")[0]
        if v >= "8.5p1" and v < "9.8p1":   # bug: string comparison
            r.append((s[0], "bad ssh", 3))
    if s[0] == 23 or s[0] == 21:
        r.append((s[0], "cleartext", 2))
    return r
```

How many problems can you find? At least: meaningless names, a magic slice offset, tuples instead of objects, magic severity numbers, an unused parameter, mixed concerns (parsing and checking), and a real bug: comparing versions as strings means `"10.0p1" < "8.5p1"`. NetWarden's `version_key` exists precisely to avoid that bug, and `test_version_key_orders_real_versions` proves it.

## Summary

- Code is read much more than written; optimise for the reader.
- Use **intention-revealing names** from the domain, following language conventions.
- Write **small functions** that do one thing at one level of abstraction, with few parameters and no hidden side effects.
- **Comments explain why**; docstrings document contracts; otherwise let the code speak.
- Handle **expected conditions** locally, raise **specific exceptions**, and report failures at a **boundary**; never swallow errors silently.
- Use **type hints** and a strict **type checker**; prefer enums, frozen dataclasses and protocols.
- Let a **formatter** and **linter** enforce style automatically, locally and in CI.

## Check your understanding

Choose the best answer for each question, then check your answers in [Answers to Chapter Questions](answers.md#chapter-9-clean-code).

**1. Why optimise code for the reader?**

- A. Code is read far more often than it is written
- B. Readers pay for software
- C. Compilers prefer readable code
- D. Short code runs faster

**2. Which is the best name for a variable holding the open services found on a host?**

- A. data
- B. list1
- C. open_services
- D. x

**3. What should a comment usually explain?**

- A. What the code does, line by line
- B. Why the code is the way it is
- C. Who wrote it
- D. When it was written

**4. How should a function be designed?**

- A. Long, to keep logic together
- B. With many flags to cover all cases
- C. With global state for speed
- D. Small, doing one thing at one level of abstraction, with few parameters and no hidden side effects

**5. What is wrong with except Exception: pass?**

- A. Nothing
- B. It silently swallows every error, hiding failures
- C. It is slow
- D. It is not valid Python

**6. What do type hints plus a strict type checker give you?**

- A. Faster programs
- B. Automatic tests
- C. Smaller files
- D. Errors caught before running, and documentation that cannot go stale

**7. Who should enforce code formatting?**

- A. A formatter and linter, automatically, locally and in CI
- B. Reviewers, in comments
- C. The team lead
- D. Nobody

**8. Which describes an expected condition, such as a closed port during a scan?**

- A. An exception to raise and crash
- B. A bug
- C. A normal outcome to handle locally
- D. A reason to stop the scan
