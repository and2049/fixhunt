function test() {
  var a = new RegExp('a', '');
  var b = new RegExp('a', '');
  console.log(a !== b);
}
test();
