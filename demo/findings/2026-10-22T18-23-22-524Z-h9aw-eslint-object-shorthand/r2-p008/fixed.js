function f(a, b = 1) {
  let o = {a}; // triggers rule
  console.log(o.a === arguments[0], f.length);
  return o;
}
f(5); // logs: true 1
