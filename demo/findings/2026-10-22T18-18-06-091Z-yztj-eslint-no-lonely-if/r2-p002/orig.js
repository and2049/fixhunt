for (let i = 0; i < 2; i++) {
  if (i === 0) {
    console.log('first');
  } else {
    if (true) {
      var x = i;
      console.log(x);
    }
  }
}
// After loop, x should be 1 due to hoisting
console.log(typeof x === 'number' ? x : 'undef');
