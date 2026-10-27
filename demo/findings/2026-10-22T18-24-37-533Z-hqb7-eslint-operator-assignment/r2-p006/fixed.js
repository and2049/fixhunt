const obj = {
  x: 0,
  update: function() {
    this.x += 1;
  }
};
const fn = obj.update;
fn.call(obj);
console.log(obj.x);
