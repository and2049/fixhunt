class C {
  static s = { prop: 'static' };
  inst = { prop: 'instance' };
  getProp() {
    const x = this.inst.prop; // rule triggers
    return x;
  }
}
const c = new C();
console.log(c.getProp()); // instance
console.log(C.s.prop); // static
