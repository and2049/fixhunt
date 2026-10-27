const obj = { m() { return this.val + "\251"; }, val: 'X' };
const fn = obj.m;
console.log(fn.call(obj));
console.log(obj.m());
