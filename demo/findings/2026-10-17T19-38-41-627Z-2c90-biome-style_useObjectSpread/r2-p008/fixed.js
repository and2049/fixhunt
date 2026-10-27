const obj = {val: 1, getVal() { return this.val }};
const fn = obj.getVal;
console.log(fn.call(obj))
const copied = ({...obj,});
console.log(copied.getVal?.call(obj))
