let y = 1
if (y) { return; } else {
  (function(){ y = 2; })()
}
console.log(y)
