const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', {
  get() {
    console.log('Getter called');
    return Object.prototype.hasOwnProperty;
  }
});
obj.hasOwnProperty('x');
