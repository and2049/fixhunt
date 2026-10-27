class B { constructor() { this.x = 1; } }
class D extends B {
  constructor() {
    super();
    if (true)
      this.y = 2;
  }
}
console.log(new D().y);
