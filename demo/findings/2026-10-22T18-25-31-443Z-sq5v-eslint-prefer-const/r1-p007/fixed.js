let a = 1, b = 2;
a = 3;
console.log(a, b);
// After fix: let a = 1, const b = 2; → a reassigned, b const → valid but mixed
