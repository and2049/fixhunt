let x = 0;
function f() {
  if (false) { return; }
  x += 1; 
}
f();
console.log(x);
