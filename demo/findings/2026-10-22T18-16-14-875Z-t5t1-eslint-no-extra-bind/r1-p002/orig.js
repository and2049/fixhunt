class C {
  prop = function () {
    return this.x;
  }.bind({x: 1});
}
const c = new C();
console.log(c.prop());
