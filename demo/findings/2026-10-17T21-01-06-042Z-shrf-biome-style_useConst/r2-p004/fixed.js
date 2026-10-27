const o = { valueOf: () => 2, toString: () => '3' };
const result = o + '';
console.log(result);
