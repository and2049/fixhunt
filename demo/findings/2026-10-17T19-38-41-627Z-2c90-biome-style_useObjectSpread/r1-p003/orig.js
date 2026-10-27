"use sloppy";
let log = [];
const target = {};
const proxy = new Proxy(target, {
  set(t, p, v) {
    log.push(p + '=' + v);
    return true;
  }
});
Object.assign(proxy, { a: 1 });
console.log(log.join(','));
