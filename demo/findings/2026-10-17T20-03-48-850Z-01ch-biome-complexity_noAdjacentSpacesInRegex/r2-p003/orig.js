const re = /foo  |  bar/;
console.log(re.test('foo'));
console.log(re.test('  bar'));
console.log(re.test('foobar'));
