class Base {
  static static_base = 1;
  base_prop = 2;
  #private_base = 3;
  method() {
    return 'base';
  }
}
class Derived extends Base {
  static {
    Derived.static_derived = Base.static_base + 10;
  }
  derived_prop = 4;
  #private_derived = 5;
  method() {
    return super.method() + ' -> derived';
  }
}
const d = new Derived();
console.log('static_base:', Base.static_base);
console.log('static_derived:', Derived.static_derived);
console.log('base_prop:', d.base_prop);
console.log('derived_prop:', d.derived_prop);
console.log('method:', d.method());
