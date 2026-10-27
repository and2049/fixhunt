const actual = "a\251b";
const expected = "a\u00A9b"; // pre-fix source would differ
console.log(actual === expected ? 'equal' : 'not equal', '|', actual, '|', expected);
