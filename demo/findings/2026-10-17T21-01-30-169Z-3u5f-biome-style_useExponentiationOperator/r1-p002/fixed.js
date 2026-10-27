function test(a, b = 2 ** 3) {
  console.log('b:', b);
}
test(); // Expected: b: 8
// After fix: still works? But we test capture via closure
const fn = () => 2 ** 3;
console.log('fn():', fn()); // Expected: 8
