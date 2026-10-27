let total = 0;
const arr = [1, 2, 3, 4];
let i = 0;
while (i < arr.length) {
  if (arr[i] % 2 === 0) {
    total += arr[i];
    break;
  }
    i++;
}
console.log('total:', total, 'i:', i);
console.log('expected: total 1 i 1');
