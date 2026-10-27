let counter = 0;
function sideEffect() { counter++; return 42; }
let x = sideEffect();
console.log('x before fix:', x, 'counter:', counter);
try { console.log('x after fix:', ({ x }).x, 'counter after fix:', counter); } catch(e) { console.log('x after fix error:', e.message); }
