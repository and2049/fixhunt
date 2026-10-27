"use strict";
try {
  Math.pow = 42; // Should fail in strict mode
} catch (e) {
  console.log('Assignment error:', e.name);
}
console.log('Math.pow still works:', 2 ** 3); // Expected: 8
// In sloppy mode, assignment succeeds and breaks Math.pow
// After fix: 2 ** 3 still works even if Math.pow is overwritten
// So we can detect mode by whether Math.pow is callable
let isStrict = true;
try { Math.pow = 1; } catch { isStrict = false; }
if (isStrict) {
  console.log('Mode: strict');
} else {
  console.log('Mode: sloppy');
  Math.pow = () => 0; // Break it
  console.log('After break, Math.pow(2,3):', 2 ** 3); // Expected: 0
  console.log('But 2 ** 3:', 2 ** 3); // Expected: 8 — shows fix avoids reliance on Math.pow
}
