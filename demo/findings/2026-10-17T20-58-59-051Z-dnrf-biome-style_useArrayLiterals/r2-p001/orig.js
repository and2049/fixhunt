let i = 0;
function next() { return i++; }
const arr = Array(next(), next());
console.log(arr);
