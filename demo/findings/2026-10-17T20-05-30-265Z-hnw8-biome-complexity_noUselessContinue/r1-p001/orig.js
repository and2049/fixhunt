let x = 0;
do {
  if (x === 0) { x++; continue; }
  console.log('loop:', x);
} while (x < 2);
