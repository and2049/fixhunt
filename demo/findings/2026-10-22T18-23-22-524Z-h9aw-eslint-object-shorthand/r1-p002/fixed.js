"use strict";
const obj = {
  m() { return this === undefined ? 'strict' : typeof this; }
};
obj.val = 1;
console.log(obj.m());
const fn = obj.m;
console.log(fn());
