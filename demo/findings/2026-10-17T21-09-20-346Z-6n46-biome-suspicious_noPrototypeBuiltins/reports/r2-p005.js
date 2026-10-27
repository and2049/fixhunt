let accessCount = 0;
const handler = {
  get(target, prop) {
    if (prop === 'hasOwnProperty') {
      console.log('Trap hit for hasOwnProperty, access #', accessCount);
    }
    return target[prop];
  }
};
const obj = new Proxy({ foo: 1 }, handler);
obj.hasOwnProperty('foo');
