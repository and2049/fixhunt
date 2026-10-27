if (true) {
  function foo() { return 1; }
  let x = typeof foo;
  foo = foo || function() { return 2; };
  console.log(typeof foo, x);
}
