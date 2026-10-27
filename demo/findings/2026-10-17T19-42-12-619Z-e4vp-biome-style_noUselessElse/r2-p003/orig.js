function f() {
  if (false) {
    return g();
  } else {
    function g() { return 'early'; }
    return g();
  }
}
console.log(f());
