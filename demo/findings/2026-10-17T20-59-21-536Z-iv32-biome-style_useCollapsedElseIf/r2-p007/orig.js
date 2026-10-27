let count = 0;
outer:
if (false) {
} else {
  while (count < 2) {
    if (count === 0) {
      count++;
      continue outer;
    }
    console.log('inner', count); // should print 'inner 1'
    break;
  }
}
console.log('done', count); // should be 'done 2'
// After fix: else if(false) { ... } -> label 'outer' still valid, continue works
