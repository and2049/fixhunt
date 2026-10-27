'use strict';
try {
  Object.prototype.hasOwnProperty.call(null, 'x');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
try {
  Object.hasOwn(null, 'x');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
