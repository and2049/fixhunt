// Dashboard pages. Each returns a full HTML document; links go through `Links` so the same pages work served live or exported statically.
import { readFileSync } from "node:fs";
import type { Finding, Run, Scan, ScanFindingRow, ScanUpstream, Spend, Stats } from "./data";
import { MODELS } from "../config";
import { badge, codeBlock, empty, esc, exitBadge, ext, gradeBadge, kindBadge, kv, labelBadge, layout, modelBadge, money, outputPair, pre, safeUrl, section, sideBySide, table, unifiedDiff, upstreamBadge, when, type Links } from "./html";

const KIND_TITLE: Record<string, string> = { "fix-changes-behavior": "fix changes program behavior", "fix-breaks-syntax": "fixed output does not parse", "fix-not-fixpoint": "fix is not a fixpoint", "fix-introduces-diagnostic": "fix introduces new diagnostics", "tool-crash": "tool crashes", "fix-breaks-build": "fix breaks the build" };
const kindTitle = (k: string) => KIND_TITLE[k] ?? k;
const ruleLabel = (r: Run) => `${r.tool} ${r.rule.rule}`;
/** "ruff 0.17.1", "biome 2.5.15": ruff's version string already starts with the tool name. */
const toolVersion = (r: { tool: string; version: string }) => (r.version.toLowerCase().startsWith(r.tool.toLowerCase()) ? r.version : `${r.tool} ${r.version}`);
const versionOnly = (r: { tool: string; version: string }) => toolVersion(r).slice(r.tool.length + 1);
const projectName = (p: string) => p.replace(/\/+$/, "").split("/").pop() ?? p;
const projectLink = (p: string) => (/^https?:\/\//.test(p) ? ext(p, p) : `<span class="mono">${esc(p)}</span>`);
/** JSON for an inline script: "<" is escaped so no value can close the script element. */
const js = (v: unknown) => JSON.stringify(v).replace(/</g, "\\u003c");
const h1 = (title: string, meta = "", actions = "") => `<div><div class="row between"><h1>${title}</h1>${actions ? `<div class="row">${actions}</div>` : ""}</div>${meta ? `<div class="meta mt1">${meta}</div>` : ""}</div>`;

// ---------------------------------------------------------------------------------------------- home: new hunt or scan

export type HuntPageData = {
  catalog: Record<string, Array<{ rule: string; fixKind: string }>>; toolIds: string[]; scanTools: string[]; sweep?: Record<string, number>; busy?: { id: string; kind: string }; gated: boolean;
  findings: Finding[]; limits: { maxN: number; maxRounds: number; scanLimit: number };
  /** Prefills offered under the forms. */
  examples?: { hunts: Array<{ tool: string; rule: string }>; scans: Array<{ tool: string; repo: string; path: string; run: string; rules: string }> };
};

export function huntPage(d: HuntPageData, L: Links): string {
  const sel = (ids: string[]) => `<select name="tool">${ids.map((t) => `<option value="${esc(t)}">${esc(t)}</option>`).join("")}</select>`;
  const access = d.gated && !L.static ? `<form id="af" class="row"><input id="code" name="code" placeholder="access code" autocomplete="off" class="code-in"><button class="btn outline" type="submit">Unlock</button><span class="xs mut" id="astatus"></span></form>` : "";
  const forms = L.static ? `<p class="mut small">Live hunts and scans need the server: <code>bun src/cli.ts serve</code></p>` : `
<section><h2 id="h1">Hunt a rule</h2><div class="seg" id="mode"><button type="button" class="on" data-m="rule">Rule</button><button type="button" data-m="repo">Repository</button></div>
<form id="hf" class="form">
<label class="field c2"><span>tool</span>${sel(d.toolIds)}</label>
<label class="field c4"><span>rule</span><input name="rule" list="rules" placeholder="rule id" required autocomplete="off"><datalist id="rules"></datalist></label>
<label class="field c1"><span>programs</span><input name="n" type="number" min="2" max="${d.limits.maxN}" value="6"></label>
<label class="field c1"><span>rounds</span><input name="rounds" type="number" min="1" max="${d.limits.maxRounds}" value="1"></label>
<label class="field chk c2"><input type="checkbox" name="unsafe">unsafe fixes</label>
<div class="last"><button class="btn full" type="submit">Start hunt</button></div>
</form>
<form id="sf" class="form" hidden>
<label class="field c2"><span>tool</span>${sel(d.scanTools)}</label>
<label class="field c4"><span>repository</span><input name="repo" type="url" placeholder="https://github.com/owner/repo" required></label>
<label class="field c2"><span>path</span><input name="path" placeholder="optional subdirectory" autocomplete="off"></label>
<label class="field c4"><span>command</span><input name="run" placeholder="pip install -q . && pytest -q" required></label>
<label class="field c6"><span>rules</span><input name="rules" placeholder="ids separated by commas" autocomplete="off"></label>
<label class="field c1"><span>limit</span><input name="limit" type="number" min="1" max="${d.limits.scanLimit}" value="${d.limits.scanLimit}"></label>
<label class="field chk c2"><input type="checkbox" name="unsafe">unsafe fixes</label>
<div class="last"><button class="btn full" type="submit">Start scan</button></div>
</form>
${d.examples ? `<p class="small mt2" id="ex"><span class="mut">Examples:</span> <span data-for="rule">${d.examples.hunts.map((e) => `<a href="#" data-ex="${esc(JSON.stringify(e))}">${esc(e.tool)} ${esc(e.rule.split("/").pop() ?? e.rule)}</a>`).join(" · ")}</span><span data-for="repo" hidden>${d.examples.scans.map((e) => `<a href="#" data-ex="${esc(JSON.stringify(e))}">${esc(e.tool)} on ${esc(e.path || e.repo)}</a>`).join(" · ")}</span></p>` : ""}
${d.busy ? `<p class="xs mt2">A ${esc(d.busy.kind)} is running. <a href="#" id="attach" data-id="${esc(d.busy.id)}" data-kind="${esc(d.busy.kind)}">Attach</a></p>` : ""}</section>`;
  const job = L.static ? "" : `<section id="job" hidden><h2 id="jt">job</h2><div class="meta" id="jmeta"></div><p class="small" id="jstatus" class="my2"></p>
<div class="tw"><table class="tbl" id="jtbl"><thead id="jhead"></thead><tbody id="jrows"></tbody></table></div>
<p class="small" id="jfoot" class="mt2"></p>
<details class="mt2"><summary>log</summary><pre class="code" id="log"></pre></details></section>`;
  const byRule = groupByRule(d.findings).slice(0, 12);
  const recent = byRule.length ? section("Rules with findings", ruleTable(byRule, L), `<a href="${L.findings}">all findings</a>`) : "";
  const script = L.static ? "" : `<script>
var RULES=${js(d.catalog)},SWEEP=${js(d.sweep ?? {})};
(function(){
var $=function(s){return document.querySelector(s)};
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function badge(t,c){return '<span class="badge '+(c||"")+'">'+esc(t)+'</span>'}
function tv(t,v){return v.toLowerCase().indexOf(t.toLowerCase())===0?v:t+" "+v}
function gh(u){return u.replace(/^https:\\/\\/github\\.com\\//,"")}
function lnk(u,t,c){if(!/^https?:\\/\\//i.test(String(u)))return badge(t,c);return '<a class="badge '+(c||"")+'" href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(t)+'</a>'}
var job=$("#job"),jt=$("#jt"),jmeta=$("#jmeta"),jstatus=$("#jstatus"),jhead=$("#jhead"),jrows=$("#jrows"),jfoot=$("#jfoot"),log=$("#log");
var S={kind:"hunt",n:0,done:0,f:0,t0:0,timer:null,sid:""};
var HEAD={hunt:'<tr><th>program</th><th>result</th><th>title</th><th>detail</th></tr>',scan:'<tr><th>rule</th><th>result</th><th class="n">files</th><th class="n">sites</th><th class="n">exit</th><th>detail</th></tr>'};
function status(t){jstatus.textContent=t}
function tick(){var s=Math.round((Date.now()-S.t0)/1000);jt.textContent=S.kind+" · "+s+" s"}
function buttons(on){[].forEach.call(document.querySelectorAll("#hf button[type=submit],#sf button[type=submit]"),function(b){b.disabled=!on})}
function start(kind){clearInterval(S.timer);S={kind:kind,n:0,done:0,f:0,t0:Date.now(),timer:setInterval(tick,1000),sid:""};job.hidden=false;jhead.innerHTML=HEAD[kind];jrows.innerHTML="";jfoot.innerHTML="";jmeta.innerHTML="";log.textContent="";status("starting");tick();buttons(false)}
function finish(){clearInterval(S.timer);buttons(true);var a=$("#attach");if(a)a.parentNode.remove()}
function fail(msg){jstatus.innerHTML='<span class="err">'+esc(msg)+'</span>';finish()}
function row(key,html,first){var tr=document.createElement("tr");tr.setAttribute("data-key",key);tr.innerHTML=html;if(first)jrows.prepend(tr);else jrows.appendChild(tr);return tr}
function find(key){return [].filter.call(jrows.children,function(t){return t.getAttribute("data-key")===key})[0]}
function append(key,html){var r=find(key);if(r)r.lastChild.insertAdjacentHTML("beforeend",'<div class="row">'+html+'</div>')}
function onHunt(e){
 if(e.type==="start"){jmeta.innerHTML='<b>'+esc(tv(e.tool,e.version))+'</b><span>'+esc(e.rule)+'</span>'+badge("labelled "+e.fixKind,e.fixKind==="safe"?"warn":"")+'<span>'+esc(e.sandbox)+'</span>';status("reading the rule documentation")}
 else if(e.type==="analysis"){status("analysis: "+e.hazards.length+" hazards, "+e.firingShapes+" firing shapes ($"+e.cost.toFixed(4)+"); generating programs")}
 else if(e.type==="round"){S.n+=e.programs;status("round "+e.round+": "+e.programs+" programs ($"+e.cost.toFixed(4)+"); evaluating")}
 else if(e.type==="round-failed"){status("round "+e.round+" failed");log.textContent+=e.error+"\\n"}
 else if(e.type==="program"){var f=e.status==="finding";var st=f?e.kinds.filter(function(k){return k!=="disputed"}).map(function(k){return badge(k,"bad")}).join(" "):e.status==="fix-ok"?badge("fix ok","ok"):e.status==="silent"?badge("silent"):e.status==="fired-no-fix"?badge("fired, no fix"):badge(e.status,"warn");
   row(e.id,'<td class="mono">'+esc(e.id)+'</td><td>'+st+'</td><td>'+esc(e.title)+'</td><td class="w xs">'+esc(e.detail.length>160?e.detail.slice(0,160)+"…":e.detail)+'</td>',f);S.done++;if(f)S.f++;status(S.done+"/"+S.n+" evaluated"+(S.f?", "+S.f+" findings":""))}
 else if(e.type==="log"){log.textContent+=e.message+"\\n";status(e.message)}
 else if(e.type==="report"){append(e.programId,badge(e.lines.before+" → "+e.lines.after+" lines")+(e.grade?badge(e.grade+(e.severity?" · "+e.severity:""),e.grade==="real"?"bad":""):"")+(e.duplicates.length?e.duplicates.map(function(x){return lnk(x.url,x.relation+" "+gh(x.url))}).join(""):badge("no upstream match","info")))}
 else if(e.type==="done"){status(e.findings+" findings; model cost $"+e.cost.toFixed(4));jfoot.innerHTML='<a href="/r/'+encodeURIComponent(e.runId)+'">Open run</a>';finish()}
 else if(e.type==="error")fail(e.message)}
function onScan(e){
 if(e.type==="clone"){if(e.done)status("cloned "+e.mb+" MB"+(e.head?" at "+e.head:""));else{jmeta.innerHTML='<b>'+esc(e.url)+'</b>';status("cloning")}}
 else if(e.type==="start"){jmeta.innerHTML='<b>'+esc(tv(e.tool,e.version))+'</b><span>'+esc(e.dir)+'</span><code>'+esc(e.run)+'</code><span>'+esc(e.sandbox)+'</span>';status("reading the configuration")}
 else if(e.type==="risk"){var t=e.enabled!=null?e.enabled+" rules enabled by "+(e.file||"the defaults"):(e.note||"");if(e.known.length)t+="; known-risk: "+e.known.map(function(k){return k.rule}).join(", ");status(t)}
 else if(e.type==="rules"){S.n=e.count;status(S.n+" rules to try; running the command on the unmodified project twice")}
 else if(e.type==="baseline"){status(e.deterministic?"baseline exit "+e.code+", "+e.lines+" lines; applying fixes":"baseline is not deterministic")}
 else if(e.type==="rule"){S.done++;if(e.status==="finding")S.f++;var st=e.status==="finding"?badge(e.kind,"bad"):e.status==="same"?badge("no difference","ok"):e.status==="no-change"?badge("no change"):badge("not compared","warn");if(e.lint&&e.lint.after)st+=" "+badge("sites left","warn");
   row(e.rule,'<td class="mono">'+esc(e.rule)+'</td><td>'+st+'</td><td class="n">'+(e.changedFiles||0)+'</td><td class="n">'+(e.lint?e.lint.before+" → "+e.lint.after:"")+'</td><td class="n">'+(e.exitBefore!=null?e.exitBefore+" → "+e.exitAfter:"")+'</td><td class="w xs">'+esc(e.detail||"")+'</td>',e.status==="finding");status(S.done+"/"+S.n+" rules"+(S.f?", "+S.f+" changed the outcome":""))}
 else if(e.type==="minimal"){append(e.rule,badge("reduced to "+e.minimal.hunks+" of "+e.minimal.of+" hunks"+(e.minimal.complete?"":", budget exhausted"),e.minimal.confirmed?"":"warn")+'<span class="xs mut">'+esc(e.minimal.files.join(", "))+(e.minimal.confirmed?"; patch confirmed":"; "+esc(e.minimal.note||"not confirmed"))+'</span>')}
 else if(e.type==="judge"){append(e.rule,badge(e.verdict.grade+" · "+e.verdict.severity,e.verdict.grade==="real"?"bad":"")+'<span class="xs mut">'+esc(e.verdict.why.slice(0,200))+'</span>')}
 else if(e.type==="upstream"){var u=e.upstream;append(e.rule,(u.duplicates.length?u.duplicates.map(function(d){return lnk(d.url,d.relation+" "+gh(d.url))}).join(""):badge("no upstream match","info"))+(u.fixedIn?lnk(u.fixedUrl||"","a snippet says fixed in "+u.fixedIn):"")+(u.bank?'<a class="badge" href="/f/'+encodeURIComponent(u.bank.runId)+'/'+encodeURIComponent(u.bank.programId)+'">'+u.bank.findings+' in the findings bank</a>':""))}
 else if(e.type==="combined"){var c=e.combined;jfoot.innerHTML=c.rules.length+' rule(s) applied together changed '+c.files+' file(s) with '+(c.verified?'no difference under the command':'a difference: '+esc(c.note||("exit "+c.exitBefore+" → "+c.exitAfter)))+'.'+(c.patch?' <a id="patch" href="#">accepted.patch</a>':"")}
 else if(e.type==="done"){status(e.findings+" of "+e.rules+" rules changed the outcome, "+e.accepted+" did not"+(e.errors?", "+e.errors+" not compared":"")+"; model cost $"+e.cost.toFixed(4));jfoot.insertAdjacentHTML("beforeend",' <a href="/s/'+encodeURIComponent(e.scanId)+'">Open scan</a>');var pl=$("#patch");if(pl)pl.href="/s/"+encodeURIComponent(e.scanId)+"/accepted.patch";finish()}
 else if(e.type==="error")fail(e.message)}
function watch(id,kind){var es=new EventSource("/api/jobs/"+encodeURIComponent(id)+"/events"),opened=false;es.onopen=function(){if(opened)start(kind);opened=true};es.onmessage=function(m){var e=JSON.parse(m.data);(kind==="scan"?onScan:onHunt)(e);if(e.type==="done"||e.type==="error")es.close()};es.onerror=function(){status("connection lost; reload to re-attach")}}
function submit(url,body,kind){start(kind);fetch(url,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(body)}).then(function(r){return r.json()}).then(function(j){if(j.error){fail(j.error);return}watch(j.id,kind)}).catch(function(e){fail(String(e))})}
$("#hf").addEventListener("submit",function(ev){ev.preventDefault();var f=new FormData(ev.target);submit("/api/hunt",{tool:f.get("tool"),rule:f.get("rule"),n:Number(f.get("n")),rounds:Number(f.get("rounds")),unsafe:!!f.get("unsafe")},"hunt")});
$("#sf").addEventListener("submit",function(ev){ev.preventDefault();var f=new FormData(ev.target);submit("/api/scan",{tool:f.get("tool"),repo:f.get("repo"),path:f.get("path"),run:f.get("run"),rules:f.get("rules"),limit:Number(f.get("limit")),unsafe:!!f.get("unsafe")},"scan")});
function hint(){var t=$("#sf [name=tool]").value,n=SWEEP[t]||0,u=$("#sf [name=unsafe]").checked,i=$("#sf [name=rules]");i.placeholder=n?"all "+n+" fixes labelled safe, or ids separated by commas":u?"every rule, or ids separated by commas":"ids separated by commas (no fix of this tool is labelled safe)";i.required=!n&&!u}
$("#sf").addEventListener("change",hint);hint();
$("#mode").addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;var m=b.getAttribute("data-m");[].forEach.call($("#mode").children,function(x){x.classList.toggle("on",x===b)});$("#hf").hidden=m!=="rule";$("#sf").hidden=m!=="repo";$("#h1").textContent=m==="rule"?"Hunt a rule":"Scan a repository";[].forEach.call(document.querySelectorAll("#ex [data-for]"),function(x){x.hidden=x.getAttribute("data-for")!==m})});
var ex=$("#ex");if(ex)ex.addEventListener("click",function(e){var a=e.target.closest("a[data-ex]");if(!a)return;e.preventDefault();var v=JSON.parse(a.getAttribute("data-ex"));var f=v.repo?$("#sf"):$("#hf");Object.keys(v).forEach(function(k){var i=f.querySelector("[name="+k+"]");if(i)i.value=v[k]});if(!v.repo)rules();else hint();f.querySelector("[name="+(v.repo?"run":"rule")+"]").focus()});
var tsel=$("#hf [name=tool]"),dl=$("#rules");function rules(){var t=tsel.value;dl.innerHTML=(RULES[t]||[]).map(function(r){return '<option value="'+esc(r.rule)+'">'+esc(r.rule+" ("+r.fixKind+")")+'</option>'}).join("")}
tsel.addEventListener("change",function(){$("#hf [name=rule]").value="";rules()});rules();
var af=$("#af");function showBudget(j){var s=$("#astatus");if(!s)return;s.textContent=j.ok?"$"+j.remaining.toFixed(2)+" of $"+j.daily.toFixed(2)+" today":"locked · $"+j.global.toFixed(2)+" left today"}
if(af){fetch("/api/access").then(function(r){return r.json()}).then(showBudget).catch(function(){});af.addEventListener("submit",function(ev){ev.preventDefault();fetch("/api/access",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({code:$("#code").value.trim()})}).then(function(r){return r.json()}).then(function(j){if(j.error){$("#astatus").textContent=j.error;return}$("#code").value="";showBudget(j)})})}
var at=$("#attach");if(at)at.addEventListener("click",function(ev){ev.preventDefault();start(at.getAttribute("data-kind"));watch(at.getAttribute("data-id"),at.getAttribute("data-kind"))});
})();
</script>`;
  const body = `${access ? `<div class="row end">${access}</div>` : ""}${forms}${job}${recent}${script}`;
  return layout({ title: "fixhunt", active: "hunt", L, body });
}

// ---------------------------------------------------------------------------------------------- findings

type RuleGroup = { tool: string; rule: string; fixKind: string; safe: boolean; findings: Finding[]; real: number; best: Finding };

/** One row per tool and rule, ordered like the ranked findings (the best finding of a rule decides). */
function groupByRule(fs: Finding[]): RuleGroup[] {
  const m = new Map<string, RuleGroup>();
  for (const f of fs) {
    const key = `${f.run.tool}|${f.run.rule.rule}`;
    const g = m.get(key) ?? { tool: f.run.tool, rule: f.run.rule.rule, fixKind: f.run.rule.fixKind, safe: false, findings: [], real: 0, best: f };
    g.findings.push(f);
    if (f.report.safeLabel) g.safe = true;
    if (f.grade === "real") g.real++;
    m.set(key, g);
  }
  return [...m.values()];
}

function ruleTable(groups: RuleGroup[], L: Links): string {
  return table(["rule", "tool", "label", "#findings", "#judged real", "upstream", "example"], groups.map((g) => {
    return `<tr data-tool="${esc(g.tool)}"><td class="mono"><a href="${L.finding(g.best.run.id, g.best.report.programId)}">${esc(g.rule)}</a></td><td>${esc(g.tool)}</td><td>${labelBadge(g.safe, g.fixKind)}</td><td class="n">${g.findings.length}</td><td class="n">${g.real}</td><td>${upstreamBadge(g.best.upstream)}</td><td class="w">${esc(trunc(g.best.report.verdict?.why ?? g.best.result.title, 120))}</td></tr>`;
  }).join(""));
}

export function findingsPage(st: Stats, fs: Finding[], L: Links): string {
  const rows = fs.map((f) => `<tr data-tool="${esc(f.run.tool)}" data-grade="${esc(f.grade)}" data-safe="${f.report.safeLabel ? 1 : 0}" data-up="${esc(f.upstream)}">
<td class="n">${f.rank}</td><td class="mono"><a href="${L.finding(f.run.id, f.report.programId)}">${esc(f.run.rule.rule)}</a></td><td>${esc(f.run.tool)}</td><td>${kindBadge(f.report.kind)}</td><td>${labelBadge(f.report.safeLabel, f.run.rule.fixKind)}</td><td>${gradeBadge(f.grade, f.severity)}</td><td>${upstreamBadge(f.upstream)}</td><td class="w">${esc(trunc(f.report.verdict?.why ?? f.result.title, 140))}</td></tr>`).join("");
  const grades = Object.entries(st.grades).sort((a, b) => b[1] - a[1]).map((g) => g[0]);
  const opt = (vs: string[], all: string) => `<option value="">${esc(all)}</option>${vs.map((v) => `<option value="${esc(v)}">${esc(v)}</option>`).join("")}`;
  const groups = groupByRule(fs);
  const body = `${h1("Findings")}
${section("By rule", ruleTable(groups, L))}
${section("All findings", `<div class="toolbar" data-filters="#ft"><select name="tool">${opt(st.tools, "all tools")}</select><select name="grade">${opt(grades, "all grades")}</select><select name="safe"><option value="">any label</option><option value="1">labelled safe</option><option value="0">labelled unsafe</option></select><select name="up"><option value="">any upstream</option><option value="none">no match</option><option value="related">related</option><option value="duplicate">duplicate</option></select><input name="q" placeholder="search"><span class="cnt"></span></div>${rows ? table(["#", "rule", "tool", "oracle", "label", "judge", "upstream", "summary"], rows, "ft") : empty("No findings yet")}`)}`;
  return layout({ title: "Findings · fixhunt", active: "findings", L, body });
}

export function findingPage(f: Finding, L: Links): string {
  const { run, report: rep, result: res } = f;
  const ev = rep.evidence;
  const before = rep.minimized;
  const after = ev?.fixed || applyHint(res);
  const v = rep.verdict;
  const dd = rep.dedup;
  const rerun = L.static ? "" : `<div class="row mt2"><button class="btn outline" id="rerun" type="button">Re-run in a sandbox</button><span id="rerun-out" class="small"></span></div><div id="rerun-res"></div>
<script>
(function(){var b=document.getElementById("rerun"),o=document.getElementById("rerun-out"),r=document.getElementById("rerun-res");
function esc(s){return String(s==null?"":s).replace(/[&<>]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;"}[c]})}
function badge(t,c){return '<span class="badge '+(c||"")+'">'+esc(t)+'</span>'}
b.addEventListener("click",function(){b.disabled=true;o.textContent="running";r.innerHTML="";
fetch("/api/rerun/"+encodeURIComponent(${js(run.id)})+"/"+encodeURIComponent(${js(rep.programId)}),{method:"POST"}).then(function(x){return x.json()}).then(function(j){b.disabled=false;
if(j.error){o.innerHTML='<span class="err">'+esc(j.error)+'</span>';return}
o.innerHTML=badge(j.reproduced?"reproduced":"not reproduced",j.reproduced?"ok":"warn")+' <span class="xs mut">'+(j.ms/1000).toFixed(1)+' s · '+esc(j.sandbox)+' · '+esc(j.version)+'</span>';
var snap=function(s,t){return s?'<div><div class="hd">'+t+' '+badge(s.timedOut?"timed out":"exit "+s.code,s.code===0&&!s.timedOut?"ok":"bad")+'</div><pre class="code">'+esc((s.stdout||"").trim()||"(no stdout)")+(s.stderr1?"\\n"+esc(s.stderr1):"")+'</pre></div>':""};
r.innerHTML='<div class="out mt2">'+snap(j.before,"stdout before · fresh run")+snap(j.after,"stdout after · fresh run")+'</div>';}).catch(function(e){b.disabled=false;o.innerHTML='<span class="err">'+esc(String(e))+'</span>'})});})();
</script>`;
  const facts: Array<[string, string]> = [];
  if (ev) facts.push(["fired", `${ev.fired} before · ${ev.firedAfter} after`], ["runs", "each version twice, same file name, no network"]);
  if (rep.minimizer) facts.push(["minimizer", `${rep.minimizer.evaluations} oracle evaluations${rep.minimizer.proposal === "accepted" ? " · Lightning proposal accepted" : rep.minimizer.proposal === "rejected" ? " · Lightning proposal rejected" : ""}`]);
  const body = `${h1(`${esc(ruleLabel(run))}: ${esc(kindTitle(rep.kind))}`, `<span><a href="${L.findings}">Findings</a> / <a href="${L.run(run.id)}">${esc(run.id)}</a> / ${esc(rep.programId)}</span><span>${esc(toolVersion(run))}</span><span>${rep.lines.before} → ${rep.lines.after} lines</span><span>${esc(when(run.when))}</span>`,
    `${kindBadge(rep.kind)}${labelBadge(rep.safeLabel, run.rule.fixKind)}${gradeBadge(f.grade, f.severity)}${upstreamBadge(f.upstream)}${ev && ev.confirmed === false ? badge("not reproduced in a sandbox", "warn") : ""}`)}
${section("Hypothesis", `<p>${esc(res.hazard || res.title)}</p>`, `${modelBadge("Nemotron 3 Super")} ${badge(res.predicted?.expectTrigger ? "predicted to fire" : "predicted not to fire", ev && (ev.fired > 0) === !!res.predicted?.expectTrigger ? "ok" : "warn")}${ev ? ` ${badge(ev.fired ? `fired ${ev.fired}×` : "did not fire")}` : ""}`)}
${section("Program", sideBySide(before, after))}
${section("Output", `${ev ? outputPair(ev.before, ev.after) : pre(res.findings.find((x) => x.kind === rep.kind)?.detail ?? "")}${facts.length ? `<div class="mt2">${kv(facts)}</div>` : ""}${rerun}`)}
${v ? section("Judge", `<p>${esc(v.why)}</p>`, `${modelBadge("Nemotron 3 Ultra")} ${badge("advisory")} ${gradeBadge(v.grade, v.severity)}`) : ""}
${ev?.explanation ? section("Explanation", `<p>${esc(ev.explanation)}</p>`, `${modelBadge("Nemotron 3 Super")} ${badge("unverified")}`) : ""}
${section("Reproduce", `${kv([["file", `<code>prog.${esc(run.ext)}</code> (the before program)`], ["minimized program", `<a href="${L.report(run.id, rep.programId).replace(/\.md$/, `.${esc(run.ext)}`)}">${esc(rep.programId)}.${esc(run.ext)}</a>`], ["evidence sheet", `<a href="${L.report(run.id, rep.programId)}">${esc(rep.programId)}.md</a>`], ["regression fixture", `<a href="${L.fixture(run.id, rep.programId, run.ext)}" download>${esc(rep.programId)}.${esc(run.ext)}</a> <span class="mut">the minimized program with a header stating the observed change, for the tool's test suite</span>`]])}<div class="mt2">${pre((ev?.commands ?? []).join("\n") || "(see evidence sheet)")}</div>`)}
${section("Upstream search", dd
    ? `<p class="small mut">${dd.queries.map((q) => `<code>${esc(q)}</code>`).join(" · ")}</p>${dd.verdicts.filter((x) => x.relation !== "unrelated").length
      ? `<ul class="lst">${dd.verdicts.filter((x) => x.relation !== "unrelated").map((x) => `<li>${badge(x.relation, x.relation === "duplicate" ? "" : "info")} ${ext(x.url, x.url.replace(/^https:\/\/github\.com\//, ""))} <span class="mut">${esc(x.why)}</span></li>`).join("")}</ul>`
      : `<p>${badge("no duplicate or related report", "info")} <span class="xs mut">${dd.hits.length} hits triaged</span></p>`}`
    : `<p class="small mut">not searched</p>`, `${badge("GitHub issues")} ${badge("Tavily")} ${modelBadge("Nemotron 3 Super + Ultra")}`)}
${section("Details", `${kv([["program", esc(res.title)], ["hazard", esc(res.hazard)], ["oracle", `<code>${esc(trunc(ev?.observed ?? "", 400))}</code>`], ["run", `<a href="${L.run(run.id)}">${esc(run.id)}</a>`]])}
<details class="mt2"><summary>generated program (${rep.lines.before} lines) and the fix's diff</summary>${codeBlock(srcOf(run, res.id))}${res.after?.diff ? unifiedDiff(res.after.diff) : ""}</details>
<details><summary>rule documentation given to the models</summary><pre class="code wrapped">${esc(run.rule.docs)}</pre></details>`)}`;
  return layout({ title: `${ruleLabel(run)} · fixhunt`, active: "findings", L, body });
}

// ---------------------------------------------------------------------------------------------- runs

export function runsPage(runs: Run[], fs: Finding[], L: Links): string {
  const rows = runs.map((r) => {
    const mine = fs.filter((f) => f.run.id === r.id);
    const real = mine.filter((f) => f.grade === "real" || f.grade === "unclear" || f.grade === "unjudged").length;
    return `<tr data-tool="${esc(r.tool)}" data-has="${mine.length ? 1 : 0}"><td class="mono"><a href="${L.run(r.id)}">${esc(r.rule.rule)}</a></td><td>${esc(toolVersion(r))}</td><td class="n">${r.summary.programs ?? 0}</td><td class="n">${r.summary.fired ?? 0}</td><td class="n">${r.summary.fixed ?? 0}</td><td>${mine.length ? badge(`${real} / ${mine.length}`, real ? "bad" : "") : '<span class="mut">0</span>'}</td><td class="n">${money(r.cost)}</td><td class="n xs mut">${esc(when(r.when))}</td></tr>`;
  }).join("");
  const tools = [...new Set(runs.map((r) => r.tool))];
  const body = `${h1("Runs", `<span><b>${runs.length}</b> hunts, one rule each</span>`)}
<div class="toolbar" data-filters="#rt"><select name="tool"><option value="">all tools</option>${tools.map((t) => `<option value="${esc(t)}">${esc(t)}</option>`).join("")}</select><label class="field chk"><input type="checkbox" name="has">with findings</label><input name="q" placeholder="search"><span class="cnt"></span></div>
${rows ? table(["rule", "tool", "#programs", "#fired", "#fixed", "findings", "#cost", "#when"], rows, "rt") : empty("No runs yet")}`;
  return layout({ title: "Runs · fixhunt", active: "runs", L, body });
}

export function runPage(run: Run, fs: Finding[], L: Links): string {
  const mine = fs.filter((f) => f.run.id === run.id);
  const s = run.summary;
  const rowFor = (r: Run["results"][number]) => {
    const kinds = r.findings.map((x) => x.kind).filter((k) => k !== "disputed");
    const disputed = r.findings.some((x) => x.kind === "disputed");
    const fnd = mine.find((f) => f.report.programId === r.id);
    const status = r.error ? badge("invalid") : kinds.length ? kinds.map((k) => kindBadge(k)).join(" ") : r.before.diagnostics.length ? (r.after?.changed ? badge("fix ok", "ok") : badge("fired, no fix")) : badge("silent");
    return `<tr><td class="mono">${fnd ? `<a href="${L.finding(run.id, r.id)}">${esc(r.id)}</a>` : `<a href="#${esc(r.id)}">${esc(r.id)}</a>`}</td><td>${status}${disputed ? ` ${badge("prediction off", "warn")}` : ""}</td><td>${esc(r.title)}</td><td class="w xs">${esc(r.hazard)}</td></tr>`;
  };
  const programs = run.results.map((r) => `<details id="${esc(r.id)}"><summary>${esc(r.id)} · ${esc(r.title)}${r.error ? ` (${esc(r.error.split("\n")[0].slice(0, 80))})` : ""}</summary>${codeBlock(srcOf(run, r.id))}${r.after?.diff ? unifiedDiff(r.after.diff) : ""}${r.before.run.stdout ? `<pre class="code">${esc(r.before.run.stdout.trimEnd())}</pre>` : ""}</details>`).join("");
  const body = `${h1(esc(ruleLabel(run)), `<span><a href="${L.runs}">Runs</a> / ${esc(run.id)}</span><span>${esc(toolVersion(run))}</span><span>${esc(when(run.when))}</span><span>${run.opts?.n ?? "?"} programs × ${run.opts?.rounds ?? "?"} round(s)</span>${run.opts?.unsafe ? "<span>unsafe fixes applied</span>" : ""}<span><b>${s.programs ?? 0}</b> programs, <b>${s.fired ?? 0}</b> fired, <b>${s.fixed ?? 0}</b> fixed, <b>${mine.length}</b> findings, <b>${s.invalid ?? 0}</b> rejected</span><span>model cost <b>${money(run.cost)}</b></span>`, labelBadge(run.rule.fixKind === "safe", run.rule.fixKind))}
${run.analysis ? section("Analysis", `<p>${esc(run.analysis.summary)}</p><p class="small mut">Fix: ${esc(run.analysis.fixDescription)}</p><details><summary>${(run.analysis.hazards ?? []).length} hazards</summary><ul class="lst">${(run.analysis.hazards ?? []).map((h: string) => `<li>${esc(h)}</li>`).join("")}</ul></details>`, modelBadge("Nemotron 3 Super")) : ""}
${mine.length ? section("Findings", table(["program", "oracle", "label", "judge", "status", "summary"], mine.map((f) => `<tr><td class="mono"><a href="${L.finding(run.id, f.report.programId)}">${esc(f.report.programId)}</a></td><td>${kindBadge(f.report.kind)}</td><td>${labelBadge(f.report.safeLabel, run.rule.fixKind)}</td><td>${gradeBadge(f.grade, f.severity)}</td><td>${upstreamBadge(f.upstream)}</td><td class="w">${esc(trunc(f.report.verdict?.why ?? "", 160))}</td></tr>`).join(""))) : ""}
${section("Programs", table(["id", "result", "title", "hazard"], run.results.map(rowFor).join("")))}
${section("Sources", programs)}`;
  return layout({ title: `${ruleLabel(run)} · fixhunt`, active: "runs", L, body });
}

// ---------------------------------------------------------------------------------------------- scans

export function scansPage(scans: Scan[], L: Links): string {
  const rows = scans.map((s) => `<tr data-tool="${esc(s.tool)}" data-has="${s.findings.length ? 1 : 0}"><td><a href="${L.scan(s.id)}">${esc(projectName(s.project))}</a><div class="xs mut mono">${esc(s.run)}</div></td><td>${esc(toolVersion(s))}</td><td class="n">${s.rules}</td><td class="n">${s.applied}</td><td>${s.findings.length ? badge(String(s.findings.length), "bad") : '<span class="mut">0</span>'}</td><td class="n">${s.incomplete.length || ""}</td><td class="n xs mut">${esc(when(s.when))}</td></tr>`).join("");
  const tools = [...new Set(scans.map((s) => s.tool))];
  const body = `${h1("Scans", `<span><b>${scans.length}</b> repository scans</span>`)}
<div class="toolbar" data-filters="#st"><select name="tool"><option value="">all tools</option>${tools.map((t) => `<option value="${esc(t)}">${esc(t)}</option>`).join("")}</select><label class="field chk"><input type="checkbox" name="has">with findings</label><input name="q" placeholder="search"><span class="cnt"></span></div>
${rows ? table(["repository · command", "tool", "#rules", "#changed files", "changed outcome", "#sites left", "#when"], rows, "st") : empty("No scans yet")}`;
  return layout({ title: "Scans · fixhunt", active: "scans", L, body });
}

const ghShort = (u: string) => u.replace(/^https:\/\/github\.com\//, "");
function upstreamLine(u: ScanUpstream | undefined, L: Links): string {
  if (!u) return "";
  const dups = u.duplicates.length ? u.duplicates.map((d) => `<a class="badge" href="${esc(safeUrl(d.url))}" target="_blank" rel="noopener">${esc(d.relation + " " + ghShort(d.url))}</a>`).join(" ") : badge("no upstream match", "info");
  const fixed = u.fixedIn ? ` <a class="badge" href="${esc(safeUrl(u.fixedUrl ?? ""))}" target="_blank" rel="noopener" title="advisory: a release note or issue snippet says so">a snippet says fixed in ${esc(u.fixedIn)}</a>` : "";
  const bank = u.bank ? ` <a class="badge" href="${L.finding(u.bank.runId, u.bank.programId)}">${u.bank.findings} in the findings bank · ${esc(u.bank.grade)}</a>` : "";
  return `<div class="row">${dups}${fixed}${bank}</div>`;
}

export function scanPage(s: Scan, details: Array<{ row: ScanFindingRow; finding: any }>, L: Links): string {
  const sh = (t: string, aside = "") => `<h3 class="sh">${esc(t)}${aside ? ` <span>${aside}</span>` : ""}</h3>`;
  const tail = (x: string, n: number) => x.trim().split("\n").slice(-n).join("\n");
  const findingCard = ({ row, finding: f }: { row: ScanFindingRow; finding: any }) => {
    const v = f.verdict;
    const m = f.minimal;
    const head = `${kindBadge(f.kind)} ${labelBadge(f.fixKind === "safe", f.fixKind)} ${exitBadge(f.before)} <span class="xs mut">→</span> ${exitBadge(f.after)} ${v ? gradeBadge(v.grade, v.severity) : ""}`;
    const facts: Array<[string, string]> = [
      ["files changed", `${f.changedFiles.length}: ${esc(f.changedFiles.slice(0, 6).join(", "))}${f.changedFiles.length > 6 ? "…" : ""}`],
      ["reduced to", m ? `${m.hunks} of ${m.of} hunk(s) in ${esc(m.files.join(", "))}, ${m.evaluations} run(s)${m.complete ? "" : ", budget exhausted"}; ${m.confirmed ? "the patch was applied with git apply and reproduced the same difference" : `<span class="err">${esc(m.note ?? "not confirmed")}</span>`}` : ""],
      ["sites reported", f.lint ? `${f.lint.before} → ${f.lint.after} in ${f.lint.files} linted file(s)${f.lint.after ? " (the fix left sites behind)" : ""}${f.lint.note ? `; ${esc(f.lint.note)}` : ""}` : ""],
    ];
    const after = (tail(f.after.stdout, 25) + (f.after.stderr.trim() ? "\n" + tail(f.after.stderr, 12) : "")).trim() || "(no output)";
    return `<section><h2 class="fh"><span class="mono">${esc(f.rule)}</span><span class="k">${esc(kindTitle(f.kind))}</span></h2><div class="row mb2">${head}</div>${kv(facts)}
${sh(m ? "Change (reduced)" : "Change")}${unifiedDiff((m?.diff ?? f.diff).slice(0, 20000))}
<div class="out">
<div>${sh("Observed")}<pre class="code wrapped">${esc(f.observed ?? "")}</pre></div>
<div>${sh("Output after", "tail")}<pre class="code">${esc(after)}</pre></div>
</div>
${v ? `${sh("Judge", "Nemotron 3 Ultra, advisory")}<p>${esc(v.why)}</p>` : ""}
${f.explanation ? `${sh("Explanation", "Nemotron 3 Super, model draft")}<p class="small">${esc(f.explanation)}</p>` : ""}
${f.upstream ? `${sh("Upstream")}${upstreamLine(f.upstream, L)}` : ""}
${sh("Files")}<div class="meta">${f.report ? `<a href="${L.scanFile(s.id, f.report)}">evidence sheet</a>` : ""}${m && !L.static ? `<a href="${L.scanFile(s.id, `rules/${encodeURIComponent(f.rule.replace(/[^\w.-]+/g, "_"))}/minimal.patch`)}">minimal.patch</a>` : ""}<details class="inl"><summary class="inl">full diff (${f.diff.split("\n").length} lines)</summary>${unifiedDiff(f.diff.slice(0, 40000))}</details></div></section>`;
  };
  const r = s.risk;
  const risk = r?.known.length ? `<details class="rk"><summary>${r.known.length} enabled rule(s) already have a finding in the bank${r.notEnabled ? ` <span class="mut">(${r.notEnabled} more known-risk rules of ${esc(s.tool)} are not enabled here)</span>` : ""}</summary>${table(["rule", "label", "#findings", "judge", "upstream"], r.known.map((k) => `<tr><td class="mono"><a href="${L.finding(k.runId, k.programId)}">${esc(k.rule)}</a></td><td>${labelBadge(k.safe > 0, k.fixKind)}</td><td class="n">${k.findings}${k.confirmed !== undefined && k.confirmed < k.findings ? ` <span class="xs mut">${k.confirmed} re-verified</span>` : ""}</td><td>${gradeBadge(k.grade, k.severity)}</td><td>${k.urls.slice(0, 2).map((u) => ext(u.url, `${u.relation} ${ghShort(u.url)}`)).join(" ")}${k.urls.length > 2 ? ` <span class="xs mut">+${k.urls.length - 2}</span>` : ""}</td></tr>`).join(""))}</details>` : "";
  const c = s.combined;
  const applied = c ? `<p class="small">${c.rules.length} rule(s) changed ${c.files} file(s) ${c.verified ? "with no difference under the command, applied together" : `but applied together the outcome ${esc(c.note ?? `changed (exit ${c.exitBefore} → ${c.exitAfter}${c.timedOut ? ", timed out" : ""})`)}`}.${c.patch && !L.static ? ` <a href="${L.scanFile(s.id, "accepted.patch")}">accepted.patch</a> applies with <code>git apply -p1</code>.` : ""} <span class="mono xs">${c.rules.map((x) => esc(x)).join(" ")}</span></p>` : s.accepted?.length ? `<p class="small">${s.accepted.length} rule(s) changed files with no difference under the command: <span class="mono xs">${s.accepted.map((x) => esc(x)).join(" ")}</span></p>` : "";
  const incomplete = s.incomplete.length ? section("Fixes that left sites behind", `<p class="small mut">The rule still reports in the changed files after its own fix; no difference under the command.</p>${table(["rule", "#before", "#after", "#files linted", "sample"], s.incomplete.map((l) => `<tr><td class="mono">${esc(l.rule)}</td><td class="n">${l.before}</td><td class="n">${l.after}</td><td class="n">${l.files}</td><td class="w xs">${esc(l.sample.slice(0, 3).join(" · "))}${l.note ? ` <span class="mut">(${esc(l.note)})</span>` : ""}</td></tr>`).join(""))}`) : "";
  const body = `${h1(esc(projectName(s.project)), `<span><a href="${L.scans}">Scans</a> / ${esc(s.id)}</span><span>${projectLink(s.project)}${s.path ? ` <span class="mono">/${esc(s.path)}</span>` : ""}${s.commit ? ` at <span class="mono">${esc(s.commit)}</span>` : ""}</span><span><code>${esc(s.run)}</code></span><span>${esc(toolVersion(s))}</span><span>${esc(when(s.when))}</span><span><b>${s.rules}</b> rules tried, <b>${s.applied}</b> changed files, <b>${s.findings.length}</b> changed the outcome, <b>${s.accepted?.length ?? 0}</b> did not${s.errors.length ? `, <b>${s.errors.length}</b> not compared` : ""}</span>${s.cost ? `<span>model cost <b>${money(s.cost)}</b></span>` : ""}</span>`)}
<p class="note">One command was observed. Code it does not exercise is not observed; "no difference" means the normalized output and exit status matched, not that the fix is correct.</p>
${risk}
${s.errors.length ? section("Not compared", `<ul class="lst">${s.errors.map((e) => `<li>${esc(e)}</li>`).join("")}</ul>`) : ""}
${s.warnings.length ? section("Warnings", `<ul class="lst">${s.warnings.map((e) => `<li>${esc(e)}</li>`).join("")}</ul>`) : ""}
${details.length && details.length < s.findings.length ? `<p class="small mut">${s.findings.length - details.length} finding(s) recorded whose evidence files are no longer on disk: ${esc(s.findings.filter((f) => !details.some((d) => d.row.rule === f.rule)).map((f) => f.rule).join(", "))}.</p>` : ""}
${details.length ? details.map(findingCard).join("") : s.findings.length ? `<p class="small">${s.findings.length} finding(s) recorded, but their evidence files are no longer on disk.</p>` : s.errors.length ? `<p class="small">No fix that was compared changed the command's output or exit status; ${s.errors.length} rule(s) were not compared.</p>` : `<p class="small">No fix that changed files changed the command's output or exit status.</p>`}
${incomplete}
${applied ? section("Applied without a difference", applied) : ""}`;
  return layout({ title: `${projectName(s.project)} · fixhunt`, active: "scans", L, body });
}

// ---------------------------------------------------------------------------------------------- docs

export function docsPage(st: Stats, sp: Spend, L: Links): string {
  const models = Object.entries(sp.byModel).sort((a, b) => b[1].cost - a[1].cost);
  const stage = (n: string, what: string, who: string) => `<tr><td class="mono">${esc(n)}</td><td>${esc(what)}</td><td class="xs mut">${esc(who)}</td></tr>`;
  const body = `${h1("Docs")}
${section("What it is", `<p>fixhunt tests the automatic fixes of a linter. A fix that changes what the program does is a finding; everything else is noise. It is written for the people who maintain those fixes: a rule's fix can be hunted with generated programs, or tried on a real repository under that repository's own tests. Findings come with the smallest reproducer the tool could reach, the exact tool version, both outputs, an advisory grade against the rule documentation, an upstream search, and an evidence sheet. Nothing is posted anywhere.</p>`)}
${section("Hunt a rule", `${table(["stage", "what", "runs on"], [
    stage("analyze", "Read the rule documentation; list firing shapes and rule-specific semantic hazards.", "Nemotron 3 Super"),
    stage("generate", "Write N small deterministic programs, one per hazard, each with a prediction of whether the rule fires.", "Nemotron 3 Super"),
    stage("run", "Lint, apply the fix with the pinned tool version, run the program before and after, twice each, in a fresh VM without network.", "Token Factory Sandboxes"),
    stage("oracles", "Crash, parse failure, output or exit-code difference, fixpoint violation, safe-label mismatch. No model.", ""),
    stage("minimize", "Delta debugging over lines with the oracle as the test; a Lightning proposal is tried first; the result is confirmed in a sandbox.", "Nemotron 3.5 Lightning"),
    stage("judge", "Grade against the rule documentation: real, intended-change, introspection-only, program-bug, unclear. Advisory.", "Nemotron 3 Ultra"),
    stage("dedup", "GitHub issue search plus Tavily on the project repository, strict duplicate triage.", "Super + Ultra, Tavily"),
    stage("report", "Evidence sheet: reproducer, commands, outputs, diff, one model-written paragraph, upstream matches.", "Nemotron 3 Super"),
  ].join(""))}`)}
${section("Scan a repository", `<ul class="lst">
<li>One rule at a time, its fix is applied to a copy of the project.</li>
<li>The project's command (tests, a build, a script) runs before and after in a sandbox, network on.</li>
<li>The command runs twice on the unmodified project first; a non-deterministic command stops the scan.</li>
<li>A finding is a fix that changed the command's normalized output or exit status.</li>
<li>Delta debugging over the fix's hunks reduces it to a 1-minimal set that still reproduces the difference, within a run budget.</li>
<li>The reduced patch is applied with git apply and run once more before it is called confirmed.</li>
<li>The changed files are linted again with the rule: sites the fix left behind are counted.</li>
<li>Then judge, upstream search and evidence sheet, as for a hunt finding.</li>
<li>Fixes with no difference are applied together, run once more and published as a patch.</li>
<li>Default rules: the fixes the tool labels safe among the rules the repository enables; clang-tidy takes rule ids.</li>
<li>From the dashboard the repository is cloned at depth 1 from an allow-listed host and discarded afterwards.</li>
</ul>`)}
${section("What a finding is not", `<ul class="lst">
<li>A finding is an observation of one deterministic run, not a proof that the rewrite is wrong for every input, and not a reading of the rule author's intent. The judge's grade is a model's reading of the documentation; it is labelled advisory.</li>
<li>Several generated programs can share one root cause. The findings page groups them by rule; the counts are programs, not bugs.</li>
<li>A scan observes one command. "No difference" means the normalized output and exit status matched for that command; code it does not exercise is not observed.</li>
<li>Hunts observe stdout, the exit code and the first stderr line; scans compare stdout and the last stderr line after scrubbing timings, paths and positions. "Fix breaks the build" is a heuristic on that output (a parse, import or compile error at the start of a line).</li>
<li>Fixers run on the host with the repository's own tool configuration disabled; programs and project commands run in disposable sandboxes.</li>
<li>Only GitHub issue and pull-request URLs count as upstream matches. A "fixed in" note comes from a snippet and is advisory.</li>
</ul>`)}
${section("CLI", pre(`bun src/cli.ts hunt --tool <id> --rule <rule> [--n 8] [--rounds 1] [--unsafe]
bun src/cli.ts scan --tool <id> --dir <checkout> --run "<command>" [--rules A,B] [--limit k] [--no-net] [--no-minimize] [--no-judge] [--no-upstream]
bun src/cli.ts apply --tool <id> --dir <checkout> --run "<command>"     # scan, then apply the fixes that made no difference
bun src/cli.ts risk --tool <id> --dir <checkout>                        # enabled rules with a finding in the bank (no sandbox, no model)
bun src/cli.ts sweep --tool <id> [--n 8] [--rounds 2] [--limit k]       # hunt every rule with a safe fix
bun src/cli.ts check --tool <id> --rule <rule> --file prog.<ext>        # one program through the oracles
bun src/cli.ts serve [--port 8731] · render [--out runs/site] · tools · catalog --tool <id>`))}
${section("Tool specs", `<p>A tool is a JSON file in <code>tools/</code> (or a directory in <code>FIXHUNT_TOOLS</code>, or <code>--tool-file</code>): how to print the version, look up a rule and its documentation, lint one file for one rule, apply the fix, check syntax, run a program in a sandbox image, read which rules a repository enables, and build the rule catalog. Biome, ruff, ESLint and clang-tidy ship as specs; no code in the pipeline names a tool. See <code>docs/tool-spec.md</code>.</p>`)}
${section("Models and spend", `${kv(Object.entries(MODELS).map(([k, v]) => [k, `<code>${esc(v)}</code>`]))}
<div class="mt2">${table(["model", "#calls", "#prompt", "#completion", "#cost"], models.map(([m, v]) => `<tr><td class="mono">${esc(m)}</td><td class="n">${v.calls}</td><td class="n">${v.prompt.toLocaleString()}</td><td class="n">${v.completion.toLocaleString()}</td><td class="n">${money(v.cost)}</td></tr>`).join("") + `<tr><td>total</td><td></td><td></td><td></td><td class="n">${money(sp.total)}</td></tr>`)}</div>`, `${st.sandboxRuns} sandbox runs · ${money(st.sandboxCost)}`)}
<div class="meta">${Object.entries(st.versions).map(([t, v]) => `<span>${esc(t)} <b>${esc(versionOnly({ tool: t, version: v }))}</b></span>`).join("")}</div>`;
  return layout({ title: "Docs · fixhunt", active: "docs", L, body });
}

// helpers
function trunc(s: string, n: number) { return s.length > n ? s.slice(0, n - 1) + "…" : s; }
function inline(s: string) { return esc(s).replace(/`([^`]+)`/g, "<code>$1</code>"); }
function srcOf(run: Run, id: string): string {
  try { return readFileSync(`${run.dir}/${id}/orig.${run.ext}`, "utf8"); } catch { return "(source missing)"; }
}
/** Fallback when evidence is missing: show the unified diff target only. */
function applyHint(res: Run["results"][number]): string { return res.after?.diff ? "(fixed source not recorded; see the unified diff below)" : "(no fix applied)"; }
