let b = 0;
let orig = 5 * (b ? b : 0);
let fixed = 5 * (b || 0);
console.log(`b=${b}: orig=${orig}, fixed=${fixed}`);
if (orig !== fixed) {
  throw new Error(`Precedence failure: ${orig} !== ${fixed}`);
}
b = 2;
orig = 5 * (b ? b : 0);
fixed = 5 * (b || 0);
console.log(`b=${b}: orig=${orig}, fixed=${fixed}`);
if (orig !== fixed) {
  throw new Error(`Precedence failure: ${orig} !== ${fixed}`);
}
