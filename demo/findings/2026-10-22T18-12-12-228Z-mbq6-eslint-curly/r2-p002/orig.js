let n = 0
function g() {
  if (n < 2)
    console.log('a')
    (function(){ n++; return })()
}
g();
g();
console.log(n)
