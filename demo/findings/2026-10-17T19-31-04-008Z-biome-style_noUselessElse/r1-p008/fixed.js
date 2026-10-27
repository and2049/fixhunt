function f() {
  if (true) return;
  
    throw new Error('trapped');
}
try { f(); } catch(e) { console.log(e.name); }
