const obj = { __proto__: { x: 1 } };
let __proto__ ;
let c = 1;
let d = 2;
console.log('before:', obj.__proto__.x);
console.log('after Object.assign:', Object.assign({}, obj, { __proto__: null }).__proto__);
try { console.log('after fix:', ({ __proto__: null, ...obj }).__proto__); } catch(e) { console.log('after fix error:', e.message); }
