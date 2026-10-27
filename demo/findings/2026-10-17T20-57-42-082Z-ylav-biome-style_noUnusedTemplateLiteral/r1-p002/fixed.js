const pattern = "\\d"; // actually '\d' due to double escaping
const re = new RegExp(pattern, 'ug');
console.log(re.test('a')); // false
console.log(re.test('1')); // true
// rule does NOT fire because pattern has backslash -> escaped char
