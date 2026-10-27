(function () {
  // var counter /* inline comment */ = 0;
  let counter /* inline comment */ = 0;
  (function inner() {
    counter++;
    console.log(counter);
  })();
  console.log(counter);
})()
