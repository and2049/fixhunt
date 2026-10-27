function fn(a, b = /x  y/.test('x  y')) {
  console.log(arguments.length, b);
}
fn(1);
