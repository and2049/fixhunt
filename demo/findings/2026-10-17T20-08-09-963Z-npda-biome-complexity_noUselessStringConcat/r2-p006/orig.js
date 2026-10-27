"use strict";
let s1 = 'a' + 'b';
(function() {
  'use sloppy';
  let s2 = 'a' + 'b';
  console.log(s1 === s2);
})();
