const obj = {
  value: 42,
  check: function() { return this.value; }
};
const func = obj.check;
let x = func(); // x = undefined (in strict mode? but we're not strict)
// Actually in non-strict, func() -> this=global, value undefined -> x=undefined
// Let's make it return 0 to falsify
obj.value = 0;
x = obj.check(); // returns 0
let y = !!x; // triggers rule
console.log('y:', y); // should be false
// If rewritten as y = x, y=0 (still falsy, but 0 !== false)
// We'll see difference in type
