const obj = {
  prop: 'value',
  check: function() { return this.prop === 'value'; }
};
const fn = obj.check;
console.log(fn());
try {
  console.log(Object.hasOwn(obj, 'check'));
} catch (e) {
  console.log(e.name, e.message);
}
