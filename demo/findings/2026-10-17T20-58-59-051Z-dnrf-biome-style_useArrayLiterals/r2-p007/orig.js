function Base() {}
Base.prototype = Array(1); // becomes [1]
const obj = new Base();
console.log(obj.length === 1 && obj[0] === 1 && typeof obj.push === 'function');
