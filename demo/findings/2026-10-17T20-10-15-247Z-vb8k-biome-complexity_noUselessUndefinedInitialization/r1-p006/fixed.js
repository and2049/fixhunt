let log = '';
function mark() { log += 'called'; return undefined; }

for (let i = 0, j = mark(); i < 2; i++) { // Rule does NOT trigger (not isolated undefined)
  log += `-i${i}-j${j}`;
}
console.log('Log (should show call):', log);

// Separate test: isolated undefined in comma decl
log = '';
for (let i = 0; i < 1; i++) {
  let a , b = 1; // Rule triggers on a
  log += `a${a}b${b}`;
}
console.log('After fix equivalent:', log);
