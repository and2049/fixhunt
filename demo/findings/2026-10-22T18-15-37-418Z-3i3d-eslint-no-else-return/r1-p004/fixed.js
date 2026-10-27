function process(data) {
  outer: for (let i = 0; i < 3; i++) {
    if (data[i] === undefined) { continue outer; }
    if (data[i] === null) {    // Trigger point
      return i * 2;            // Returns from loop
    }                          
                         // Hazard: else after return
      break outer;             // Breaks labeled loop
    
    console.log('skipped', i); // Should not print
  }
  return -1;
}
console.log(process([1, null, 3]));
