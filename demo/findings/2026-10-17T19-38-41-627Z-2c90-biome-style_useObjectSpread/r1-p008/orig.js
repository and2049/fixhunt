for (var i = 0; i < 2; i++) {
  var obj = { x: i };
  if (i === 0) {
    var copied = Object.assign({}, obj);
  }
  obj.x = 99;
}
console.log('copied.x:', copied.x);
