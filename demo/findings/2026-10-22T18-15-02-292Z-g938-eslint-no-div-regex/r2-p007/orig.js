"use strict";
(function() {
  const result = /=(.+)/.test('=value') ? RegExp.$1 : 'none';
  console.log(result);
})();
