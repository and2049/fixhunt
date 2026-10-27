// Hazard 8
'use strict';
function f() {
  export { arguments }; // invalid, but we avoid syntax error by not actually exporting
  return arguments;
}
try {
  f();
} catch (e) {
  console.log(e.name);
}
