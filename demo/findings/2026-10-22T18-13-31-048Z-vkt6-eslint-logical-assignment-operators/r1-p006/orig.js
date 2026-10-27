let i = 0;
function next() { return i++; }
const arr = [0, 0];
arr[next()] = arr[next()] || 42;
console.log('i:', i, 'arr:', arr);
