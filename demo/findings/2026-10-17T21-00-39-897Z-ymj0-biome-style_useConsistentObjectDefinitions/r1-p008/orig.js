function f(a, b) {
  // Biome would rewrite {a: a, b: b} -> {a, b}
  const obj = {a: a, b: b};
  console.log(obj.a + ', ' + obj.b);
  console.log(arguments.length);
}
f(10, 20);
