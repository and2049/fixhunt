let obj = { prop: 5 };
// comment before bracket
let x = obj[\'prop\']; // comment after
console.log('x:', x);
// After fix, the inline comment may be lost if tool replaces whole token
// We detect by checking if a known comment pattern survives via function.toString
const fn = function() { /* ignore */ return obj[\'prop\']; };
console.log('has comment:', fn.toString().includes('comment after')); // may be false after fix
