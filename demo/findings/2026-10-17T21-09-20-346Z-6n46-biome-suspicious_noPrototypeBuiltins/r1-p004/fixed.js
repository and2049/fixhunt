const obj = {
  [Symbol.toPrimitive](hint) { return hint === 'string' ? 'prop' : 42; }
};
console.log(Object.hasOwn(obj, 'prop'), Object.hasOwn(obj, 42));
console.log(Object.hasOwn(obj, 'prop'), Object.hasOwn(obj, 42));
