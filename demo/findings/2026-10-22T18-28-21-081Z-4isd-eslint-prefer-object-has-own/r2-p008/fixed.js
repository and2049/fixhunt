let obj = {};
let val = 42;
Object.defineProperty(obj, 'prop', {
  get() { console.log('getter called'); return val; },
  enumerable: true,
  configurable: true
});
console.log('Before check, val =', val);
if (Object.hasOwn(obj, 'prop')) {
  console.log('Has own prop');
}
console.log('After check, val =', val);
