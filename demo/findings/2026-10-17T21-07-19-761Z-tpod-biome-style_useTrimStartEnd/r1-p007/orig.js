let s = '  x  ';
let desc = Object.getOwnPropertyDescriptor(String.prototype, 'trimLeft');
console.log(desc.enumerable);
console.log(s.trimLeft());
