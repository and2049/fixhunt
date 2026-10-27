try {
  Math.pow = 42; // Should fail in strict mode
} catch (e) {
}
console.log('Math.pow still works:', Math.pow(2, 3)); // Expected: 8
