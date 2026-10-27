const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._value || 0; },
  set(v) { this._value = v; },
  enumerable: false
});
let result = { ...obj};
console.log('desc:', Object.getOwnPropertyDescriptor(result, 'prop'));
result = { ...obj };
console.log('desc:', Object.getOwnPropertyDescriptor(result, 'prop'));
