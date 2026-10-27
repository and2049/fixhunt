// Hazard 5: debugger statement
let x = 0;
if (true) {
  if (false) {
    debugger;
    x = 1;
  }
}
console.log('x:', x);
