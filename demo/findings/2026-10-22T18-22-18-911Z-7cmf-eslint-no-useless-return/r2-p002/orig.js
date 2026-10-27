let x = 1;
function f() {
  let x = 2;
  return;
}
f();
console.log(x); // Should print 1
// If 'return;' removed and f inlined incorrectly, shadowing breaks
