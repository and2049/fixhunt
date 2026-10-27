function test() {
  try {
    return a;
  } catch (e) {
    console.log(e.name);
  }
  let a;
}
test();
