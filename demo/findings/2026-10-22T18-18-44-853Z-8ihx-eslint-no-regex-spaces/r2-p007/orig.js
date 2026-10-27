let obj = {};
Object.defineProperty(obj, 'prop', {
  get: () => /test  value/.test('test  value'),
  enumerable: true
});
console.log(obj.prop);
