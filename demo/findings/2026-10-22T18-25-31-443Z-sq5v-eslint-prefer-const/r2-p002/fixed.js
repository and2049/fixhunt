class C {
  static {
    const x = 1;
    console.log('static init:', x);
  }
  constructor() { console.log('instance:', C.x ?? 'undefined'); }
}
new C();
