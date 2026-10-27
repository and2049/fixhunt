// Hazard 2: break target change
let sum = 0;
outer:
for (let i = 0; i < 2; i++) {
  if (i === 0 && true) {
      break outer;
    }
  sum += i;
}
console.log('sum:', sum);
