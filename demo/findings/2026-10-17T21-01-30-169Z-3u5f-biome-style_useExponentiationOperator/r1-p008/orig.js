switch (1) {
  case 1:
    function helper() {
      return Math.pow(2, 3);
    }
    break;
}
console.log('Helper result:', helper()); // Expected: 8
// After fix: helper uses 2 ** 3 — same result
// But we want to test if hoisting/scoping affects it
// Add re-declaration attempt
try {
  function helper() { return 0; } // Should throw in strict? But we're not strict
} catch (e) {
  console.log('Redeclaraion error:', e.message);
}
console.log('Helper again:', helper()); // Still 8
// No change expected — but we include as structural hazard
