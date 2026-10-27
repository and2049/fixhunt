const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', {
  get() {
    console.log('Getter called');
    return Object.prototype.hasOwnProperty;
  }
});
console.log('Before:');
obj.hasOwnProperty('x');
console.log('After:');
