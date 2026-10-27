outer:
for (let i = 0; i < 2; i++) {
  try {
    const arr = Array(i, i + 1);
    if (arr[0] === 0) break outer;
    console.log('loop', arr);
  } finally {
    console.log('finally', i);
  }
}
console.log('done');
