console.log(typeof a); // 'undefined'
var a = 5;
let o = {a}; // rule would trigger but no semantic change
console.log(o.a); // 5
