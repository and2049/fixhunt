outer: {
  try {
    if (true) break outer;
    console.log(Number.parseInt('1'));
  } finally {
    console.log('finally');
  }
}
console.log('after');
