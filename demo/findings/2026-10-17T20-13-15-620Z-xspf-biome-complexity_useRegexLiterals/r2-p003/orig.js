const maybePattern = null;
console.log((maybePattern ?? '\\d+').length);
try {
  console.log(new RegExp(maybePattern ?? '\\d+', 'g').test('1'));
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
