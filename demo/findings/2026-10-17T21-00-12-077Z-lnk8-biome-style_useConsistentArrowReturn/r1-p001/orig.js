const pattern = 'ab';
const matchIt = s => {
  return new RegExp(pattern, 'u').test(s);
};
console.log(matchIt('áb'));
