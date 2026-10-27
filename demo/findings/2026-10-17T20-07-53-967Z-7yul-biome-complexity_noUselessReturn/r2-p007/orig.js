class C {
  static { console.log('static'); }
  static f() { return; }
  static get p() { return 1; }
}
console.log(C.p);
C.f();
