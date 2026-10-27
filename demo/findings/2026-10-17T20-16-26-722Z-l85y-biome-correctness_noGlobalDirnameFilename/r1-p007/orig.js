// Hazard 7
(function() {
  'use sloppy';
  with ({}) {
    console.log(__dirname);
  }
})();
