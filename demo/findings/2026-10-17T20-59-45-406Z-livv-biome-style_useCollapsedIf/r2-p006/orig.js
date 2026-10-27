// Hazard 7: falsy outer skips inner
let called = false;
function side() {
  called = true;
  return true;
}
if (false) {
  if (side()) {
    // should not run
  }
}
console.log('side called:', called);
