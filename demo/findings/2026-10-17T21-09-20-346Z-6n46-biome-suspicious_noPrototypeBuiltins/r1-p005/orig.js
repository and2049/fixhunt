const obj = { __proto__: { toString: 1 }, toString: 'own' };
console.log(obj.hasOwnProperty('toString'));
console.log(Object.prototype.hasOwnProperty.call(obj, 'toString'));
