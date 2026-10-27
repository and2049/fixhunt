(function f() {
  with ({x: 1}) {
    console.log(x);
  }
});
