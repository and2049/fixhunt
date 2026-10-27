let calls = 0;
function f() { calls++; return 1; }
console.log(f() == 1);
console.log(calls);
