let a = true;
let counter = 0;
function b() { counter++; return true; }
if (a && b()) { console.log('inner'); }
console.log('counter:', counter);
