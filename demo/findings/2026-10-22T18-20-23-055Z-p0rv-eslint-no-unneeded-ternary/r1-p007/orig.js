(() => {
  'use strict';
  let x = undefined;
  let a = x ? x : 1; // triggers rule: x?x:1 -> should become x||1
  console.log('a:', a); // 1
  // Now test with null
  x = null;
  a = x ? x : 1;
  console.log('a (null):', a); // 1
  // Both x||1 and x?x:1 give 1 for null/undefined
  // To see difference, need a falsy object that is not document.all (unavailable)
  // Instead, use 0: but 0?0:1 -> 1, 0||1 -> 1 same
  // Use '' -> same
  // Actually no difference for primitives. Hazard is theoretical for host objects.
  // We show that rewrite is safe for undefined/null
  x = 0;
  a = x ? x : 1;
  console.log('a (0):', a); // 1
})();
