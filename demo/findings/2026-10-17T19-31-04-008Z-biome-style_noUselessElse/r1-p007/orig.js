"use strict";
function f() {
  if (true) return;
  else {
    return function() { console.log(this); };
  }
}
const g = f();
g && g();
