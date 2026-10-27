function g(a, b = 1, ...rest) {
  if (\"hi\" == arguments[0]) console.log('first arg matched'); // rule triggers
  return [a, b, rest.length];
}
console.log(g('hi', 2, 3, 4));
