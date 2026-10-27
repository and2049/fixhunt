class C {
  static r = /a/;
  static {
    console.log(C.r.test('a'));
  }
}
