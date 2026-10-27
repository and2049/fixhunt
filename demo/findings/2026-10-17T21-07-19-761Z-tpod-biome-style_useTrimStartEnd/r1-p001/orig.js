outer: {
  let s = '   hello   ';
  inner: {
    if (true) break outer;
    console.log(s.trimLeft());
  }
}
console.log('done');
