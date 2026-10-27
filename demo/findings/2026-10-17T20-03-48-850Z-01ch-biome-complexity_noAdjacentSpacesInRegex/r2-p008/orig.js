const re = /💩  💩/gu;
console.log('First:', re.test('💩  💩'));
console.log('lastIndex after:', re.lastIndex);
re.lastIndex = 0;
console.log('Second:', re.test('💩💩'));
