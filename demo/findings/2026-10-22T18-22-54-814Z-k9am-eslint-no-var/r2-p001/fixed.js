function test() {
  const funcs = [];
  for (var i = 0; i < 3; i++) {
    funcs.push(() => i);
  }
  return funcs.map(f => f());
}
console.log(test().join(','));
