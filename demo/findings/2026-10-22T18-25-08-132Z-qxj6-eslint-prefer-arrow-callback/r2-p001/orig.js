function outer() {
  [1,2].map(function(v) { if (v === 2) return 'found'; });
  return 'not found';
}
console.log(outer());
