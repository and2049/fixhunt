function test() {
  console.log(typeof x); // Should log 'undefined' before init
  var x = undefined;
  console.log(x);
}
test();
