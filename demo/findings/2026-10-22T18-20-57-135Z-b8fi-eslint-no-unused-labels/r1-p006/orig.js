const obj = {
  method: function() {
    LABEL: return () => this;
  }
};
const fn = obj.method();
console.log(fn() === obj);
