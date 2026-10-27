function fn(a, b = /x {2}y/.test('x  y')) {
  console.log(arguments.length, b);
}
fn(1);
