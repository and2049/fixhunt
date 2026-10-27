const tokenRx = /^[👶🏻]$/u;
function validateId(s) { return tokenRx.test(s); }
function parseEmoji(s) { return s.match(tokenRx); }
console.log(validateId('👶🏻'), parseEmoji('👶🏻')[0]); // true 👶🏻
// After fix: tokenRx becomes /^[$/u -> invalid or matches nothing
// Actually: removing 👶🏻 from class leaves empty class -> error
// But per spec: [] is invalid, so let's avoid error by having other chars
// Rewrite to have backup:
const tokenRx2 = /^[👶🏻A]$/u; // now has two options
console.log(tokenRx2.test('👶🏻'), tokenRx2.test('A')); // true true
// After fix: becomes /^[A]$/u
console.log(tokenRx2.test('👶🏻')); // false after fix
