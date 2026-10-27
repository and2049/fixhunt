const arr = [, 1]; // hole at index 0
let target = {};
const val = arr[0] || false;
target.prop = val;
console.log('Stored value:', target.prop, typeof target.prop);
// After fix: target.prop = arr[0]; → stores undefined
