const spacer = '  ';
const pat = new RegExp('foo' + spacer + 'bar');
console.log(pat.test('foo  bar') ? 'ok' : 'bad');
