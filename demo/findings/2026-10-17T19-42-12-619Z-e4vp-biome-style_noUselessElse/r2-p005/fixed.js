function f() {
  if (true) { return; }
  
    debugger;
    console.log('unreachable');
}
f();
