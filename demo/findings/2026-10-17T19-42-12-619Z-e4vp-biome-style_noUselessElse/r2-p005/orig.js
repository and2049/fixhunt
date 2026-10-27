function f() {
  if (true) { return; }
  else {
    debugger;
    console.log('unreachable');
  }
}
f();
