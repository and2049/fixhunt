function f() {
  if (false) {
    return g();
  }
    function g() { return 'early'; }
    return g();
}
console.log(f());
