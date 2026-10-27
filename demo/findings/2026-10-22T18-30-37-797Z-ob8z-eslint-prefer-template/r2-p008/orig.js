const obj = {
  get a() { return console.log('get a'), 1; },
  get b() { return console.log('get b'), 2; }
};
console.log('Result: ' + obj.a + obj.b);
