function g(a, b = /=/i.test('x'), ...r) {
  console.log(arguments.length, b, r.length);
}
g(1);
