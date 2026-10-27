function f() {
  for (var i = 0; i < 2; i++) {
    if (\"test\" == x) console.log('match'); // rule triggers here
    var x = i;
  }
  console.log('x:', typeof x);
}
f();
