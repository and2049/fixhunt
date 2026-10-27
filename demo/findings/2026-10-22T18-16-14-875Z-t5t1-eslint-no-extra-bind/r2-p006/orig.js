const regex = /\\u{1f600}/gu;
const test = (function () {
  return regex.lastIndex;
}).bind(null);
regex.test('😀');
console.log(test());
