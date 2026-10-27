let i = 0;
function next() { return i++; }
const arr = [next(), next()];
console.log(arr);
