const arr = [1,,3]; // hole at index 1
let sum = 0;
for (let i = 0; i < arr.length; i++) {
  if (!(i in arr)) continue; // skip holes
  sum += arr[i];
}
console.log(sum); // Before fix: skips hole -> 4. After fix? Same logic.
// But if we remove a useless continue elsewhere...
for (let j = 0; j < 1; j++) {
  continue; // <-- fired, removed
}
console.log('sparse done', sum);
