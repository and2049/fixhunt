if (true) {
  function f() { return 0b1010; } // triggers rule: rewrite to 0b1010
  console.log('f():', f());
}
// After fix: f() returns 10
console.log('After fix behavior:', typeof f === 'function' ? f() : 'ReferenceError');
