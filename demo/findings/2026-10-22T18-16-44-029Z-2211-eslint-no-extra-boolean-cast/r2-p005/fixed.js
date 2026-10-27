const arr = Array(3);
arr[1] = 0;
let sum = 0;
for (let i = 0; i < arr.length; i++) {
  if (arr[i]) sum += arr[i];
}
console.log(sum);
