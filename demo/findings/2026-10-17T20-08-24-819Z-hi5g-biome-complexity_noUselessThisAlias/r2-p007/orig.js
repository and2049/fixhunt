const obj = { method() { return this.val; }, val: 10 };
const self = obj;
function inner() {
  return self.method();
}
console.log(inner());
