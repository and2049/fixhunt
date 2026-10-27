function test() {
  if (false) var r = /a  b/;
  else var r = /c  d/;
  console.log(r.test('a  b'));
}
test();
