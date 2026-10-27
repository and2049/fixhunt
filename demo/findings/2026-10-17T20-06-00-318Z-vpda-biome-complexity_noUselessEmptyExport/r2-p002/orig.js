const arr = new Array(3);
arr[1] = 'hole';
export {};
console.log(arr.length, arr[0] === undefined, arr[1] === 'hole', arr[2] === undefined);
