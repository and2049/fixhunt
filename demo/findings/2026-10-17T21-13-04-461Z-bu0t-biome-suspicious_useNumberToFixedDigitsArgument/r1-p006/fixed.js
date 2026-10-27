class Base {
  #value = 3.14159;
  getFormatted() {
    return this.#value.toFixed();
  }
}
class Derived extends Base {
  static { console.log('static block'); }
  getFormatted() {
    return super.getFormatted() + ' derived';
  }
}
const d = new Derived();
console.log(d.getFormatted());
