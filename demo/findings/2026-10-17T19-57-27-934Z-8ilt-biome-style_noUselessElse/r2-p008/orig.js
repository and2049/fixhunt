let obj = null;
if (false) {}
else {
  console.log(obj?.prop ?? 'default');
}
// After fix, if obj is reassigned later, timing matters
obj = { prop: 'present' };
