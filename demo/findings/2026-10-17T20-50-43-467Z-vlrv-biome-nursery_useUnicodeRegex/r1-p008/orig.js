function f() {
  for (let i = 0; i < 2; i++) {
    if (i === 0) {
      var r = /a/;
    }
    console.log(r.test('a'));
  }
}
f();
