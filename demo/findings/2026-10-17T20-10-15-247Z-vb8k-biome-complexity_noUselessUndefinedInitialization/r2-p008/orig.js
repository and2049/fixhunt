const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._val; },
  set(v) { this._val = v; }
});
obj.prop = undefined;
console.log(obj.prop);
