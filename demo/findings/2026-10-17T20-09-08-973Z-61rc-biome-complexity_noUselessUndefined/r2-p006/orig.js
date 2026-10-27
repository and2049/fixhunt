class C {
  static field = undefined;
  static {
    console.log(C.field);
  }
  method() {}
}
// No output expected from rule, but static block runs
