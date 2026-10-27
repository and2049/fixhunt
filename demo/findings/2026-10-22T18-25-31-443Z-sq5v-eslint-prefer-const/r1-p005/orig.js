let obj = {
  value: 42,
  getValue: function() { return this.value; }
};
let fn = obj.getValue;
console.log(fn()); // undefined (sloppy)
'use strict';
let obj2 = {
  value: 99,
  getValue: function() { return this.value; }
};
let fn2 = obj2.getValue;
console.log(fn2()); // undefined (strict)
