const arr = [];
arr[2] = 3;
console.log('arr[0]:', arr[0]); // undefined
let x = arr[0]; // rule does NOT trigger (index is not numeric literal)
console.log('x:', x); // undefined
console.log('arr:', JSON.stringify(arr)); // [,,3]
