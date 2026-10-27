function outer() {
  let RegExp = class {};
  try {
    console.log(new RegExp('a', 'g').test('a'));
  } catch (e) {
    console.log(e.constructor.name + ': ' + e.message);
  }
}
outer();
