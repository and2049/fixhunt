let count = '3';
console.log(count < 5 ? 'gt' : 'le'); // NOT yoda trigger: 5 > '3' -> true
// Rule does not fire because fix would change operator direction
// Output remains deterministic regardless
count = '10';
console.log(count < 5 ? 'gt' : 'le');
