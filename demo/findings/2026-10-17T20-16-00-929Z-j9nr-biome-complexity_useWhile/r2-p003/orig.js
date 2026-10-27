for (; false;) {
  function f() { return 1; }
  break;
}
try { console.log(f()); } catch (e) { console.log(e.name + ': ' + e.message); }
