class C {
  static x = 1;
  #p;
  constructor() {
    this.#p = 0;
    if (false) { return; }
    this.#p = 2; 
  }
  get p() { return this.#p; }
}
const c = new C();
console.log(c.p);
