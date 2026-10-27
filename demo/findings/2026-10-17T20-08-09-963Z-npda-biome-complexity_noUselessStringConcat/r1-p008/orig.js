// Hazard 8: Class with private field and static block
class Test {
  #private = \"secret\";
  static {
    console.log(\"static\" + \" block\");
  }
  constructor() {
    console.log(\"instance\" + \" created\");
  }
}
new Test();
