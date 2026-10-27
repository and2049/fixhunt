const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', { value: 42, writable: false });
console.log('obj.hasOwnProperty:', obj.hasOwnProperty);
try {
  obj.hasOwnProperty('x');
} catch (e) {
  console.log('Original threw:', e.name, ':', e.message);
}
try {
  Object.prototype.hasOwnProperty.call(obj, 'x');
} catch (e) {
  console.log('Fixed threw:', e.name, ':', e.message);
}
