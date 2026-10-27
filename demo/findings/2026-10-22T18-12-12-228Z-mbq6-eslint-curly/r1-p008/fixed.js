const obj = { valueOf: () => 2, toString: () => '3' };
let sum = 0;
if (true)
  {sum += obj;}
console.log(sum, typeof sum);
