class Base {
  static "staticProp" = "base";
}
class Derived extends Base {
  static {
    console.log(this["staticProp"]); // reads rewritten literal
  }
  static "staticProp" = "derived";
}
