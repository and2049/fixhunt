const obj = {
  value: 42,
  getValue: function() { return this.value; }
};
const fn = obj.getValue;
console.log("Value is " + fn());
