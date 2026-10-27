class C {
  static staticField;
  static {
    let tmp = { prop: 1 };
    C.staticField = Object.prototype.hasOwnProperty.call(tmp, 'prop') ? 'yes' : 'no';
  }
  instanceField = Object.hasOwn(C.prototype, 'instanceField') ? 1 : 0;
}
console.log(C.staticField);
console.log(new C().instanceField);
