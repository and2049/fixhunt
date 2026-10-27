try {
  console.log(new RegExp('a', 'xy').test(''));
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
