"use strict";
(function() {
  try {
    with ({Math: {pow: (b, e) => b + e}}) {
      console.log(Math.pow(2, 3));
    }
  } catch (e) {
    console.log(e.name);
  }
})();
(function() {
  "use strict";
  try {
    with ({Math: {pow: (b, e) => b + e}}) {
      console.log(2 ** 3);
    }
  } catch (e) {
    console.log(e.name);
  }
})();
