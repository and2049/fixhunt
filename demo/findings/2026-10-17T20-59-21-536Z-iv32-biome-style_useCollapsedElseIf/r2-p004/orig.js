const obj = { val: 42, getVal: function() { return this.val; } };
const getVal = obj.getVal;
if (false) {
} else {
  const bound = getVal.bind(obj);
  console.log(bound()); // should be 42
}
// After fix: else if(false) { ... } -> bind still happens in same scope, obj captured
// So output remains 42
