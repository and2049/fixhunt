let that = this;
const obj = { x: 1, y: 2 };
(() => {
  'use strict';
  return Function('return that.x')();
})();
