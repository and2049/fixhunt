const obj = { __proto__: { x: 1 }, y: 2 };
const copy1 = { ...obj };
const copy2 = Object.assign({}, obj);
console.log(copy1.hasOwnProperty('__proto__') + ',' + copy2.hasOwnProperty('__proto__'));
