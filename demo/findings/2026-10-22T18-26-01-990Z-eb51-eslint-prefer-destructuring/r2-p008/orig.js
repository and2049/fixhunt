"use strict"; // Hazard 8: strict mode
const obj = {};
try {
  // Rule fires: const x = obj.x;
  let x = obj.x; // in strict, ok (undefined)
  console.log('x:', x);
} catch (e) {
  console.log(e.name);
}
