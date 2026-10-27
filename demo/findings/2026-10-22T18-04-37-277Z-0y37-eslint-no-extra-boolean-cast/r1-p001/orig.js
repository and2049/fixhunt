function f() {
  var x = false;
  for (var i = 0; i < 2; i++) {
    var x = !!(i % 2); // redeclaration + !! triggers rule
    console.log(x);
  }
}
f();
