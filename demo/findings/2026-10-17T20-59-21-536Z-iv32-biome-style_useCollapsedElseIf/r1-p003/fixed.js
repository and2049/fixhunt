const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._val || 0; },
  set(v) { this._val = v * 2; }
});
if (false) {} else if (true) { obj.prop = 5; }
console.log(obj.prop); // Should be 10 due to setter doubling
