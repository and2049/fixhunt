function sparseCheck(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === undefined) {  // Trigger: hole detection
      return sum;                // Returns early on hole
    }                            
                           // Hazard: else after return
      sum += arr[i] || 0;        // Would skip if rewritten poorly
    
  }
  return sum;
}
const sparse = [1, , 3];         // Hole at index 1
console.log(sparseCheck(sparse));
console.log(sparseCheck([1,2,3]));
