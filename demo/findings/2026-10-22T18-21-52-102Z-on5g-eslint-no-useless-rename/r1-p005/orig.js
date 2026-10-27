function test() {
  let { y: y /* important */ } = { y: 7 };
  return y;
}
console.log(test()); // Should print 7 even if comment is stripped
