const obj = {
  value: 42,
  method() { return this.value; }
};
const fn = obj.method;
console.log(Object.assign({}, { getValue: fn }).getValue());
