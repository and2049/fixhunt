// Static export of the dashboard (no live actions) into runs/site/, for hosting without a server.
import { cpSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { RUNS_DIR } from "../config";
import { findings, fixtureText, loadRuns, loadScans, scanFinding, spend, stats } from "./data";
import { staticLinks } from "./html";
import { docsPage, findingPage, findingsPage, huntPage, runPage, runsPage, scanPage, scansPage } from "./pages";

export function exportSite(out = join(RUNS_DIR, "site")): string {
  const runs = loadRuns(); const fs = findings(runs);
  const scans = loadScans();
  const w = (rel: string, s: string) => { const p = join(out, rel); mkdirSync(dirname(p), { recursive: true }); writeFileSync(p, s); };
  w("index.html", huntPage({ catalog: {}, toolIds: [], scanTools: [], gated: false, findings: fs, limits: { maxN: 10, maxRounds: 2, scanLimit: 30 } }, staticLinks(0)));
  w("findings.html", findingsPage(stats(runs, fs), fs, staticLinks(0)));
  w("runs.html", runsPage(runs, fs, staticLinks(0)));
  w("docs.html", docsPage(stats(runs), spend(), staticLinks(0)));
  w("scans.html", scansPage(scans, staticLinks(0)));
  for (const s of scans) {
    w(`s/${encodeURIComponent(s.id)}.html`, scanPage(s, s.findings.map((f) => ({ row: f, finding: scanFinding(s.id, f.rule) })).filter((x) => x.finding), staticLinks(1)));
    const rep = join(s.dir, "reports");
    if (existsSync(rep)) cpSync(rep, join(out, "raw", s.id, "reports"), { recursive: true });
  }
  for (const r of runs) {
    w(`r/${encodeURIComponent(r.id)}.html`, runPage(r, fs, staticLinks(1)));
    const rep = join(r.dir, "reports");
    if (existsSync(rep)) cpSync(rep, join(out, "raw", r.id, "reports"), { recursive: true });
  }
  for (const f of fs) {
    w(`f/${encodeURIComponent(f.run.id)}/${encodeURIComponent(f.report.programId)}.html`, findingPage(f, staticLinks(2)));
    w(`raw/${encodeURIComponent(f.run.id)}/fixtures/${encodeURIComponent(f.report.programId)}.${f.run.ext}`, fixtureText(f));
  }
  return out;
}
