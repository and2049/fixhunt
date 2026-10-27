class C {
  static { <static></static>; }
  #x = 1;
  method() { <inst></inst>; return this.#x; }
}
console.log(new C().method());
