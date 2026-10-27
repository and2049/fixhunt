let log = [];
function side() { log.push('side'); return undefined; }
function f(a = side()) {
  return a;
}
f(); // call with no arg -> evaluates side()
f(undefined); // call with undefined arg -> does NOT evaluate side()
console.log(log.join(','));
