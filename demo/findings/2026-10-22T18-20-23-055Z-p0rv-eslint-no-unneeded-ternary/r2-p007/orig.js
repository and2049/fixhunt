const arr = [1, , 3];
let sumOrig = 0;
let sumFixed = 0;
for (let i = 0; i < arr.length; i++) {
  const val = arr[i] ? arr[i] : 0;
  sumOrig += val;
  const val2 = arr[i] || 0;
  sumFixed += val2;
}
console.log(`sumOrig=${sumOrig}, sumFixed=${sumFixed}`);
if (sumOrig !== sumFixed) {
  throw new Error(`Sparse array mismatch: ${sumOrig} !== ${sumFixed}`);
}
