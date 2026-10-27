const obj = {
  get rx() { return /^[Á]$/; },
  test(v) { return this.rx.test(v); }
};
const fn = obj.test;
console.log(fn.call(obj, 'Á')); // true
obj.test('Á'); // true
// After fix: /^[A]$/ fails on 'Á'
console.log(obj.test('Á')); // false after fix - but we show before-fix behavior here
// Note: This prints pre-fix truth; post-fix would differ.
