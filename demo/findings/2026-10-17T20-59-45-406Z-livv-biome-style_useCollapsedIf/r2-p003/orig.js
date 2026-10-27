// Hazard 4: label and finally with break
let result = [];
loop:
for (let i = 0; i < 2; i++) {
  try {
    if (i === 0) {
      if (true) {
        break loop;
      }
    }
    result.push(i);
  } finally {
    result.push('finally');
  }
}
console.log(result.join(','));
