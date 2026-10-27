let fCalled = false;
if (false) {
  function f() { fCalled = true; }
} else {
  f();
}
console.log(fCalled);
