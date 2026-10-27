for (var i = 0; i < 2; i++) {
  var obj = { x: i };
  Object.assign({}, obj);
}
console.log(typeof obj, obj.x);
