class Base { constructor() { this.base = true; } getVal() { return '\251'; } }
class Derived extends Base { #pri = 42; str = super.getVal(); getStr() { return this.str + this.#pri; } }
const d = new Derived();
console.log(d.getStr());
