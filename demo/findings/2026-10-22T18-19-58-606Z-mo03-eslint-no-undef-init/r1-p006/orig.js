function g(a) {
  console.log(arguments.length);
  var a = undefined; // removed
  return arguments[0];
}
console.log(g(1, 2));
