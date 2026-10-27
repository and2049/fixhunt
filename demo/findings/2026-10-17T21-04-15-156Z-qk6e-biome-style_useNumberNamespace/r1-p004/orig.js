"use strict";
(() => {
  try {
    return parseInt('1');
  } catch (e) {
    return e instanceof ReferenceError ? 'TDZ' : 'other';
  }
})();
let Number = 42;
