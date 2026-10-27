"use strict";
let result = [];
function test(val) {
  if (val === "red") {   // rule fires: swap to val === "red"
    try { x = 1; } catch(e) { result.push('strict-assign-error'); }
    result.push('matched');
  } else {
    try { x = 2; } catch(e) { result.push('non-strict-assign-error'); }
    result.push('unmatched');
  }
}
test("red");
test("blue");
console.log(result.join('|'));
