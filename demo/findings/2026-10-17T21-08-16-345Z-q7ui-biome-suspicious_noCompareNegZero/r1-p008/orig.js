const obj = {
  value: 42,
  getValue: function() { return this.value; }
};
const fn = obj.getValue;
console.log(fn()); // undefined in strict mode
const bound = obj.getValue.bind(obj);
console.log(bound()); // 42
