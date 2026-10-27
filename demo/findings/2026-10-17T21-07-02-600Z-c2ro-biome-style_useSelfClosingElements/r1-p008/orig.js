const arr = Array(3);
arr[1] = <hole></hole>;
console.log(arr.length, arr[0] === undefined, arr[1] !== undefined);
