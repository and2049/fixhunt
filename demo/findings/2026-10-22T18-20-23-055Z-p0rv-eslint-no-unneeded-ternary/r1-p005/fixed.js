const obj = { __proto__: { toString: () => 'proto' }, toString: () => 'obj' };
let x = obj.__proto__;
let str = x ? x.toString() : 'fallback'; // x is truthy object -> calls obj.__proto__.toString()
console.log('str:', str);
// Rule does NOT fire here (x?expr:fallback not x?true:false form)
// But if we had: let y = !!x; that would be different hazard
// Adjusting to hit rule: need x?true:false
let flag = !!x; // triggers rule: x is truthy -> flag=true
console.log('flag:', flag);
