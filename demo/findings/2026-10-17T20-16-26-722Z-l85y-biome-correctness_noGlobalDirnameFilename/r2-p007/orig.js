__dirname = 'overridden'; // assignment fails in strict, but assume non-strict
const obj = {};
obj[__dirname] = 'value';
console.log(obj['overridden'] ?? 'not set');
