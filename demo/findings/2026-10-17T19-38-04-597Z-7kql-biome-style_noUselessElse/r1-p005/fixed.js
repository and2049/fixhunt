function f() {
  if (true) { return; }
  debugger; console.log('reached'); 
}
f();
console.log('done');
