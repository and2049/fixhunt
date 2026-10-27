function test() {
  if (false) var r = /a {2}b/;
  else var r = /c {2}d/;
  console.log(r.test('a  b'));
}
test();
