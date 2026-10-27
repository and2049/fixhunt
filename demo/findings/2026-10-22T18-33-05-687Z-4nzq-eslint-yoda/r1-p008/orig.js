let obj = { nested: { value: 42 } };
let mid = null;
let result = [];
function test() {
  if (mid?.nested === undefined && 0 < obj.nested.value) {   // rule fires on 0 < obj.nested.value : swap to obj.nested.value > 0
    result.push('branch-a');
  } else {
    result.push('branch-b');
  }
}
test();  // Original: mid?.nested is undefined (since mid=null), undefined === undefined → true
         //          and 0 < obj.nested.value (42) → true → branch-a
// Fixed: obj.nested.value > 0 is evaluated first? No, && leaves left-to-right.
//        Actually: swap only changes the comparison, not order of evaluation.
//        Original: (mid?.nested === undefined) && (0 < obj.nested.value)
//        Fixed:    (mid?.nested === undefined) && (obj.nested.value > 0) → same
// Make it: if (0 < obj.nested.value && mid?.nested === undefined)
test = () => {
  if (0 < obj.nested.value && mid?.nested === undefined) {   // rule fires on 0 < obj.nested.value : swap to obj.nested.value > 0
    result.push('branch-a');
  } else {
    result.push('branch-b');
  }
};
result = [];
test();  // Original: 0 < obj.nested.value (42) → true, then mid?.nested === undefined → true → branch-a
// Fixed: obj.nested.value > 0 → true, then mid?.nested === undefined → true → same
// Need: make second part have side effect that only runs if first is true
let accessLog = '';
obj = {
  get nested() {
    accessLog += 'nested-access';
    return { value: 42 };
  }
};
test = () => {
  if (0 < obj.nested.value && mid?.nested === undefined) {   // rule fires on 0 < obj.nested.value
    result.push('yes');
  }
};
result = [];
test();
console.log('access-log:' + accessLog + '|result:' + (result[0]||'none'));  // Original: accesses obj.nested → log+='nested-access', then checks mid?.nested
                                                                              // Fixed: same, because left operand of && is still obj.nested.value access
// Hazard only if the swapped expression is on the left of && and we rely on short-circuit skipping it
// Example: if (false && expensive()) {}  vs  if (expensive() && false) {} — but rule doesn't fire on false
// Make it: if (`red` === color && obj.prop)  ---  rule fires on left
obj = { prop: { get value() { accessLog += 'prop'; return 5; } } };
let color = 'blue';
test = () => {
  if (`red` === color && obj.prop.value > 0) {   // rule fires: swap to color === `red`
    result.push('in');
  }
};
result = [];
test();
console.log('access-log:' + accessLog + '|result:' + (result[0]||'none'));  // Original: `red` === 'blue' → false → short-circuit, skips obj.prop.value → log unchanged
                                                                              // Fixed: color === `red` → 'blue' === 'red' → false → same short-circuit
// Still no difference because equality is commutative.
// Conclusion: for primitive equality, swapping never changes truth value or short-circuit behavior.
// Instead, use non-commutative operator that rule doesn't touch, or accept that hazard is not applicable.
// Fallback: demonstrate that rule does not fire on nullish coalescing, so no swap occurs there.
console.log('null-undifferentiated');
