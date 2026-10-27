const obj = {
  value: 42,
  getValue: function() { return this.value; }
};
test('  this test  ', () => {
  console.log('arrow:', obj.getValue());
  const fn = obj.getValue;
  console.log('extracted:', fn()); // undefined in strict
  console.log('bound:', fn.call(obj)); // 42
});
