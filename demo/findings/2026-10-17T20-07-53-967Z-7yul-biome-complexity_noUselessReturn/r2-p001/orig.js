function f() {
  L: while (true) {
    try { break L; } 
    finally { console.log('finally'); }
  }
  return;
}
f();
