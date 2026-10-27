function commaTest() {
  var a , b = 1; // Rule triggers on a
  console.log('Initial:', typeof a, b);
  a = 'assigned';
  console.log('After reassignment:', a, b);
  
  // Re-enter scope to test re-declaration
  if (true) {
    var a , c = 2; // Rule triggers again
    console.log('Redecled:', a, c);
  }
  console.log('After redeclaration:', a, typeof c);
}

commaTest();
