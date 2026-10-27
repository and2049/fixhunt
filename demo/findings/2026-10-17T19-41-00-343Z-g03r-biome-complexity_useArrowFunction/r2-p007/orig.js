const obj = {
  get value() { return 42; },
  set value(v) { this._val = v; }
};
obj.value = 10;
console.log(obj.value, obj._val);
