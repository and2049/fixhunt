for (var i = 0; i < 2; i++) {
  if (i === 0) var pattern = /test {2}case/;
  console.log(pattern.test('test  case'));
}
console.log(typeof pattern);
