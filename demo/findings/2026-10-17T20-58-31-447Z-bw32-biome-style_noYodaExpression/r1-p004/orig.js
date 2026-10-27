const scope = {x: 1};
let y = 2;
with (scope) {
  if ("x" == y) {
    console.log('matched in scope');
  } else {
    console.log('not matched in scope:', y);
  }
}
// Outside with, y is outer
if ("x" == y) {
  console.log('matched outer');
} else {
  console.log('not matched outer:', y);
}
