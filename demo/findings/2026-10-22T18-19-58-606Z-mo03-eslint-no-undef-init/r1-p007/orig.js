class Base { constructor() { this.flag = true; } }
class Derived extends Base {
  constructor() {
    super();
    let x = undefined; // removed
    console.log(this.flag);
    this.flag = false;
  }
}
new Derived();
