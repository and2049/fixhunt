let finallyRan = false;
function f() {
  try {
    if (false) { return; }
  } finally {
    finallyRan = true;
  }
  else { console.log('else'); }
}
f();
console.log(finallyRan);
