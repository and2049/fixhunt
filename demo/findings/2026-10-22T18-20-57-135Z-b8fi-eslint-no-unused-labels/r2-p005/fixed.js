{
  const arr = Array(3);
  arr[1] = 'present';
  console.log(arr.length); // 3
  console.log(arr[0]); // undefined (hole)
  console.log(arr[1]); // 'present'
}
