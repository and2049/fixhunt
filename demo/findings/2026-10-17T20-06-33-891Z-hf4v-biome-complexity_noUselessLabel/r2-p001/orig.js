function test() {
  let result = [];
  label: for (let i = 0; i < 2; i++) {
    var x = i + 1;
    result.push(typeof x, x);
    if (i === 0) {
      var x = 99; // re-declaration in same function scope
    }
    break label;
  }
  console.log(result.join(' '));
}
test();
