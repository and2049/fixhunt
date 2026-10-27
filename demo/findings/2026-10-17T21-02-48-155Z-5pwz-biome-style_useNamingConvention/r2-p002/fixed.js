class Base {
  method_name() {
    return 'base';
  }
  call() {
    return this['method_name']();
  }
}
class Derived extends Base {
  method_name() {
    return 'derived';
  }
}
console.log(new Derived().call());
