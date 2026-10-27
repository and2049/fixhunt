const obj = { valueOf() { return 42; }, toString() { return 'hello'; } };
let sum = ({ ...obj}) + 8;
console.log('sum:', sum);
sum = ({ ...obj }) + 8;
console.log('sum:', sum);
