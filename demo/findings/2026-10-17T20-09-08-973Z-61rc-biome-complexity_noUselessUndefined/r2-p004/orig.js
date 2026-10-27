let log = [];
const obj = {};
Object.defineProperty(obj, 'prop', {
  get() {
    log.push('get');
    return undefined;
  }
});
x = obj.prop;
y = obj.prop;
console.log(log.join(','));
// After fix: getter still returns undefined implicitly, but we trace call count
