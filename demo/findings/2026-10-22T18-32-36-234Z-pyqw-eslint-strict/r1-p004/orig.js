function f(a, ...rest) {
  console.log(arguments.length === 1 + rest.length);
  arguments[0] = 99;
  console.log(a);
}
f(1, 2, 3);
