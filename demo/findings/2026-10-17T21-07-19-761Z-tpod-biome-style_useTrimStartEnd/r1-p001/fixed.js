outer: {
  let s = '   hello   ';
  inner: {
    if (true) break outer;
    console.log(s.trimStart());
  }
}
console.log('done');
