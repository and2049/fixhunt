let count = 0;
const obj = { get arr() { count++; return [[1], [2]]; } };
const result = obj.arr.flatMap(x => x);
console.log(count, result.length);
// After fix, getter called once instead of twice if map and flat were separate?
