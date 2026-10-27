// Access codes and spending budgets for the hosted dashboard's live actions (hunts, re-runs).
//   FIXHUNT_ACCESS="judges:5,public:0.5"  code → daily USD budget; unset means live actions are open
//   FIXHUNT_DAILY_CAP=10                   global daily USD cap across all codes (default 10)
// Spend is attributed per code per UTC day in runs/budget.json. Reads use the same ledger, so a restart keeps the day's totals.
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { RUNS_DIR } from "./config";

export type Access = { code: string; daily: number };
type Ledger = { day: string; byCode: Record<string, number>; total: number; actions: number };

const FILE = join(RUNS_DIR, "budget.json");
export const GLOBAL_CAP = Number(process.env.FIXHUNT_DAILY_CAP ?? 10);

export function accessCodes(): Access[] {
  return (process.env.FIXHUNT_ACCESS ?? "").split(",").map((s) => s.trim()).filter(Boolean).map((s) => {
    const [code, d] = s.split(":");
    return { code: code.trim(), daily: Number(d ?? 1) };
  });
}
export const gated = () => accessCodes().length > 0;

function today() { return new Date().toISOString().slice(0, 10); }
function load(): Ledger {
  try { const l = JSON.parse(readFileSync(FILE, "utf8")) as Ledger; if (l.day === today()) return l; } catch { /* new day or no file */ }
  return { day: today(), byCode: {}, total: 0, actions: 0 };
}
function save(l: Ledger) { try { writeFileSync(FILE, JSON.stringify(l, null, 1)); } catch { /* read-only fs: budgets are then per process */ } }

export function lookup(code: string | undefined): Access | undefined {
  if (!gated()) return { code: "open", daily: GLOBAL_CAP };
  return accessCodes().find((a) => a.code === code);
}

/** Remaining budget for a code today, and the global remainder. */
export function remaining(code: string): { code: number; global: number } {
  const a = lookup(code);
  const l = load();
  return { code: a ? Math.max(0, a.daily - (l.byCode[a.code] ?? 0)) : 0, global: Math.max(0, GLOBAL_CAP - l.total) };
}

/** Check that an action estimated at `estimate` USD fits the code's and the global budget. */
export function allow(code: string | undefined, estimate: number): { ok: true; access: Access } | { ok: false; reason: string } {
  const a = lookup(code);
  if (!a) return { ok: false, reason: "access code required for live actions" };
  const r = remaining(a.code);
  if (r.global < estimate) return { ok: false, reason: "the demo's daily budget is used up; try again tomorrow" };
  if (r.code < estimate) return { ok: false, reason: `this access code's daily budget ($${a.daily.toFixed(2)}) is used up` };
  return { ok: true, access: a };
}

/** Record actual spend for a code. */
export function charge(code: string, usd: number) {
  const l = load();
  l.byCode[code] = (l.byCode[code] ?? 0) + usd;
  l.total += usd; l.actions++;
  save(l);
}
