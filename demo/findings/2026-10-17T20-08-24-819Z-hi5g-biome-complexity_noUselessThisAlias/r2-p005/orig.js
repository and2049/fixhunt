const obj = {};
let _this = obj;
Object.defineProperty(obj, 'prop', {
  get() { return this.value || 0; },
  set(v) { this.value = v * 2; }
});
obj.value = 5;
console.log(_this.prop);
