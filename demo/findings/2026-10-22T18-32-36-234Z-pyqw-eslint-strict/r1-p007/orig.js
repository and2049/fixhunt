const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this.counter++; }
});
console.log(obj.prop);
console.log(obj.prop);
