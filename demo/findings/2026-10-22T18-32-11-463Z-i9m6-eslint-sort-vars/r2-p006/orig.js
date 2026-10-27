let obj = {};
let log = [];
Object.defineProperty(obj, 'a', {
  get() { log.push('get'); return 1; }
});
Object.defineProperty(obj, 'b', {
  set(v) { log.push('set:' + v); }
});
obj.b = 2;
console.log(obj.a, log.join('|'));
