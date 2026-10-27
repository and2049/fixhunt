let o = {a: 1}; let p = {}; p.__proto__ = o;
function f(x){ return x + 0; }
console.log(f(p.a));
