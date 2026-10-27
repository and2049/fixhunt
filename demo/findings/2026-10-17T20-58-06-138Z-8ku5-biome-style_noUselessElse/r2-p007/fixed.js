function f(a, b = 0) {
  if (arguments.length === 0) {
    return;
  }
    b = arguments[0];
  return b;
}
console.log(f(5));
