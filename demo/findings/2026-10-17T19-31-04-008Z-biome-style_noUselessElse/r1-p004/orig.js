outer: {
  if (false) break outer;
  else {
    console.log('else');
    break outer;
  }
}
console.log('done');
