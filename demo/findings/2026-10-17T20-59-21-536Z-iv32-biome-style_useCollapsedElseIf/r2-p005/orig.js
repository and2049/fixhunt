class Base {
  static staticVal = 100;
}
if (false) {
} else {
  class Derived extends Base {
    static staticVal = 200;
    static {
      console.log(Base.staticVal + Derived.staticVal); // 100 + 200 = 300
    }
  }
}
// After fix: else if(false) { ... } -> static block still runs in same scope
// So output is 300
