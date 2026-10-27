const obj = { __proto__: { toString: () => 'proto' }, 12345: 'value' };
console.log(obj.__proto__.toString(), obj[12_345]);
