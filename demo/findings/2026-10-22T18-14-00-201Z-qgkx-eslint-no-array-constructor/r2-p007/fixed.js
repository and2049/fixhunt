Array = function(...args) { return { length: args.length, custom: true }; };
Array.prototype.push = Array.prototype.push || function(){};
const arr = [1, 2];
console.log(arr.custom ? 'redefined' : 'literal');
