function test() {
  lbl: for (var i = 0; i < 2; i++) {
    console.log('i:', i);
    if (i === 0) break lbl;
  }
  var i = 99;
  console.log('after loop i:', i);
}
test();
