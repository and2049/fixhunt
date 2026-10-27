function scopeTest() {
  for (let i = 0; i < 2; i++) {
    var a = undefined; // Rule triggers twice
    console.log('Iteration', i, 'a =', a);
    a = i * 10;
  }
}
scopeTest();
