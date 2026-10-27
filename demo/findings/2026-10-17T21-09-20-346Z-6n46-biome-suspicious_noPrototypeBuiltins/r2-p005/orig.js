let accessCount = 0;
const handler = {
  get(target, prop) {
    accessCount++;
    if (prop === 'hasOwnProperty') {
      console.log('Trap hit for hasOwnProperty, access #', accessCount);
      return Object.prototype.hasOwnProperty;
    }
    return target[prop];
  }
};
const obj = new Proxy({ foo: 1 }, handler);
accessCount = 0;
console.log('Before (original):');
obj.hasOwnProperty('foo');
console.log('Access count after original:', accessCount);
accessCount = 0;
console.log('\nAfter (fixed):');
Object.prototype.hasOwnProperty.call(obj, 'foo');
console.log('Access count after fixed:', accessCount);
