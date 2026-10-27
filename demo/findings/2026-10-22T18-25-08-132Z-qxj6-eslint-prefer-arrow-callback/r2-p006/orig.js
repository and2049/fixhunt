const obj = { valueOf: () => 5, toString: () => '5' };
console.log(+obj);
console.log(`${obj}`);
