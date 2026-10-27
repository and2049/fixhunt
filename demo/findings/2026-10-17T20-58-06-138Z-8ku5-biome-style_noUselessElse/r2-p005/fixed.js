let log = [];
function f() {
  log.push('start');
  if (false) {
    return;
  }
    log.push('else');
  log.push('end');
  return log.join(',');
}
console.log(f());
