const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', { value: 42, writable: false });
try {
  obj.hasOwnProperty('x');
} catch (e) {
  console.log('Original threw:', e.name, ':', e.message);
}
try {
} catch (e) {
}
