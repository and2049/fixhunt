const obj = {};
obj.__proto__ = [0, 1];
console.log(obj.length);
const copy = { ...obj };
console.log(copy.length);
