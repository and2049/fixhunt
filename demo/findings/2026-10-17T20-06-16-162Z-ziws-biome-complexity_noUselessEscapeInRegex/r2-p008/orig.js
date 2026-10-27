function f(a, b = 1, ...rest) {
  const re = /\d/;
  return [arguments.length, f.length, rest.length, re.test('a')];
}
console.log(f().join(','));
