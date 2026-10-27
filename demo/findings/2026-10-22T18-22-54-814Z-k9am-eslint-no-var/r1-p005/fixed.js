(function () {
  console.log(typeof x); // 'undefined' due to hoisting
  var x = 1;
  try {
    console.log(y); // ReferenceError if let/const
    var y = 2;
  } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
  console.log(x, y);
})()
