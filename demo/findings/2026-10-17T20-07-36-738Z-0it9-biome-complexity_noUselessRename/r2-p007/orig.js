let arr = Array(3);
arr[1] = 'hole';
let {1: v, 1: v} = arr;
console.log('v1:', v, 'v2:', v, 'length:', arr.length, 'has hole:', !(0 in arr));
