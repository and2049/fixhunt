const arr = Array(3);
arr[1] = 'a';
console.log({ ...arr}); // { '1': 'a' }
console.log({ ...arr });             // { '1': 'a' }
// Both same for enum props, but test toString
arr.toString = () => 'custom';
console.log(String({ ...arr})); // [object Object]
console.log(String({ ...arr }));            // [object Object]
