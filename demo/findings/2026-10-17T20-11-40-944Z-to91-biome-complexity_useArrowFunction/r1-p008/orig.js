function test() {
  console.log(typeof f);
  let f = function() { return 42; };
}
test();
