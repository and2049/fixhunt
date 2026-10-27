function test(arr) {
  return arr.length === 3 && Number.isNaN(arr[1]);
}

// Create sparse array via direct assignment to index 2
let a = [];
a[2] = 1; // Creates hole at index 0,1 -> [empty × 2, 1]
console.log('Direct:', test(a));

// Recreate using pattern rule flags: explicit undefined then assignment
let b = [];
b[0] = undefined; // Rule triggers here
b[2] = 1;
console.log('After undefined assign:', test(b)); // Should differ due to hole vs undefined
