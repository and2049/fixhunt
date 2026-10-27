function scopeTest() {
  console.log('a before loop:', typeof a); // hoisted, undefined
  for (let i = 0; i < 2; i++) {
    var a ; // Rule triggers twice
    console.log('Iteration', i, 'a =', a);
    a = i * 10;
  }
  console.log('a after loop:', a); // Should be 10 from last iteration
}

scopeTest();
