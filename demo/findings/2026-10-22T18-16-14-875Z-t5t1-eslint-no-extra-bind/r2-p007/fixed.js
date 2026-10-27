class Base {
  #x = 42;
  getX() { return this.#x; }
}
class Derived extends Base {
  getXBound = (() => this.getX());
}
const d = new Derived();
console.log(d.getXBound());
