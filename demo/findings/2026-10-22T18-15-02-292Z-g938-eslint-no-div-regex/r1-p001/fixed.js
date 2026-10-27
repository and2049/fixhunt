function f() {
  var foo = 1;
  { let foo = 2; console.log(/[=]/.test(foo)); }
}
f();
