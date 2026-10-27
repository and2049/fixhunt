"use strict";
function g(a, a) { // duplicate param: SyntaxError in strict
  try {
    return !!a; // triggers rule
  } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
}
g(1, 2);
