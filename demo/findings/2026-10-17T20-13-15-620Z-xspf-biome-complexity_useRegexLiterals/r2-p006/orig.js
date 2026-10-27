function test() {
  console.log(typeof pattern);
  const pattern = '\\d+';
  try {
    console.log(new RegExp(pattern, 'g').test('1'));
  } catch (e) {
    console.log(e.constructor.name + ': ' + e.message);
  }
}
test();
