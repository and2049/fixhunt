var x = 1;
var objA = {x: x};
var objB = {x};
with (objA) {
  console.log(x); // logs 1 from objA.x
}
with (objB) {
  console.log(x); // logs undefined because x not found (no property named 'x')
}
