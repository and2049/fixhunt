// HTML building blocks for the dashboard: layout, theme tokens, badges, code views, side-by-side line diff.
// Server-rendered, no framework; the same pages are served live and exported statically through `Links`.
import type { Snap } from "../oracles";

export const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);

export type Links = {
  hunt: string; findings: string; runs: string; scans: string; docs: string; static: boolean;
  scan(id: string): string; scanFile(id: string, rel: string): string; run(id: string): string; finding(runId: string, pid: string): string; report(runId: string, pid: string): string; fixture(runId: string, pid: string, ext: string): string; events(jobId: string): string;
};

export function serverLinks(): Links {
  return {
    hunt: "/", findings: "/findings", runs: "/runs", scans: "/scans", docs: "/docs", static: false,
    scan: (id) => `/s/${enc(id)}`, scanFile: (id, rel) => `/s/${enc(id)}/${rel}`, run: (id) => `/r/${enc(id)}`, finding: (id, pid) => `/f/${enc(id)}/${enc(pid)}`, report: (id, pid) => `/raw/${enc(id)}/reports/${enc(pid)}.md`, fixture: (id, pid) => `/f/${enc(id)}/${enc(pid)}/fixture`, events: (j) => `/api/jobs/${enc(j)}/events`,
  };
}

/** Links for the static export; `depth` is how many directories below the site root the page lives. */
export function staticLinks(depth: number): Links {
  const b = "../".repeat(depth);
  return {
    hunt: `${b}index.html`, findings: `${b}findings.html`, runs: `${b}runs.html`, scans: `${b}scans.html`, docs: `${b}docs.html`, static: true,
    scan: (id) => `${b}s/${enc(id)}.html`, scanFile: (id, rel) => `${b}raw/${enc(id)}/${rel}`, run: (id) => `${b}r/${enc(id)}.html`, finding: (id, pid) => `${b}f/${enc(id)}/${enc(pid)}.html`, report: (id, pid) => `${b}raw/${enc(id)}/reports/${enc(pid)}.md`, fixture: (id, pid, ext) => `${b}raw/${enc(id)}/fixtures/${enc(pid)}.${ext}`, events: () => "",
  };
}
const enc = (s: string) => encodeURIComponent(s);

// Paper and ink in light mode, neutral greys in dark mode; system fonts, nothing downloaded.
export const CSS = `
:root{--bg:oklch(.975 .004 95);--fg:oklch(.24 .012 150);--mut:oklch(.52 .012 130);--line:oklch(.89 .008 95);--soft:oklch(.955 .006 95);--primary:oklch(.26 .014 150);--primaryfg:oklch(.975 .005 95);--ok:oklch(.5 .14 150);--warn:oklch(.58 .14 70);--info:oklch(.5 .12 250);--bad:oklch(.53 .2 27);--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
@media(prefers-color-scheme:dark){:root{--bg:oklch(.16 0 0);--fg:oklch(.96 0 0);--mut:oklch(.7 0 0);--line:oklch(1 0 0/.12);--soft:oklch(.22 0 0);--primary:oklch(.92 0 0);--primaryfg:oklch(.2 0 0);--ok:oklch(.72 .14 150);--warn:oklch(.78 .14 80);--info:oklch(.7 .12 250);--bad:oklch(.7 .19 22)}}
*{box-sizing:border-box}[hidden]{display:none!important}html{scrollbar-gutter:stable}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 var(--sans);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:underline;text-underline-offset:3px;text-decoration-color:color-mix(in oklch,var(--fg) 30%,transparent)}a:hover{text-decoration-color:var(--fg)}
code,pre,.mono{font-family:var(--mono)}code{font-size:.92em}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px}
header.top{border-bottom:1px solid var(--line)}header.top .wrap{display:flex;align-items:baseline;gap:18px;padding:12px 16px}
.brand{font-weight:600;text-decoration:none}nav.nl{display:flex;gap:14px;margin-left:auto;font-size:13.5px}nav.nl a{text-decoration:none;color:var(--mut)}nav.nl a.on,nav.nl a:hover{color:var(--fg)}
main{padding:24px 0 56px}main>.wrap{display:flex;flex-direction:column;gap:28px}
h1{font-size:20px;font-weight:600;margin:0;letter-spacing:-.01em}h2{font-size:13px;font-weight:600;margin:0 0 8px;text-transform:uppercase;letter-spacing:.06em;color:var(--mut)}h2 .aside,h2.fh .k,h3.sh span{text-transform:none;letter-spacing:0;font-weight:400}
.mt1{margin-top:4px}.mt2{margin-top:8px}.mb2{margin-bottom:8px}.my2{margin:6px 0}.full{width:100%}.inl{display:inline}.between{justify-content:space-between}.end{justify-content:flex-end}.code-in{width:150px}
section{min-width:0}section>p{margin:0 0 8px}p{margin:0}
.meta{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:12.5px;color:var(--mut)}.meta b{font-weight:500;color:var(--fg)}
.mut{color:var(--mut)}.small{font-size:12.5px}.xs{font-size:12px}.err{color:var(--bad)}
.row{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.badge{display:inline-block;border-radius:4px;padding:0 6px;font-size:11.5px;line-height:18px;white-space:nowrap;background:var(--soft);color:var(--fg);text-decoration:none;vertical-align:middle}
.badge.ok{color:var(--ok)}.badge.warn{color:var(--warn)}.badge.bad{color:var(--bad)}.badge.info{color:var(--info)}
.tw{overflow-x:auto}.tbl{border-collapse:collapse;width:100%;font-size:13px}
.tbl th{text-align:left;font-weight:500;font-size:12px;color:var(--mut);padding:4px 8px;border-bottom:1px solid var(--line);white-space:nowrap}
.tbl td{padding:5px 8px;border-bottom:1px solid var(--line);vertical-align:top}.tbl td:first-child,.tbl th:first-child{padding-left:0}.tbl td:last-child,.tbl th:last-child{padding-right:0}
.tbl td.n,.tbl th.n{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}.tbl td.w{min-width:220px;color:var(--mut)}
.toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:10px}.toolbar .cnt{margin-left:auto;font-size:12px;color:var(--mut);font-family:var(--mono)}
input,select{background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:4px;padding:0 8px;height:30px;font:inherit;font-size:13px;min-width:0;width:100%}.toolbar input,.toolbar select{width:auto}
input:focus,select:focus{outline:2px solid color-mix(in oklch,var(--info) 40%,transparent);outline-offset:0}
input[type=checkbox]{appearance:none;width:15px;height:15px;padding:0;margin:0;border:1px solid var(--line);border-radius:3px;display:inline-grid;place-content:center;cursor:pointer}input[type=checkbox]::before{content:"";width:8px;height:4px;border:2px solid var(--primaryfg);border-top:0;border-right:0;transform:translateY(-1px) rotate(-45deg);opacity:0}input[type=checkbox]:checked{background:var(--primary);border-color:var(--primary)}input[type=checkbox]:checked::before{opacity:1}
.field{display:flex;flex-direction:column;gap:3px;min-width:0}.field>span{font-size:11.5px;color:var(--mut)}.field.chk{flex-direction:row;align-items:center;gap:7px;height:30px;font-size:13px;cursor:pointer;user-select:none}
.form{display:grid;gap:10px 12px;grid-template-columns:1fr}@media(min-width:720px){.form{grid-template-columns:repeat(12,1fr);align-items:end}.form .c1{grid-column:span 1}.form .c2{grid-column:span 2}.form .c3{grid-column:span 3}.form .c4{grid-column:span 4}.form .c5{grid-column:span 5}.form .c6{grid-column:span 6}.form .last{grid-column:11/span 2}}
.btn{display:inline-flex;align-items:center;justify-content:center;height:30px;padding:0 12px;border-radius:4px;border:1px solid transparent;background:var(--primary);color:var(--primaryfg);font:inherit;font-size:13px;font-weight:500;cursor:pointer;white-space:nowrap}.btn[disabled]{opacity:.5;cursor:default}
.btn.outline{background:transparent;color:var(--fg);border-color:var(--line)}
.seg{display:inline-flex;background:var(--soft);border-radius:4px;padding:2px;gap:2px;margin-bottom:10px}.seg button{border:0;background:transparent;color:var(--mut);font:inherit;font-size:13px;padding:3px 10px;border-radius:3px;cursor:pointer}.seg button.on{background:var(--bg);color:var(--fg)}
.code{position:relative;background:var(--soft);border-radius:4px;overflow:auto;font-family:var(--mono);font-size:12.5px;line-height:1.5;margin:0}
pre.code{padding:8px 10px;white-space:pre}pre.code.wrapped{white-space:pre-wrap}
.code .ln{display:grid;grid-template-columns:2.6em 1fr;white-space:pre}.code .ln>i{color:var(--mut);text-align:right;padding:0 .8em 0 .4em;user-select:none;font-style:normal;opacity:.7}.code .ln>s{text-decoration:none;padding-right:12px}
.code .ln.del{background:color-mix(in oklch,var(--bad) 14%,transparent)}.code .ln.add{background:color-mix(in oklch,var(--ok) 16%,transparent)}.code .ln.gap{background:repeating-linear-gradient(135deg,transparent 0 6px,var(--line) 6px 7px);min-height:1.5em}
.code .ln:first-child{padding-top:6px}.code .ln:last-child{padding-bottom:6px}
.cp{position:absolute;top:4px;right:4px;opacity:0;height:22px;padding:0 6px;font-size:11px}.code:hover .cp,.cp:focus{opacity:1}
.sbs,.out{display:grid;grid-template-columns:1fr;gap:12px}@media(min-width:860px){.sbs,.out{grid-template-columns:1fr 1fr}}.sbs>div,.out>div{min-width:0}.sbs .hd,.out .hd{display:flex;align-items:center;gap:8px;margin-bottom:4px;font-size:12px;color:var(--mut)}
.kv{display:grid;grid-template-columns:max-content 1fr;gap:4px 14px;font-size:12.5px;margin:0}.kv dt{color:var(--mut)}.kv dd{margin:0;min-width:0;overflow-wrap:anywhere}
.diff .a{color:var(--ok)}.diff .d{color:var(--bad)}.diff .h{color:var(--info)}
details>summary{cursor:pointer;font-size:13px;color:var(--mut)}details>summary:hover{color:var(--fg)}details>*:not(summary){margin-top:8px}
.lst{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:3px;font-size:13px}
.note{border-left:2px solid var(--line);padding:2px 10px;font-size:13px;color:var(--mut)}
h2.fh{font-size:17px;font-weight:600;color:var(--fg);text-transform:none;letter-spacing:-.01em;margin:0 0 10px;padding-top:18px;border-top:1px solid var(--line)}h2.fh .k{color:var(--mut);font-size:14px;margin-left:6px}
h3.sh{font-size:12px;font-weight:600;color:var(--mut);margin:14px 0 4px;text-transform:uppercase;letter-spacing:.05em}
details.rk>summary{font-size:13px;color:var(--fg)}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
`;

const SCRIPT = `
(function(){
document.addEventListener("click",function(e){var b=e.target.closest("[data-copy]");if(!b)return;var t=document.getElementById(b.getAttribute("data-copy"));var s=t?(t.getAttribute("data-text")||t.textContent):"";navigator.clipboard.writeText(s).then(function(){var o=b.textContent;b.textContent="copied";setTimeout(function(){b.textContent=o},1200)})});
var tb=document.querySelector("[data-filters]");if(!tb)return;var tbl=document.querySelector(tb.getAttribute("data-filters"));if(!tbl)return;
var rows=[].slice.call(tbl.querySelectorAll("tbody tr")),cnt=tb.querySelector(".cnt"),ctl=[].slice.call(tb.querySelectorAll("[name]"));
function val(c){return c.type==="checkbox"?(c.checked?"1":""):c.value}
function apply(){var n=0;rows.forEach(function(r){var ok=ctl.every(function(c){var v=val(c);if(!v)return true;if(c.name==="q")return r.textContent.toLowerCase().indexOf(v.toLowerCase())>=0;return r.getAttribute("data-"+c.name)===v});r.style.display=ok?"":"none";if(ok)n++});if(cnt)cnt.textContent=n+" / "+rows.length;
var h=ctl.filter(function(c){return val(c)}).map(function(c){return c.name+"="+encodeURIComponent(val(c))}).join("&");history.replaceState(null,"",location.pathname+(h?"#"+h:""))}
var h=location.hash.slice(1);if(h)h.split("&").forEach(function(p){var kv=p.split("=");ctl.forEach(function(c){if(c.name!==kv[0])return;if(c.type==="checkbox")c.checked=true;else c.value=decodeURIComponent(kv[1]||"")})});
ctl.forEach(function(c){c.addEventListener("input",apply);c.addEventListener("change",apply)});apply();
})();`;

export type Active = "hunt" | "findings" | "runs" | "scans" | "docs" | "";

export function layout(o: { title: string; active: Active; L: Links; body: string; head?: string }): string {
  const nl = (href: string, key: Active, text: string) => `<a class="${o.active === key ? "on" : ""}" href="${href}">${text}</a>`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(o.title)}</title><style>${CSS}</style>${o.head ?? ""}</head><body>
<header class="top"><div class="wrap"><a class="brand" href="${o.L.hunt}">fixhunt</a><nav class="nl">${nl(o.L.hunt, "hunt", "New")}${nl(o.L.findings, "findings", "Findings")}${nl(o.L.runs, "runs", "Runs")}${nl(o.L.scans, "scans", "Scans")}${nl(o.L.docs, "docs", "Docs")}</nav></div></header>
<main><div class="wrap">${o.body}</div></main>
<script>${SCRIPT}</script>
</body></html>`;
}

// components
export const badge = (text: string, cls = "") => `<span class="badge ${cls}">${esc(text)}</span>`;
export const section = (title: string | undefined, body: string, aside = "") => `<section>${title ? `<h2>${esc(title)}${aside ? ` <span class="aside">${aside}</span>` : ""}</h2>` : ""}${body}</section>`;
export const kv = (rows: Array<[string, string]>) => `<dl class="kv">${rows.filter(([, v]) => v).map(([k, v]) => `<dt>${esc(k)}</dt><dd>${v}</dd>`).join("")}</dl>`;
export const table = (head: string[], rows: string, id = "") => `<div class="tw"><table class="tbl" ${id ? `id="${id}"` : ""}><thead><tr>${head.map((h) => `<th${h.startsWith("#") ? ' class="n"' : ""}>${esc(h.replace(/^#/, ""))}</th>`).join("")}</tr></thead><tbody>${rows}</tbody></table></div>`;
export const empty = (text: string) => `<p class="mut small">${esc(text)}</p>`;

export function gradeBadge(grade: string, severity?: string): string {
  const cls = grade === "real" ? "bad" : grade === "unclear" || grade === "unjudged" ? "warn" : "";
  return badge(grade === "unjudged" ? "unjudged" : severity && severity !== "-" ? `${grade} · ${severity}` : grade, cls);
}
export const kindBadge = (kind: string) => badge(kind, kind === "fix-breaks-syntax" || kind === "tool-crash" || kind === "fix-breaks-build" ? "bad" : "warn");
export const labelBadge = (safe: boolean, fixKind = "unsafe") => (safe ? badge("labelled safe", "warn") : badge(`labelled ${fixKind}`));
export const upstreamBadge = (u: string) => (u === "duplicate" ? badge("duplicate") : u === "related" ? badge("related") : badge("no match", "info"));
export const modelBadge = (name: string) => badge(name);

let ids = 0;
const copyBtn = (id: string) => `<button class="btn outline cp" type="button" data-copy="${id}">copy</button>`;

/** Plain code block with line numbers and a copy button. */
export function codeBlock(code: string, marks: Map<number, "del" | "add"> = new Map()): string {
  const id = `c${++ids}`;
  const lines = code.replace(/\n$/, "").split("\n");
  return `<div class="code"><div id="${id}" data-text="${esc(code)}">${lines.map((l, i) => `<div class="ln ${marks.get(i) ?? ""}"><i>${i + 1}</i><s>${esc(l) || " "}</s></div>`).join("")}</div>${copyBtn(id)}</div>`;
}
/** Preformatted text (commands, outputs) with a copy button. */
export function pre(text: string, cls = ""): string {
  const id = `c${++ids}`;
  return `<div class="code"><pre class="code ${cls}" id="${id}" style="background:none">${esc(text)}</pre>${copyBtn(id)}</div>`;
}

type Op = { t: "same" | "del" | "add"; a?: string; b?: string };

/** Line-level LCS diff; inputs are small (minimized programs). */
export function diffLines(a: string, b: string): Op[] {
  const A = a.replace(/\n$/, "").split("\n"), B = b.replace(/\n$/, "").split("\n");
  const n = A.length, m = B.length;
  const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) dp[i][j] = A[i] === B[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const ops: Op[] = [];
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (A[i] === B[j]) { ops.push({ t: "same", a: A[i], b: B[j] }); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { ops.push({ t: "del", a: A[i] }); i++; }
    else { ops.push({ t: "add", b: B[j] }); j++; }
  }
  while (i < n) ops.push({ t: "del", a: A[i++] });
  while (j < m) ops.push({ t: "add", b: B[j++] });
  return ops;
}

/** Two aligned columns: the program before the fix and after it, changed lines highlighted. */
export function sideBySide(before: string, after: string, titles: [string, string] = ["before", "after"]): string {
  const ops = diffLines(before, after);
  const left: string[] = [], right: string[] = [];
  let la = 0, lb = 0;
  const cell = (n: number | null, text: string | undefined, cls: string) => `<div class="ln ${cls}"><i>${n ?? ""}</i><s>${text === undefined ? "" : esc(text) || " "}</s></div>`;
  let k = 0;
  while (k < ops.length) {
    if (ops[k].t === "same") { left.push(cell(++la, ops[k].a, "")); right.push(cell(++lb, ops[k].b, "")); k++; continue; }
    const dels: Op[] = [], adds: Op[] = [];
    while (k < ops.length && ops[k].t !== "same") { (ops[k].t === "del" ? dels : adds).push(ops[k]); k++; }
    const rows = Math.max(dels.length, adds.length);
    for (let r = 0; r < rows; r++) {
      left.push(r < dels.length ? cell(++la, dels[r].a, "del") : cell(null, undefined, "gap"));
      right.push(r < adds.length ? cell(++lb, adds[r].b, "add") : cell(null, undefined, "gap"));
    }
  }
  const col = (title: string, cells: string[], text: string) => { const id = `c${++ids}`; return `<div><div class="hd">${esc(title)}</div><div class="code"><div id="${id}" data-text="${esc(text)}">${cells.join("")}</div>${copyBtn(id)}</div></div>`; };
  return `<div class="sbs">${col(titles[0], left, before)}${col(titles[1], right, after)}</div>`;
}

export const exitBadge = (s: { code: number | null; timedOut: boolean } | undefined) => (!s ? badge("not run") : s.timedOut ? badge("timed out", "bad") : badge(`exit ${s.code}`, s.code === 0 ? "ok" : "bad"));

function snapHtml(s: Snap | undefined, title: string): string {
  if (!s) return `<div><div class="hd">${esc(title)}${exitBadge(undefined)}</div><pre class="code">(not run)</pre></div>`;
  const body = [s.stdout.trimEnd() || "(no stdout)", s.stderr1 ? `\n${s.stderr1}` : ""].join("");
  return `<div><div class="hd">${esc(title)}${exitBadge(s)}</div><pre class="code">${esc(body)}</pre></div>`;
}

export function outputPair(before: Snap, after?: Snap, titles: [string, string] = ["stdout before", "stdout after"]): string {
  return `<div class="out">${snapHtml(before, titles[0])}${snapHtml(after, titles[1])}</div>`;
}

export function unifiedDiff(d: string): string {
  return `<pre class="code diff">${d.split("\n").map((l) => (l.startsWith("+++") || l.startsWith("---") || l.startsWith("@@") ? `<span class="h">${esc(l)}</span>` : l.startsWith("+") ? `<span class="a">${esc(l)}</span>` : l.startsWith("-") ? `<span class="d">${esc(l)}</span>` : esc(l))).join("\n")}</pre>`;
}

/** Only http(s) links are rendered as links; anything else becomes a harmless anchor. */
export const safeUrl = (u: string) => (/^https?:\/\//i.test(u) ? u : "#");
export const ext = (u: string, text: string) => `<a href="${esc(safeUrl(u))}" target="_blank" rel="noopener">${esc(text)}</a>`;
export const money = (n: number) => (n < 0.01 ? `$${n.toFixed(4)}` : `$${n.toFixed(2)}`);
export const when = (iso: string) => iso.replace("T", " ").slice(0, 16) + " UTC";
