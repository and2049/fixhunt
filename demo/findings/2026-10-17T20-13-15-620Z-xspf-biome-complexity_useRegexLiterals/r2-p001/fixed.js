try {
  console.log(/a/xy.test(''));
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
