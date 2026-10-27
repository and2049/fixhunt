class Base {
  constructor() {
    this.baseVal = this.compute();
  }
  compute() { return 1; }
}
class Derived extends Base {
  val = this.compute();
  compute() { return this.baseVal + 1; }
  render() {
    return <span open>{this.val}</span>;
  }
}
console.log(new Derived().render());
