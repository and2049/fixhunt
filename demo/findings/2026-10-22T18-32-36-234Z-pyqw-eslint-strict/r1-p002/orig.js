function f() {
  return
}(
  () => 42
)();
console.log(typeof f());
