class C {
  instance = 12345;
  static staticVal = 67890;
  #private = 11111;
  constructor() { console.log(this.instance, C.staticVal, this.#private); }
}
new C();
