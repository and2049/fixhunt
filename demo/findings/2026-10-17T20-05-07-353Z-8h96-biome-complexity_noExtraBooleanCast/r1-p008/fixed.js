const obj = { __proto__: { count: 0 } };
console.log('!!obj.count:', !!obj.count);
console.log('obj.count:', obj.count);
if (obj.count) {
  console.log('Truthy path')
} else {
  console.log('Falsy path: distinguishes absent (undefined) from present-but-false')
}
// Fix would remove !! in condition — making falsy existing props take falsy path
