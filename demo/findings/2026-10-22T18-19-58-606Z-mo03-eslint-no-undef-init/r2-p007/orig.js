function g(a, b = undefined) {
  console.log('args.len:', arguments.length);
  console.log('b:', b === undefined ? 'undef' : b);
  b = 99;
  console.log('b after:', b);
  console.log('arguments[1]:', arguments[1]);
}
g(1);
