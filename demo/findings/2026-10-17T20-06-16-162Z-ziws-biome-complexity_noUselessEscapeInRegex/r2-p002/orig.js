function test() {
  const re = /(.)\1/;
  return re.test('aa') && !re.test('ab');
}
console.log(test());
