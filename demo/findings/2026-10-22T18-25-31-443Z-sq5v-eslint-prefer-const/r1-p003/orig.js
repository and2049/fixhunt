let obj = {a: 1, b: 2};
let {a, b} = obj;
a = 99; // reassigned
console.log(a, b);
obj.b = 88; // b not mutated via obj, but user might expect it could be
console.log(obj.b); // shows 88, but b is const → confusion risk
