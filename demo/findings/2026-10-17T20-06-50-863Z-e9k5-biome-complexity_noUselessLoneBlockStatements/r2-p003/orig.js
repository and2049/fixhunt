let x = 1;
switch (x) {
  case 1: {}; // block meant to isolate
  console.log('one');
  break;
  case 2:
    console.log('two');
}
// Prints 'one' both before and after fix, but after fix looks like fallthrough
