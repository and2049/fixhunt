let code = 'return DATA_1_000;';
const DATA_1_000 = 999;
try {
  const result = eval(code);
  console.log('eval result:', result);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
// After fix: if rule rewrote 1_000 in string? No — but if codegen inserted 1_000 as key, and fix alters runtime object shape, lookup fails
// Simulate: object built with 1_000 key, then accessed via string that expects underscore
const map = { 1000: 'found' };
console.log(map['1_000']); // undefined after fix because key becomes 1000 (number), but we're accessing string '1_000' — wait, JS coerces
// Better: rely on Object.keys to show key change
const o = { 1000: 'value' };
console.log(Object.keys(o)[0]); // prints '1000' after fix, was '1_000' before → breaks code expecting underscore in key string
