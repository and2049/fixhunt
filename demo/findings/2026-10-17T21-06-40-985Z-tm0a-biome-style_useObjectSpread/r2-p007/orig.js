let obj = {x: 1};
if (true) {
  let obj = {y: 2}; // inner obj
  Object.assign({}, obj); // triggers rule, copies inner {y:2}
  console.log('inner:', obj.y);
}
console.log('outer:', obj.x); // outer obj unchanged
