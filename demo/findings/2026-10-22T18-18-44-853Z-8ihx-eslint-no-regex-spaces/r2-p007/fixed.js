let obj = {};
Object.defineProperty(obj, 'prop', {
  get: () => /test {2}value/.test('test  value'),
  enumerable: true
});
console.log(obj.prop);
