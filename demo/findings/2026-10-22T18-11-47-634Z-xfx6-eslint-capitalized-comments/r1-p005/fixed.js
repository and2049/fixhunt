// Obj prop
const obj = {};
Object.defineProperty(obj, 'val', {
  // Get value
  get() { return this._v || 0; },
  // Set value
  set(v) { this._v = v; }
});
console.log(obj.val);
obj.val = 99;
console.log(obj.val);
