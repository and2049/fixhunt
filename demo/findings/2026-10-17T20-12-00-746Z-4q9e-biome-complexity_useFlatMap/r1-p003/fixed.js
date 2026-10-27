const nums = [1, 2, 3, 4];
const result = nums.filter(n => n % 2 === 0).flatMap(n => [n, n*10]);
console.log(result.join('-'));
// After fix: .flatMap should preserve filter behavior
