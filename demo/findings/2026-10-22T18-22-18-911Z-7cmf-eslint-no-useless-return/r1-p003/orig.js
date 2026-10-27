const obj = {
  get prop() {
    console.log('getter entered');
    return; // TRIGGER: explicit undefined
  }
};
console.log(obj.prop); // logs 'getter entered', then undefined
// If return removed, still undefined
// To show difference: compare with actual return value
const obj2 = {
  get prop() {
    console.log('getter2 entered');
    return 42;
  }
};
console.log(obj2.prop); // 42
// Now test: if someone expects value, but gets undefined
try {
  const val = obj.prop;
  if (val === undefined) console.log('got undefined as expected');
  else console.log('unexpected:', val);
} catch (e) {
  console.log('error:', e);
}
