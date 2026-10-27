const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', { value: 42, writable: false });
try {
  console.log(obj.hasOwnProperty('x'));
} catch (e) {
  console.log(e.name, e.message);
}
try {
  console.log(Object.prototype.hasOwnProperty.call(obj, 'x'));
} catch (e) {
  console.log(e.name, e.message);
}
