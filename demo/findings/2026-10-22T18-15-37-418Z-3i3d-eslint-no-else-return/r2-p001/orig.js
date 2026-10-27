"use strict";
let result = [];
function test(x) {
  if (x === 0) { return "zero"; }
  else { 
    try { eval("arguments[0] = 99"); }
    catch(e) { result.push(e.message); }
    result.push(x);
  }
}
test(5);
test(0);
console.log(result.join("|"));
