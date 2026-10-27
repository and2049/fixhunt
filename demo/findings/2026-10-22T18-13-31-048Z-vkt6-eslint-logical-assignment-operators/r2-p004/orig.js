for (var i = 0; i < 2; i++) {
  var x = 0;
  x = x || i;
  console.log('loop:', x);
}
console.log('after:', x);
var x = 99;
console.log('redeclared:', x);
