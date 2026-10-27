const arr = Array(3); arr[1] = 'a';
while (arr.length > 1) {
  console.log(arr.length);
  arr.pop();
}
console.log('end')
