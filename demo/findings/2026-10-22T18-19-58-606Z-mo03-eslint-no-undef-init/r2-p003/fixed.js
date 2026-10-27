function f() {
  var x = undefined;
  console.log('first:', x === undefined ? 'undef' : x);
  var x;
  console.log('second:', x === undefined ? 'undef' : x);
  x = 5;
  console.log('third:', x);
}
f();
