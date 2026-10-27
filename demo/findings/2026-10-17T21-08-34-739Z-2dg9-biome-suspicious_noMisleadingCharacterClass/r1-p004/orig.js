// First version has comment inside class
const rx = /^[Á /* accented A */]$/;
console.log(rx.test('Á')); // true
// After fix: becomes /^[A /* accented A */]$/
// Still syntactically valid, but now tests for plain 'A'
console.log(rx.test('Á')); // false after fix
