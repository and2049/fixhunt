function test() {
  LABEL: var x = 1;
  console.log(typeof x);
  let x = 2;
}
try { test(); } catch (e) { console.log(e.name + ': ' + e.message); }
