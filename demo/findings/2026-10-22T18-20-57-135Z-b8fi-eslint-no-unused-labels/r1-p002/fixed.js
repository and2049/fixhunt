function test() {
  var x = 10;
  { const x = 20; }
  console.log(x);
}
try { test(); } catch (e) { console.log(e.name + ': ' + e.message); }
