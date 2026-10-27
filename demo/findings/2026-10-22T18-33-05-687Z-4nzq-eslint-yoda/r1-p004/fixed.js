function test() {
  if (typeof helper === 'function') {
    if (helper() === 0) {   // rule fires: swap to helper() === 0
      return 'early';
    }
  }
  function helper() { return 42; }
  return helper();
}
console.log(test());
