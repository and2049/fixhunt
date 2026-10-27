function tags(strings, ...values) {
  return strings.raw[0] + '|' + values[0] + '|' + strings.raw[1];
}
const output = tags`${Math.pow(2, 3)} end`;
console.log('Output:', output); // Expected: '|8|'
// After fix: tags`${2 ** 3} end` → same? Wait — no, if misgrouped...
// Actually: if base/expr has comma, but here safe.
// We need a case where ** changes grouping in interpolation
// Let's use comma in exponent to break it
const bad = tags`${Math.pow(2, 1, 2)}`; // 2^(1,2) → 2^2=4
console.log('Bad:', bad); // Expected: '|4|'
// If autofix makes 2 ** 1, 2 → (2**1), 2 → comma expr → value is 2
// So bad becomes '|2|' → mismatch!
