let a = { val: 0 };
let b = { val: 0 };
a.val = (b.val = 1) + a.val;
console.log(a.val, b.val); // depends on order: original: a.val used after b.val assigned
