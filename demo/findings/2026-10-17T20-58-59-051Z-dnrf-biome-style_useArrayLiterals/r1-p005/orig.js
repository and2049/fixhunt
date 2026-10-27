const obj = {};
obj.__proto__ = Array(0, 1);
console.log(obj.length);
const copy = { ...obj };
console.log(copy.length);
