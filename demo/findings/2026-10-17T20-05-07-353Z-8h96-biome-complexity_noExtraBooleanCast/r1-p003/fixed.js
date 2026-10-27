let a = 0, b = 1;
console.log('Original:', (a && b) ? 1 : 0);
a = 2, b = 3;
console.log('Original:', (a && b) ? 1 : 0);
// After fix: (a && b) ? 1 : 0 would output 0 then 6 — demonstrating type shift
console.log('Fixed sim:', (a && b) ? 1 : 0); // Shows hazard: 0 becomes 0 (not 1)
