function C() { this.custom = true; }
C.prototype = [];
const arr = new C();
arr.push(1);
console.log(arr.__proto__ === Array.prototype ? 'base' : 'custom');
