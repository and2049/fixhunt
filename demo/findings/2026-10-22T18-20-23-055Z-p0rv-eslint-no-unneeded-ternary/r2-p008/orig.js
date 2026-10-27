function test(a, b = 1) {
  console.log('args.length:', arguments.length);
  console.log('function.length:', test.length);
  const x = arguments[0];
  const orig = x ? x : 2;
  const fixed = x || 2;
  console.log(`x=${x}: orig=${orig}, fixed=${fixed}`);
  if (!Object.is(orig, fixed)) {
    throw new Error(`Arguments mismatch: ${orig} !== ${fixed}`);
  }
  return orig;
}
test();
test(0);
test(-0);
