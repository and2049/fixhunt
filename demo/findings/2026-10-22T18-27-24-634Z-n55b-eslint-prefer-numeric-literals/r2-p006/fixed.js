console.log(typeof y); // y not declared yet -> undefined
var y = (function() { return 0b11; })(); // triggers rule: rewrite to 0b11 = 3
console.log('y:', y);
// After fix: y = 3
// Before fix: same value, but let's make TDZ visible via let
// Redo with let to trigger TDZ error if accessed before declaration
console.log('\nSecond part:');
try {
  console.log(z); // z not declared -> ReferenceError
} catch (e) {
  console.log('Caught:', e.name + ': ' + e.message);
}
let z = (() => 0b11)(); // triggers rule
console.log('z:', z);
