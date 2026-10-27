outer: {
  try {
    let val = 123.456;
    while (val > 0) {
      console.log(val.toFixed());
      if (val < 100) break outer;
      val -= 10;
    }
  } finally {
    console.log('finally');
  }
}
console.log('done');
