// no semicolons; relies on ASI
let g 
let h = (function() { return 1; })()
console.log('g before fix:', g);
console.log('h before fix:', h);
try { console.log('g after fix:', ({ g }).g); } catch(e) { console.log('g after fix error:', e.message); }
try { console.log('h after fix:', ({ h }).h); } catch(e) { console.log('h after fix error:', e.message); }
