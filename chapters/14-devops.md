# Chapter 14: Deployment and DevOps

Software only creates value when it runs where people need it. For decades, development teams "threw releases over the wall" to separate operations teams, who then had to install, run and fix software they had not built. **DevOps**, a term that spread from a 2009 conference series, is the movement to tear down that wall: one team owns software from commit to production, supported by automation. This chapter covers how software is packaged, configured, deployed, released, observed and kept running, with NetWarden as a scheduled security service.

## The DevOps loop

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The DevOps loop as an infinity shape: plan, code, build and test on the development side; release, deploy, operate and monitor on the operations side; monitoring feeds back into planning. One team owns the whole loop, with automation at every step." xmlns="http://www.w3.org/2000/svg">
<style>
.s14a{ font-family:var(--sans),sans-serif; }
.s14a .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14a .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14a .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14a .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14a .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14a .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14a .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14a .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14a .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14a .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14a .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14a .s{ fill:var(--text-dim); font-size:13px; }
.s14a .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14a .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14a .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14a .c{ fill:var(--text-faint); font-size:12.5px; }
.s14a .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14a .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14a .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14a .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14a-a); }
.s14a .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14a-a); marker-start:url(#s14a-s); }
.s14a .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14a-g); }
.s14a .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14a-a); }
.s14a .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14a .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14a .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14a .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14a .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14a .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14a-tri); }
.s14a .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14a-tri); }
.s14a .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14a-open); }
.s14a .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14a-open); }
.s14a .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14a-dia); }
.s14a .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14a-odia); }
.s14a .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14a-dia); marker-end:url(#s14a-open); }
.s14a .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14a-solid); }
.s14a .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14a-open); }
.s14a .fill{ fill:var(--text); stroke:none; }
.s14a .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14a .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14a .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14a .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14a .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s14a .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s14a .ks-blue{ fill:#185FA5; font-size:13px; }
.s14a .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s14a .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14a .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s14a .kb-blue, :root[data-theme="dark"] .s14a .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s14a .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s14a .kh-blue{ fill:#85B7EB; }
.s14a .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s14a-blue); }
.s14a .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14a-blue); }
.s14a .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s14a .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s14a .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s14a .ks-coral{ fill:#993C1D; font-size:13px; }
.s14a .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s14a .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14a .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s14a .kb-coral, :root[data-theme="dark"] .s14a .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s14a .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s14a .kh-coral{ fill:#F0997B; }
.s14a .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s14a-coral); }
.s14a .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14a-coral); }
.s14a .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s14a .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s14a .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s14a .ks-green{ fill:#3B6D11; font-size:13px; }
.s14a .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s14a .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14a .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s14a .kb-green, :root[data-theme="dark"] .s14a .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s14a .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s14a .kh-green{ fill:#97C459; }
.s14a .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s14a-green); }
.s14a .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14a-green); }
.s14a .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14a-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14a-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14a-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14a-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14a-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14a-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14a-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14a-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14a-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s14a-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s14a-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker></defs>
<g class="s14a">
<path d="M360 135 C 300 40, 80 40, 80 135 C 80 230, 300 230, 360 135 C 420 40, 640 40, 640 135 C 640 230, 420 230, 360 135 Z" class="ln-coral"/>
<rect x="88" y="54" width="84" height="32" rx="16" class="k-blue"/>
<text x="130.0" y="74.5" text-anchor="middle" class="kb-blue">plan</text>
<rect x="28" y="119" width="84" height="32" rx="16" class="k-blue"/>
<text x="70.0" y="139.5" text-anchor="middle" class="kb-blue">code</text>
<rect x="88" y="184" width="84" height="32" rx="16" class="k-blue"/>
<text x="130.0" y="204.5" text-anchor="middle" class="kb-blue">build</text>
<rect x="248" y="184" width="84" height="32" rx="16" class="k-blue"/>
<text x="290.0" y="204.5" text-anchor="middle" class="kb-blue">test</text>
<rect x="384" y="54" width="92" height="32" rx="16" class="k-green"/>
<text x="430.0" y="74.5" text-anchor="middle" class="kb-green">release</text>
<rect x="544" y="54" width="92" height="32" rx="16" class="k-green"/>
<text x="590.0" y="74.5" text-anchor="middle" class="kb-green">deploy</text>
<rect x="604" y="119" width="92" height="32" rx="16" class="k-green"/>
<text x="650.0" y="139.5" text-anchor="middle" class="kb-green">operate</text>
<rect x="544" y="184" width="92" height="32" rx="16" class="k-green"/>
<text x="590.0" y="204.5" text-anchor="middle" class="kb-green">monitor</text>
<text x="200" y="140" text-anchor="middle" class="kh-blue">Dev</text>
<text x="520" y="140" text-anchor="middle" class="kh-green">Ops</text>
<text x="360" y="262" text-anchor="middle" class="c">culture, automation, lean, measurement, sharing (CALMS)</text>
</g>
</svg>
<figcaption>DevOps removes the wall between the people who build software and the people who run it.</figcaption>
</figure>

DevOps is often summarised by **CALMS**: **C**ulture (shared responsibility, no blame), **A**utomation (pipelines, infrastructure as code), **L**ean (small batches, flow, limiting work in progress), **M**easurement (data about delivery and operations), and **S**haring (knowledge and tools across teams). The practices in Chapters 8 to 13, version control, automated tests, continuous integration, are its foundation.

## Packaging with containers

<figure class="diagram">
<svg viewBox="0 0 720 270" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Virtual machines versus containers. Each virtual machine runs a full guest operating system on a hypervisor. Containers share the host&#x27;s kernel and package only the application and its libraries, so they start in seconds and are much smaller. NetWarden&#x27;s image is a slim Python base plus one wheel." xmlns="http://www.w3.org/2000/svg">
<style>
.s14b{ font-family:var(--sans),sans-serif; }
.s14b .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14b .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14b .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14b .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14b .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14b .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14b .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14b .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14b .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14b .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14b .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14b .s{ fill:var(--text-dim); font-size:13px; }
.s14b .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14b .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .c{ fill:var(--text-faint); font-size:12.5px; }
.s14b .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14b .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14b .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14b .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14b-a); }
.s14b .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14b-a); marker-start:url(#s14b-s); }
.s14b .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14b-g); }
.s14b .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-a); }
.s14b .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14b .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14b .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14b .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14b .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14b .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14b-tri); }
.s14b .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-tri); }
.s14b .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14b-open); }
.s14b .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-open); }
.s14b .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14b-dia); }
.s14b .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14b-odia); }
.s14b .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14b-dia); marker-end:url(#s14b-open); }
.s14b .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14b-solid); }
.s14b .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14b-open); }
.s14b .fill{ fill:var(--text); stroke:none; }
.s14b .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14b .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14b .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14b .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14b .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s14b .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s14b .ks-blue{ fill:#185FA5; font-size:13px; }
.s14b .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14b .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s14b .kb-blue, :root[data-theme="dark"] .s14b .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s14b .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s14b .kh-blue{ fill:#85B7EB; }
.s14b .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s14b-blue); }
.s14b .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-blue); }
.s14b .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s14b .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s14b .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s14b .ks-amber{ fill:#854F0B; font-size:13px; }
.s14b .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14b .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s14b .kb-amber, :root[data-theme="dark"] .s14b .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s14b .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s14b .kh-amber{ fill:#EF9F27; }
.s14b .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s14b-amber); }
.s14b .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-amber); }
.s14b .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s14b .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s14b .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s14b .ks-coral{ fill:#993C1D; font-size:13px; }
.s14b .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14b .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s14b .kb-coral, :root[data-theme="dark"] .s14b .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s14b .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s14b .kh-coral{ fill:#F0997B; }
.s14b .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s14b-coral); }
.s14b .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-coral); }
.s14b .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
.s14b .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s14b .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s14b .ks-purple{ fill:#534AB7; font-size:13px; }
.s14b .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14b .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s14b .kb-purple, :root[data-theme="dark"] .s14b .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s14b .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s14b .kh-purple{ fill:#AFA9EC; }
.s14b .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s14b-purple); }
.s14b .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-purple); }
.s14b .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s14b .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s14b .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s14b .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s14b .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s14b .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14b .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s14b .kb-gray, :root[data-theme="dark"] .s14b .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s14b .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s14b .kh-gray{ fill:#B4B2A9; }
.s14b .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s14b-gray); }
.s14b .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14b-gray); }
.s14b .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14b-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14b-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14b-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14b-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14b-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14b-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14b-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14b-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14b-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s14b-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s14b-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker><marker id="s14b-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s14b-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s14b">
<text x="170" y="20" text-anchor="middle" class="b">virtual machines</text>
<rect x="20" y="196" width="300" height="34" rx="3" class="k-gray"/>
<text x="170.0" y="217.5" text-anchor="middle" class="ks-gray">hardware</text>
<rect x="20" y="156" width="300" height="34" rx="3" class="k-gray"/>
<text x="170.0" y="177.5" text-anchor="middle" class="ks-gray">host OS + hypervisor</text>
<rect x="20" y="116" width="140" height="34" rx="3" class="k-coral"/>
<text x="90.0" y="137.5" text-anchor="middle" class="ks-coral">guest OS</text>
<rect x="20" y="76" width="140" height="34" rx="3" class="k-amber"/>
<text x="90.0" y="97.5" text-anchor="middle" class="ks-amber">libs</text>
<rect x="20" y="36" width="140" height="34" rx="3" class="k-blue"/>
<text x="90.0" y="57.5" text-anchor="middle" class="ks-blue">app</text>
<rect x="180" y="116" width="140" height="34" rx="3" class="k-coral"/>
<text x="250.0" y="137.5" text-anchor="middle" class="ks-coral">guest OS</text>
<rect x="180" y="76" width="140" height="34" rx="3" class="k-amber"/>
<text x="250.0" y="97.5" text-anchor="middle" class="ks-amber">libs</text>
<rect x="180" y="36" width="140" height="34" rx="3" class="k-blue"/>
<text x="250.0" y="57.5" text-anchor="middle" class="ks-blue">app B</text>
<text x="530" y="20" text-anchor="middle" class="b">containers</text>
<rect x="380" y="196" width="300" height="34" rx="3" class="k-gray"/>
<text x="530.0" y="217.5" text-anchor="middle" class="ks-gray">hardware</text>
<rect x="380" y="156" width="300" height="34" rx="3" class="k-gray"/>
<text x="530.0" y="177.5" text-anchor="middle" class="ks-gray">host OS (shared kernel)</text>
<rect x="380" y="116" width="300" height="34" rx="3" class="k-purple"/>
<text x="530.0" y="137.5" text-anchor="middle" class="ks-purple">container runtime</text>
<rect x="380" y="76" width="140" height="34" rx="3" class="k-amber"/>
<text x="450.0" y="97.5" text-anchor="middle" class="ks-amber">python:3.13-slim</text>
<rect x="380" y="36" width="140" height="34" rx="3" class="k-blue"/>
<text x="450.0" y="57.5" text-anchor="middle" class="ks-blue">netwarden</text>
<rect x="540" y="76" width="140" height="34" rx="3" class="k-amber"/>
<text x="610.0" y="97.5" text-anchor="middle" class="ks-amber">other libs</text>
<rect x="540" y="36" width="140" height="34" rx="3" class="k-blue"/>
<text x="610.0" y="57.5" text-anchor="middle" class="ks-blue">other app</text>
<text x="170" y="262" text-anchor="middle" class="c">minutes, gigabytes, strong isolation</text>
<text x="530" y="262" text-anchor="middle" class="c">seconds, megabytes, shared kernel</text>
</g>
</svg>
<figcaption>"It works on my machine" stops being an excuse when the machine is shipped too.</figcaption>
</figure>

A **container** packages an application with its libraries and runtime into an **image** that runs the same way on a laptop, a CI runner and a production server. Docker popularised containers in 2013; images now follow the Open Container Initiative (OCI) standard. NetWarden's `Dockerfile` uses a **multi-stage build**:

```dockerfile
# Two stages: build a wheel, then install it into a small image that runs as a normal user.
FROM python:3.13-slim AS build
WORKDIR /src
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir build && python -m build --wheel

FROM python:3.13-slim
RUN useradd --create-home --uid 10001 warden
COPY --from=build /src/dist/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl && rm /tmp/*.whl
USER warden
WORKDIR /home/warden
ENTRYPOINT ["netwarden"]
CMD ["--help"]
```

The first stage has build tools; the final image contains only the installed package and runs as an unprivileged user (least privilege, Chapter 12). Usage:

```bash
docker build -t netwarden:1.0.0 netwarden/
docker run --rm netwarden:1.0.0 --version
docker run --rm --network host -v "$PWD:/data" -w /data netwarden:1.0.0 \
    scan 192.168.56.0/24 --scope lab-scope.txt --format html --output report.html
```

`--network host` lets the container reach the lab network directly; `-v` mounts the current directory so the scope file goes in and the report comes out. At larger scale, **orchestrators** such as Kubernetes schedule many containers across many machines, restart failed ones and roll out new versions.

## Configuration and environments

Software runs in several **environments**: development, test, staging (a production-like rehearsal), and production. The code is the same in all of them; the **configuration** differs. The **Twelve-Factor App** guidelines (Heroku, 2011) recommend keeping configuration in the environment, not in code, so the same artifact can be promoted unchanged (Chapter 13). For NetWarden, configuration is the scope file, the database path and the command-line options; for a web service it would be environment variables such as `DATABASE_URL`.

**Infrastructure as code** applies the same idea to the machines themselves.

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Infrastructure as code. The desired infrastructure, servers, networks and the scheduled NetWarden runner, is described in version-controlled files, reviewed like code, and applied by a tool such as Terraform or Ansible, which makes the real environment match the description. The same files can rebuild the environment from scratch." xmlns="http://www.w3.org/2000/svg">
<style>
.s14d{ font-family:var(--sans),sans-serif; }
.s14d .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14d .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14d .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14d .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14d .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14d .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14d .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14d .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14d .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14d .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14d .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14d .s{ fill:var(--text-dim); font-size:13px; }
.s14d .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14d .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14d .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14d .c{ fill:var(--text-faint); font-size:12.5px; }
.s14d .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14d .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14d .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14d .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14d-a); }
.s14d .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14d-a); marker-start:url(#s14d-s); }
.s14d .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14d-g); }
.s14d .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-a); }
.s14d .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14d .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14d .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14d .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14d .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14d .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14d-tri); }
.s14d .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-tri); }
.s14d .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14d-open); }
.s14d .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-open); }
.s14d .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14d-dia); }
.s14d .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14d-odia); }
.s14d .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14d-dia); marker-end:url(#s14d-open); }
.s14d .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14d-solid); }
.s14d .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14d-open); }
.s14d .fill{ fill:var(--text); stroke:none; }
.s14d .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14d .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14d .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14d .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14d .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s14d .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s14d .ks-amber{ fill:#854F0B; font-size:13px; }
.s14d .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s14d .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14d .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s14d .kb-amber, :root[data-theme="dark"] .s14d .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s14d .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s14d .kh-amber{ fill:#EF9F27; }
.s14d .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s14d-amber); }
.s14d .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-amber); }
.s14d .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s14d .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s14d .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s14d .ks-purple{ fill:#534AB7; font-size:13px; }
.s14d .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s14d .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14d .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s14d .kb-purple, :root[data-theme="dark"] .s14d .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s14d .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s14d .kh-purple{ fill:#AFA9EC; }
.s14d .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s14d-purple); }
.s14d .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-purple); }
.s14d .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s14d .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s14d .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s14d .ks-green{ fill:#3B6D11; font-size:13px; }
.s14d .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s14d .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14d .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s14d .kb-green, :root[data-theme="dark"] .s14d .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s14d .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s14d .kh-green{ fill:#97C459; }
.s14d .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s14d-green); }
.s14d .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-green); }
.s14d .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s14d .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s14d .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s14d .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s14d .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s14d .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14d .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s14d .kb-gray, :root[data-theme="dark"] .s14d .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s14d .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s14d .kh-gray{ fill:#B4B2A9; }
.s14d .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s14d-gray); }
.s14d .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14d-gray); }
.s14d .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14d-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14d-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14d-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14d-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14d-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14d-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14d-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14d-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14d-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s14d-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s14d-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s14d-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s14d">
<rect x="20" y="60" width="170" height="90" rx="7" class="k-purple"/>
<text x="105.0" y="91.5" text-anchor="middle" class="kb-purple">infra code</text>
<text x="105.0" y="109.5" text-anchor="middle" class="ks-purple">Terraform, Ansible,</text>
<text x="105.0" y="127.5" text-anchor="middle" class="ks-purple">Kubernetes YAML</text>
<rect x="230" y="70" width="120" height="70" rx="7" class="k-gray"/>
<text x="290.0" y="100.5" text-anchor="middle" class="kb-gray">git + PR</text>
<text x="290.0" y="118.5" text-anchor="middle" class="ks-gray">review, history</text>
<rect x="390" y="70" width="120" height="70" rx="7" class="k-amber"/>
<text x="450.0" y="100.5" text-anchor="middle" class="kb-amber">apply</text>
<text x="450.0" y="118.5" text-anchor="middle" class="ks-amber">plan, then apply</text>
<line x1="192" y1="105" x2="228" y2="105" class="ar"/>
<line x1="352" y1="105" x2="388" y2="105" class="ar"/>
<rect x="560" y="30" width="140" height="44" rx="4" class="k-green"/>
<text x="630.0" y="56.5" text-anchor="middle" class="kb-green">runner VM</text>
<line x1="512" y1="105" x2="558" y2="52" class="ar"/>
<rect x="560" y="86" width="140" height="44" rx="4" class="k-green"/>
<text x="630.0" y="112.5" text-anchor="middle" class="kb-green">lab VLAN</text>
<line x1="512" y1="105" x2="558" y2="108" class="ar"/>
<rect x="560" y="142" width="140" height="44" rx="4" class="k-green"/>
<text x="630.0" y="168.5" text-anchor="middle" class="kb-green">storage</text>
<line x1="512" y1="105" x2="558" y2="164" class="ar"/>
<text x="360" y="214" text-anchor="middle" class="c">repeatable, reviewable, auditable; drift is detected and corrected</text>
</g>
</svg>
<figcaption>Servers become cattle, not pets: rebuilt from code, never hand-tuned.</figcaption>
</figure>

Tools such as **Terraform** (and its open-source fork OpenTofu) describe infrastructure declaratively; **Ansible** configures machines; Kubernetes manifests describe workloads. Because the description is code, it is reviewed, versioned and repeatable, and a lost server can be rebuilt in minutes.

## Deployment and release strategies

<figure class="diagram">
<svg viewBox="0 0 720 300" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Three release strategies. Rolling: replace instances one at a time. Blue-green: run the new version, green, alongside the old, blue, and switch the router at once, switching back if needed. Canary: send a small share of traffic, such as 5 percent, to the new version, watch the metrics, then increase." xmlns="http://www.w3.org/2000/svg">
<style>
.s14c{ font-family:var(--sans),sans-serif; }
.s14c .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14c .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14c .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14c .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14c .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14c .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14c .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14c .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14c .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14c .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14c .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14c .s{ fill:var(--text-dim); font-size:13px; }
.s14c .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14c .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .c{ fill:var(--text-faint); font-size:12.5px; }
.s14c .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14c .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14c .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14c .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14c-a); }
.s14c .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14c-a); marker-start:url(#s14c-s); }
.s14c .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14c-g); }
.s14c .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-a); }
.s14c .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14c .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14c .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14c .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14c .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14c .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14c-tri); }
.s14c .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-tri); }
.s14c .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14c-open); }
.s14c .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-open); }
.s14c .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14c-dia); }
.s14c .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14c-odia); }
.s14c .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14c-dia); marker-end:url(#s14c-open); }
.s14c .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14c-solid); }
.s14c .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14c-open); }
.s14c .fill{ fill:var(--text); stroke:none; }
.s14c .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14c .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14c .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14c .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14c .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s14c .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s14c .ks-blue{ fill:#185FA5; font-size:13px; }
.s14c .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14c .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s14c .kb-blue, :root[data-theme="dark"] .s14c .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s14c .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s14c .kh-blue{ fill:#85B7EB; }
.s14c .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s14c-blue); }
.s14c .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-blue); }
.s14c .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s14c .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s14c .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s14c .ks-teal{ fill:#0F6E56; font-size:13px; }
.s14c .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14c .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s14c .kb-teal, :root[data-theme="dark"] .s14c .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s14c .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s14c .kh-teal{ fill:#5DCAA5; }
.s14c .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s14c-teal); }
.s14c .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-teal); }
.s14c .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s14c .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s14c .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s14c .ks-amber{ fill:#854F0B; font-size:13px; }
.s14c .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14c .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s14c .kb-amber, :root[data-theme="dark"] .s14c .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s14c .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s14c .kh-amber{ fill:#EF9F27; }
.s14c .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s14c-amber); }
.s14c .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-amber); }
.s14c .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s14c .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s14c .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s14c .ks-purple{ fill:#534AB7; font-size:13px; }
.s14c .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14c .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s14c .kb-purple, :root[data-theme="dark"] .s14c .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s14c .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s14c .kh-purple{ fill:#AFA9EC; }
.s14c .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s14c-purple); }
.s14c .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-purple); }
.s14c .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s14c .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s14c .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s14c .ks-green{ fill:#3B6D11; font-size:13px; }
.s14c .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14c .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s14c .kb-green, :root[data-theme="dark"] .s14c .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s14c .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s14c .kh-green{ fill:#97C459; }
.s14c .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s14c-green); }
.s14c .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-green); }
.s14c .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s14c .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s14c .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s14c .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s14c .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s14c .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14c .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s14c .kb-gray, :root[data-theme="dark"] .s14c .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s14c .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s14c .kh-gray{ fill:#B4B2A9; }
.s14c .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s14c-gray); }
.s14c .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14c-gray); }
.s14c .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14c-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14c-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14c-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14c-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14c-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14c-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14c-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14c-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14c-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s14c-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s14c-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s14c-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s14c-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s14c-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s14c">
<text x="120" y="20" text-anchor="middle" class="kh-blue">rolling</text>
<rect x="30" y="40" width="40" height="30" rx="3" class="k-green"/>
<text x="50.0" y="59.5" text-anchor="middle" class="ks-green">v2</text>
<rect x="76" y="40" width="40" height="30" rx="3" class="k-green"/>
<text x="96.0" y="59.5" text-anchor="middle" class="ks-green">v2</text>
<rect x="122" y="40" width="40" height="30" rx="3" class="k-blue"/>
<text x="142.0" y="59.5" text-anchor="middle" class="ks-blue">v1</text>
<rect x="168" y="40" width="40" height="30" rx="3" class="k-blue"/>
<text x="188.0" y="59.5" text-anchor="middle" class="ks-blue">v1</text>
<text x="120" y="96" text-anchor="middle" class="c">replace one at a time</text>
<text x="360" y="20" text-anchor="middle" class="kh-teal">blue-green</text>
<rect x="320" y="40" width="80" height="30" rx="3" class="k-gray"/>
<text x="360.0" y="59.5" text-anchor="middle" class="ks-gray">router</text>
<rect x="270" y="110" width="80" height="36" rx="3" class="k-blue"/>
<text x="310.0" y="132.5" text-anchor="middle" class="ks-blue">blue v1</text>
<rect x="370" y="110" width="80" height="36" rx="3" class="k-green"/>
<text x="410.0" y="132.5" text-anchor="middle" class="ks-green">green v2</text>
<line x1="360" y1="72" x2="410" y2="108" class="ar"/>
<line x1="350" y1="72" x2="310" y2="108" class="ad"/>
<text x="360" y="170" text-anchor="middle" class="c">switch all at once; instant rollback</text>
<text x="600" y="20" text-anchor="middle" class="kh-amber">canary</text>
<rect x="560" y="40" width="80" height="30" rx="3" class="k-gray"/>
<text x="600.0" y="59.5" text-anchor="middle" class="ks-gray">router</text>
<rect x="510" y="110" width="80" height="36" rx="3" class="k-blue"/>
<text x="550.0" y="132.5" text-anchor="middle" class="ks-blue">v1  95%</text>
<rect x="610" y="110" width="80" height="36" rx="3" class="k-amber"/>
<text x="650.0" y="132.5" text-anchor="middle" class="ks-amber">v2  5%</text>
<line x1="590" y1="72" x2="550" y2="108" class="ar"/>
<line x1="610" y1="72" x2="650" y2="108" class="ad-amber"/>
<text x="600" y="170" text-anchor="middle" class="c">watch errors, then 25%, 50%, 100%</text>
<rect x="20" y="210" width="680" height="70" rx="7" class="k-purple"/>
<text x="360.0" y="237.5" text-anchor="middle" class="kb-purple">feature flags: deploy code switched off, release it later by configuration</text>
<text x="360.0" y="261.5" text-anchor="middle" class="km-purple">if flags.enabled("smb-check"): checks.append(SmbSigningCheck())</text>
</g>
</svg>
<figcaption>Deployment (installing code) and release (exposing it to users) can be separated, which makes both safer.</figcaption>
</figure>

| Strategy | How | Benefit | Cost |
|---|---|---|---|
| **Recreate** | Stop old, start new | Simple | Downtime |
| **Rolling** | Replace instances one at a time | No downtime | Two versions run together for a while |
| **Blue-green** | Run both; switch traffic at once | Instant rollback | Double capacity during the switch |
| **Canary** | Send a small share of traffic to the new version first | Real-world testing with limited blast radius | Needs good metrics and routing |
| **Feature flags** | Ship code switched off; turn on by configuration | Separates deployment from release; quick kill switch | Flags must be cleaned up, or they become debt |

**Rollback** must be planned before it is needed. Database schema changes are the usual obstacle: use **expand and contract** migrations, adding new columns first, migrating, and only later removing old ones, so both versions can run against the same schema.

## Running NetWarden as a service

A security scan that depends on someone remembering to run it will not be run. NetWarden's `examples/scheduled-scan.yml` turns it into a weekly automated service.

<figure class="diagram">
<svg viewBox="0 0 720 290" style="width:100%;height:auto;max-width:720px" role="img" aria-label="NetWarden in operation: a scheduled GitHub Actions workflow runs every Monday at 06:00 on a self-hosted runner inside the lab network. It runs the netwarden container against the lab scope, saves the HTML report as an artifact, keeps the history database, and fails, notifying the team, if any high or critical finding appears; the diff shows new and resolved findings." xmlns="http://www.w3.org/2000/svg">
<style>
.s14e{ font-family:var(--sans),sans-serif; }
.s14e .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14e .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14e .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14e .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14e .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14e .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14e .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14e .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14e .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14e .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14e .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14e .s{ fill:var(--text-dim); font-size:13px; }
.s14e .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14e .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .c{ fill:var(--text-faint); font-size:12.5px; }
.s14e .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14e .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14e .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14e .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14e-a); }
.s14e .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14e-a); marker-start:url(#s14e-s); }
.s14e .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14e-g); }
.s14e .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-a); }
.s14e .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14e .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14e .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14e .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14e .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14e .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14e-tri); }
.s14e .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-tri); }
.s14e .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14e-open); }
.s14e .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-open); }
.s14e .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14e-dia); }
.s14e .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14e-odia); }
.s14e .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14e-dia); marker-end:url(#s14e-open); }
.s14e .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14e-solid); }
.s14e .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14e-open); }
.s14e .fill{ fill:var(--text); stroke:none; }
.s14e .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14e .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14e .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14e .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14e .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s14e .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s14e .ks-teal{ fill:#0F6E56; font-size:13px; }
.s14e .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14e .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s14e .kb-teal, :root[data-theme="dark"] .s14e .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s14e .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s14e .kh-teal{ fill:#5DCAA5; }
.s14e .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s14e-teal); }
.s14e .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-teal); }
.s14e .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s14e .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s14e .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s14e .ks-amber{ fill:#854F0B; font-size:13px; }
.s14e .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14e .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s14e .kb-amber, :root[data-theme="dark"] .s14e .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s14e .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s14e .kh-amber{ fill:#EF9F27; }
.s14e .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s14e-amber); }
.s14e .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-amber); }
.s14e .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s14e .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s14e .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s14e .ks-purple{ fill:#534AB7; font-size:13px; }
.s14e .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14e .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s14e .kb-purple, :root[data-theme="dark"] .s14e .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s14e .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s14e .kh-purple{ fill:#AFA9EC; }
.s14e .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s14e-purple); }
.s14e .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-purple); }
.s14e .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s14e .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s14e .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s14e .ks-green{ fill:#3B6D11; font-size:13px; }
.s14e .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14e .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s14e .kb-green, :root[data-theme="dark"] .s14e .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s14e .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s14e .kh-green{ fill:#97C459; }
.s14e .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s14e-green); }
.s14e .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-green); }
.s14e .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s14e .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s14e .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s14e .ks-red{ fill:#A32D2D; font-size:13px; }
.s14e .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14e .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s14e .kb-red, :root[data-theme="dark"] .s14e .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s14e .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s14e .kh-red{ fill:#F09595; }
.s14e .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s14e-red); }
.s14e .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-red); }
.s14e .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
.s14e .k-gray{ fill:#F1EFE8; stroke:#888780; stroke-width:1.6; }
.s14e .kb-gray{ fill:#444441; font-size:13px; font-weight:700; }
.s14e .ks-gray{ fill:#5F5E5A; font-size:13px; }
.s14e .km-gray{ fill:#444441; font-size:12.5px; font-family:var(--mono),monospace; }
.s14e .kh-gray{ fill:#5F5E5A; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14e .k-gray{ fill:#444441; stroke:#B4B2A9; }
:root[data-theme="dark"] .s14e .kb-gray, :root[data-theme="dark"] .s14e .km-gray{ fill:#F1EFE8; }
:root[data-theme="dark"] .s14e .ks-gray{ fill:#D3D1C7; }
:root[data-theme="dark"] .s14e .kh-gray{ fill:#B4B2A9; }
.s14e .ar-gray{ stroke:#888780; stroke-width:2; fill:none; marker-end:url(#s14e-gray); }
.s14e .ad-gray{ stroke:#888780; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14e-gray); }
.s14e .ln-gray{ stroke:#888780; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14e-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14e-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14e-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14e-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14e-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14e-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14e-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14e-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14e-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s14e-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s14e-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s14e-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s14e-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker><marker id="s14e-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888780"/></marker></defs>
<g class="s14e">
<rect x="20" y="60" width="124" height="64" rx="7" class="k-gray"/>
<text x="82.0" y="87.5" text-anchor="middle" class="kb-gray">schedule</text>
<text x="82.0" y="105.5" text-anchor="middle" class="ks-gray">cron: Mon 06:00</text>
<rect x="160" y="60" width="124" height="64" rx="7" class="k-purple"/>
<text x="222.0" y="87.5" text-anchor="middle" class="kb-purple">runner in lab</text>
<text x="222.0" y="105.5" text-anchor="middle" class="ks-purple">self-hosted</text>
<line x1="146" y1="92" x2="158" y2="92" class="ar"/>
<rect x="300" y="60" width="124" height="64" rx="7" class="k-teal"/>
<text x="362.0" y="87.5" text-anchor="middle" class="kb-teal">netwarden scan</text>
<text x="362.0" y="105.5" text-anchor="middle" class="ks-teal">--fail-on high</text>
<line x1="286" y1="92" x2="298" y2="92" class="ar"/>
<rect x="440" y="60" width="124" height="64" rx="7" class="k-amber"/>
<text x="502.0" y="87.5" text-anchor="middle" class="kb-amber">artifacts</text>
<text x="502.0" y="105.5" text-anchor="middle" class="ks-amber">report.html, db</text>
<line x1="426" y1="92" x2="438" y2="92" class="ar"/>
<rect x="580" y="60" width="124" height="64" rx="7" class="k-red"/>
<text x="642.0" y="87.5" text-anchor="middle" class="kb-red">notify</text>
<text x="642.0" y="105.5" text-anchor="middle" class="ks-red">if exit status 1</text>
<line x1="566" y1="92" x2="578" y2="92" class="ar"/>
<rect x="170" y="170" width="380" height="70" rx="7" class="k-green"/>
<text x="360.0" y="198.5" text-anchor="middle" class="km-green">netwarden diff &lt;last&gt; &lt;this&gt;</text>
<text x="360.0" y="220.5" text-anchor="middle" class="km-green">new: 1   resolved: 3   unchanged: 8</text>
<line x1="360" y1="126" x2="360" y2="168" class="ar"/>
<text x="360" y="30" text-anchor="middle" class="kh-teal">a security check that runs whether anyone remembers or not</text>
<text x="360" y="274" text-anchor="middle" class="c">the scope file lives in the repository and is changed only through reviewed PRs</text>
</g>
</svg>
<figcaption>Exit codes and JSON output (requirement NW-FR-10) are what make NetWarden easy to automate.</figcaption>
</figure>

```yaml
on:
  schedule:
    - cron: "0 6 * * 1"        # Mondays 06:00 UTC
  workflow_dispatch: {}         # allow manual runs

jobs:
  assess:
    runs-on: [self-hosted, lab]
    steps:
      - uses: actions/checkout@v6
      - name: Scan
        run: |
          docker run --rm --network host -v "$PWD:/data" -w /data netwarden:1.0.0 \
            --db netwarden.db scan 192.168.56.0/24 --scope lab-scope.txt \
            --format html --output report.html --fail-on high
```

The job runs on a **self-hosted runner** inside the lab network, because GitHub's hosted runners cannot and must not reach private networks. Exit status 1 fails the job and notifies the team; the report is kept as an artifact. The scope file lives in the repository, so changing what is scanned requires a reviewed pull request: an operational control enforced by the development workflow. Requirement NW-FR-10, the exit code, written in Chapter 3, is what makes this possible.

## Observability

<figure class="diagram">
<svg viewBox="0 0 720 260" style="width:100%;height:auto;max-width:720px" role="img" aria-label="Observability: applications emit logs, metrics and traces; these are collected into dashboards and alert rules; alerts page the on-call engineer, who uses the same data to diagnose the problem. Service level objectives define what good enough means, such as 99.9 percent of scheduled scans completing." xmlns="http://www.w3.org/2000/svg">
<style>
.s14f{ font-family:var(--sans),sans-serif; }
.s14f .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14f .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14f .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14f .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14f .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14f .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14f .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14f .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14f .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14f .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14f .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14f .s{ fill:var(--text-dim); font-size:13px; }
.s14f .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14f .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .c{ fill:var(--text-faint); font-size:12.5px; }
.s14f .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14f .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14f .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14f .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14f-a); }
.s14f .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14f-a); marker-start:url(#s14f-s); }
.s14f .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14f-g); }
.s14f .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-a); }
.s14f .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14f .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14f .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14f .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14f .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14f .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14f-tri); }
.s14f .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-tri); }
.s14f .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14f-open); }
.s14f .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-open); }
.s14f .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14f-dia); }
.s14f .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14f-odia); }
.s14f .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14f-dia); marker-end:url(#s14f-open); }
.s14f .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14f-solid); }
.s14f .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14f-open); }
.s14f .fill{ fill:var(--text); stroke:none; }
.s14f .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14f .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14f .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14f .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14f .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s14f .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s14f .ks-blue{ fill:#185FA5; font-size:13px; }
.s14f .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14f .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s14f .kb-blue, :root[data-theme="dark"] .s14f .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s14f .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s14f .kh-blue{ fill:#85B7EB; }
.s14f .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s14f-blue); }
.s14f .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-blue); }
.s14f .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s14f .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s14f .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s14f .ks-teal{ fill:#0F6E56; font-size:13px; }
.s14f .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14f .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s14f .kb-teal, :root[data-theme="dark"] .s14f .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s14f .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s14f .kh-teal{ fill:#5DCAA5; }
.s14f .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s14f-teal); }
.s14f .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-teal); }
.s14f .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s14f .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s14f .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s14f .ks-amber{ fill:#854F0B; font-size:13px; }
.s14f .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14f .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s14f .kb-amber, :root[data-theme="dark"] .s14f .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s14f .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s14f .kh-amber{ fill:#EF9F27; }
.s14f .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s14f-amber); }
.s14f .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-amber); }
.s14f .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s14f .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s14f .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s14f .ks-purple{ fill:#534AB7; font-size:13px; }
.s14f .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14f .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s14f .kb-purple, :root[data-theme="dark"] .s14f .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s14f .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s14f .kh-purple{ fill:#AFA9EC; }
.s14f .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s14f-purple); }
.s14f .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-purple); }
.s14f .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s14f .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s14f .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s14f .ks-green{ fill:#3B6D11; font-size:13px; }
.s14f .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14f .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s14f .kb-green, :root[data-theme="dark"] .s14f .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s14f .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s14f .kh-green{ fill:#97C459; }
.s14f .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s14f-green); }
.s14f .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-green); }
.s14f .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s14f .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s14f .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s14f .ks-red{ fill:#A32D2D; font-size:13px; }
.s14f .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s14f .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14f .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s14f .kb-red, :root[data-theme="dark"] .s14f .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s14f .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s14f .kh-red{ fill:#F09595; }
.s14f .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s14f-red); }
.s14f .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14f-red); }
.s14f .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14f-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14f-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14f-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14f-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14f-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14f-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14f-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14f-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14f-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s14f-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s14f-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s14f-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s14f-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s14f-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s14f">
<rect x="20" y="20" width="150" height="56" rx="7" class="k-blue"/>
<text x="95.0" y="43.5" text-anchor="middle" class="kb-blue">logs</text>
<text x="95.0" y="61.5" text-anchor="middle" class="ks-blue">events, errors</text>
<line x1="172" y1="48" x2="238" y2="118" class="ar"/>
<rect x="20" y="90" width="150" height="56" rx="7" class="k-teal"/>
<text x="95.0" y="113.5" text-anchor="middle" class="kb-teal">metrics</text>
<text x="95.0" y="131.5" text-anchor="middle" class="ks-teal">counts, timings</text>
<line x1="172" y1="118" x2="238" y2="118" class="ar"/>
<rect x="20" y="160" width="150" height="56" rx="7" class="k-purple"/>
<text x="95.0" y="183.5" text-anchor="middle" class="kb-purple">traces</text>
<text x="95.0" y="201.5" text-anchor="middle" class="ks-purple">request paths</text>
<line x1="172" y1="188" x2="238" y2="118" class="ar"/>
<rect x="240" y="80" width="150" height="76" rx="7" class="k-amber"/>
<text x="315.0" y="104.5" text-anchor="middle" class="kb-amber">dashboards</text>
<text x="315.0" y="122.5" text-anchor="middle" class="ks-amber">and alert rules</text>
<text x="315.0" y="140.5" text-anchor="middle" class="ks-amber">SLOs</text>
<line x1="392" y1="118" x2="448" y2="118" class="ar"/>
<rect x="450" y="90" width="120" height="56" rx="7" class="k-red"/>
<text x="510.0" y="113.5" text-anchor="middle" class="kb-red">on-call</text>
<text x="510.0" y="131.5" text-anchor="middle" class="ks-red">paged</text>
<line x1="572" y1="118" x2="598" y2="118" class="ar"/>
<rect x="600" y="90" width="100" height="56" rx="7" class="k-green"/>
<text x="650.0" y="113.5" text-anchor="middle" class="kb-green">diagnose</text>
<text x="650.0" y="131.5" text-anchor="middle" class="ks-green">fix</text>
<text x="360" y="230" text-anchor="middle" class="c">SLO example: 99.9% of scheduled scans complete within 15 minutes</text>
</g>
</svg>
<figcaption>Monitoring tells you that something is wrong; observability helps you find out why.</figcaption>
</figure>

Once software runs, the team needs to know whether it is working and, when it is not, why.

| Signal | What it is | NetWarden example |
|---|---|---|
| **Logs** | Timestamped records of events, ideally structured (JSON) | "scan 42 started: 254 hosts, 17 ports" |
| **Metrics** | Numbers over time | Scan duration, findings per severity, failed scans |
| **Traces** | The path of one request through many services | One scan job through scheduler, worker, results service |

**Monitoring** watches for known failure conditions; **observability** is the ability to ask new questions of the data when something unexpected happens. **OpenTelemetry** is the vendor-neutral standard for emitting all three signals. **Service level objectives** (SLOs), from Google's site reliability engineering (SRE) practice, define "good enough" numerically, for example "99.9% of scheduled scans complete within 15 minutes", and alerts fire when the objective is at risk, not on every blip.

## Measuring delivery: DORA

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The four key DORA metrics. Throughput: deployment frequency and lead time for changes. Stability: change failure rate and time to restore service. Research found that high performers do well on both kinds at once: speed and stability are not a trade-off." xmlns="http://www.w3.org/2000/svg">
<style>
.s14g{ font-family:var(--sans),sans-serif; }
.s14g .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14g .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14g .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14g .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14g .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14g .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14g .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14g .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14g .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14g .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14g .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14g .s{ fill:var(--text-dim); font-size:13px; }
.s14g .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14g .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14g .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14g .c{ fill:var(--text-faint); font-size:12.5px; }
.s14g .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14g .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14g .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14g .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14g-a); }
.s14g .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14g-a); marker-start:url(#s14g-s); }
.s14g .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14g-g); }
.s14g .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14g-a); }
.s14g .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14g .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14g .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14g .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14g .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14g .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14g-tri); }
.s14g .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14g-tri); }
.s14g .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14g-open); }
.s14g .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14g-open); }
.s14g .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14g-dia); }
.s14g .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14g-odia); }
.s14g .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14g-dia); marker-end:url(#s14g-open); }
.s14g .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14g-solid); }
.s14g .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14g-open); }
.s14g .fill{ fill:var(--text); stroke:none; }
.s14g .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14g .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14g .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14g .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14g .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s14g .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s14g .ks-blue{ fill:#185FA5; font-size:13px; }
.s14g .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s14g .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14g .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s14g .kb-blue, :root[data-theme="dark"] .s14g .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s14g .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s14g .kh-blue{ fill:#85B7EB; }
.s14g .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s14g-blue); }
.s14g .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14g-blue); }
.s14g .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s14g .k-coral{ fill:#FAECE7; stroke:#D85A30; stroke-width:1.6; }
.s14g .kb-coral{ fill:#712B13; font-size:13px; font-weight:700; }
.s14g .ks-coral{ fill:#993C1D; font-size:13px; }
.s14g .km-coral{ fill:#712B13; font-size:12.5px; font-family:var(--mono),monospace; }
.s14g .kh-coral{ fill:#993C1D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14g .k-coral{ fill:#712B13; stroke:#F0997B; }
:root[data-theme="dark"] .s14g .kb-coral, :root[data-theme="dark"] .s14g .km-coral{ fill:#FAECE7; }
:root[data-theme="dark"] .s14g .ks-coral{ fill:#F5C4B3; }
:root[data-theme="dark"] .s14g .kh-coral{ fill:#F0997B; }
.s14g .ar-coral{ stroke:#D85A30; stroke-width:2; fill:none; marker-end:url(#s14g-coral); }
.s14g .ad-coral{ stroke:#D85A30; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14g-coral); }
.s14g .ln-coral{ stroke:#D85A30; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14g-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14g-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14g-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14g-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14g-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14g-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14g-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14g-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14g-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s14g-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#D85A30"/></marker></defs>
<g class="s14g">
<rect x="20" y="30" width="330" height="70" rx="7" class="k-blue"/>
<text x="185.0" y="60.5" text-anchor="middle" class="kb-blue">deployment frequency</text>
<text x="185.0" y="78.5" text-anchor="middle" class="ks-blue">how often to production</text>
<rect x="370" y="30" width="330" height="70" rx="7" class="k-blue"/>
<text x="535.0" y="60.5" text-anchor="middle" class="kb-blue">lead time for changes</text>
<text x="535.0" y="78.5" text-anchor="middle" class="ks-blue">commit to production</text>
<rect x="20" y="114" width="330" height="70" rx="7" class="k-coral"/>
<text x="185.0" y="144.5" text-anchor="middle" class="kb-coral">change failure rate</text>
<text x="185.0" y="162.5" text-anchor="middle" class="ks-coral">deploys causing failure</text>
<rect x="370" y="114" width="330" height="70" rx="7" class="k-coral"/>
<text x="535.0" y="144.5" text-anchor="middle" class="kb-coral">recovery time</text>
<text x="535.0" y="162.5" text-anchor="middle" class="ks-coral">failed deploy to restored</text>
<text x="185" y="20" text-anchor="middle" class="kh-blue">throughput</text>
<text x="535" y="20" text-anchor="middle" class="kh-coral">stability</text>
<text x="360" y="215" text-anchor="middle" class="c">elite teams: frequent, small deploys with low failure rates and fast recovery</text>
</g>
</svg>
<figcaption>The classic four from DORA and Accelerate (2018). Since 2024 DORA also tracks a fifth, deployment rework rate.</figcaption>
</figure>

The DevOps Research and Assessment (DORA) programme surveyed tens of thousands of professionals over many years. Its four key metrics, popularised by Forsgren, Humble and Kim in *Accelerate* (2018), measure delivery **throughput** and **stability**. DORA's later reports renamed time to restore as **failed deployment recovery time**, regrouped the metrics, and in 2024 added a fifth, **deployment rework rate** (the share of deployments that are unplanned fixes for production problems), but the core finding stands: the best-performing teams deploy more often **and** fail less, because small, frequent, automated changes are both faster and safer than large, rare, manual ones. The capabilities that predict performance include version control, trunk-based development, continuous integration, test automation, loosely coupled architecture and a blameless culture: much of this book.

## When things go wrong

<figure class="diagram">
<svg viewBox="0 0 720 230" style="width:100%;height:auto;max-width:720px" role="img" aria-label="The incident lifecycle: detect, through an alert or a report; triage and declare, assigning a severity and an incident commander; mitigate, restoring service first, for example by rolling back; resolve the underlying cause; hold a blameless postmortem; and track the follow-up actions to completion." xmlns="http://www.w3.org/2000/svg">
<style>
.s14h{ font-family:var(--sans),sans-serif; }
.s14h .box{ fill:var(--bg-soft); stroke:var(--border); stroke-width:1.5; }
.s14h .pnl{ fill:var(--panel); stroke:var(--border); stroke-width:1.5; }
.s14h .hov{ fill:var(--panel-hover); stroke:var(--border); stroke-width:1.5; }
.s14h .acc{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.6; }
.s14h .dark{ fill:var(--accent); stroke:var(--accent); stroke-width:1.6; }
.s14h .out{ fill:none; stroke:var(--accent); stroke-width:2; }
.s14h .dash{ fill:none; stroke:var(--accent); stroke-width:1.6; stroke-dasharray:6 4; }
.s14h .zone{ fill:none; stroke:var(--border); stroke-width:1.5; stroke-dasharray:6 4; }
.s14h .tint{ fill:var(--accent-dim); stroke:var(--accent); stroke-width:1.2; opacity:0.28; }
.s14h .h{ fill:var(--text); font-size:15px; font-weight:700; }
.s14h .b{ fill:var(--text); font-size:13px; font-weight:700; }
.s14h .s{ fill:var(--text-dim); font-size:13px; }
.s14h .a{ fill:var(--accent); font-size:13px; font-weight:700; }
.s14h .m{ fill:var(--text); font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .ma{ fill:var(--accent); font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .c{ fill:var(--text-faint); font-size:12.5px; }
.s14h .on{ fill:var(--bg); font-size:13px; font-weight:700; }
.s14h .ln{ stroke:var(--border); stroke-width:1.5; fill:none; }
.s14h .lk{ stroke:var(--text-faint); stroke-width:2.2; fill:none; }
.s14h .ar{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14h-a); }
.s14h .ar2{ stroke:var(--accent); stroke-width:2; fill:none; marker-end:url(#s14h-a); marker-start:url(#s14h-s); }
.s14h .ag{ stroke:var(--text-faint); stroke-width:1.8; fill:none; marker-end:url(#s14h-g); }
.s14h .ad{ stroke:var(--accent); stroke-width:1.8; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-a); }
.s14h .gd{ stroke:var(--text-faint); stroke-width:1.6; fill:none; stroke-dasharray:4 4; }
.s14h .x{ stroke:var(--text-faint); stroke-width:2.4; fill:none; }
.s14h .bad{ stroke:var(--text); stroke-width:3; fill:none; }
.s14h .u{ stroke:var(--text-dim); stroke-width:1.6; fill:none; }
.s14h .ud{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; }
.s14h .gen{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14h-tri); }
.s14h .real{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-tri); }
.s14h .assoc{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14h-open); }
.s14h .dep{ stroke:var(--text-dim); stroke-width:1.6; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-open); }
.s14h .comp{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14h-dia); }
.s14h .agg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14h-odia); }
.s14h .compa{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-start:url(#s14h-dia); marker-end:url(#s14h-open); }
.s14h .msg{ stroke:var(--text-dim); stroke-width:1.6; fill:none; marker-end:url(#s14h-solid); }
.s14h .ret{ stroke:var(--text-dim); stroke-width:1.4; fill:none; stroke-dasharray:5 4; marker-end:url(#s14h-open); }
.s14h .fill{ fill:var(--text); stroke:none; }
.s14h .act{ fill:var(--panel); stroke:var(--text-dim); stroke-width:1.4; }
.s14h .stick{ stroke:var(--text); stroke-width:1.8; fill:none; }
.s14h .note{ fill:var(--panel-hover); stroke:var(--text-faint); stroke-width:1.2; }
.s14h .i{ fill:var(--text-dim); font-size:12.5px; font-style:italic; }
.s14h .k-blue{ fill:#E6F1FB; stroke:#378ADD; stroke-width:1.6; }
.s14h .kb-blue{ fill:#0C447C; font-size:13px; font-weight:700; }
.s14h .ks-blue{ fill:#185FA5; font-size:13px; }
.s14h .km-blue{ fill:#0C447C; font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .kh-blue{ fill:#185FA5; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14h .k-blue{ fill:#0C447C; stroke:#85B7EB; }
:root[data-theme="dark"] .s14h .kb-blue, :root[data-theme="dark"] .s14h .km-blue{ fill:#E6F1FB; }
:root[data-theme="dark"] .s14h .ks-blue{ fill:#B5D4F4; }
:root[data-theme="dark"] .s14h .kh-blue{ fill:#85B7EB; }
.s14h .ar-blue{ stroke:#378ADD; stroke-width:2; fill:none; marker-end:url(#s14h-blue); }
.s14h .ad-blue{ stroke:#378ADD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-blue); }
.s14h .ln-blue{ stroke:#378ADD; stroke-width:2; fill:none; }
.s14h .k-teal{ fill:#E1F5EE; stroke:#1D9E75; stroke-width:1.6; }
.s14h .kb-teal{ fill:#085041; font-size:13px; font-weight:700; }
.s14h .ks-teal{ fill:#0F6E56; font-size:13px; }
.s14h .km-teal{ fill:#085041; font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .kh-teal{ fill:#0F6E56; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14h .k-teal{ fill:#085041; stroke:#5DCAA5; }
:root[data-theme="dark"] .s14h .kb-teal, :root[data-theme="dark"] .s14h .km-teal{ fill:#E1F5EE; }
:root[data-theme="dark"] .s14h .ks-teal{ fill:#9FE1CB; }
:root[data-theme="dark"] .s14h .kh-teal{ fill:#5DCAA5; }
.s14h .ar-teal{ stroke:#1D9E75; stroke-width:2; fill:none; marker-end:url(#s14h-teal); }
.s14h .ad-teal{ stroke:#1D9E75; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-teal); }
.s14h .ln-teal{ stroke:#1D9E75; stroke-width:2; fill:none; }
.s14h .k-amber{ fill:#FAEEDA; stroke:#BA7517; stroke-width:1.6; }
.s14h .kb-amber{ fill:#633806; font-size:13px; font-weight:700; }
.s14h .ks-amber{ fill:#854F0B; font-size:13px; }
.s14h .km-amber{ fill:#633806; font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .kh-amber{ fill:#854F0B; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14h .k-amber{ fill:#633806; stroke:#EF9F27; }
:root[data-theme="dark"] .s14h .kb-amber, :root[data-theme="dark"] .s14h .km-amber{ fill:#FAEEDA; }
:root[data-theme="dark"] .s14h .ks-amber{ fill:#FAC775; }
:root[data-theme="dark"] .s14h .kh-amber{ fill:#EF9F27; }
.s14h .ar-amber{ stroke:#BA7517; stroke-width:2; fill:none; marker-end:url(#s14h-amber); }
.s14h .ad-amber{ stroke:#BA7517; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-amber); }
.s14h .ln-amber{ stroke:#BA7517; stroke-width:2; fill:none; }
.s14h .k-purple{ fill:#EEEDFE; stroke:#7F77DD; stroke-width:1.6; }
.s14h .kb-purple{ fill:#3C3489; font-size:13px; font-weight:700; }
.s14h .ks-purple{ fill:#534AB7; font-size:13px; }
.s14h .km-purple{ fill:#3C3489; font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .kh-purple{ fill:#534AB7; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14h .k-purple{ fill:#3C3489; stroke:#AFA9EC; }
:root[data-theme="dark"] .s14h .kb-purple, :root[data-theme="dark"] .s14h .km-purple{ fill:#EEEDFE; }
:root[data-theme="dark"] .s14h .ks-purple{ fill:#CECBF6; }
:root[data-theme="dark"] .s14h .kh-purple{ fill:#AFA9EC; }
.s14h .ar-purple{ stroke:#7F77DD; stroke-width:2; fill:none; marker-end:url(#s14h-purple); }
.s14h .ad-purple{ stroke:#7F77DD; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-purple); }
.s14h .ln-purple{ stroke:#7F77DD; stroke-width:2; fill:none; }
.s14h .k-green{ fill:#EAF3DE; stroke:#639922; stroke-width:1.6; }
.s14h .kb-green{ fill:#27500A; font-size:13px; font-weight:700; }
.s14h .ks-green{ fill:#3B6D11; font-size:13px; }
.s14h .km-green{ fill:#27500A; font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .kh-green{ fill:#3B6D11; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14h .k-green{ fill:#27500A; stroke:#97C459; }
:root[data-theme="dark"] .s14h .kb-green, :root[data-theme="dark"] .s14h .km-green{ fill:#EAF3DE; }
:root[data-theme="dark"] .s14h .ks-green{ fill:#C0DD97; }
:root[data-theme="dark"] .s14h .kh-green{ fill:#97C459; }
.s14h .ar-green{ stroke:#639922; stroke-width:2; fill:none; marker-end:url(#s14h-green); }
.s14h .ad-green{ stroke:#639922; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-green); }
.s14h .ln-green{ stroke:#639922; stroke-width:2; fill:none; }
.s14h .k-red{ fill:#FCEBEB; stroke:#E24B4A; stroke-width:1.6; }
.s14h .kb-red{ fill:#791F1F; font-size:13px; font-weight:700; }
.s14h .ks-red{ fill:#A32D2D; font-size:13px; }
.s14h .km-red{ fill:#791F1F; font-size:12.5px; font-family:var(--mono),monospace; }
.s14h .kh-red{ fill:#A32D2D; font-size:13px; font-weight:700; }
:root[data-theme="dark"] .s14h .k-red{ fill:#791F1F; stroke:#F09595; }
:root[data-theme="dark"] .s14h .kb-red, :root[data-theme="dark"] .s14h .km-red{ fill:#FCEBEB; }
:root[data-theme="dark"] .s14h .ks-red{ fill:#F7C1C1; }
:root[data-theme="dark"] .s14h .kh-red{ fill:#F09595; }
.s14h .ar-red{ stroke:#E24B4A; stroke-width:2; fill:none; marker-end:url(#s14h-red); }
.s14h .ad-red{ stroke:#E24B4A; stroke-width:2; fill:none; stroke-dasharray:6 4; marker-end:url(#s14h-red); }
.s14h .ln-red{ stroke:#E24B4A; stroke-width:2; fill:none; }
</style>
<defs><marker id="s14h-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--accent)"/></marker><marker id="s14h-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 z" fill="var(--accent)"/></marker><marker id="s14h-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-faint)"/></marker><marker id="s14h-tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.3"/></marker><marker id="s14h-open" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/></marker><marker id="s14h-solid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker><marker id="s14h-dia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--text-dim)"/></marker><marker id="s14h-odia" viewBox="0 0 16 10" refX="1" refY="5" markerWidth="16" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1 5 L8 1 L15 5 L8 9 z" fill="var(--bg)" stroke="var(--text-dim)" stroke-width="1.2"/></marker><marker id="s14h-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#378ADD"/></marker><marker id="s14h-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#1D9E75"/></marker><marker id="s14h-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#BA7517"/></marker><marker id="s14h-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#7F77DD"/></marker><marker id="s14h-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#639922"/></marker><marker id="s14h-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#E24B4A"/></marker></defs>
<g class="s14h">
<rect x="20" y="60" width="104" height="64" rx="7" class="k-amber"/>
<text x="72.0" y="87.5" text-anchor="middle" class="kb-amber">detect</text>
<text x="72.0" y="105.5" text-anchor="middle" class="ks-amber">alert, report</text>
<rect x="136" y="60" width="104" height="64" rx="7" class="k-purple"/>
<text x="188.0" y="87.5" text-anchor="middle" class="kb-purple">triage</text>
<text x="188.0" y="105.5" text-anchor="middle" class="ks-purple">severity, roles</text>
<line x1="124" y1="92" x2="134" y2="92" class="ar"/>
<rect x="252" y="60" width="104" height="64" rx="7" class="k-red"/>
<text x="304.0" y="87.5" text-anchor="middle" class="kb-red">mitigate</text>
<text x="304.0" y="105.5" text-anchor="middle" class="ks-red">roll back first</text>
<line x1="240" y1="92" x2="250" y2="92" class="ar"/>
<rect x="368" y="60" width="104" height="64" rx="7" class="k-blue"/>
<text x="420.0" y="87.5" text-anchor="middle" class="kb-blue">resolve</text>
<text x="420.0" y="105.5" text-anchor="middle" class="ks-blue">root cause</text>
<line x1="356" y1="92" x2="366" y2="92" class="ar"/>
<rect x="484" y="60" width="104" height="64" rx="7" class="k-teal"/>
<text x="536.0" y="87.5" text-anchor="middle" class="kb-teal">postmortem</text>
<text x="536.0" y="105.5" text-anchor="middle" class="ks-teal">blameless</text>
<line x1="472" y1="92" x2="482" y2="92" class="ar"/>
<rect x="600" y="60" width="104" height="64" rx="7" class="k-green"/>
<text x="652.0" y="87.5" text-anchor="middle" class="kb-green">actions</text>
<text x="652.0" y="105.5" text-anchor="middle" class="ks-green">tracked to done</text>
<line x1="588" y1="92" x2="598" y2="92" class="ar"/>
<path d="M660 126 C 660 190, 70 190, 70 126" class="ad"/>
<text x="360" y="204" text-anchor="middle" class="c">learning feeds back into prevention</text>
</g>
</svg>
<figcaption>Restore service first, investigate second, and focus the postmortem on systems, not on blame.</figcaption>
</figure>

Failures will happen. What matters is detecting them quickly, limiting the damage, and learning from them.

- **Mitigate first**: roll back, switch a feature flag off, fail over. Diagnosis can wait until users are no longer affected.
- **Clear roles**: an incident commander coordinates; others investigate or communicate.
- **Blameless postmortems** ask how the system allowed the failure, not who caused it. People who fear blame hide information; people who feel safe share it. Each postmortem ends with tracked actions.

A NetWarden example: a weekly scan disrupted an old network printer that crashed when probed on port 9100. Mitigation: exclude the printer from the scope. Root cause: fragile devices and no way to exclude single hosts. Actions: add an exclusion list to the scope file (a new requirement), and lower concurrency for the printer subnet.

## Hands on

1. Build the NetWarden image with `docker build -t netwarden:dev netwarden/` and run `docker run --rm netwarden:dev --version`. Compare the image size with `python:3.13`.
2. Run the demo targets on your host and scan them from the container, using `--network host` on Linux.
3. Adapt `examples/scheduled-scan.yml` for your own lab, if you have one you are authorised to scan, or run it with `workflow_dispatch` against the demo targets on a self-hosted runner.
4. Write a short blameless postmortem for the printer incident above, using the headings: summary, impact, timeline, root causes, what went well, actions.

## Summary

- **DevOps** unites development and operations through culture, automation, lean flow, measurement and sharing (**CALMS**).
- **Containers** package an application with its dependencies; **multi-stage builds** keep images small; run as a non-root user.
- Keep **configuration** out of code; describe infrastructure as **code**.
- Release safely with **rolling**, **blue-green** and **canary** deployments and **feature flags**; plan rollbacks.
- Automate operations: NetWarden runs as a **scheduled pipeline** that fails on serious findings.
- Observe with **logs, metrics and traces**; define **SLOs**.
- **DORA metrics** show that speed and stability improve together.
- Handle **incidents** by mitigating first and learning through **blameless postmortems**.
