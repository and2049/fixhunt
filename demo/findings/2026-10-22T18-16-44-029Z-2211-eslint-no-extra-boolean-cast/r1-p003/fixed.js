const arr = Array(3);
arr[1] = false;
if (arr[0]) console.log('truthy'); else console.log('falsy'); // hole -> undefined
console.log(arr.length);
