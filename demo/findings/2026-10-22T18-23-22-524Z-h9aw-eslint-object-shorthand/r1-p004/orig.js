const obj = { a: a, b: b };
let a = 1, b = 2;
let s = '';
for (const k in obj) s += k + obj[k];
console.log(s);
