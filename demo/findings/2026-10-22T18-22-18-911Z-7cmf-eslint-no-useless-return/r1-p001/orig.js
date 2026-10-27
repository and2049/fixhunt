function f() {
  let executed = false;
  try {
    return;
  } finally {
    executed = true;
  }
}
f();
console.log('executed:', executed);
