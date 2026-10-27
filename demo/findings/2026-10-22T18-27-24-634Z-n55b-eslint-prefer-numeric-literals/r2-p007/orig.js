const obj = {
  val: 5,
  getNum: function() { return parseInt('101', 2); } // triggers rule: rewrite to 0b101 = 5
};
const fn = obj.getNum;
console.log('obj.getNum():', obj.getNum()); // this bound to obj, but unused -> 5
console.log('fn():', fn()); // this is global -> still 5 (no this use)
// Need to use this in the parsed value? Not possible.
// Instead, make the string depend on this? No, string is literal.
// Alternative: use this in a way that if rewritten, affects something else.
// Actually, the value is same. Must rely on side effect.
// Let's make the parseInt call have a side effect via getter.
const obj2 = {
  get str() { return '101'; },
  getNum: function() { return parseInt(this.str, 2); }
};
console.log('obj2.getNum():', obj2.getNum()); // '101' -> 5
// After fix: still 5
// Not showing difference. Abandon this hazard for now and use a working one.
// Switch to label/break hazard which we know works.
