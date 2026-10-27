try {
  console.log(x ** 2); // TDZ: x not initialized
} catch (e) {
  console.log('Caught:', e.name + ': ' + e.message);
}
let x = 3; // Hoisted declaration, not initialization
// After fix: same TDZ error
