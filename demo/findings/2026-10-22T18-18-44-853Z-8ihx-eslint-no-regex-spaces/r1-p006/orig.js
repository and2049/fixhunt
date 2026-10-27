function scopeTest() {
  if (true) {
    var v = 1;
    if (/pattern{1,3}   tail/.test('patternxx   tail')) v = 2;
    {
      var v = 3;
      console.log(v);
    }
  }
}
scopeTest();
