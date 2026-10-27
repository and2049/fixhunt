function test() {
  console.log(typeof x); // undefined due to hoisting
  LABEL: var x = 5;
  console.log(x);
}
try { test(); } catch (e) { console.log(e.name + ': ' + e.message); }
