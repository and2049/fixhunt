const arr = [];
arr[0] = /a  b/.test('a  b');
arr[2] = /x    y/.test('x    y');
console.log(arr.length, arr[0], arr[1], arr[2]);
