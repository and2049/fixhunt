let result = [];
if (false) {
} else {
  function f() { return 1; }
  result.push(typeof f === 'function' ? f() : 'not fn');
}
result.push(typeof f === 'function' ? f() : 'global fn');
console.log(result.join(','));
