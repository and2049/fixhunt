(function() {
  'use sloppy';
  let obj = {prop: prop};
  let prop = 99;
  with (obj) {
    console.log(prop);
  }
})();
