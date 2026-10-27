const obj = {};
Object.defineProperty(obj, 'test', {
  get() { return this._val * 2; },
  set(v) { this._val = v; }
});
obj.test = 5;
console.log(`Getter result: ${obj.test}`);
