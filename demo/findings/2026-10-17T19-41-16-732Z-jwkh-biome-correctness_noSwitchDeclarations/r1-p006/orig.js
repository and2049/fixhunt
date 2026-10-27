function f() {
  switch (x) {
    case 0:
      start: function helper() { return 42; }
      break;
    default:
      return helper();
  }
}
x = 0;
console.log(f()); // 42 (helper hoisted)
x = 1;
console.log(f()); // 42
// After fix: helper is block-scoped to case 0 → undefined in default → ReferenceError
