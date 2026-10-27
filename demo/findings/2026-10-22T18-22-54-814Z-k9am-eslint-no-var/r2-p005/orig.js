function test() {
  if (false) {
    var x = 1;
  } else {
    return typeof x === 'undefined' ? 'undef' : x; // x hoisted, accessible
  }
}
console.log(test());
