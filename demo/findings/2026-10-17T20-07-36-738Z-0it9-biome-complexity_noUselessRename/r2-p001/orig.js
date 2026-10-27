let proto = {a: 1}; let obj = {b: 2};
try {
  ({__proto__: __proto__} = obj);
  console.log('assigned', obj.a === undefined && '__proto__' in obj);
} catch (e) {
  console.log('error:', e.message);
}
console.log('obj.__proto__ is', Object.getPrototypeOf(obj) === proto ? 'set' : 'not set');
