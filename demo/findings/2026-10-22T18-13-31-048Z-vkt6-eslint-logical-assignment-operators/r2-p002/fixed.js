let obj = {};
obj.__proto__ = obj.__proto__ || { toString() { return 'proto'; } };
console.log(obj.toString());
obj.__proto__ = obj.__proto__ && { valueOf() { return 42; } };
console.log(obj.valueOf());
