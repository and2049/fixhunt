let log = '';
function f() { log += 'f'; return 1; }
function g() { log += 'g'; return 2; }
const arr = Array(f(), g());
console.log(log, arr);
