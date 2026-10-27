function test(a = 2, b = 3) {
  console.log(arguments.length);
  console.log(Math.pow(a, b));
}
test();
function test2() {
  console.log(arguments.length);
  console.log((arguments[0] || 2) ** (arguments[1] || 3));
}
test2();
