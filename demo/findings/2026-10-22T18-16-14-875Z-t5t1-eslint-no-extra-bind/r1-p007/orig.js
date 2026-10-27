const obj = {};
Object.defineProperty(obj, 'prop', {
  get() {
    this.accessed = true;
    return 42;
  }
});
const p = function () {
  return this.prop;
}.bind(obj);
p();
console.log(obj.accessed ? 'yes' : 'no');
