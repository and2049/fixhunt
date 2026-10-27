const obj = {};
Object.defineProperty(obj, 'hasOwnProperty', {
  get() {
    console.log('Getter called');
    return Object.prototype.hasOwnProperty;
  }
});
console.log('Before:');
Object.hasOwn(obj, 'x');
console.log('After:');
