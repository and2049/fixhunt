const obj = {
  [Symbol.toPrimitive](hint) { return hint === 'string' ? 'prop' : 42; }
};
console.log(obj.hasOwnProperty('prop'), obj.hasOwnProperty(42));
console.log(Object.prototype.hasOwnProperty.call(obj, 'prop'), Object.prototype.hasOwnProperty.call(obj, 42));
