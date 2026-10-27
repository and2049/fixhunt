class C {
  static { console.log('static'); }
  static f() { }
  static get p() { return 1; }
}
console.log(C.p);
C.f();
