function thrower() { throw new Error('boom'); }
let x = thrower();
console.log('x after throw (unreachable):', x);
try { console.log('x after fix:', ({ x }).x); } catch(e) { console.log('x after fix error:', e.name + ': ' + e.message); }
