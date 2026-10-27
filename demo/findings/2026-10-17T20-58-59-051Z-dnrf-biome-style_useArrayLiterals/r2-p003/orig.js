const x = { valueOf: () => 42 };
const arr = Array(x);
console.log(arr.length === 1 && arr[0] === 42);
