class C {
  static rx = /=/;
  m() { console.log(C.rx.test('x'));
  }
}
new C().m();
