let logged = false;
function logX() { logged = true; console.log('x'); return 0; }
let v = 0;
if ((logX(), 0) == v) console.log('matched'); // rule triggers, logs before compare
console.log('logged:', logged);
