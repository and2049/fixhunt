const arr = Array(3);
arr[1] = 'present';
console.log('sparse length:', arr.length);
console.log('sparse [1]:', arr[1]);
const copy = Object.assign({}, arr); // triggers rule
console.log('copy length:', copy.length);
console.log('copy [1]:', copy[1]);
