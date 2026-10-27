const arr = Array(3);
arr[1] = /=/.test('x');
console.log(arr.map((v, i) => v === undefined ? 'hole' : v));
