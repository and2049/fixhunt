(() => {
  const log = [];
  // Hazard: if condition contains function decl? Not directly.
  // Instead: make condition rely on a function whose decl is affected by block scoping
  if (true) { function f() { return 1; } }
  // Now use f in condition - but f is not accessible outside block in strict mode
  "use strict";
  try {
    if (! (typeof f === 'function') ) { log.push('if'); } else { log.push(f()); }
  } catch (e) {
    log.push(e.name);
  }
  console.log(log.join('|')); // In non-strict: f is hoisted -> '1'; in strict: ReferenceError
})();
