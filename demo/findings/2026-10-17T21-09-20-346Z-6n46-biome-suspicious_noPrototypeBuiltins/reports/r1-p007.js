const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', { value: 42, writable: false });
try {
  console.log(obj.hasOwnProperty('x'));
} catch (e) {
}
try {
} catch (e) {
}
