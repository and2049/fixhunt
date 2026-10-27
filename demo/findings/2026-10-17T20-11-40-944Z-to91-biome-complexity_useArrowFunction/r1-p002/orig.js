'use strict';
const f = function() { return arguments.length; };
console.log(f());

(() => {
  const g = function() { return arguments.length; };
  console.log(g());
})();
