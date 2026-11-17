# Chapter 8: Version Control and Collaboration

Every artifact of a software project changes: code, tests, documentation, configuration, even the diagrams in this book. **Configuration management** is the discipline of knowing exactly which version of every artifact went into each release, who changed what, and why. Its central tool is a **version control system** (VCS). Today that almost always means **Git**, created by Linus Torvalds in 2005 for the Linux kernel, usually hosted on a platform such as GitHub or GitLab. This chapter covers how Git works, how teams use it to collaborate, and the review practices that go with it.

## Why version control

- **History**: every change, with author, date and reason; any earlier version can be recovered.
- **Collaboration**: many people change the same code in parallel and combine their work.
- **Accountability and audit**: who approved this change to the scope logic, and when?
- **Experimentation**: branches let you try ideas without risk to working code.
- **Reproducibility**: a tag such as `v1.0.0` identifies exactly what was released.

Git is **distributed**: every clone holds the full history, so developers commit, branch and inspect history offline, and there is no single point of failure.

## How Git stores work

<figure class="diagram">
<svg viewBox="0 0 720 220" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Git&#x27;s areas: the working tree where you edit files, the staging area or index where you assemble the next commit, the local repository of commits, and a remote repository such as GitHub. git add moves changes to the staging area, git commit records them, git push sends commits to the remote, and git pull brings others&#x27; commits back." xmlns="http://www.w3.org/2000/svg">
<style>
.s8a{ font-family:var(--sans),sans-serif; }
.s8a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8a .s{ fill:var(--text-dim); font-size:13px; }
.s8a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8a .c{ fill:var(--text-faint); font-size:12.5px; }
.s8a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8a-a); }
.s8a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8a-a); marker-start:url(#s8a-s); }
.s8a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8a-g); }
.s8a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-a); }
.s8a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8a-tri); }
.s8a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-tri); }
.s8a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8a-open); }
.s8a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-open); }
.s8a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8a-dia); }
.s8a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8a-odia); }
.s8a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8a-dia); marker-end:url(#s8a-open); }
.s8a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8a-solid); }
.s8a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8a-open); }
.s8a .fill{ fill:var(--text); stroke:none; }
.s8a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s8a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s8a .ks-blue{ fill:#185FA5; font-size:13px; }
.s8a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s8a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s8a .kb-blue, :root[data-theme="dark"] .s8a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s8a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s8a .kh-blue{ fill:#85B7EB; }
.s8a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s8a-blue); }
.s8a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-blue); }
.s8a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s8a .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s8a .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s8a .ks-amber{ fill:#854F0B; font-size:13px; }
.s8a .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s8a .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8a .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s8a .kb-amber, :root[data-theme="dark"] .s8a .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s8a .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s8a .kh-amber{ fill:#EF9F27; }
.s8a .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s8a-amber); }
.s8a .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-amber); }
.s8a .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s8a .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s8a .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s8a .ks-purple{ fill:#534AB7; font-size:13px; }
.s8a .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s8a .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8a .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s8a .kb-purple, :root[data-theme="dark"] .s8a .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s8a .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s8a .kh-purple{ fill:#AFA9EC; }
.s8a .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s8a-purple); }
.s8a .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-purple); }
.s8a .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s8a .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s8a .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s8a .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s8a .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s8a .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8a .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s8a .kb-gray, :root[data-theme="dark"] .s8a .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s8a .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s8a .kh-gray{ fill:#B4B2A9; }
.s8a .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s8a-gray); }
.s8a .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8a-gray); }
.s8a .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s8a-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s8a-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s8a-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s8a">
<rect x="20" y="40" width="152" height="64" rx="7" class="k-gray"/>
<text x="96.0" y="67.5" text-anchor="middle" class="kb-gray">working tree</text>
<text x="96.0" y="85.5" text-anchor="middle" class="ks-gray">your files</text>
<rect x="196" y="40" width="152" height="64" rx="7" class="k-amber"/>
<text x="272.0" y="67.5" text-anchor="middle" class="kb-amber">staging area</text>
<text x="272.0" y="85.5" text-anchor="middle" class="ks-amber">the next commit</text>
<rect x="372" y="40" width="152" height="64" rx="7" class="k-blue"/>
<text x="448.0" y="67.5" text-anchor="middle" class="kb-blue">local repository</text>
<text x="448.0" y="85.5" text-anchor="middle" class="ks-blue">commit history</text>
<rect x="548" y="40" width="152" height="64" rx="7" class="k-purple"/>
<text x="624.0" y="67.5" text-anchor="middle" class="kb-purple">remote</text>
<text x="624.0" y="85.5" text-anchor="middle" class="ks-purple">GitHub</text>
<line x1="172" y1="62" x2="194" y2="62" class="ar"/>
<text x="183" y="30" text-anchor="middle" class="m">git add</text>
<line x1="348" y1="62" x2="370" y2="62" class="ar"/>
<text x="359" y="30" text-anchor="middle" class="m">git commit</text>
<line x1="524" y1="62" x2="546" y2="62" class="ar"/>
<text x="535" y="30" text-anchor="middle" class="m">git push</text>
<path d="M600 106 C 600 170, 96 170, 96 108" class="ad"/>
<text x="348" y="178" text-anchor="middle" class="m">git pull  (fetch + merge)</text>
</g>
</svg>
<figcaption>Staging lets you commit some changes and not others, so each commit is one logical step.</figcaption>
</figure>

A typical cycle:

```bash
git switch -c feature/US-7-scan-diff     # create and switch to a branch
# ... edit store.py and tests ...
git status                                # what changed?
git diff                                  # how did it change?
git add src/netwarden/store.py tests/test_integration.py
git commit -m "feat(store): compare two saved scans (US-7)"
git push -u origin feature/US-7-scan-diff
```

<figure class="diagram">
<svg viewBox="0 0 720 220" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Commits form a directed acyclic graph. On main: c1, c2, c3, c5. A feature branch for US-7 starts at c2 with commits c4 and c6. A merge commit m joins the branch back into main. Branch names and HEAD are just movable pointers to commits." xmlns="http://www.w3.org/2000/svg">
<style>
.s8b{ font-family:var(--sans),sans-serif; }
.s8b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8b .s{ fill:var(--text-dim); font-size:13px; }
.s8b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8b .c{ fill:var(--text-faint); font-size:12.5px; }
.s8b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8b-a); }
.s8b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8b-a); marker-start:url(#s8b-s); }
.s8b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8b-g); }
.s8b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-a); }
.s8b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8b-tri); }
.s8b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-tri); }
.s8b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8b-open); }
.s8b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-open); }
.s8b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8b-dia); }
.s8b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8b-odia); }
.s8b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8b-dia); marker-end:url(#s8b-open); }
.s8b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8b-solid); }
.s8b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8b-open); }
.s8b .fill{ fill:var(--text); stroke:none; }
.s8b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s8b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s8b .ks-blue{ fill:#185FA5; font-size:13px; }
.s8b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s8b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s8b .kb-blue, :root[data-theme="dark"] .s8b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s8b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s8b .kh-blue{ fill:#85B7EB; }
.s8b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s8b-blue); }
.s8b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-blue); }
.s8b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s8b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s8b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s8b .ks-amber{ fill:#854F0B; font-size:13px; }
.s8b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s8b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s8b .kb-amber, :root[data-theme="dark"] .s8b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s8b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s8b .kh-amber{ fill:#EF9F27; }
.s8b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s8b-amber); }
.s8b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-amber); }
.s8b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s8b .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s8b .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s8b .ks-green{ fill:#3B6D11; font-size:13px; }
.s8b .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s8b .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8b .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s8b .kb-green, :root[data-theme="dark"] .s8b .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s8b .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s8b .kh-green{ fill:#97C459; }
.s8b .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s8b-green); }
.s8b .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-green); }
.s8b .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s8b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s8b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s8b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s8b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s8b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s8b .kb-gray, :root[data-theme="dark"] .s8b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s8b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s8b .kh-gray{ fill:#B4B2A9; }
.s8b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s8b-gray); }
.s8b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8b-gray); }
.s8b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s8b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s8b-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s8b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s8b">
<circle cx="60" cy="70" r="13" class="k-blue"/>
<text x="60" y="74.5" text-anchor="middle" class="kb-blue">c1</text>
<circle cx="150" cy="70" r="13" class="k-blue"/>
<text x="150" y="74.5" text-anchor="middle" class="kb-blue">c2</text>
<line x1="73" y1="70" x2="137" y2="70" class="ln-blue"/>
<circle cx="240" cy="70" r="13" class="k-blue"/>
<text x="240" y="74.5" text-anchor="middle" class="kb-blue">c3</text>
<line x1="163" y1="70" x2="227" y2="70" class="ln-blue"/>
<circle cx="380" cy="70" r="13" class="k-blue"/>
<text x="380" y="74.5" text-anchor="middle" class="kb-blue">c5</text>
<line x1="253" y1="70" x2="367" y2="70" class="ln-blue"/>
<circle cx="290" cy="150" r="13" class="k-amber"/>
<text x="290" y="154.5" text-anchor="middle" class="kb-amber">c4</text>
<circle cx="420" cy="150" r="13" class="k-amber"/>
<text x="420" y="154.5" text-anchor="middle" class="kb-amber">c6</text>
<line x1="162" y1="78" x2="278" y2="144" class="ln-amber"/>
<line x1="303" y1="150" x2="407" y2="150" class="ln-amber"/>
<circle cx="520" cy="70" r="13" class="k-green"/>
<text x="520" y="74.5" text-anchor="middle" class="kb-green">m</text>
<line x1="393" y1="70" x2="507" y2="70" class="ln-blue"/>
<line x1="432" y1="144" x2="508" y2="78" class="ln-amber"/>
<rect x="580" y="52" width="110" height="36" rx="4" class="k-blue"/>
<text x="635.0" y="74.5" text-anchor="middle" class="kb-blue">main</text>
<line x1="578" y1="70" x2="534" y2="70" class="ar-blue"/>
<rect x="470" y="170" width="160" height="36" rx="4" class="k-amber"/>
<text x="550.0" y="192.5" text-anchor="middle" class="km-amber">feature/US-7-diff</text>
<line x1="468" y1="180" x2="434" y2="158" class="ar-amber"/>
<rect x="580" y="10" width="110" height="30" rx="4" class="k-gray"/>
<text x="635.0" y="29.5" text-anchor="middle" class="km-gray">HEAD</text>
<line x1="635" y1="40" x2="635" y2="50" class="ar"/>
</g>
</svg>
<figcaption>A branch is not a copy of the code; it is a 41-byte file naming a commit. That is why Git branches are cheap.</figcaption>
</figure>

Each commit is a snapshot of the whole project plus metadata and a pointer to its parent(s), identified by a hash of its contents. History is a **directed acyclic graph** of commits. A **branch** is a movable pointer to a commit; `HEAD` points to the branch you are on. Because branches are so cheap, Git encourages using one for every piece of work.

### Integrating work: merge and rebase

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Merge versus rebase. Merging the feature branch creates a merge commit with two parents and keeps the true history. Rebasing replays the feature commits c4 and c6 on top of main as new commits c4&#x27; and c6&#x27;, giving a straight line; the old commits are abandoned, so never rebase commits others already have." xmlns="http://www.w3.org/2000/svg">
<style>
.s8c{ font-family:var(--sans),sans-serif; }
.s8c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8c .s{ fill:var(--text-dim); font-size:13px; }
.s8c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .c{ fill:var(--text-faint); font-size:12.5px; }
.s8c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8c-a); }
.s8c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8c-a); marker-start:url(#s8c-s); }
.s8c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8c-g); }
.s8c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-a); }
.s8c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8c-tri); }
.s8c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-tri); }
.s8c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8c-open); }
.s8c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-open); }
.s8c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8c-dia); }
.s8c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8c-odia); }
.s8c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8c-dia); marker-end:url(#s8c-open); }
.s8c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8c-solid); }
.s8c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8c-open); }
.s8c .fill{ fill:var(--text); stroke:none; }
.s8c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s8c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s8c .ks-blue{ fill:#185FA5; font-size:13px; }
.s8c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s8c .kb-blue, :root[data-theme="dark"] .s8c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s8c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s8c .kh-blue{ fill:#85B7EB; }
.s8c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s8c-blue); }
.s8c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-blue); }
.s8c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s8c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s8c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s8c .ks-amber{ fill:#854F0B; font-size:13px; }
.s8c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s8c .kb-amber, :root[data-theme="dark"] .s8c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s8c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s8c .kh-amber{ fill:#EF9F27; }
.s8c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s8c-amber); }
.s8c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-amber); }
.s8c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s8c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s8c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s8c .ks-purple{ fill:#534AB7; font-size:13px; }
.s8c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s8c .kb-purple, :root[data-theme="dark"] .s8c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s8c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s8c .kh-purple{ fill:#AFA9EC; }
.s8c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s8c-purple); }
.s8c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-purple); }
.s8c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s8c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s8c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s8c .ks-green{ fill:#3B6D11; font-size:13px; }
.s8c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s8c .kb-green, :root[data-theme="dark"] .s8c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s8c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s8c .kh-green{ fill:#97C459; }
.s8c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s8c-green); }
.s8c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-green); }
.s8c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s8c .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s8c .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s8c .ks-red{ fill:#A32D2D; font-size:13px; }
.s8c .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s8c .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8c .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s8c .kb-red, :root[data-theme="dark"] .s8c .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s8c .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s8c .kh-red{ fill:#F09595; }
.s8c .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s8c-red); }
.s8c .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8c-red); }
.s8c .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s8c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s8c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s8c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s8c-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s8c">
<text x="180" y="20" text-anchor="middle" class="kh-blue">merge: true history</text>
<circle cx="40" cy="70" r="13" class="k-blue"/>
<text x="40" y="74.5" text-anchor="middle" class="kb-blue">c2</text>
<circle cx="120" cy="70" r="13" class="k-blue"/>
<text x="120" y="74.5" text-anchor="middle" class="kb-blue">c3</text>
<line x1="53" y1="70" x2="107" y2="70" class="ln-blue"/>
<circle cx="200" cy="70" r="13" class="k-blue"/>
<text x="200" y="74.5" text-anchor="middle" class="kb-blue">c5</text>
<line x1="133" y1="70" x2="187" y2="70" class="ln-blue"/>
<circle cx="120" cy="150" r="13" class="k-amber"/>
<text x="120" y="154.5" text-anchor="middle" class="kb-amber">c4</text>
<circle cx="200" cy="150" r="13" class="k-amber"/>
<text x="200" y="154.5" text-anchor="middle" class="kb-amber">c6</text>
<circle cx="290" cy="70" r="13" class="k-green"/>
<text x="290" y="74.5" text-anchor="middle" class="kb-green">m</text>
<line x1="48" y1="80" x2="110" y2="142" class="ln-amber"/>
<line x1="133" y1="150" x2="187" y2="150" class="ln-amber"/>
<line x1="213" y1="70" x2="277" y2="70" class="ln-blue"/>
<line x1="212" y1="142" x2="280" y2="80" class="ln-amber"/>
<text x="540" y="20" text-anchor="middle" class="kh-purple">rebase: straight line</text>
<circle cx="400" cy="70" r="13" class="k-blue"/>
<text x="400" y="74.5" text-anchor="middle" class="kb-blue">c2</text>
<circle cx="470" cy="70" r="13" class="k-blue"/>
<text x="470" y="74.5" text-anchor="middle" class="kb-blue">c3</text>
<line x1="413" y1="70" x2="457" y2="70" class="ln-blue"/>
<circle cx="540" cy="70" r="13" class="k-blue"/>
<text x="540" y="74.5" text-anchor="middle" class="kb-blue">c5</text>
<line x1="483" y1="70" x2="527" y2="70" class="ln-blue"/>
<circle cx="610" cy="70" r="13" class="k-purple"/>
<text x="610" y="74.5" text-anchor="middle" class="kb-purple">c4'</text>
<line x1="553" y1="70" x2="597" y2="70" class="ln-blue"/>
<circle cx="680" cy="70" r="13" class="k-purple"/>
<text x="680" y="74.5" text-anchor="middle" class="kb-purple">c6'</text>
<line x1="623" y1="70" x2="667" y2="70" class="ln-blue"/>
<circle cx="470" cy="150" r="13" class="k-amber" style="opacity:0.35"/>
<circle cx="540" cy="150" r="13" class="k-amber" style="opacity:0.35"/>
<text x="505" y="186" text-anchor="middle" class="c">old c4, c6: abandoned</text>
<text x="360" y="236" text-anchor="middle" class="kh-red">golden rule: rebase only your own, unpushed (or unshared) commits</text>
</g>
</svg>
<figcaption>Both integrate the same changes. Teams choose by whether they value an exact record or a readable line.</figcaption>
</figure>

When two lines of work have diverged, Git can **merge** them, creating a commit with two parents, or **rebase** one onto the other, rewriting its commits as if they had been made later. Both give the same final code. Merging preserves what actually happened; rebasing gives a tidier, linear history. Many teams rebase their own feature branch locally to keep it current, then **squash-merge** it into `main`, so each pull request becomes one commit on `main`.

### Conflicts

If two branches change the same lines, Git cannot decide and marks a **conflict**:

```text
<<<<<<< HEAD
TOP_PORTS = [21, 22, 23, 25, 80, 443]
=======
TOP_PORTS = [21, 22, 23, 80, 443, 3389]
>>>>>>> feature/rdp-check
```

You edit the file to the correct combined result (here, probably both 25 and 3389), remove the markers, run the tests, then `git add` and continue. Conflicts are not errors; they are Git asking a human to make a decision. Small, frequent integrations keep them small.

## Collaboration workflows

### GitHub flow

<figure class="diagram">
<svg viewBox="0 0 720 240" style="width:100%;height:auto;max-width:720px" role="img" aria-label="GitHub flow for NetWarden: create a short-lived branch from main; commit small steps; push and open a pull request; CI runs lint, type checks and tests while teammates review; address feedback; squash and merge to main; delete the branch. Main is always releasable." xmlns="http://www.w3.org/2000/svg">
<style>
.s8d{ font-family:var(--sans),sans-serif; }
.s8d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8d .s{ fill:var(--text-dim); font-size:13px; }
.s8d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .c{ fill:var(--text-faint); font-size:12.5px; }
.s8d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8d-a); }
.s8d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8d-a); marker-start:url(#s8d-s); }
.s8d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8d-g); }
.s8d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-a); }
.s8d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8d-tri); }
.s8d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-tri); }
.s8d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8d-open); }
.s8d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-open); }
.s8d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8d-dia); }
.s8d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8d-odia); }
.s8d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8d-dia); marker-end:url(#s8d-open); }
.s8d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8d-solid); }
.s8d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8d-open); }
.s8d .fill{ fill:var(--text); stroke:none; }
.s8d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8d .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s8d .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s8d .ks-blue{ fill:#185FA5; font-size:13px; }
.s8d .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8d .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s8d .kb-blue, :root[data-theme="dark"] .s8d .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s8d .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s8d .kh-blue{ fill:#85B7EB; }
.s8d .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s8d-blue); }
.s8d .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-blue); }
.s8d .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s8d .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s8d .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s8d .ks-teal{ fill:#0F6E56; font-size:13px; }
.s8d .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8d .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s8d .kb-teal, :root[data-theme="dark"] .s8d .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s8d .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s8d .kh-teal{ fill:#5DCAA5; }
.s8d .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s8d-teal); }
.s8d .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-teal); }
.s8d .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s8d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s8d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s8d .ks-amber{ fill:#854F0B; font-size:13px; }
.s8d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s8d .kb-amber, :root[data-theme="dark"] .s8d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s8d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s8d .kh-amber{ fill:#EF9F27; }
.s8d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s8d-amber); }
.s8d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-amber); }
.s8d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s8d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s8d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s8d .ks-purple{ fill:#534AB7; font-size:13px; }
.s8d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s8d .kb-purple, :root[data-theme="dark"] .s8d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s8d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s8d .kh-purple{ fill:#AFA9EC; }
.s8d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s8d-purple); }
.s8d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-purple); }
.s8d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s8d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s8d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s8d .ks-green{ fill:#3B6D11; font-size:13px; }
.s8d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s8d .kb-green, :root[data-theme="dark"] .s8d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s8d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s8d .kh-green{ fill:#97C459; }
.s8d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s8d-green); }
.s8d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-green); }
.s8d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s8d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s8d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s8d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s8d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s8d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s8d .kb-gray, :root[data-theme="dark"] .s8d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s8d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s8d .kh-gray{ fill:#B4B2A9; }
.s8d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s8d-gray); }
.s8d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8d-gray); }
.s8d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8d-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s8d-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s8d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s8d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s8d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s8d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s8d">
<rect x="20" y="70" width="104" height="60" rx="7" class="k-blue"/>
<text x="72.0" y="95.5" text-anchor="middle" class="kb-blue">branch</text>
<text x="72.0" y="113.5" text-anchor="middle" class="ks-blue">from main</text>
<rect x="136" y="70" width="104" height="60" rx="7" class="k-teal"/>
<text x="188.0" y="95.5" text-anchor="middle" class="kb-teal">commit</text>
<text x="188.0" y="113.5" text-anchor="middle" class="ks-teal">small steps</text>
<line x1="124" y1="100" x2="134" y2="100" class="ar"/>
<rect x="252" y="70" width="104" height="60" rx="7" class="k-purple"/>
<text x="304.0" y="95.5" text-anchor="middle" class="kb-purple">pull request</text>
<text x="304.0" y="113.5" text-anchor="middle" class="ks-purple">describe why</text>
<line x1="240" y1="100" x2="250" y2="100" class="ar"/>
<rect x="368" y="70" width="104" height="60" rx="7" class="k-amber"/>
<text x="420.0" y="95.5" text-anchor="middle" class="kb-amber">CI + review</text>
<text x="420.0" y="113.5" text-anchor="middle" class="ks-amber">comments</text>
<line x1="356" y1="100" x2="366" y2="100" class="ar"/>
<rect x="484" y="70" width="104" height="60" rx="7" class="k-green"/>
<text x="536.0" y="95.5" text-anchor="middle" class="kb-green">merge</text>
<text x="536.0" y="113.5" text-anchor="middle" class="ks-green">squash</text>
<line x1="472" y1="100" x2="482" y2="100" class="ar"/>
<rect x="600" y="70" width="104" height="60" rx="7" class="k-gray"/>
<text x="652.0" y="95.5" text-anchor="middle" class="kb-gray">delete</text>
<text x="652.0" y="113.5" text-anchor="middle" class="ks-gray">branch</text>
<line x1="588" y1="100" x2="598" y2="100" class="ar"/>
<path d="M424 132 C 424 180, 312 180, 312 134" class="ad"/>
<text x="368" y="196" text-anchor="middle" class="c">changes requested</text>
<line x1="20" y1="40" x2="700" y2="40" class="ln-blue"/>
<text x="20" y="30" text-anchor="start" class="kh-blue">main: always releasable, protected</text>
</g>
</svg>
<figcaption>Simple and effective for teams that deploy continuously. Branch protection rules enforce the review and CI steps.</figcaption>
</figure>

NetWarden uses **GitHub flow**: `main` is always releasable and protected, all work happens on short-lived branches, and changes reach `main` only through a **pull request** (PR; GitLab calls it a merge request) that has passed CI and been approved by a reviewer. **Branch protection rules** on the hosting platform enforce this, so even a tired administrator cannot push directly to `main` at midnight.

### Branching strategies

<figure class="diagram">
<svg viewBox="0 0 720 280" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Two branching strategies. Gitflow uses long-lived main and develop branches plus feature, release and hotfix branches, suited to scheduled versioned releases. Trunk-based development has everyone integrating into main at least daily through very short-lived branches, with unfinished features hidden behind feature flags, suited to continuous delivery." xmlns="http://www.w3.org/2000/svg">
<style>
.s8e{ font-family:var(--sans),sans-serif; }
.s8e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8e .s{ fill:var(--text-dim); font-size:13px; }
.s8e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .c{ fill:var(--text-faint); font-size:12.5px; }
.s8e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8e-a); }
.s8e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8e-a); marker-start:url(#s8e-s); }
.s8e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8e-g); }
.s8e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-a); }
.s8e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8e-tri); }
.s8e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-tri); }
.s8e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8e-open); }
.s8e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-open); }
.s8e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8e-dia); }
.s8e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8e-odia); }
.s8e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8e-dia); marker-end:url(#s8e-open); }
.s8e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8e-solid); }
.s8e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8e-open); }
.s8e .fill{ fill:var(--text); stroke:none; }
.s8e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8e .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s8e .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s8e .ks-blue{ fill:#185FA5; font-size:13px; }
.s8e .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8e .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s8e .kb-blue, :root[data-theme="dark"] .s8e .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s8e .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s8e .kh-blue{ fill:#85B7EB; }
.s8e .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s8e-blue); }
.s8e .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-blue); }
.s8e .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s8e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s8e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s8e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s8e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s8e .kb-teal, :root[data-theme="dark"] .s8e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s8e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s8e .kh-teal{ fill:#5DCAA5; }
.s8e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s8e-teal); }
.s8e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-teal); }
.s8e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s8e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s8e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s8e .ks-amber{ fill:#854F0B; font-size:13px; }
.s8e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s8e .kb-amber, :root[data-theme="dark"] .s8e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s8e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s8e .kh-amber{ fill:#EF9F27; }
.s8e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s8e-amber); }
.s8e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-amber); }
.s8e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s8e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s8e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s8e .ks-purple{ fill:#534AB7; font-size:13px; }
.s8e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s8e .kb-purple, :root[data-theme="dark"] .s8e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s8e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s8e .kh-purple{ fill:#AFA9EC; }
.s8e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s8e-purple); }
.s8e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-purple); }
.s8e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s8e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s8e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s8e .ks-green{ fill:#3B6D11; font-size:13px; }
.s8e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s8e .kb-green, :root[data-theme="dark"] .s8e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s8e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s8e .kh-green{ fill:#97C459; }
.s8e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s8e-green); }
.s8e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-green); }
.s8e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s8e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s8e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s8e .ks-red{ fill:#A32D2D; font-size:13px; }
.s8e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s8e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s8e .kb-red, :root[data-theme="dark"] .s8e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s8e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s8e .kh-red{ fill:#F09595; }
.s8e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s8e-red); }
.s8e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8e-red); }
.s8e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8e-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s8e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s8e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s8e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s8e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s8e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s8e">
<text x="180" y="20" text-anchor="middle" class="kh-purple">Gitflow</text>
<text x="20" y="54" text-anchor="start" class="c">main</text>
<line x1="80" y1="50" x2="330" y2="50" class="ln-blue"/>
<text x="20" y="84" text-anchor="start" class="c">hotfix</text>
<line x1="80" y1="80" x2="330" y2="80" class="ln-red"/>
<text x="20" y="114" text-anchor="start" class="c">release</text>
<line x1="80" y1="110" x2="330" y2="110" class="ln-amber"/>
<text x="20" y="144" text-anchor="start" class="c">develop</text>
<line x1="80" y1="140" x2="330" y2="140" class="ln-teal"/>
<text x="20" y="174" text-anchor="start" class="c">feature</text>
<line x1="80" y1="170" x2="330" y2="170" class="ln-purple"/>
<circle cx="100" cy="50" r="6" class="k-blue"/>
<circle cx="300" cy="50" r="6" class="k-blue"/>
<circle cx="220" cy="80" r="6" class="k-red"/>
<circle cx="250" cy="110" r="6" class="k-amber"/>
<circle cx="110" cy="140" r="6" class="k-teal"/>
<circle cx="200" cy="140" r="6" class="k-teal"/>
<circle cx="290" cy="140" r="6" class="k-teal"/>
<circle cx="140" cy="170" r="6" class="k-purple"/>
<circle cx="175" cy="170" r="6" class="k-purple"/>
<line x1="110" y1="140" x2="140" y2="170" class="ln-purple"/>
<line x1="175" y1="170" x2="200" y2="140" class="ln-purple"/>
<line x1="200" y1="140" x2="250" y2="110" class="ln-amber"/>
<line x1="250" y1="110" x2="300" y2="50" class="ln-amber"/>
<line x1="100" y1="50" x2="220" y2="80" class="ln-red"/>
<line x1="220" y1="80" x2="300" y2="50" class="ln-red"/>
<text x="180" y="220" text-anchor="middle" class="c">scheduled releases, several</text>
<text x="180" y="238" text-anchor="middle" class="c">supported versions</text>
<text x="540" y="20" text-anchor="middle" class="kh-green">trunk-based</text>
<text x="390" y="104" text-anchor="start" class="c">main</text>
<line x1="430" y1="100" x2="700" y2="100" class="ln-green"/>
<circle cx="450" cy="100" r="6" class="k-green"/>
<circle cx="482" cy="100" r="6" class="k-green"/>
<path d="M450 100 C 458 70, 474 70, 482 100" class="ln-teal"/>
<circle cx="514" cy="100" r="6" class="k-green"/>
<circle cx="546" cy="100" r="6" class="k-green"/>
<path d="M514 100 C 522 70, 538 70, 546 100" class="ln-teal"/>
<circle cx="578" cy="100" r="6" class="k-green"/>
<circle cx="610" cy="100" r="6" class="k-green"/>
<path d="M578 100 C 586 70, 602 70, 610 100" class="ln-teal"/>
<circle cx="642" cy="100" r="6" class="k-green"/>
<circle cx="674" cy="100" r="6" class="k-green"/>
<path d="M642 100 C 650 70, 666 70, 674 100" class="ln-teal"/>
<text x="560" y="150" text-anchor="middle" class="c">branches live hours, not weeks</text>
<text x="560" y="170" text-anchor="middle" class="c">unfinished work behind feature flags</text>
<text x="560" y="220" text-anchor="middle" class="c">continuous delivery</text>
</g>
</svg>
<figcaption>Long-lived branches delay integration and make merges painful; the DORA research links trunk-based development to better delivery performance.</figcaption>
</figure>

| Strategy | How it works | Suits |
|---|---|---|
| **Gitflow** (Vincent Driessen, 2010) | Long-lived `main` and `develop`; feature, release and hotfix branches | Scheduled, versioned releases; several versions supported at once |
| **GitHub flow** | `main` plus short-lived feature branches and PRs | Web services and tools that deploy often |
| **Trunk-based development** | Everyone integrates into `main` at least daily; unfinished features hidden behind **feature flags** | Continuous delivery; strong automated tests |

Long-lived branches feel safe but delay integration, and the longer two branches diverge, the more painful and risky the merge. The research behind the DORA reports (Chapter 14) found trunk-based development to be one of the practices associated with higher delivery performance. Its author, Driessen, has himself noted that Gitflow is a poor fit for continuously delivered software.

### Forks

Open-source projects add one step: contributors without write access **fork** the repository (their own server-side copy), push branches there, and open pull requests back to the original project.

## Commits that help

<figure class="diagram">
<svg viewBox="0 0 720 220" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Anatomy of a Conventional Commits message: a type such as feat, fix, docs, test or refactor; an optional scope in parentheses; a short imperative summary; a blank line; a body explaining why; and footers such as Refs US-7 or BREAKING CHANGE." xmlns="http://www.w3.org/2000/svg">
<style>
.s8f{ font-family:var(--sans),sans-serif; }
.s8f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8f .s{ fill:var(--text-dim); font-size:13px; }
.s8f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8f .c{ fill:var(--text-faint); font-size:12.5px; }
.s8f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8f-a); }
.s8f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8f-a); marker-start:url(#s8f-s); }
.s8f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8f-g); }
.s8f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8f-a); }
.s8f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8f-tri); }
.s8f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8f-tri); }
.s8f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8f-open); }
.s8f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8f-open); }
.s8f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8f-dia); }
.s8f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8f-odia); }
.s8f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8f-dia); marker-end:url(#s8f-open); }
.s8f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8f-solid); }
.s8f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8f-open); }
.s8f .fill{ fill:var(--text); stroke:none; }
.s8f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8f .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s8f .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s8f .ks-coral{ fill:#993C1D; font-size:13px; }
.s8f .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s8f .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8f .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s8f .kb-coral, :root[data-theme="dark"] .s8f .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s8f .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s8f .kh-coral{ fill:#F0997B; }
.s8f .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s8f-coral); }
.s8f .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8f-coral); }
.s8f .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8f-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s8f">
<rect x="20" y="20" width="680" height="160" rx="7" class="pnl"/>
<text x="40" y="50" text-anchor="start" class="m">feat(store): compare two saved scans (US-7)</text>
<text x="40" y="90" text-anchor="start" class="m">Add ScanRepository.get() and diff(), which classify findings as</text>
<text x="40" y="110" text-anchor="start" class="m">new, resolved or unchanged by (host, port, CVE or check id).</text>
<text x="40" y="150" text-anchor="start" class="m">Refs: US-7, NW-FR-9</text>
<text x="470" y="50" text-anchor="start" class="kh-coral">type(scope): summary, &lt; 72 chars</text>
<text x="560" y="100" text-anchor="start" class="kh-coral">body: why, not how</text>
<text x="470" y="150" text-anchor="start" class="kh-coral">footers: links, BREAKING CHANGE</text>
<text x="360" y="206" text-anchor="middle" class="c">feat bumps MINOR, fix bumps PATCH, BREAKING CHANGE bumps MAJOR (Chapter 13)</text>
</g>
</svg>
<figcaption>Consistent messages make history searchable and let tools generate changelogs and version numbers.</figcaption>
</figure>

Good commits are **atomic** (one logical change that builds and passes tests) and have messages that explain **why**. The **Conventional Commits** specification adds a machine-readable prefix, which tools use to generate changelogs and choose the next version number (Chapter 13). NetWarden's `CONTRIBUTING.md` requires it, and every message links to a story or requirement ID, which provides traceability (Chapter 3) for free.

## Code review

Code review is one of the most effective quality practices known. Studies of inspections since Michael Fagan's work at IBM in the 1970s have found that reviews catch a large share of defects before testing, and modern review spreads knowledge across the team as a side effect.

<figure class="diagram">
<svg viewBox="0 0 720 250" style="width:100%;height:auto;max-width:720px" role="img" aria-label="What reviewers look for in a pull request, in priority order: correctness and requirements; design and fit with the architecture; security and safety; tests; readability and naming; documentation. Style issues are left to automated formatters and linters." xmlns="http://www.w3.org/2000/svg">
<style>
.s8g{ font-family:var(--sans),sans-serif; }
.s8g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s8g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s8g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s8g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s8g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s8g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s8g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s8g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s8g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s8g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s8g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s8g .s{ fill:var(--text-dim); font-size:13px; }
.s8g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s8g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .c{ fill:var(--text-faint); font-size:12.5px; }
.s8g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s8g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s8g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s8g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8g-a); }
.s8g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s8g-a); marker-start:url(#s8g-s); }
.s8g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s8g-g); }
.s8g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-a); }
.s8g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s8g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s8g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s8g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s8g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s8g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8g-tri); }
.s8g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-tri); }
.s8g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8g-open); }
.s8g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-open); }
.s8g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8g-dia); }
.s8g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8g-odia); }
.s8g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s8g-dia); marker-end:url(#s8g-open); }
.s8g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s8g-solid); }
.s8g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s8g-open); }
.s8g .fill{ fill:var(--text); stroke:none; }
.s8g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s8g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s8g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s8g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s8g .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s8g .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s8g .ks-blue{ fill:#185FA5; font-size:13px; }
.s8g .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8g .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s8g .kb-blue, :root[data-theme="dark"] .s8g .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s8g .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s8g .kh-blue{ fill:#85B7EB; }
.s8g .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s8g-blue); }
.s8g .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-blue); }
.s8g .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s8g .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s8g .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s8g .ks-teal{ fill:#0F6E56; font-size:13px; }
.s8g .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8g .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s8g .kb-teal, :root[data-theme="dark"] .s8g .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s8g .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s8g .kh-teal{ fill:#5DCAA5; }
.s8g .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s8g-teal); }
.s8g .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-teal); }
.s8g .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s8g .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s8g .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s8g .ks-amber{ fill:#854F0B; font-size:13px; }
.s8g .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8g .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s8g .kb-amber, :root[data-theme="dark"] .s8g .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s8g .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s8g .kh-amber{ fill:#EF9F27; }
.s8g .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s8g-amber); }
.s8g .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-amber); }
.s8g .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s8g .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s8g .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s8g .ks-coral{ fill:#993C1D; font-size:13px; }
.s8g .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8g .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s8g .kb-coral, :root[data-theme="dark"] .s8g .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s8g .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s8g .kh-coral{ fill:#F0997B; }
.s8g .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s8g-coral); }
.s8g .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-coral); }
.s8g .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s8g .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s8g .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s8g .ks-purple{ fill:#534AB7; font-size:13px; }
.s8g .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8g .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s8g .kb-purple, :root[data-theme="dark"] .s8g .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s8g .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s8g .kh-purple{ fill:#AFA9EC; }
.s8g .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s8g-purple); }
.s8g .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-purple); }
.s8g .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s8g .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s8g .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s8g .ks-red{ fill:#A32D2D; font-size:13px; }
.s8g .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s8g .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s8g .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s8g .kb-red, :root[data-theme="dark"] .s8g .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s8g .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s8g .kh-red{ fill:#F09595; }
.s8g .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s8g-red); }
.s8g .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s8g-red); }
.s8g .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s8g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s8g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s8g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s8g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s8g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s8g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s8g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s8g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s8g-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s8g-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s8g-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s8g-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s8g-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s8g-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s8g">
<rect x="20" y="20" width="218" height="76" rx="7" class="k-red"/>
<text x="129.0" y="53.5" text-anchor="middle" class="kb-red">1. correct?</text>
<text x="129.0" y="71.5" text-anchor="middle" class="ks-red">meets the story's criteria</text>
<rect x="250" y="20" width="218" height="76" rx="7" class="k-purple"/>
<text x="359.0" y="53.5" text-anchor="middle" class="kb-purple">2. design</text>
<text x="359.0" y="71.5" text-anchor="middle" class="ks-purple">fits the architecture</text>
<rect x="480" y="20" width="218" height="76" rx="7" class="k-coral"/>
<text x="589.0" y="53.5" text-anchor="middle" class="kb-coral">3. secure</text>
<text x="589.0" y="71.5" text-anchor="middle" class="ks-coral">validated input, no secrets</text>
<rect x="20" y="112" width="218" height="76" rx="7" class="k-amber"/>
<text x="129.0" y="145.5" text-anchor="middle" class="kb-amber">4. tested</text>
<text x="129.0" y="163.5" text-anchor="middle" class="ks-amber">new tests, edge cases</text>
<rect x="250" y="112" width="218" height="76" rx="7" class="k-blue"/>
<text x="359.0" y="145.5" text-anchor="middle" class="kb-blue">5. readable</text>
<text x="359.0" y="163.5" text-anchor="middle" class="ks-blue">names, size, clarity</text>
<rect x="480" y="112" width="218" height="76" rx="7" class="k-teal"/>
<text x="589.0" y="145.5" text-anchor="middle" class="kb-teal">6. documented</text>
<text x="589.0" y="163.5" text-anchor="middle" class="ks-teal">README, CHANGELOG, ADR</text>
<text x="360" y="226" text-anchor="middle" class="c">style and formatting: leave to ruff and the formatter, not to humans</text>
</g>
</svg>
<figcaption>Small pull requests get better reviews: aim for changes a reviewer can understand in under an hour.</figcaption>
</figure>

Practical guidance:

- **Keep PRs small.** Large reviews get rubber-stamped. A few hundred changed lines is a common upper limit.
- **Describe the change**: what, why, how to test, screenshots or output. Link the story.
- **Automate style.** Formatters and linters settle formatting so humans discuss substance.
- **Review the code, not the person.** Ask questions ("what happens if the banner is empty?") rather than issue verdicts.
- **Respond promptly.** A PR waiting two days for review blocks a teammate and invites conflicts.

A short PR description template, saved as `.github/pull_request_template.md`, nudges everyone towards good habits:

```markdown
## What and why
Closes US-7. Adds `netwarden diff OLD NEW`.

## How to test
pytest tests/test_integration.py::test_history_and_diff

## Checklist
- [ ] Tests added or updated
- [ ] CHANGELOG updated
- [ ] No secrets, reports or databases committed
```

## What belongs in the repository

| Commit | Do not commit |
|---|---|
| Source code and tests | Generated files: `__pycache__/`, `dist/`, coverage output |
| Build and CI configuration (`pyproject.toml`, workflows) | Virtual environments (`.venv/`) |
| Documentation, ADRs, diagrams as code | **Secrets**: passwords, API keys, tokens |
| Small sample data (the knowledge base) | Scan results and `netwarden.db` (sensitive; Chapter 12) |

A `.gitignore` file lists what to leave out. Leaked secrets are a serious, common incident: bots scan public repositories for credentials within minutes of a push. Removing a secret in a later commit does not remove it from history; the secret must be **revoked and rotated**. GitHub's secret scanning and push protection can block many such pushes.

## Hands on

1. Clone the book's repository and run `git log --oneline --graph -- netwarden/` to see NetWarden's history.
2. Create a branch, add a port to `TOP_PORTS`, commit with a Conventional Commits message, and compare `git diff main` before and after.
3. On a second branch, change the same line differently, then merge both into `main` to practise resolving a conflict.
4. Run `git blame src/netwarden/scope.py` and `git log -p -S MAX_HOSTS` to discover who added the host limit and why.

## Summary

- **Version control** gives history, collaboration, accountability and reproducibility; Git is **distributed**.
- Work flows from the **working tree** to the **staging area** to **commits**, and is shared with a **remote**.
- History is a **graph of commits**; **branches** are cheap movable pointers. **Merge** keeps true history; **rebase** rewrites it, so only rebase unshared commits.
- **GitHub flow** and **trunk-based development** favour short-lived branches and frequent integration; **Gitflow** suits scheduled releases.
- Write **atomic commits** with messages that explain why; **Conventional Commits** enable automation.
- **Code review** catches defects and spreads knowledge; keep PRs small and automate style checks.
- Never commit **secrets** or generated files; a leaked secret must be revoked.
