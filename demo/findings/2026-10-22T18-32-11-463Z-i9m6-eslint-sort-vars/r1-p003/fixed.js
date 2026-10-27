function test() {
  try {
    console.log(typeof x); // 'undefined' due to hoisting
    var x, y = 1;
    return typeof x;
  } catch (e) {
    return e.name + ': ' + e.message;
  }
}
console.log(test());
