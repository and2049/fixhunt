const obj = {};
Object.defineProperty(obj, 'pattern', {
  get() { return /hello {2}world/.source; },
  enumerable: true,
  configurable: true
});
console.log('Match:', /hello {2}world/.test(obj.pattern));
