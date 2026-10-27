let o = {a: 1};
if (typeof Object.hasOwn !== 'function') {
  console.log('Object.hasOwn not available, simulating old engine');
  // We still call the original to show it works
  console.log(Object.prototype.hasOwnProperty.call(o, 'a'));
} else {
  console.log(Object.prototype.hasOwnProperty.call(o, 'a'));
  console.log(Object.hasOwn(o, 'a'));
}
