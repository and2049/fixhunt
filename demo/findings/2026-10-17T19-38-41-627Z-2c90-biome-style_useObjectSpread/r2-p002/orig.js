let obj = {a: 1}; let ref = obj;
const res1 = Object.assign(ref, {b: 2});
obj.a = 99;
console.log(res1.a, ref === obj)
obj = {a: 1}; ref = obj;
const res2 = {...ref, b: 2};
obj.a = 99;
console.log(res2.a, ref === obj)
