'use strict';
function f() {
  var x = 1;
  var y = 2;
  try { delete x; } catch (e) { console.log(e.name); }
  try { delete y; } catch (e) { console.log(e.name); }
}
f();
