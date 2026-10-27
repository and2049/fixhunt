outer: {
  try {
    if (/test/u.test('x')) break outer;
    console.log('should not reach');
  } finally {
    console.log('finally ran');
  }
}
console.log('after label');
