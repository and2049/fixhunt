Array = function(...args) { return { length: args.length, custom: true }; };
const arr = Array(1, 2);
console.log(arr.custom ? 'redefined' : 'literal');
