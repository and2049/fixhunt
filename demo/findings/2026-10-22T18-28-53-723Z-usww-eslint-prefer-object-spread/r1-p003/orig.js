let obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._val; },
  set(v) { this._val = v * 2; }
});
obj.prop = 5;
const copied = Object.assign({}, obj);
console.log(copied.prop, obj._val);
