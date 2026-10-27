let arr = new Array(3);
arr[1] = 'present';
let obj = {arr: arr};
console.log('length:', obj.arr.length);
console.log('0 in obj.arr:', 0 in obj.arr);
console.log('1 in obj.arr:', 1 in obj.arr);
console.log('2 in obj.arr:', 2 in obj.arr);
