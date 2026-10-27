function test() {
  try {
    console.log(typeof x); // 'undefined' due to hoisting
    var y = 1, x;
    return typeof x;
  } catch (e) {
    return e.name + ': ' + e.message;
  }
}
console.log(test());
