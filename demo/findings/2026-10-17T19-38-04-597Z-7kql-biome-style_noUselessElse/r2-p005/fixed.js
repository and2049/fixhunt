for (let i = 0; i < 2; i++) {
  if (i === 0) continue;
  var x = 10;
  console.log(x);
}
// After fix: var x hoisted and re-declared each loop -> still works but let's make it fail
// Let's force error by using same var in else that gets moved
let result = [];
for (let i = 0; i < 2; i++) {
  if (i === 0) continue;
  
    var x = i + 1;
    result.push(x);
}
console.log(result.join(','));
