"use strict";
function f() {
  if (true) return;
  
    return function() { console.log(this); };
}
const g = f();
g && g();
