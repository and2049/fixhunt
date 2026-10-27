let obj = { prop: { value: 5 } };
let maybeNull = null;
let orig = maybeNull ? maybeNull.prop?.value : 99;
let fixed = maybeNull ?? maybeNull.prop?.value;
console.log(`maybeNull=${maybeNull}: orig=${orig}, fixed=${fixed}`);
if (orig !== fixed) {
  throw new Error(`Nullish coalescing mismatch: ${orig} !== ${fixed}`);
}
maybeNull = undefined;
orig = maybeNull ? maybeNull.prop?.value : 99;
fixed = maybeNull ?? maybeNull.prop?.value;
console.log(`maybeNull=${maybeNull}: orig=${orig}, fixed=${fixed}`);
if (orig !== fixed) {
  throw new Error(`Nullish coalescing mismatch: ${orig} !== ${fixed}`);
}
