import type { ExecResult } from "../sandbox";

export type Diagnostic = { rule: string; severity: string; message: string; span?: [number, number] | null; fix?: "safe" | "unsafe" | "unknown" | "none" };

export type RuleInfo = {
  tool: string;
  rule: string; // full id, e.g. complexity/noUselessUndefinedInitialization
  fixKind: "safe" | "unsafe" | "none" | "unknown";
  docs: string; // human text used in the generation prompt
};

export interface Tool {
  id: string;
  language: string; // language id used for hazard catalogs and static screens ("js", "py", "cpp", ...)
  ext: string; // file extension for generated programs
  repo?: string; // upstream "owner/name" on GitHub, for the dedup search
  runnerHint?: string; // how a generated program is run, for the generation prompt
  docsFence?: string; // code-fence language for evidence sheets
  version(): Promise<string>;
  ruleInfo(rule: string): Promise<RuleInfo>;
  /** Diagnostics for one rule on one file. */
  lint(file: string, rule: string, cwd: string): Promise<{ diagnostics: Diagnostic[]; crashed: boolean; raw: ExecResult }>;
  /** Apply fixes for one rule in place. unsafe=true also applies fixes the tool labels unsafe. */
  fix(file: string, rule: string, cwd: string, unsafe: boolean): Promise<{ crashed: boolean; failed?: string; raw: ExecResult }>;
  /** Syntax / type check. */
  check(file: string, cwd: string): Promise<ExecResult>;
  /** Run the program. */
  run(file: string, cwd: string): Promise<ExecResult>;
  /** Copy-pasteable commands that reproduce lint → fix → run for a report. */
  reproCommands(rule: string, file: string, unsafe: boolean): string[];
}
