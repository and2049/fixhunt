"use strict";
(function() {
  try {
    let args = 1, arguments;
    return typeof arguments;
  } catch (e) {
    return e.name + ': ' + e.message;
  }
})();
