function f() {
  switch (x) {
    case 0: {
      class C { constructor() { this.val = 99; } }
      break;
    }
    case 1:
      return new C().val;
  }
  return 0;
}
x = 0;
console.log(f()); // undefined (no return)
x = 1;
console.log(f()); // 99
// After fix: case 0 wrapped → C not in scope for case 1 → ReferenceError
