OUTER: {
  const fn = () => { break OUTER; };
  fn();
}
console.log('reached');
