const obj = {
  get value() {
    console.log('getter called');
    return 42;
  }
};
if (!!obj.value) {
  console.log('value:', obj.value);
}
