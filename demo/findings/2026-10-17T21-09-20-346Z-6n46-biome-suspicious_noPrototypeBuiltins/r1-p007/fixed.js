const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', { value: 42, writable: false });
try {
  console.log(Object.hasOwn(obj, 'x'));
} catch (e) {
  console.log(e.name, e.message);
}
try {
  console.log(Object.hasOwn(obj, 'x'));
} catch (e) {
  console.log(e.name, e.message);
}
