class C {
  static r = /a/u;
  static {
    console.log(C.r.test('a'));
  }
}
