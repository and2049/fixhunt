let callCount = 0;
const obj = {
  get num() {
    callCount++;
    return 123.456;
  }
};
console.log(`First: ${obj.num.toFixed()}, calls: ${callCount}`);
console.log(`Second: ${obj.num.toFixed()}, calls: ${callCount}`);
Object.defineProperty(obj, 'num', { value: 99.99, writable: true });
console.log(`After: ${obj.num.toFixed()}, calls: ${callCount}`);
