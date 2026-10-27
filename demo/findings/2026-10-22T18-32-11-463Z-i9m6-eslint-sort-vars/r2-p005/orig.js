function f(z, y, x = 0) {
  console.log(f.length, arguments.length, x);
}
f(1, 2);
