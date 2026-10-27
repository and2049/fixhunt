const target = {};
Object.defineProperty(target, 'prop', {
  get() { console.log('GET'); return 42; },
  configurable: true
});
console.log('before:', typeof target.prop);
Object.assign({}, target); // triggers rule
console.log('after:', typeof target.prop);
