function f(a = 12345, b, ...rest) {
  console.log(arguments[0], a, b, rest.length);
}
f(undefined, 67890);
