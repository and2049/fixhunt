function test(a, b, ...rest) {
  console.log(!!arguments.length);
  if (arguments.length) {
    console.log('args present:', arguments.length);
  }
}
test();
test(1);
