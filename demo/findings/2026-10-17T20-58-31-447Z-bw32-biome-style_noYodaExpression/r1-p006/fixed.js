let callCount = 0;
const obj = {get val() { callCount++; return 'blue'; }};
let a = true;
if (a && obj.val != "red" ) {
  console.log('unequal');
}
console.log('Calls after first:', callCount);
a = true;
if (a && obj.val != "red") {
  console.log('unequal swapped');
}
console.log('Calls after second:', callCount);
