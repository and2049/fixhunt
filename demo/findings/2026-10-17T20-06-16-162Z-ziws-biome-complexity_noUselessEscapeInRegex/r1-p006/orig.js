const re = /[\\s]/;
console.log(re.test('\\')); // true before fix: matches literal backslash
console.log(re.test('s'));    // false before fix
console.log(re.test(' '));    // false before fix: space not matched
// After fix: /[\s]/ → matches any whitespace
// So we test space to see if it starts matching
console.log('After fix simulation:', /[\s]/.test(' ')); // true → behavioral change
