const arr = Array(3);
arr[1] = 'present';
for (let i = 0; i < 3; i++) {
  if (i in arr) {
    console.log('has', arr[i]);
  } else {
    if (i === 0) {
      console.log('hole at', i);
    }
  }
}
