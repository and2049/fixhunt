function f() {
  switch (0) {
    case 0:
      if (true) { break; }
      else {
        function g() { return 1; }
        return g();
      }
  }
}
console.log(f());
