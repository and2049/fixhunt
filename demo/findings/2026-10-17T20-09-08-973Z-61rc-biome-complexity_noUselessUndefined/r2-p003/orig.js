function f() {
  return
  [
    function() { return 1; },
    function() { return 2; }
  ]
}
try {
  let arr = f();
  console.log(arr[0]());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
