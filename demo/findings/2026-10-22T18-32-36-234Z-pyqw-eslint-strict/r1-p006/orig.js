(function outer() {
  function inner() { return v; }
  var v = 1;
  console.log(inner());
  var v = 2;
  console.log(inner());
})();
