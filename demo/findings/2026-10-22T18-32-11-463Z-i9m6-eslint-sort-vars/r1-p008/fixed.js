const obj = { val: 42, getVal: function() { return this.val; } };
let fn = obj.getVal, bound = fn.bind(obj);
console.log(fn(), bound());
