const arr = Array(2);
arr[0] = /a/g;
console.log(arr[0].test('a'));
console.log(arr[1] === undefined ? 'hole' : arr[1]);
