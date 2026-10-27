let log = [];
function f() { log.push('cond'); return true; }
if (f()) { return; } else {
  log.push('else');
}
console.log(log.join(','));
