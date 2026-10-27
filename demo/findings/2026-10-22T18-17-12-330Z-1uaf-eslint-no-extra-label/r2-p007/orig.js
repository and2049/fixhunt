class C {
  F: {
    instanceField = 1;
    break F;
  }
  static getValue() { return new C().instanceField; }
}
console.log(C.getValue());
