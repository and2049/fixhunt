const obj = { test: () => 'original' };
obj.__proto__.test = () => 'overridden';
console.log(obj.test());
const copy = Object.assign({}, obj);
console.log(copy.test());
