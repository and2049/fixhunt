function commaTest() {
  a = 'assigned';
  if (true) {
    var a = undefined, c = 2; // Rule triggers again
  }
  console.log('After redeclaration:', a, typeof c);
}
commaTest();
