function test() {
  for (var i = 0, j = 10; i < 3; i++, j--) {
    // j must be function-scoped to be accessible after loop
  }
  return typeof j !== 'undefined' ? j : 'undef';
}
console.log(test());
