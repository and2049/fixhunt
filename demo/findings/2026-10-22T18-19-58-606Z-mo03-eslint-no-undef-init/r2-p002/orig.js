class C {
  static #p;
  static {
    try { console.log(#p); } catch(e) { console.log('uninit'); }
    #p = 42;
    console.log(#p);
  }
}
new C();
