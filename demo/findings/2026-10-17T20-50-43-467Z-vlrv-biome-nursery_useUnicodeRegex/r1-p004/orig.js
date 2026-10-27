let obj = { valueOf: () => 'b', toString: () => 'B' };
let p = +obj;
let r = new RegExp(p, '');
console.log(r.test('b'));
