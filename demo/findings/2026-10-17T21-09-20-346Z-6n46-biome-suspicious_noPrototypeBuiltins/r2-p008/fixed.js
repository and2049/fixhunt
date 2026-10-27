const obj = {
  value: 42,
  check: function() {
    return this.value === 42;
  },
  checkArrow: () => {
    return this.value === 42;
  }
};
const fn = obj.check;
const arrowFn = obj.checkArrow;
console.log('Function method call:', obj.check());
console.log('Extracted function call:', fn());
console.log('Arrow method call:', obj.checkArrow());
console.log('Extracted arrow call:', arrowFn());
try {
  Object.hasOwn(obj, 'value');
} catch (e) {
  console.log('hasOwnProperty call failed:', e.name);
}
