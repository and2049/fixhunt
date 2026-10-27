if (true) { return; }
else {
  function f() { return 1; }
  console.log(f());
}
// After fix, f is hoisted and callable before
console.log(typeof f);
