// This line would be invalid if fixed incorrectly
// Math.pow(1, 2, 3); // Rule does not fire (too many args)
// 1 ** 2 ** 3; // Would be SyntaxError if mistakenly generated
console.log('No trigger - comma in args invalid for Math.pow');
