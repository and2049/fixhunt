"use strict";
FUNC: function f() { return 42; }
try {
  console.log(f());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
