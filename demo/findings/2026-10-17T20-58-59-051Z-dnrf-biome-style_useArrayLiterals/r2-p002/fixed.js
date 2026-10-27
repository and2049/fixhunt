const obj = {};
obj[`__proto__`] = [1, 2];
console.log(obj.__proto__.length === 2 && obj.__proto__[0] === 1);
