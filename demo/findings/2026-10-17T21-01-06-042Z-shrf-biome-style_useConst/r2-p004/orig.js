let o = { valueOf: () => 2, toString: () => '3' };
let result = o + '';
console.log(result);
