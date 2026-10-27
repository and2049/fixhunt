function f() {
  console.log(x); // Hazard: x used before init
  if (false) {
    return;
  }
    var x = 1;
  return x;
}
f();
