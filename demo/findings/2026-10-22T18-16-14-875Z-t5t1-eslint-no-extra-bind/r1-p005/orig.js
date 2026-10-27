for (var i = 0; i < 2; i++) {
  var g = function () {
    return i;
  }.bind(null);
}
console.log(g());
