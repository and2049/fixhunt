var Math = { pow: (b, e) => b * e }; // Local rebinding
console.log('Local Math.pow(2,3):', Math.pow(2, 3));
try {
  // This would be rewritten to 2 ** 3 by the rule, ignoring local Math
  // But we simulate what the broken fix would do:
  const brokenFix = 2 ** 3;
  console.log('Broken fix (2**3):', brokenFix);
} catch (e) {
  console.log('Error in fix simulation:', e.name, e.message);
}
