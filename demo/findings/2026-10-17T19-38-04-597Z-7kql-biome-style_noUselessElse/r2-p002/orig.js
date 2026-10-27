let x = 0;
function f(flag) {
  if (flag) return;
  x += 1;
}
f(true);
f(false);
f(false);
console.log(x);
