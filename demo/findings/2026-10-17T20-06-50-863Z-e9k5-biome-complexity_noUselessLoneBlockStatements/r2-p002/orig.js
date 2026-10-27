let n = 0;
do { n++; } while (n < 3);
console.log('Iterations:', n);
// Before: 3 // After fix: infinite loop? No -- removed block makes body empty, but condition still runs. Actually: do ; while(...) is valid but does nothing -> n stays 0
