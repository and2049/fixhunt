"use strict";
let obj = { value: 42 };
function getValue() {
  if (this === obj) return this.value;
  this.value = 99; // should error in strict
  return -1;
}
try {
  console.log(getValue.call(obj));
  console.log(getValue());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
