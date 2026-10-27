const re = /[=]🌟/gu;
re.lastIndex = 0;
console.log(re.test('a🌟b'));
re.lastIndex = 0;
console.log(re.exec('x🌟y'));
