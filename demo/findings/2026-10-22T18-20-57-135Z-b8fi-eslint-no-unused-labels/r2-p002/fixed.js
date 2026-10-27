function test() {
  let x = 99;
  {
    let x = 5;
    console.log(x); // should be 5
  }
  console.log(x); // should be 99
}
test();
