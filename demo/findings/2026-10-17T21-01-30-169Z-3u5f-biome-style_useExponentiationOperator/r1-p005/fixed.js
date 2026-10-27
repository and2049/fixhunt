class C {
  static pow = 2 ** 3;
  static {
    console.log('Static block:', C.pow); // Expected: 8
  }
  get value() {
    return this.prop ** 2;
  }
}
const inst = new C();
inst.prop = 4;
console.log('Instance value:', inst.value); // Expected: 16
// All Math.pow calls should fire and be fixed correctly
