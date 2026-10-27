let x ;
const obj = { toString() { return '42'; }, valueOf() { return 0; } };
console.log(String(x) + obj);
console.log(`${x}${obj}`);
