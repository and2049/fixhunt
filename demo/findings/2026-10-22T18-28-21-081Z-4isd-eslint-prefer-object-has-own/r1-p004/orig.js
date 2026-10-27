let obj = { a: 1 };
let result = typeof Object.hasOwn === 'function'
  ? Object.hasOwn(obj, 'a')
  : Object.prototype.hasOwnProperty.call(obj, 'a');
console.log(result); // prints true only if polyfilled or modern
