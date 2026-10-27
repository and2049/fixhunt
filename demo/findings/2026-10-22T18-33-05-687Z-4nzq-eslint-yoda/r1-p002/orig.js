function test() {
  if (5 > count) {       // rule fires: swap to count > 5
    var count = 3;
    return 'inside';
  }
  var count = 10;
  return 'outside';
}
console.log(test());
