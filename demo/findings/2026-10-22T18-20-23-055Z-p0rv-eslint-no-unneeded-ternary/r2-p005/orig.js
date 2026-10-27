const obj = {
  value: 42,
  getValue: function() { return this.value; }
};
const fn = obj.getValue;
const x = undefined;
const result = x ? x : fn.call(obj);
console.log('result:', result);
if (result !== 42) {
  throw new Error(`Expected 42, got ${result}`);
}
