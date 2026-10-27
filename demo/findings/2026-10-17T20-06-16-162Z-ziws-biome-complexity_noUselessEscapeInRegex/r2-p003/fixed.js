const re = /[[\]]/;
console.log(re.test('[') + ',' + re.test(']') + ',' + re.test('a'));
