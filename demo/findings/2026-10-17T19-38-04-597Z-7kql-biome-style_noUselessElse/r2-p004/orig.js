function test() {
  if (false) {
    function f() { return 1; }
  } else {
    function f() { return 2; }
    return f();
  }
}
console.log(test());
