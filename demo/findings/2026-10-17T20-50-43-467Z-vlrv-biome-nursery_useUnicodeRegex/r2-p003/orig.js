const obj = {};
Object.defineProperty(obj, 'getter', {
  get() { return /pattern/.test('input'); }
});
console.log(obj.getter);
