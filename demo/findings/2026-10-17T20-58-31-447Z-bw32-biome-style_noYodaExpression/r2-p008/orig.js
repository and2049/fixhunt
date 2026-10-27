class Base {
  constructor() {
    if (\"base\" == this.kind) console.log('base match'); // rule triggers
  }
}
class Derived extends Base {
  kind = 'base';
}
new Derived();
