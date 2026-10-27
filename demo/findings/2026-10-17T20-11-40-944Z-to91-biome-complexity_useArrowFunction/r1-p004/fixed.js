const arr = Array(3);
arr[0] = 10;
arr[2] = 30;
const result = arr.map((v) => v === undefined ? -1 : v * 2);
console.log(result.join(','));
