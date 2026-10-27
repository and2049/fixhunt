function f() { console.log('called'); return 'Y'; }
let s = '' + f();
console.log(s);
