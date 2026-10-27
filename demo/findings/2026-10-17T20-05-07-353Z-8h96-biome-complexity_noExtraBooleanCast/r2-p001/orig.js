function test() {
  console.log(typeof foo);
  if (!!foo) {
    console.log('inside');
  }
  var foo;
}
test();
