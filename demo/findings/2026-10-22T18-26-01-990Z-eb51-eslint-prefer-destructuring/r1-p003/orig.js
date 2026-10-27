function g(a) {
  console.log('args:', arguments.length, arguments[0]);
  const a = { prop: 99 }.prop; // rule triggers: reassigns param
  console.log('after:', arguments.length, arguments[0]);
  return a;
}
console.log(g(1)); // args: 1 1 -> after: 1 1 -> 99
