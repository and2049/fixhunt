outer: for (let i = 0; i < 2; i++) {
  for (let j = 0; j < 2; j++) {
    if (i === 1) { break outer; } else {
      break; // inner break
    }
  }
}
console.log('escaped');
