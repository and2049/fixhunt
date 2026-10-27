var obj = { m() { this.x = 1 } };
var f = obj.m;
f();
try { console.log(window.x); } catch(e) { console.log(e.name); }
