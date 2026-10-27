"use strict";
let s1 = "ab";
(function() {
  'use sloppy';
  let s2 = "ab";
  console.log(s1 === s2);
})();
