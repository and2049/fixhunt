// Hazard 2
const o = {};
o[`__proto__${__dirname}`] = 'tampered';
console.log(Object.getPrototypeOf(o));
