for (var i = 0; i < 2; i++) {
  var obj = {value: i};
  const copy = Object.assign({}, obj);
  obj.value += 10;
  console.log(copy.value)
}
