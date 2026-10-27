"use sloppy";
(function(){
  console.log(delete a); // false before init
  var a;
  var a = undefined; // removed
  console.log(delete a); // true after
})();
