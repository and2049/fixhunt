'use strict';
let x = 1;
try { delete x; } catch(e) { console.log(e.name); }

// Sloppy mode equivalent
(function() {
  let y = 1;
  try { delete y; } catch(e) { console.log(e.name); }
})();
