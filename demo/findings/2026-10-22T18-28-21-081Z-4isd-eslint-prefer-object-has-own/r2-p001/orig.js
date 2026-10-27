let o = {a: 1}; let x;
function getObj() { return x; }
console.log(getObj()?.a ?? 'missing');
if (Object.prototype.hasOwnProperty.call(getObj(), 'a')) {
  console.log('has own');
} else {
  console.log('does not have own');
}
