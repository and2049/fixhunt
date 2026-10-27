let obj = {};
Object.defineProperty(obj, 'prop', {
  get() {
    console.log('getter called');
    return 0;
  }
});
if (obj.prop) { // triggers rule, calls getter once
  console.log('truthy');
} else {
  console.log('falsy');
}
