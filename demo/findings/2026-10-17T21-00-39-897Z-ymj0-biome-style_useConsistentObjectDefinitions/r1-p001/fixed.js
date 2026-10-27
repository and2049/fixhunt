function outer() {
  var e = 'outer';
  try {
    throw new Error('test');
  } catch (e) {
    // Biome would rewrite {e: e} -> {e}
    const obj = {e};
    console.log(obj.e);
  }
  return e;
}
console.log(outer());
