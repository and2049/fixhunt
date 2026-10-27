class Base { constructor() { this.x = 1; } static y = 2; }
class Derived extends Base { #z = 3; static { console.log('static block'); }
  getZ() { return this.#z + super.x; }
  process() { return [this].map(i => [i.getZ()]).flat(); }
}
const d = new Derived();
console.log('process result:', d.process());
d.process(); // expect_trigger
