"use strict";
(() => {
  const log = [];
  // Hazard: 'this' in condition is undefined in strict mode
  if (!this) { log.push('a'); } else { log.push(typeof this); }
  console.log(log.join('|')); // Expected: 'a'
})();
