function* gen() {
  let x, y;
  y = 1;
  yield y;
  x = 2;
  yield x;
}
console.log([...gen()]);
