function test() {
  const Array = () => ({ length: 0, push: () => {} });
  const x = [];
  x.push(Array(1, 2));
  console.log(x[0].length);
}
test();
