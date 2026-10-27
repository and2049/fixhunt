class Test {
  #a_value = 42;
  method() {
    return this[#a_value];
  }
}
console.log(new Test().method());
