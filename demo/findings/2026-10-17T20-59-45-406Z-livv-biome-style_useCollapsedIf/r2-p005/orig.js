'use strict';
// Hazard 6: strict mode
let obj = {};
if (obj) {
  if (obj.prop === undefined) {
    obj.prop = 42;
  }
}
console.log('obj.prop:', obj.prop);
