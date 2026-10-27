const obj = { name: 'obj', getName: function() { return this.name; } };
const fn = obj.getName;
const arrowFn = () => this.name;
let s1 = 'Hello ' + fn.call(obj);
let s2 = 'Hello ' + arrowFn();
console.log(s1, s2);
