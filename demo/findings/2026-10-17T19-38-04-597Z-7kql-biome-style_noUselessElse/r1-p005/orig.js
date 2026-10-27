function f() {
  if (true) { return; }
  else { debugger; console.log('reached'); }
}
f();
console.log('done');
