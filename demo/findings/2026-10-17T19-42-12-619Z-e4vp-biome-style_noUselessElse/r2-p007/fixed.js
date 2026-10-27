let log = [];
function f() {
  if (true) { return; }
  
    log.push(1);
    log.push(2);
}
f();
console.log(log);
