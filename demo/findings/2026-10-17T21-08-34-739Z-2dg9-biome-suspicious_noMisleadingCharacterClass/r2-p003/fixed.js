const re = /^[👶🏻]$/u;
console.log(re.test('👶🏻')); // Should be true
// After fix: /^[👶]$/u → matches high surrogate only, false
console.log(/^[👶]$/u.test('👶🏻'));
