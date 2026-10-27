"use strict";
try {
  console.log(Object.prototype.hasOwnProperty.call(null, 'x'));
} catch (e) {
  console.log(e.name);
}
try {
  console.log(Object.hasOwn(null, 'x'));
} catch (e) {
  console.log(e.name);
}
