// Runtime configuration. Bun loads .env automatically.

export const MODELS = {
  // cheap tier: minimization proposals, bulk classification
  fast: process.env.FIXHUNT_MODEL_FAST ?? "nvidia/Nemotron-3_5-Lightning",
  // program generation: Lightning ignores constraints and truncates under json_schema, Super follows the brief
  gen: process.env.FIXHUNT_MODEL_GEN ?? "nvidia/nemotron-3-super-120b-a12b",
  // report drafting
  mid: process.env.FIXHUNT_MODEL_MID ?? "nvidia/nemotron-3-super-120b-a12b",
  // judge for disputed cases only
  judge: process.env.FIXHUNT_MODEL_JUDGE ?? "nvidia/Nemotron-3-Ultra-550b-a55b",
} as const;

export const LLM = {
  baseUrl: (process.env.NEBIUS_BASE_URL ?? "https://api.tokenfactory.nebius.com/v1/").replace(/\/?$/, "/"),
  apiKey: process.env.NEBIUS_API_KEY ?? "",
};

export const RUNS_DIR = process.env.FIXHUNT_RUNS_DIR ?? "runs";

export function requireEnv(name: string): string {
  const v = process.env[name];
  if (!v) throw new Error(`${name} is not set (see .env.example)`);
  return v;
}
