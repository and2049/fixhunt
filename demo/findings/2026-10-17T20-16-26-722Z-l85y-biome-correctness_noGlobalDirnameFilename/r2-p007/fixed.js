__dirname = 'overridden'; // assignment fails in strict, but assume non-strict
const obj = {};
obj[import.meta.dirname] = 'value';
console.log(obj['overridden'] ?? 'not set');
