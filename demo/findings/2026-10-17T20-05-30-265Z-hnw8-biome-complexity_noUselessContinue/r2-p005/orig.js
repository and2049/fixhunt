for (let i = 0; i < 1; i++) {
  console.log(i);
  continue;
}; // <-- semicolon after block
console.log('after'); // Should still run
// If fix removes continue, we have: } ; <-- empty stmt, but harmless
// To make it matter: put something sensitive after
let x = 1;
for (let i = 0; i < 1; i++) { x++; continue; }; // semicolon here
console.log(x); // Should be 2 regardless
