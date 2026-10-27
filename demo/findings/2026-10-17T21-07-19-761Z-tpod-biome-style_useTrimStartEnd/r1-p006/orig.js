let s = '   hi   ';
let o = { __proto__: String.prototype };
console.log(o.trimLeft.call(s));
