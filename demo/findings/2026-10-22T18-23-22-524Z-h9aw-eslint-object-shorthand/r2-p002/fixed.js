let result = '';
for (let i = 0; i < 2; i++) {
  var x = i;
  let obj = {x}; // triggers rule
  result += obj.x;
}
console.log(result);
// After first iteration: x=0, obj={x:0} -> result='0'
// After second: x=1 (same var), obj={x:1} -> result='01'
