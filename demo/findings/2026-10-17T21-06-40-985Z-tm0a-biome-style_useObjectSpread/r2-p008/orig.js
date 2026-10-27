function risky() {
  throw new TypeError('intentional');
}
try {
  Object.assign({}, {a: risky()}); // triggers rule, risky() throws
} catch (e) {
  console.log('caught:', e.name, e.message);
}
console.log('continued');
