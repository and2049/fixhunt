// enable strict mode
'use strict';
function test() {
  // sloppy leak attempt
  leaked = 5;
}
try { test(); } catch(e) { console.log(e.name); }
console.log(leaked);
