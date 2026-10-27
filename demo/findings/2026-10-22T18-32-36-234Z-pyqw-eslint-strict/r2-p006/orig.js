const obj = {
  value: 42,
  getValue: function() {
    return this.value;
  }
};
const fn = obj.getValue;
console.log(fn.call(obj)); // should be 42 in non-strict, undefined in strict
