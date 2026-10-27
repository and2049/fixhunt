function test() {
  const arr = [];
  for (let i = 0; i < 3; i++) {
    let val = undefined;
    if (i !== 1) arr[i] = val;
  }
  console.log(arr.length, arr[1]);
}
test();
