function outer(a) {
  const b = `arg is ${a}`;
  function inner() {
    console.log(arguments[0]); // expects 'inner'
    const c = `static`; // triggers rule
    console.log(c); // prints static before fix, but after fix still works...
    return c;
  }
  console.log(inner());
}
outer('x');
