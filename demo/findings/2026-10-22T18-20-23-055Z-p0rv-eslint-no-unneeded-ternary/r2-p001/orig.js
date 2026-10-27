function test() {
  const vals = [-0, NaN];
  for (const x of vals) {
    const orig = x ? x : 1;
    const fixed = x || 1;
    console.log(`x=${x}: orig=${orig}, fixed=${fixed}`);
    if (Object.is(orig, fixed)) continue;
    throw new Error(`Mismatch: ${orig} !== ${fixed}`);
  }
}
test();
