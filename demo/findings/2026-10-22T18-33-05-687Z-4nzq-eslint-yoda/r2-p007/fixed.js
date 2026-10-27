let callCount = 0;
const obj = {
  get val() {
    callCount++;
    return 42;
  }
};
if (obj.val === 42) { // triggers yoda: 42 === obj.val
  console.log('first:', callCount); // 1
}
callCount = 0;
if (obj.val === 42) { // would be fix
  console.log('second:', callCount); // 1
}
