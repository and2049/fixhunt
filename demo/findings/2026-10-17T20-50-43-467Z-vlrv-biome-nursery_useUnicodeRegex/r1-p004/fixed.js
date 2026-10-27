let obj = { valueOf: () => 'b', toString: () => 'B' };
let p = +obj;
let r = new RegExp(p, 'u');
console.log(r.test('b'));
