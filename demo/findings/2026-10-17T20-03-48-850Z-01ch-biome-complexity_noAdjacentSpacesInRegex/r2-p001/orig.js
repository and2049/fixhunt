const obj = {};
Object.defineProperty(obj, 'pattern', {
  get() { return /hello  world/.source; },
  enumerable: true,
  configurable: true
});
console.log('Match:', /hello  world/.test(obj.pattern));
