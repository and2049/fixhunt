for (let i = 0; i < 2; i++) {
  var x = parseInt('10', 2); // triggers rule: rewrite to 0b10 = 2
  if (i === 0) {
    var x = 99; // redeclaration in same scope
    console.log('Loop 0, x after redeclare:', x); // should be 99
  } else {
    console.log('Loop 1, x:', x); // after fix: x is 2 from rewritten parseInt
  }
}
console.log('Final x:', x);
