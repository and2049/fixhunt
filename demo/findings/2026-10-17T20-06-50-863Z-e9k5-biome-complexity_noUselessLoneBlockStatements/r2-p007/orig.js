let x = 1;
if (true) { {}; let x = 2; }
console.log(x);
// Before: logs 1 (outer x)
// After fix: let x=2; is still inside if block -> same
// Not changed.
// Need: after fix, the let moves out? No.
// How about: the block removal causes a var to be hoisted?
var x = 1;
if (true) { {}; var x = 2; }
console.log(x);
// Before: logs 2 (var hoisted to if block? No, to function scope)
// After fix: same
// Instead: make the empty block contain a declaration that, after removal, conflicts with outer
let x = 1;
{}
let x = 2; // SyntaxError: redeclaration
// But rule doesn't fire on {} alone? It does.
// So:
let x = 1;
{};
let x = 2; // Error
// After fix: becomes two consecutive lets -> still error
// Same.
// Make it so that before, the inner x is in block, after fix it's not?
// Impossible: removing {} doesn't change scope of later let.
// Unless the block was a with or something.
// Give up and use:
function f() {
  let x = 1;
  if (true) { {}; let x = 2; }
  return x;
}
console.log(f());
// Always 1
// Not helpful.
// Alternative: the block was preventing a fallback via {} in object destructuring? No.
// We'll output a program where the trace is same, but note in comment.
