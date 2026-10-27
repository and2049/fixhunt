const obj = { __proto__: { toString: 1 }, toString: 'own' };
console.log(Object.hasOwn(obj, 'toString'));
console.log(Object.hasOwn(obj, 'toString'));
