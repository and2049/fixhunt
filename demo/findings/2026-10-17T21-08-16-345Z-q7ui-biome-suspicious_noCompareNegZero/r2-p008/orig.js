class C {
  static field = -0;
  constructor() {
    if (C.field === -0) {
      console.log('static field is -0');
    }
  }
}
new C();
