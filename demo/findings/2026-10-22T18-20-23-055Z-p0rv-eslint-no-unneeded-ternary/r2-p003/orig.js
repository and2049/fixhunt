function test() {
  for (var i = 0; i < 2; i++) {
    var x = i ? i : 1;
    if (i === 0) {
      var x = 99;
    }
    console.log(`i=${i}, x=${x}`);
  }
  console.log('final x:', x);
}
test();
