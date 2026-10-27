let log = '';
outer: {
  if (false) {
    break outer;
  } else {
    log += 'a';
  }
  log += 'b';
}
console.log(log);
