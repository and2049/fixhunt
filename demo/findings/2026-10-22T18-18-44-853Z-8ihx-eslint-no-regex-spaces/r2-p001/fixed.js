const arr = [];
arr[0] = /a {2}b/.test('a  b');
arr[2] = /x {4}y/.test('x    y');
console.log(arr.length, arr[0], arr[1], arr[2]);
