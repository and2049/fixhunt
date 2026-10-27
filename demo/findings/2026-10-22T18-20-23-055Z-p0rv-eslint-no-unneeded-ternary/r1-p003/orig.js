function test(a, b = 1, ...rest) {
  let x = arguments[0];
  let y = x ? true : false; // triggers rule
  console.log('y:', y, '| args:', [].slice.call(arguments));
}
test(0, 2, 3); // x=0 -> y=false; if rewritten as y=x, y=0 (differs)
