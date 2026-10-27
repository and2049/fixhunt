const obj = {};
obj.__proto__ = { Number: { parseInt: (s) => 'shadow' } };
console.log(Number.parseInt('123')); // Should be 'shadow', fixed becomes 123
