let obj = {};
obj.__proto__ = {toString: () => 'changed'};
console.log(obj.toString());
