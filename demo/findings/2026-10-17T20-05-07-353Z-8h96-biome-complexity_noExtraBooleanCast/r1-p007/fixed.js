let x = 2;
outer: while (x) {
  console.log('Enter loop, x=', x);
  if (x === 2) { x = 0; continue outer; }
  console.log('After continue, x=', x);
  x--;
}
console.log('Loop exited, x=', x);
// Fix: while (x) would behave identically for numbers, but demonstrates !! in loop header
