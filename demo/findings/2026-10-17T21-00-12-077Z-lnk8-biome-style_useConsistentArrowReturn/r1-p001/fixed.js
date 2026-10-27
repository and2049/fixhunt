const pattern = 'ab';
const matchIt = s => new RegExp(pattern, 'u').test(s);
console.log(matchIt('áb'));
