outer: for (let i = 0; i < 2; i++) {
  if (i === 0) { continue outer; }
  else {
    console.log('reached');
    break outer;
  }
}
