class Base {
  constructor() {
    this.pub = 1;
  }
}
class Derived extends Base {
  #priv = 2;
  static staticVal = 3;
  get obj() {
    return {
      pub: this.pub,          // triggers rule
      priv: this.#priv,
      static: Derived.staticVal
    };
  }
}
const d = new Derived();
console.log(d.obj.pub, d.obj.priv, d.obj.static);
