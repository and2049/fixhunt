"use strict";
const g = Function('return this')();
defineProperty(g, 'Number', { value: undefined });
try {
  console.log(Number.parseInt('1'));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
function defineProperty(obj, name, desc) { Object.defineProperty(obj, name, desc); }
