let x = 0;
function f() {
  if (false) { return; }
  else { x += 1; }
}
f();
console.log(x);
