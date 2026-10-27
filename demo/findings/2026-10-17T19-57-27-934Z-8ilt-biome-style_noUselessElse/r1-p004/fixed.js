let log = '';
outer: {
  inner: {
    if (false) { break inner; }
    break outer; 
  }
  log += 'after inner';
}
log += 'end';
console.log(log);
