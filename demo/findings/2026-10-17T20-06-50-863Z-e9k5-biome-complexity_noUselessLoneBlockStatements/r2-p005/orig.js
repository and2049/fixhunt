with ({ x: 10 }) {
  {};
  console.log(x);
}
// With block: x resolved to 10
// After fix: with ({x:10}) ; console.log(x); -> still 10? Yes, because with object unchanged.
// But: if block had var x=20, it would leak. Here no decl -> safe. So revise:
// Let's make block declare a var that shadows
with ({ x: 10 }) {
  { var x = 20; }
  console.log(x);
}
// Before: logs 20 (block-scoped? No, var is function-scoped, but with doesn't create scope)
// Actually: var inside with block is still function-scoped -> x=20 in outer scope
// After fix: var x=20; runs -> same. Not good.
// Use let:
with ({ x: 10 }) {
  { let x = 20; }
  console.log(x);
}
// Before: logs 10 (let in block)
// After fix: let x=20; is outside with -> throws ReferenceError? No, x not in with scope -> ReferenceError
// So:
