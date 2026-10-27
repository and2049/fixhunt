let callCount = 0;
const obj = {
  get value() {
    callCount++;
    return 42;
  }
};
if (obj.value) {
  // first call
}
if (obj.value) {
  // second call after fix
}
console.log('Getter called:', callCount);
