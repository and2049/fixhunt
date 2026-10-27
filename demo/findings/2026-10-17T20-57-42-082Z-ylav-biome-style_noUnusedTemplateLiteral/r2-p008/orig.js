function f() {
  function g() {
    const args = `args: ${arguments.length}`;
    console.log(args);
  }
  g();
}
f(1, 2, 3);
