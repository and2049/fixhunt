let o = {a: 1};
let result = !Object.prototype.hasOwnProperty.call(o, 'a') && 0;
console.log('Result:', result);
result = !Object.hasOwn(o, 'a') && 0;
console.log('Result after fix:', result);
