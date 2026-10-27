function test() {
  console.log(typeof _this);
  var _this = this;
}
try {
  console.log(test.call({value: 'ok'}));
} catch (e) {
}
