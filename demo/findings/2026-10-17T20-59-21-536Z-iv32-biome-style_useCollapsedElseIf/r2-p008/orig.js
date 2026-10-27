"use strict";
let err = null;
try {
  if (false) {
  } else {
    function junk() {}
    junk();
    delete junk; // TypeError in strict mode
  }
} catch (e) {
  err = e.name + ': ' + e.message;
}
console.log(err || 'no error');
// After fix: else if(false) { ... } -> delete junk still throws in strict mode
// So output shows error
