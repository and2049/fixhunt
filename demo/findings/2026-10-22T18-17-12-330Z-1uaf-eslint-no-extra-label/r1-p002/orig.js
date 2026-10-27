function f() {
  console.log(typeof g);
}
F: function g() { return 42; }
console.log(g());
