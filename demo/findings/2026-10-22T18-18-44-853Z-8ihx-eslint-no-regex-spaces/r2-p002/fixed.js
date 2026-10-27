let obj = { __proto__: null };
obj.__proto__ = { test: /hello {2}world/.test('hello  world') };
const copy = Object.assign({}, obj);
console.log(copy.test);
