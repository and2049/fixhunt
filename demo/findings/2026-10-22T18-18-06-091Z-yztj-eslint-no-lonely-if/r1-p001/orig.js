function test() {
  let x = 0;
  outer: if (false) {
    x = 1;
  } else {
    inner: if (true) {
      x += 2;
      break inner;
    }
  }
  if (x === 2) console.log('label worked');
  else console.log('label failed:', x);
}
test();
