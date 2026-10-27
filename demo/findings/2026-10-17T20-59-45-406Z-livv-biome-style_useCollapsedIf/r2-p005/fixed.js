'use strict';
// Hazard 6: strict mode
let obj = {};
if (obj && obj.prop === undefined) {
    obj.prop = 42;
  }
console.log('obj.prop:', obj.prop);
