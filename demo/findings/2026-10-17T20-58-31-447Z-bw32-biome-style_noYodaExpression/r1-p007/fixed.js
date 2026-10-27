function foo(a) {
  arguments[0] = 99;
  if (a == 5) {
    return 'match';
  }
  return 'no';
}
console.log(foo(5));
function bar(a) {
  arguments[0] = 99;
  if (a == 5) {
    return 'match';
  }
  return 'no';
}
console.log(bar(5));
