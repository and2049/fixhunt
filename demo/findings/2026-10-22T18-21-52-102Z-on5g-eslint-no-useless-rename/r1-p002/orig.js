const arr = Array(3);
arr[1] = 9;
let { 1: 1 } = arr;
console.log(arr[1]); // Should be 9 if fix works correctly
