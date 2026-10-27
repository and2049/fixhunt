const arr = Array(3);
arr[1] = 'a';
const obj = Object.assign({}, arr);
console.log(obj.length, obj[0], obj[1], obj[2]);
