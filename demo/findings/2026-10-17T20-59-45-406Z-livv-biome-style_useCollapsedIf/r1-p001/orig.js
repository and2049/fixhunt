let a = false;
let bEval = 0;
function b() { bEval++; return true; }
if (a) { if (b()) { console.log('inner'); } }
console.log('bEval:', bEval);
