const obj = { multiplier: 2 };
function mapper(x) { return [x * this.multiplier]; }
const arr = [1, 2, 3];
const resultWithThis = arr.map(mapper, obj).flat();
console.log('with thisArg:', resultWithThis);
arr.map(mapper, obj).flat(); // expect_trigger
const broken = arr.map(mapper).flatMap(x => x);
console.log('without thisArg:', broken);
