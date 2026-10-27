const obj = {};
Object.defineProperty(obj, 'getter', {
  get() { return /pattern/u.test('input'); }
});
console.log(obj.getter);
