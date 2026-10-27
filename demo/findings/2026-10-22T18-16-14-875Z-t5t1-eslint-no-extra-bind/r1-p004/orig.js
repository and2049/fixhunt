const f = function (a, b = 1, ...rest) {
  console.log(arguments.length, this === undefined ? 'und' : 'def', f.length);
}.bind(null, 10);
f(20, 30);
