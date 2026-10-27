function test(title, fn) {
  console.log(title.length);
  fn();
}
test('hello' + ' world', () => { console.log('ok'); });
