const re = /foo {2}| {2}bar/;
console.log(re.test('foo'));
console.log(re.test('  bar'));
console.log(re.test('foobar'));
