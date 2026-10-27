function outer() {
  var RegExp = Array;
  function inner() {
    var re = new RegExp('x', '');
    console.log(re instanceof RegExp);
  }
  inner();
}
outer();
