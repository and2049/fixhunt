const obj = {
  value: 42,
  getValue: function() { return this.value; }
};
const fn = obj.getValue;
console.log(fn()); // undefined (sloppy)
'use strict';
const obj2 = {
  value: 99,
  getValue: function() { return this.value; }
};
const fn2 = obj2.getValue;
console.log(fn2()); // undefined (strict)
