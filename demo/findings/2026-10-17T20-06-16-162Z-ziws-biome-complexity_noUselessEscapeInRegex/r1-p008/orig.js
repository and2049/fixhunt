const re = /\(foo\)/;
const str = '(foo)';
const match = str.match(re);
console.log(match ? match.length : 0); // Before fix: 1 (only full match)
                                       // After fix: /(foo)/ → 2 (full match + capture group 1)
