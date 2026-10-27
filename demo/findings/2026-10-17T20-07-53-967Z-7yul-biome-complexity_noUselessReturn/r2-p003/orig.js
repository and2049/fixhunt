function f(a, a) {
  console.log(arguments[0], arguments[1]);
  arguments[0] = 99;
  console.log(a, arguments[0]);
  return;
}
f(1, 2);
