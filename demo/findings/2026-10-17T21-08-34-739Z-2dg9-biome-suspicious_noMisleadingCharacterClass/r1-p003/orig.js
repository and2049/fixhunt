let x = 0;
function f() { return ++x; }
if (/^[A${f()}́]$/.test('A1́')) {
  console.log(x); // 1
}
// After fix: expression becomes `/^[A${f()}]$/` -> still evaluates f() once? 
// But hazard: if duplicated in alternation, could run twice.
// Let's force duplication via bug-prone pattern:
if (/^[A${f()}́]|[B${f()}́]$/.test('A1́')) {
  console.log(x); // Would be 2 if both sides evaluated
}
