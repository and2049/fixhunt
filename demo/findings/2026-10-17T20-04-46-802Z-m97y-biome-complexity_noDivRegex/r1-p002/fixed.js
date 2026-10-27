let val = 0;
Object.defineProperty(obj, 'prop', {
  get() { return /[=]/.test(String(val)); },
  set(v) { val = v; }
});
obj.prop = 99;
console.log(obj.prop);
