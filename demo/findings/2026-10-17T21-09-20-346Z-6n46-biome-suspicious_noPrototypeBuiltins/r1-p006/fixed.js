// Simulating document.all-like object
const fakeAll = { 
  [Symbol.isConcatSpreadable]: true,
  toString: () => '',
  valueOf: () => undefined
};
fakeAll.__proto__ = null;
try {
  console.log(fakeAll == null, Object.hasOwn(fakeAll, 'length'));
} catch (e) {
  console.log(e.name, e.message);
}
try {
  console.log(fakeAll == null, Object.hasOwn(fakeAll, 'length'));
} catch (e) {
  console.log(e.name, e.message);
}
