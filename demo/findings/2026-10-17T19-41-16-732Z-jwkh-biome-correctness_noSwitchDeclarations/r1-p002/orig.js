function f() {
  switch (x) {
    case 0:
      function g() { return 1; }
      break;
    case 1:
      return g();
  }
  return 0;
}
x = 0;
console.log(f()); // should be 1
x = 1;
console.log(f()); // should be 1 if not fixed, throws if fixed
