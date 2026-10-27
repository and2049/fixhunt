const arr = Array(3);
arr[1] = 2.5;
console.log('Length:', arr.length);
for (let i = 0; i < arr.length; i++) {
  const val = arr[i];
  if (val !== undefined) {
    console.log(`idx ${i}: ${val.toFixed()}`);
  } else {
    console.log(`idx ${i}: hole`);
  }
}
const arrLike = { '0': 1.1, '1': 2.9, length: 2 };
console.log(Array.from(arrLike).map(x => x.toFixed()).join(','));
