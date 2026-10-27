let x = 0.5;
if (0 <= x && x < 1) { // triggers yoda on 0 <= x
  console.log('in range'); // should print
} else {
  console.log('out');
}
x = 1.5;
if (0 <= x && x < 1) {
  console.log('in range');
} else {
  console.log('out'); // should print
}
