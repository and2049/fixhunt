function foo({ a: a } = { a: 5 }) {
  console.log(arguments.length, a);
  return a;
}
console.log(foo().toString()); // Should be '5'
