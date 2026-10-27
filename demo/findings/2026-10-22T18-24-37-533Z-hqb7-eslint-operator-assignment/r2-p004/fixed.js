function f(a = 1, b = 2, ...rest) {
  arguments[0] += 1;
  console.log(arguments.length, rest.length);
}
f(); // args: [1,2] -> after: [2,2]; length unchanged but values changed
