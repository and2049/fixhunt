function test() {
  LABEL: const val = { valueOf: () => 42, toString: () => 'hello' };
  console.log(+val);
  console.log(`${val}`);
}
test();
