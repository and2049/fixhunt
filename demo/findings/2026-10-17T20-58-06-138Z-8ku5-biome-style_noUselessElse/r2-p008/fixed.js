let log = '';
outer: {
  if (false) {
    break outer;
  }
    log += 'a';
  log += 'b';
}
console.log(log);
