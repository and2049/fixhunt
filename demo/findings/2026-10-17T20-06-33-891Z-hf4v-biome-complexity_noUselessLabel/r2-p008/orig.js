function test() {
  console.log(typeof x); // TDZ if not initialized
  label: let x = 1;
  console.log(x);
}
test();
