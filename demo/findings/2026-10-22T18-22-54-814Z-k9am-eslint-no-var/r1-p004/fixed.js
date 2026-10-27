(function () {
  let arr = Array(3); // creates [empty × 3]
  arr[0] = 'a';
  arr[2] = 'c';
  console.log(arr.length, arr.join(':'));
  let len = arr.length;
  console.log(len);
})()
