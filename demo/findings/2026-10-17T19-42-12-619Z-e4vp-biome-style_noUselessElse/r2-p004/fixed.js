function f() {
  if (true) { return 1; }
  // This comment should stay
  
    // This comment may be lost
    console.log(2);
}
f();
