class Base {
  constructor() { this.x = 0; }
  method() { return this.x; }
}
class Der extends Base {
  #y = 5;
  static {
    Der.prototype.z = Der.prototype.z + 1; // TRIGGER
  }
  constructor() {
    super();
    this.#y = this.#y + 2; // TRIGGER
  }
  getY() { return this.#y; }
}
const d = new Der();
console.log('instance y:', d.getY(), 'static z:', Object.getPrototypeOf(d).z);
