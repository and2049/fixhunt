const arr = Array(3); arr[1] = 'a';
for (; arr.length > 1;) {
  console.log(arr.length);
  arr.pop();
}
console.log('end')
