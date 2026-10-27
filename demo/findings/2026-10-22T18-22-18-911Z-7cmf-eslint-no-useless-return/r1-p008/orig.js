function f() {
  const obj = { prop: null };
  console.log('obj.prop?.length:', obj.prop?.length); // null -> undefined
  console.log('obj.prop == null:', obj.prop == null); // true
  console.log('obj.prop === undefined:', obj.prop === undefined); // false
  return; // TRIGGER
}
f();
// After fix: same output
// To make return affect outcome: make f return a value used elsewhere
let captured;
function getValue() {
  const x = undefined;
  console.log('x == null:', x == null);
  console.log('x === undefined:', x === undefined);
  return; // TRIGGER: returns undefined
}
captured = getValue();
console.log('captured === undefined:', captured === undefined);
// If return removed, captured still undefined
// But make it so that without return, fall-through returns something else?
// In JS, falling through returns undefined anyway.
// Instead: use arrow function in map
const arr = [1, null, 3];
const result = arr.map(v => {
  if (v == null) return; // TRIGGER: returns undefined for null
  return v * 2;
});
console.log('result:', result); // [2, undefined, 6]
// If return removed, still undefined
// So make it depend on whether function is called:
let called = false;
function maybeReturn() {
  called = true;
  if (false) return; // never taken
  // but we want return to be hit
  return; // TRIGGER: always hit
}
maybeReturn();
console.log('called:', called);
// Still no change.
// Final idea: make the function's return value be used in a way that distinguishes
// explicit return; from fall-through — but they are identical.
// So instead, focus on the trace depending on whether the function body runs at all.
// Use a wrapper that only calls if condition.
let log = '';
function h() {
  log += 'h-entered ';
  return; // TRIGGER
}
if (true) h();
console.log('log:', log.trim());
// If return removed, same.
// Give up and make a working version with observable diff via side effect in finally
// Hazard 8: use nullish coalescing
function process(val) {
  if (val == null) return; // TRIGGER: early return for null/undefined
  console.log('processing:', val);
  return val * 2;
}
const input = null;
const output = process(input);
console.log('output:', output); // undefined
// If return removed, process(null) would log 'processing: null' then return undefined
// So: with return: no log
// without return: logs 'processing: null'
// Perfect.
// Rewriting hazard 8:
