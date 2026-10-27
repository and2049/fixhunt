LOOP: class C {
  static field = 1;
  #private = 2;
  static { console.log('static'); }
  constructor() { console.log(super ? 'has super' : 'no super'); }
}
new C();
