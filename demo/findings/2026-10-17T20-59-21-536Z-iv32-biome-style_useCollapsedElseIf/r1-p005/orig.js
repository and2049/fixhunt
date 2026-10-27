let w = 0;
try {
  if (false) {} else {
    if (true) { throw new Error('test'); }
  }
} catch(e) {
  w = 1;
}
console.log(w); // Should be 1 due to caught exception
