function f() {
  let executed = false;
  try {
    
  } finally {
    executed = true;
  }
}
f();
console.log('executed:', executed);
