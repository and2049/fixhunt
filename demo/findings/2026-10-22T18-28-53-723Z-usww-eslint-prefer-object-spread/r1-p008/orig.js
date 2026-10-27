class Base {
  static staticVal = 10;
  instanceVal = 20;
}
class Derived extends Base {
  static {
    Derived.staticVal = Base.staticVal * 2;
  }
  method() {
    return Object.assign({}, { staticVal: Derived.staticVal, instanceVal: this.instanceVal });
  }
}
const d = new Derived();
console.log(d.method().staticVal, d.method().instanceVal);
