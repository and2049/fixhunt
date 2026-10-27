"use strict";
if (true) {
  var x = 1;
}
try {
  console.log(x); // Should work with var hoisting
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
