function f() {
  if (true) return;
  else {
    throw new Error('trapped');
  }
}
try { f(); } catch(e) { console.log(e.name); }
