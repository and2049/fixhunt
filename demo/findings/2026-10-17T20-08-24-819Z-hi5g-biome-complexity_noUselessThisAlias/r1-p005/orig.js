function outer() {
  var self = this;
  return () => self;
}
const f = outer.call({x:1});
try {
  console.log(f().x);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
