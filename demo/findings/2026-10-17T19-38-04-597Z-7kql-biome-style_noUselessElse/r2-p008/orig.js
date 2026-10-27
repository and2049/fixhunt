const obj = {
  value: 42,
  getValue() {
    if (this === obj) return this.value;
    this.value = 99;
    return -1;
  }
};
const fn = obj.getValue;
console.log(fn()); // should return -1 (global this)
console.log(fn.call(obj)); // should return 42 then 99 on second call
console.log(fn.call(obj));
