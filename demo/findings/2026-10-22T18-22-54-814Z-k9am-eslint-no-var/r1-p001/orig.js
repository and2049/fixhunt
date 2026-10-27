(function () {
  'use strict';
  const obj = {x: 42};
  try {
    with (obj) {
      // var x /* scoped comment */ ;
      var x = 99;
    }
    console.log(obj.x); // prints original value
  } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
})();
