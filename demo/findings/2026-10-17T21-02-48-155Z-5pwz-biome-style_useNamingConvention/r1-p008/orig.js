class Base {
  constructor() {
    this.baseProp = 'base';
  }
}
class Derived extends Base {
  static #privateStatic = 'secret';
  static {
    try { 
      console.log('static block:', Derived['#privateStatic']);
    } catch (e) {
      console.log('private static access failed:', e.name);
    }
  }
  #instanceField = 'instance';
  value = this.#instanceField;
  constructor() {
    super();
    this.derivedProp = 'derived';
  }
}
let d = new Derived();
console.log(d.baseProp, d.derivedProp, d.value);
