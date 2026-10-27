let x = 0;
function inc() { return x++; }
function f() { if (inc() === 0) return; }
console.log(x);
f();
console.log(x);
