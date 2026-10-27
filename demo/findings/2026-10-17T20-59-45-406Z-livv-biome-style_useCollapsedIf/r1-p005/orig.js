let a = true;
let counter = 0;
function b() { counter++; return true; }
if (a) { if (b()) { console.log('inner'); } }
console.log('counter:', counter);
