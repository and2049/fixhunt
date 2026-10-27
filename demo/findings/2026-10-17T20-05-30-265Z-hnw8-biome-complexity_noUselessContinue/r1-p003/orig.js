const arr = Array(3);
arr[1] = 'present';
for (let i = 0; i < arr.length; i++) {
  if (!(i in arr)) { continue; }
  console.log('index:', i, 'value:', arr[i]);
}
