class Test {
  static x = 0;
  static {
    await/* mark */ page.locator('.static');
    Test.x = 1;
  }
}
console.log(Test.x);
