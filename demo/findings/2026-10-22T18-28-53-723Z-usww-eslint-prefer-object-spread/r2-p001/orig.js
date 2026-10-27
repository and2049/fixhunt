const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._value || 0; },
  set(v) { this._value = v; },
  enumerable: false
});
let result = Object.assign({}, obj);
console.log(Object.getOwnPropertyDescriptor(result, 'prop')); // has getter/setter
result = { ...obj };
console.log(Object.getOwnPropertyDescriptor(result, 'prop')); // undefined
