var a = 1;
var b; // TDZ guard (will become undefined after fix)
let b = 2; // shadowing inner scope
console.log('a:', a);
console.log('inner b before fix:', b);
try { console.log('inner b after fix:', ({ a, b, c, d } = {}, b)); } catch(e) { console.log('inner b after fix error:', e.message); }
