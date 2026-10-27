const template = { 1_000: 'THOUSAND_PLACEHOLDER' };
let output = 'Value: ${1_000}';
for (let [k, v] of Object.entries(template)) {
  output = output.replace(new RegExp('\\${' + k + '}', 'g'), v);
}
console.log(output); // Before fix: replaces ${1_000} → 'Value: THOUSAND_PLACEHOLDER'
// After fix: key becomes 1000 (number) → RegExp('${1000}') → no match → output unchanged
// So print shows failure
