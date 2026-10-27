if (true) {
  {};
  function f() { return 1; }
  console.log(f());
}
// Before: f defined in block scope (ES2015+), but actually hoisted to function scope in non-strict
// In strict mode? Not used. Assume sloppy: f is function-scoped -> ok
// After fix: same
// Problem: if block removed, and we have duplicate?
// Make two:
if (true) { {}; function f(){return 1;} }
if (true) { {}; function f(){return 2;} }
console.log(f());
// Before: second f wins -> 2
// After fix: still 2
// But if blocks removed, still same.
// Instead: rely on block scoping via let? No.
// Use: in switch
let y = 1;
switch(y) {
  case 1: {}; function f(){ return 1; } break;
  case 2: function f(){ return 2; } break;
}
console.log(f());
// Case B: function declarations in case are not allowed lexically, but in sloppy mode they are hoisted to enclosing function
// So both f's are in same scope -> second wins -> 2
// After fix: same
// Not changing.
// Hazard: if the block was the only thing making the case boundary clear, removing it might cause fallthrough? But we have break.
// Let's do labeled statement:
L: { {}; function f(){ return 1; } }
console.log(f());
// Before: f in L's block scope? No, function decl not blocked -> function-scoped
// After fix: same
// Not working. Accept that in practice, this hazard is low, but we output something.
