const obj = {
  10: function() { return this.value; },
  value: 42
};
const fn = obj[0b1010];
console.log(fn.call(obj)); // Should print 42
// After fix: key becomes 10 → obj[10] is undefined → fn is undefined → TypeError
