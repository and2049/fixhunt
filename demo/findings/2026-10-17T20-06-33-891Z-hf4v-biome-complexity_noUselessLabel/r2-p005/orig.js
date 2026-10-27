"use strict";
try {
  label: function f() { return 1; };
  console.log(typeof f);
} catch (e) {
  console.log(e.name, e.message);
}
