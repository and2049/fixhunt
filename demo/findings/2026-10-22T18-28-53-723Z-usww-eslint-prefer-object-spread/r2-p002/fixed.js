const obj = { valueOf() { return 42; }, toString() { return 'hello'; } };
let sum = ({ ...obj}) + 8;
console.log(sum); // 50 because valueOf called
sum = ({ ...obj }) + 8;
console.log(sum); // NaN because spread creates plain object, valueOf lost
