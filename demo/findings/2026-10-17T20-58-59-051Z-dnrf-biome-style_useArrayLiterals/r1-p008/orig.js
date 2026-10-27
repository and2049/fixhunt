function test(a, b = Array(1, 2)) {
  console.log('args:', arguments.length, arguments[1]);
  console.log('b:', b);
}
test(0);
