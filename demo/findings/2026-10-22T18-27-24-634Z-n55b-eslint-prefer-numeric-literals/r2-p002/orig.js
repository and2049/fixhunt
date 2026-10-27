if (true) {
  function f() { return parseInt('1010', 2); } // triggers rule: rewrite to 0b1010
  console.log('f():', f());
}
// After fix: f() returns 10
console.log('After fix behavior:', typeof f === 'function' ? f() : 'ReferenceError');
