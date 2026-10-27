function f() {
  const obj = { a: 1 };
  Object.__proto__.b = 2; // pollute Object.prototype
  const copy = Object.assign({}, obj);
  console.log('b in copy:', 'b' in copy); // true due to proto
  return; // TRIGGER
}
f();
// After fix: return removed, no change
// But make it depend on whether f ran: 
let ran = false;
function g() {
  ran = true;
  const o = { x: 1 };
  Object.__proto__.y = 99;
  const p = { ...o }; // spread ignores proto
  console.log('y in p:', 'y' in p); // false
  return; // TRIGGER
}
g();
console.log('ran:', ran);
