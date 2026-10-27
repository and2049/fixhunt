function f() {
  if (true) { return; }
  let x = 1; console.log(x); 
}
try { f(); } catch (e) { console.log(e.name + ': ' + e.message); }
