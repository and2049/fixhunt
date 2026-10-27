(function() {
  'use strict';
  let z = 1;
  if (false) {} else {
    'use strict';
    try { eval('z = 2'); } catch(e) { z = 3; }
  }
  console.log(z);
})();
