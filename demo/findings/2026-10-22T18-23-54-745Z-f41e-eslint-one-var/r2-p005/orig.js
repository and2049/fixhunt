function outer() {
  'use strict';
  if (true) {
    var x = 1;
  }
  function inner() {
    console.log(typeof x);
  }
  inner();
}
outer();
