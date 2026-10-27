(function () {
  // var counter /* inline comment */ = 0;
  var counter /* inline comment */ = 0;
  (function inner() {
    counter++;
    console.log(counter);
  })();
  console.log(counter);
})()
