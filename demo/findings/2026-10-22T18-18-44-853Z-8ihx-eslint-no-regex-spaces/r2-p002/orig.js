let obj = { __proto__: null };
obj.__proto__ = { test: /hello  world/.test('hello  world') };
const copy = Object.assign({}, obj);
console.log(copy.test);
