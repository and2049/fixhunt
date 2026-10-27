function f() {
  if (true) {
    return; /* keep */
  } else {
    // this comment should stay with g()
    g();
  }
}
function g() { console.log('g'); }
f();
