"use strict";
(() => {
  const log = [];
  // Hazard: 'this' in condition is undefined in strict mode
  if (this) { log.push(typeof this); } else { log.push('a'); }
  console.log(log.join('|')); // Expected: 'a'
})();
