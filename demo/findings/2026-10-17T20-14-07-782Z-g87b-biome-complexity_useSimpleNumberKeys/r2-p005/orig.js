
let log = [];
const obj = {};
Object.defineProperty(obj, '1_000', { // will be rewritten to 1000
  get() { log.push('get'); return 'value'; },
  enumerable: true,
  configurable: true
});
console.log(obj[1000], log.length ? log[0] : 'none');
