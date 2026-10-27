function f(a, b = 1, ...rest) {
  for (let i = 0; i < 2; i++) {
    if (i === 0) continue;
    console.log('args:', arguments.length, 'rest:', rest.length);
  }
}
f(10);
