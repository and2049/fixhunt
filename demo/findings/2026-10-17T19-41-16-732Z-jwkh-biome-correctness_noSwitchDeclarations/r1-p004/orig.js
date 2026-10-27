function f() {
  switch (mode) {
    case 0:
      const arr = Array(3);
      arr[2] = 'x';
      return arr[1]; // hole → undefined
    case 1:
      return 'fallback';
  }
}
mode = 0;
console.log(f()); // undefined
mode = 1;
console.log(f()); // fallback
// After fix: same behavior — but if arr was used later, it wouldn't be
