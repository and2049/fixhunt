const obj = {
  method: function() {
    return () => this;
  }
};
const fn = obj.method();
console.log(fn() === obj);
