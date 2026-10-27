outer: {
  let { y: y } = { y: 10 };
  if (y === 10) break outer;
  console.log('not reached');
}
console.log(y);
