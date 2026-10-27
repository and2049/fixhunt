function test() {
  try {
    console.log(typeof x);
    ({ x: 1});
    let x;
  } catch (e) {
    console.log(e.name);
  }
}
test();
