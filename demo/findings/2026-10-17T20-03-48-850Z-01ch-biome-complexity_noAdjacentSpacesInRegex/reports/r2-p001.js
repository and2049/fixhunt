const obj = {};
Object.defineProperty(obj, 'pattern', {
  get() { return /hello  world/.source; },
});
console.log('Match:', /hello  world/.test(obj.pattern));
