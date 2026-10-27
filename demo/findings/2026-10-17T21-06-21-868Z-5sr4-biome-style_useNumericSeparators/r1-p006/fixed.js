class C {
  instance = 12_345;
  static staticVal = 67_890;
  #private = 11_111;
  constructor() { console.log(this.instance, C.staticVal, this.#private); }
}
new C();
