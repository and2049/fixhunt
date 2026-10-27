const nums = [1, 2, 3, 4];
const result = nums.filter(n => n % 2 === 0).map(n => [n, n*10]).flat();
console.log(result.join('-'));
// After fix: .flatMap should preserve filter behavior
