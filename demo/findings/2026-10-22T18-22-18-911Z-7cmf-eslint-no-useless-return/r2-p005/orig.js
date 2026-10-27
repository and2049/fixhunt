let obj = { prop: { value: 42 } };
function getValue() {
  return obj.prop?.value;
}
console.log(getValue()); // 42
obj = null;
console.log(getValue()); // null
// If getValue had explicit 'return;' at end, removing it doesn't change null
// But if return; was before null check, hazard appears — here we test baseline
