let x = 1;
if (false) {
} else {
  let x = 2;
  console.log(x); // should be 2
}
console.log(x); // should be 1
// After fix: else if(false) { let x = 2; ... } -> x is block-scoped to else-if, outer x unchanged
