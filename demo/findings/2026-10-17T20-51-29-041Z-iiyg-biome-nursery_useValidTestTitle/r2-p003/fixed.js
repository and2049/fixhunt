'use strict';
(function() {
  'use sloppy';
  test('strict?', function() {
    // In sloppy func, `this` is global; in strict, undefined
    console.log(this === global ? 'global' : this === undefined ? 'undefined' : 'other');
  });
})();
