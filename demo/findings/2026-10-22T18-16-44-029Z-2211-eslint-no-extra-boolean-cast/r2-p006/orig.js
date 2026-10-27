let bat;
function log() { console.log('bat eval'); }
const val = (() => {
  const bar = 1, baz = 2;
  return Boolean((bar, baz, !!bat));
})();
console.log(val);
