let x = 0;
let a = !!x; // triggers rule: x?true:false -> should become x
console.log('a:', a, '(type:', typeof a + ')');
// If rewritten as 'let a = x;' by unsafe fix, a would be 0, not false
