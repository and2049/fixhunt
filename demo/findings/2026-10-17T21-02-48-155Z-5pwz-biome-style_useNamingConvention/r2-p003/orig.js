"use sloppy";
let bad_form = 1;
with ({}) {
  bad_form = 2;
}
console.log(bad_form);
