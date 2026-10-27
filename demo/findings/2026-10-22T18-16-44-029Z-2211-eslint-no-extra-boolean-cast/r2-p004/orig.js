"use strict";
function f() {
  return !!arguments.callee;
}
try {
  const r = f();
  console.log(r);
} catch (e) {
  console.log(e.name, e.message);
}
