const obj = {
  value: 42,
  check: function() {
    return /[=]/.test(this.value.toString());
  },
  checkArrow: () => /[=]/.test(this.value.toString())
};
console.log(obj.check());
console.log(obj.checkArrow());
const fn = obj.check;
console.log(fn());
